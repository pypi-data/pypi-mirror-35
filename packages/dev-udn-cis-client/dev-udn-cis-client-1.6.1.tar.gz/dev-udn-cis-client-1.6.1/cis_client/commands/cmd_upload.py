from __future__ import unicode_literals

import os
import stat
import copy

import click

from cis_client import cli
from cis_client.commands import utils
from cis_client.lib.cis_gateway import http_upload_client
from cis_client.lib.cis_gateway import aspera_client
from cis_client.lib.cis_gateway import sftp_client
from cis_client.lib.cis_north import content_client
from cis_client import exception


@click.command('upload', context_settings=utils.CONTEXT_SETTINGS, help=
               'Uploads content via HTTP/Aspera/SFTP.')
@click.option('--protocol', type=click.Choice(['http', 'aspera', 'sftp']), default='http',
              help='Protocol for loading. Can be http, aspera or sftp.')
@click.option('--ingest-point', required=True, type=click.STRING,
              help='Ingest point to load content to.')
@click.option('--source-file-list', type=click.Path(resolve_path=True),
              help='Path to file that contains list of full source paths to content separated by new line symbol. '
                   'Files from the list will be uploaded.')
@click.option('--source-file', type=click.STRING,
              help='Comma separated list of full source paths to content that will be uploaded. '
                   'Can contain path to directory with files if upload protocol is aspera.')
@click.option('--skip-errors', type=click.BOOL, default=False,
              help='Continue upload other files if some file upload was failed.')
@click.option('--destination-path', type=click.STRING,
              help='Destination path. '
                   'Can be directory like dir1/dir2/. If value ends with / destination '
                   'file path will be composed from this value + source filename. '
                   'If this value doesn\'t end with / so destination path will be the same.'
                   'In case when full destination path is specified input path list can contain only one input file.')
@click.option('--overwrite', type=click.Choice(['no', 'ask', 'all']), default='no',
               help='Overwrites files if file exists on remote storage. "ask" means ask each time before overwriting.')
@click.option('--max-transfer-rate', type=click.STRING, default='1G',
              help='Aspera max transfer rate. For example 10G, 100m')
@utils.add_host_options
@utils.add_auth_options
@utils.add_credentials_options
@cli.pass_context
@utils.handle_exceptions
@utils.check_cis_version
def cli(ctx, **kwargs):
    paths = utils.get_source_file_list_from_kwargs(**kwargs)
    north_host = kwargs.pop('north_host')
    ingest_point = kwargs.pop('ingest_point')
    destination_path = kwargs.pop('destination_path')
    skip_errors = kwargs.pop('skip_errors')
    max_transfer_rate = kwargs.pop('max_transfer_rate')
    overwrite = kwargs.pop('overwrite')
    if destination_path and len(destination_path.split(',')) > 1:
        raise exception.OptionException(
            "Option --destination-path can contain only one path: "
            "directory with '/' suffix or full destination path for single source file.")
    if (destination_path and not destination_path.endswith('/') and
            len(paths) != 1):
        raise exception.OptionException(
            "To upload several files you need to specify destination directory in "
            "--destination-path option. Directory must contain suffix '/'. "
            'For example --destination-path "{}"/'.format(destination_path))

    for path in paths:
        kwargs_per_upload = copy.deepcopy(kwargs)
        if destination_path:
            if destination_path.endswith('/'):
                full_dst_path = ''.join([destination_path, os.path.basename(path)])
            else:
                full_dst_path = destination_path
        else:
            full_dst_path = os.path.basename(path)
        utils.display('Uploading "{}" ... to "{}"'.format(path, full_dst_path))
        try:
            # check if file already uploaded
            stat_info = os.stat(path)
            if stat.S_ISDIR(stat_info.st_mode):
                utils.display('Skip to upload directory "{}"'.format(path))
                continue
            content_info = None
            try:
                content_info = content_client.get_content(
                    north_host, ingest_point, full_dst_path, context=kwargs_per_upload, checksum='md5', **kwargs_per_upload)
                if content_info['stat']['type'] == 'directory':
                    raise exception.UploadDirConflictException(full_dst_path)
                if (content_info['stat']['type'] == 'file' and
                        content_info['stat']['size'] == stat_info.st_size and
                        content_info.get('checksum', {}).get('md5') == utils.md5(path)):
                    utils.display('File "{}" is already present on "{}"'.format(
                        path, full_dst_path))
                    continue
            except exception.HttpClientError as e:
                if e.response.status_code != 404:
                    raise

            if content_info and overwrite == 'no':
                raise exception.UploadConflictException(full_dst_path)
            if content_info and overwrite == 'ask':
                if not click.confirm('File "{}" exists on remote server. Do you want to overwrite it?'.format(
                        full_dst_path)):
                    utils.display('Skipping to upload "{}" file.'.format(path))
                    continue
                else:
                    kwargs_per_upload.pop('token', None)
            if kwargs_per_upload['protocol'] == 'aspera':
                aspera_client.aspera_upload(
                    north_host, ingest_point, path, destination_path=full_dst_path,
                    max_transfer_rate=max_transfer_rate, **kwargs_per_upload)
            else:
                total_size = os.path.getsize(path)
                with utils.ProgressBar(max_value=total_size) as progress_bar:
                    if kwargs_per_upload['protocol'] == 'http':
                        response = http_upload_client.http_upload(
                            north_host, ingest_point, path, destination_path=full_dst_path,
                            progress_callback=lambda transfered: progress_bar.update(transfered),
                            overwrite=content_info is not None,
                            **kwargs_per_upload)
                    elif kwargs_per_upload['protocol'] == 'sftp':
                        response = sftp_client.sftp_upload(
                            north_host, ingest_point, path, destination_path=full_dst_path,
                            progress_callback=lambda transfered, whole: progress_bar.update(transfered),
                            overwrite=content_info is not None,
                            **kwargs_per_upload)
            utils.display('File "{}" was successfully uploaded to "{}"'.format(path, full_dst_path))
        except Exception as e:
            if skip_errors:
                with utils.handle_exceptions_contextmanager(reraise=False, exit_on_exception=False):
                    raise
            else:
                raise

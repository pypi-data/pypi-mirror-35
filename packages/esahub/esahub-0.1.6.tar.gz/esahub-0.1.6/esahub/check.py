# coding=utf-8
""" This module contains methods to check whether a local archive is corrupted.
    It can retrieve the true MD5 from SciHub and compare with the local file
    or check whether the archive is a valid zip file.
"""
from __future__ import print_function
from . import scihub, checksum, tty
from .config import CONFIG
import zipfile
import os
import sys
import logging
try:
    from netCDF4 import Dataset
    NETCDF_INSTALLED = True
except ImportError:
    NETCDF_INSTALLED = False

logger = logging.getLogger('esahub')
PY2 = sys.version_info < (3, 0)
try:
    ZIP_ERROR = zipfile.BadZipFile
except AttributeError:
    ZIP_ERROR = zipfile.BadZipfile


# -----------------------------------------------------------------------------
# FILE LISTING
# -----------------------------------------------------------------------------
def local_ls():
    #
    # Collect a list of all files.
    #
    all_files = []
    for (root, subdirs, files) in os.walk(CONFIG['GENERAL']['TMP_DIR']):
        for f in files:
            full_file_path = os.path.join(root, f)
            if f.endswith('.zip') or f.endswith('.nc'):
                all_files.append(full_file_path)
    return all_files


def check_file(full_file_path, mode):
    return scihub.block(_check_file, full_file_path, mode)


async def _check_file(full_file_path, mode):
    """ Check an already downloaded file for consistency.

    Parameters
    ----------
    full_file_path : str
    mode : {'file', 'md5'}
        If `md5`, check if the md5 checksum matches the value stored on SciHub.
        This is safer, but potentially slow. Also, the md5 checksum may not be
        available for older files. If `file`, check if the archive is a valid
        zip archive or a valid netCDF file. This method is very fast and should
        be accurate in the case of interrupted downloads.

    Returns
    -------
    tuple (str, bool, str)
        A tuple containing the file path, a boolean whether or not the file is
        okay, and a status message.
    """
    message = None

    pbar_key = os.path.split(full_file_path)[1]

    if mode == 'file':
        #
        # Check if the archive is a valid zip archive or
        # a valid netCDF file
        #
        ext = os.path.splitext(full_file_path)[1]
        if ext == '.zip':
            try:
                zip_ref = zipfile.ZipFile(full_file_path, 'r')
                zip_ref.close()
            except ZIP_ERROR as e:
                message = tty.error('BAD ZIP FILE')
                healthy = False
            else:
                message = tty.success('OKAY')
                healthy = True
        elif ext == '.nc':
            if not NETCDF_INSTALLED:
                raise ImportError("`netCDF4` must be installed to use this "
                                  "feature!")
            try:
                nc_ref = Dataset(full_file_path, 'r')
                nc_ref.close()
            except (OSError, IOError) as e:
                message = tty.error('BAD NETCDF FILE')
                healthy = False
            else:
                message = tty.success('OKAY')
                healthy = True
        else:
            message = tty.error('UNKNOWN FILE FORMAT')
            healthy = False

    elif mode == 'md5':
        #
        # Check the md5sum against SciHub.
        #
        remote_md5 = await scihub._md5(product=full_file_path)
        if remote_md5 is False:
            message = tty.error('MD5 NOT FOUND')
            healthy = False
        else:
            if checksum.md5(full_file_path) == remote_md5:
                message = tty.success('MD5 OKAY')
                healthy = True
            else:
                message = tty.error('FILE CORRUPT')
                healthy = False

    result = (full_file_path, healthy, message)

    tty.screen[pbar_key] = (message + ': {name}', tty.NOBAR)
    tty.screen.status(progress=1)

    return result

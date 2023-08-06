import os
import warnings

import pandas as pd
import yaml

import eqi_utils.data.utils
from eqi_utils.config import config
from eqi_utils.utils import ResourceUtils
from . import s3
from . import utils

DATA_INVENTORY_FILENAME_YAML = 'data_inventory.yaml'
DIR_PREFIX = 'bundles'


def _to_user_defined_inv_path():
    return os.path.join(
        config.get_eqi_home(),
        DATA_INVENTORY_FILENAME_YAML)


def _to_default_inv_path():
    return ResourceUtils.get_resource_filename(
        __name__, '', DATA_INVENTORY_FILENAME_YAML)


def _get_effective(criteria, *args):
    for value in args:
        if criteria(value):
            return value
    return None


def update_inventory():
    """Update data inventory from remote."""
    s3.download_from_s3(bucket='eqi-project-config',
                        key=DATA_INVENTORY_FILENAME_YAML,
                        filepath=_to_user_defined_inv_path())

def _get_effective_inv_path():
    inv_path = _get_effective(os.path.isfile, _to_user_defined_inv_path(),
                              _to_default_inv_path())
    if not inv_path:
        warnings.warn(
            'Data inventory file {} cannot be found, '
            'downloading the latest version'.format(
                DATA_INVENTORY_FILENAME_YAML))
        update_inventory()
        return _to_user_defined_inv_path()
    else:
        return inv_path


def _to_local_filename(bucket, key):
    local_dir = os.path.join(eqi_utils.data.utils.get_data_dir(), DIR_PREFIX,
                             bucket)
    if not os.path.isdir(local_dir):
        utils.mkdir_p(local_dir)
    return os.path.join(local_dir, key)


def _create_inventory(filename):
    if not os.path.isfile(filename):
        with open(filename, 'w') as file:
            file.write('bundles:\n')


def _load_inventory():
    inv_path = _get_effective_inv_path()
    _create_inventory(inv_path)
    with open(inv_path) as file_stream:
        try:
            inv = yaml.load(file_stream)
            if not inv or not inv['bundles']:
                return {}
            return inv['bundles']
        except Exception as exception:
            print("Cannot parse YAML inventory file {} because of {}".format(
                inv_path, exception))
            raise exception


_INVENTORY = _load_inventory()


def reload_inventory():
    """Reload bundle inventory."""
    global _INVENTORY
    _INVENTORY = _load_inventory()


def get_bundles():
    """
    Get all available bundles
    :return: list of bundle names
    """
    return list(_INVENTORY.keys())


@utils.print_as_df(orient='columns')
def list_bundles():
    """
    Print available bundles
    """
    return get_bundles()


def get_datafiles(bundle: str):
    """
    Get all the data file names from a specific bundle
    :param bundle:
    :return: list of file names
    """
    return list(_INVENTORY[bundle]['datafiles'].keys())


@utils.print_as_df(orient='columns')
def list_datafiles(bundle: str):
    """
    Print all data files of a bundle
    :param bundle:
    :return:
    """
    return get_datafiles(bundle)


def get_datafile_desc(bundle: str):
    """
    Get the data file description table for a specific bundle
    :param bundle: bundle name
    :return: map of data file names to description
    """
    return {k: v['desc'] for k, v in _INVENTORY[bundle]['datafiles'].items()}


@utils.print_as_df(index='DataFile', columns=['Description'])
def list_datafile_desc(bundle: str):
    """
    Print data file description
    :param bundle:
    :return:
    """
    return get_datafile_desc(bundle)


def get_datafile_location(bundle: str, datafile: str):
    """
    Get data file S3 key
    :param bundle: bundle name
    :param datafile: data file name
    :return: S3 key string
    """
    return _INVENTORY[bundle]['datafiles'][datafile]['loc']


def get_bucket_name(bundle: str):
    """
    Get bucket name
    :param bundle: bundle name
    :return: S3 bucket name
    """
    return _INVENTORY[bundle]['bucket']


def download_data(bundle: str, data_file: str):
    """
    Download a data file from a bundle to local disk
    :param bundle: bundle name
    :param data_file: data file name
    :return: local file path
    """
    if bundle not in get_bundles():
        raise ValueError(
            'Bundle {} cannot be found, please double check'.format(
                bundle))
    bucket = get_bucket_name(bundle)
    key = get_datafile_location(bundle, data_file)
    try:
        local_filename = _to_local_filename(bucket, key)
        if os.path.isfile(local_filename):
            print(
                'File {} exists, skip downloading'.format(local_filename))
            return local_filename
        s3.download_from_s3(bucket, key, local_filename)
        print(
            'Succeed downloading bucket={}, key={} into {}'.format(
                bucket, key, local_filename))
        return local_filename
    except Exception as exception:
        print('Download failed because of {}'.format(exception))
        raise exception


def load_to_df(bundle, datafile, **kwargs):
    """
    Load the data file from a bundle into DataFrame
    :param bundle: bundle name
    :param datafile: data file name
    :param kwargs:
    :return: Pandas DataFrame of the data file data
    """
    local_filename = download_data(bundle, datafile)
    if utils.file_ends_with(local_filename, '.csv'):
        return pd.read_csv(local_filename, **kwargs)
    elif utils.file_ends_with(local_filename,
                              '.parquet'):
        return utils.read_parquet(local_filename, **kwargs)
    else:
        raise Exception(
            'Cannot recognize the extension of file {}'.format(
                local_filename))

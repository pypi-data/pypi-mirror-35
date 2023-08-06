import hashlib
import os

import yaml

import eqi_utils.data.utils
from eqi_utils.utils import ResourceUtils
from . import s3
from . import utils

LOCAL_VIEW_INVENTORY = 'local_view.yaml'
USER_BASE_BUCKET = 'eqi-user-views'
DIR_PREFIX = 'user_views'
DEFAULT_USER = utils.get_user_folder()


def _create_inventory(filename):
    if not os.path.isfile(filename):
        with open(filename, 'w') as file:
            file.write('views:\n')


def _get_view_inventory():
    filename = ResourceUtils.get_resource_filename(
        __name__, '', LOCAL_VIEW_INVENTORY)
    _create_inventory(filename)
    with open(filename, 'r') as file:
        inventory = yaml.load(file)
    if (inventory is None or 'views' not in inventory.keys() or
            inventory['views'] is None):
        inventory = {
            'views': {}
        }
    return inventory


def _save_view_inventory(inventory):
    filename = ResourceUtils.get_resource_filename(
        __name__, '', LOCAL_VIEW_INVENTORY)
    _create_inventory(filename)
    with open(filename, 'w') as file:
        yaml.dump(inventory, file)


def _add_to_view_inventory(view_name, view_path, desc=None, user=DEFAULT_USER):
    inventory = _get_view_inventory()
    key = view_name
    if user != DEFAULT_USER:
        key = '/'.join([user, view_name])
    inventory['views'][key] = {'path': view_path}
    if desc:
        inventory['views'][key]['desc'] = desc
    _save_view_inventory(inventory)


def _delete_from_view_intenvory(view_name):
    inventory = _get_view_inventory()
    inventory['views'].pop(view_name)
    _save_view_inventory(inventory)


def _to_path(view_name):
    inventory = _get_view_inventory()
    return inventory['views'][view_name]['path']


def _to_parquet_filename(view_name):
    return view_name + '.parquet'


def _to_local_dir(user=DEFAULT_USER):
    return os.path.join(eqi_utils.data.utils.get_data_dir(), DIR_PREFIX, user)


def _to_local_filename(view_name, user=DEFAULT_USER):
    parquet_filename = _to_parquet_filename(view_name)
    local_dir = _to_local_dir(user)
    if not os.path.isdir(local_dir):
        eqi_utils.data.utils.mkdir_p(local_dir)
    return os.path.join(local_dir, parquet_filename)


def _to_s3_key(view_name, user=DEFAULT_USER):
    return "/".join([user, _to_parquet_filename(view_name)])


def save_view(data_frame, view_name, desc='', remote=False, **kwargs):
    """
    Save a dataframe as a view in parquet format
    :param data_frame: input dataframe to save
    :param view_name: view name
    :param desc: description of the view
    :param remote: if true, use S3, otherwise use local file system
    :return:
    """
    parquet_filepath = _to_local_filename(view_name)
    data_frame.to_parquet(parquet_filepath, **kwargs)
    _add_to_view_inventory(view_name, parquet_filepath, desc)
    if remote:
        s3.upload_to_s3(USER_BASE_BUCKET,
                        _to_s3_key(view_name,
                                   eqi_utils.data.utils.get_user_folder()),
                        parquet_filepath,
                        ExtraArgs={'Metadata': {'desc': desc}})


def save_view_as_admin(data_frame, view_name, desc='', remote=False, **kwargs):
    """
    Save a dataframe as a view in parquet format as EQI admin
    You can definitely abuse this function.
    But I know I can trust you.
    :param data_frame: input dataframe to save
    :param view_name: view name
    :param desc: description of the view
    :param remote: if true, use S3, otherwise use local file system
    :return:
    """
    admin_username = 'default'
    parquet_filepath = _to_local_filename(view_name, user=admin_username)
    data_frame.to_parquet(parquet_filepath, **kwargs)
    _add_to_view_inventory(view_name, parquet_filepath, desc)
    if remote:
        s3.upload_to_s3(USER_BASE_BUCKET,
                        _to_s3_key(view_name,
                                   admin_username),
                        parquet_filepath,
                        ExtraArgs={'Metadata': {'desc': desc}})


def get_views(user=DEFAULT_USER, remote=False):
    """
    Get a list of available views
    :param user: user of query
    :param remote: if true, use S3, otherwise use local filesystem
    :return: list of available views
    """
    if remote:
        return s3.list_objects(USER_BASE_BUCKET, user)
    else:
        return _get_view_inventory()['views']


@utils.print_as_df()
def list_views(user=DEFAULT_USER, remote=False):
    """
    Print all available views of a user
    :param user: user of query
    :param remote: if true, use S3, otherwise use local file system
    :return:
    """
    return get_views(user=user, remote=remote)


def delete_view(view_name: str, remote=False):
    """
    Delete a view.
    :param view_name: the view name
    :param remote: if true, use S3, otherwise, use local filesystem
    :return:
    """
    if remote:
        s3.delete_object(USER_BASE_BUCKET, '/'.join(
            [DEFAULT_USER, _to_parquet_filename(view_name)]))
    else:
        os.remove(_to_path(view_name))
        _delete_from_view_intenvory(view_name)


def load_to_df(view_name, user=DEFAULT_USER, remote=False, force=False, **kwargs):
    """
    Load data frame from a view
    :param view_name: view name
    :param user: user of query
    :param remote: if true, use S3, otherwise use local file system
    :param kwargs:
    :return: Pandas DataFrame that contains the view data
    """
    local_filename = _to_local_filename(view_name, user)
    if remote:
        if os.path.isfile(local_filename) and not force:
            print(
                "File {} has been downloaded, skip downloading.".format(
                    local_filename))
        else:
            s3.download_from_s3(USER_BASE_BUCKET,
                            _to_s3_key(view_name, user),
                            _to_local_filename(view_name, user))
    # TODO: Add desc
    _add_to_view_inventory(view_name, local_filename, user=user)
    return utils.read_parquet(local_filename, **kwargs)

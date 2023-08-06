import functools
import hashlib
import os

import pandas as pd

from eqi_utils.config import keys
from eqi_utils.config.config import EQI_CONFIG


def to_df(dict_like, index=None, orient='index', columns=None):
    if columns:
        df = pd.DataFrame.from_dict(dict_like, orient=orient, columns=columns)
    else:
        df = pd.DataFrame.from_dict(dict_like, orient=orient)
    if index:
        df.index.name = index
    return df


def full_print(df):
    with pd.option_context("display.max_colwidth", 10000):
        try:
            from IPython.display import display
            display(df)
        except ImportError:
            print(df)


def print_as_df(index=None, orient='index', columns=None):
    def annotator(func):
        @functools.wraps(func)
        def caller(*args, **kwargs):
            df = to_df(func(*args, **kwargs), index=index, orient=orient,
                       columns=columns)
            full_print(df)

        return caller

    return annotator


def suppress_warnings(func):
    @functools.wraps(func)
    def func_no_warning(*args, **kwargs):
        import warnings
        warnings.filterwarnings("ignore")
        try:
            return func(*args, **kwargs)
        except Warning:
            print("Some warnings are ignored")
        warnings.filterwarnings("default")

    return func_no_warning


def to_dirname(filepath):
    return os.path.dirname(filepath)


def mkdir_p_file(filepath):
    os.makedirs(to_dirname(filepath), exist_ok=True)


def mkdir_p(folder):
    os.makedirs(folder, exist_ok=True)


def file_ends_with(filename, ext):
    return filename.lower().endswith(ext)


def get_user_folder():
    return EQI_CONFIG.get_mandatory(keys.USER_NAME)


def get_data_dir():
    return EQI_CONFIG.get_mandatory(keys.DATA_DIR)


def read_parquet(filename, *args, **kwargs):
    try:
        return pd.read_parquet(filename, engine='pyarrow', *args, **kwargs)
    except Exception:
        return pd.read_parquet(filename, engine='fastparquet', *args, **kwargs)

def _keccak256(input):
    m = hashlib.sha3_256()
    m.update(input.encode('utf-8'))
    return m.hexdigest()

def authenticate_admin():
    input_password = input('Please input admin password')
    pw_hash = 'a0abc1e69f18b8c5c84d15ad6a40b9fcff7bedc857c7a7c79b9bdb12a107bc51'
    if _keccak256(input_password) != pw_hash:
        raise PermissionError("Wrong password")
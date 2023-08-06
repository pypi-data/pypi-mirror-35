import boto3
from botocore.config import Config

from eqi_utils.config import keys
from eqi_utils.config.config import EQI_CONFIG
from eqi_utils.data.utils import suppress_warnings, mkdir_p_file


def _s3_client():
    profile_name = EQI_CONFIG.get_mandatory(
        keys.AWS_PROFILE_NAME)
    http_proxy = EQI_CONFIG.get_optional(
        keys.HTTP_PROXY, '')
    https_proxy = EQI_CONFIG.get_optional(
        keys.HTTPS_PROXY, '')
    client = boto3.Session(
        profile_name=profile_name).client(
        's3',
        config=Config(
            proxies={
                'https': https_proxy,
                'http': http_proxy}))
    return client


@suppress_warnings
def download_from_s3(bucket, key, filepath):
    mkdir_p_file(filepath)
    client = _s3_client()
    response = client.download_file(Bucket=bucket, Key=key, Filename=filepath)
    return response


@suppress_warnings
def upload_to_s3(bucket, key, file, **kwargs):
    client = _s3_client()
    client.upload_file(Filename=file, Bucket=bucket, Key=key, **kwargs)


def _strip_prefix(s, prefix):
    return s.split(prefix).pop()


def _strip_ext(s, suffix='.'):
    return s[0:s.rfind(suffix)]


def _to_view_name(s, prefix):
    return _strip_ext(_strip_prefix(s, prefix))


@suppress_warnings
def list_objects(bucket, prefix=None):
    prefix += '/'
    client = _s3_client()
    response = client.list_objects_v2(Bucket=bucket, Prefix=prefix)
    obj_dict = {_to_view_name(x['Key'], prefix): {'size': x['Size']}
                for x in response['Contents']
                if _strip_prefix(x['Key'], prefix)}
    return obj_dict


@suppress_warnings
def delete_object(bucket, key):
    client = _s3_client()
    client.delete_object(Bucket=bucket, Key=key)

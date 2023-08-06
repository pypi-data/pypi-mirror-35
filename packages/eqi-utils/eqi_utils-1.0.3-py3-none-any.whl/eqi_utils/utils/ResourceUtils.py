import pkg_resources


def get_resource_filename(pkg_name, folder_name, file_name):
    """
    Get the filename of a package resource.
    :param pkg_name: package name
    :param folder_name: sub folder name
    :param file_name: resource filename
    :return: absolute path string of a package resource
    """
    return pkg_resources.resource_filename(pkg_name,
                                           '/'.join((folder_name, file_name)))

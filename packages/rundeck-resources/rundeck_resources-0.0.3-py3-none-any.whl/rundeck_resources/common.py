import os


def normalize_path(path: str) -> str:
    """
    Method to expand and return an absolute
    path from a normal path.
    :param path: The path to normalize.
    :type path: str.
    :returns: The absolute path.
    :rtype: str.
    """
    exp_path = os.path.expanduser(path)
    abs_path = os.path.abspath(exp_path)
    return abs_path


def check_file(path: str) -> str:
    """
    Method to normalize the path of a file and
    check if the file exists and is a file.
    :param path: The file path to check.
    :type path: str.
    :returns: The absolute path of a file
    :rtype: str.
    :raises: FileNotFoundError
    """
    file_path = normalize_path(path)
    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        raise FileNotFoundError
    return file_path

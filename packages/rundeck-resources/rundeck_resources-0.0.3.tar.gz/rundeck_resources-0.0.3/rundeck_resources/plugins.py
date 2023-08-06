import pkg_resources


def load_plugins(config: dict, resource_types: str) -> dict:
    """
    Method to load plugins defined in the *entry_point*
    by resource_type.
    :param config: The configuration file content.
    :type config: dict.
    :param resource_types: The resource type to load (Input, Output).
    :type resource_types: str.
    :returns: The plugins loaded.
    :rtype: dict.
    """
    entry_points = get_plugins(resource_types)
    plugins = {}
    for section in config:
        if section in entry_points:
            plugins.update({section: entry_points[section].load()})
    return plugins


def get_plugins(resource_types: str) -> dict:
    """
    Method to get the plugins defined in the *entry_point*.
    :param resource_types: The resource type to get (Input, Output).
    :type resource_types: str.
    :returns: The entry points by name.
    :rtype: dict.
    """
    entry_points = {}
    for entry_point in pkg_resources.iter_entry_points(resource_types):
        entry_points.update({entry_point.name: entry_point})
    return entry_points

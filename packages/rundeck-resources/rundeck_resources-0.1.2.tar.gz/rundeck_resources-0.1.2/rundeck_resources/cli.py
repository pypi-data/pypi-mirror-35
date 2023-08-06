#!/usr/bin/env python3
import argparse
from .config import read_config
from .plugins import load_plugins

from . import __version__


def main() -> None:
    """
    Main method.
    """
    parser = argument_parse()
    args = parser.parse_args()
    config = read_config(args.config)
    input_plugins = load_plugins(config, 'Importers')
    output_plugins = load_plugins(config, 'Exporters')

    input_interfaces = initialize_interfaces(config, input_plugins)
    output_interfaces = initialize_interfaces(config, output_plugins)

    nodes = import_resources(input_interfaces)
    export_resources(output_interfaces, nodes)


def initialize_interfaces(config: dict, plugins: dict) -> dict:
    """
    Method to initialize the interfaces with the configuration.

    :param config: The configuration file content.
    :type config: dict
    :param plugins: The list of loaded plugins.
    :type plugins: dict
    :returns: The list of loaded plugins initialized.
    :rtype: dict
    """
    interfaces = []
    for interface in plugins.values():
        interfaces.append(interface(config))
    return interfaces


def import_resources(interfaces: list) -> dict:
    """
    Method to get all resources from the *input* interfaces.

    :param interfaces: The list of initialized input interfaces.
    :type interfaces: list
    :returns: The resources returned by the input interfaces.
    :rtype: dict
    """
    resources = {}
    for interface in interfaces:
        resources.update(interface.import_resources())
    return resources


def export_resources(interfaces: list, resources: dict) -> None:
    """
    Method to export the resources using the *output* interfaces.

    :param interfaces: The list of initialized output interfaces.
    :type interfaces: list
    :param resources: The resources provided by the input interfaces.
    :type resources: dict
    """
    for interface in interfaces:
        interface.export_resources(resources)


def argument_parse() -> argparse.ArgumentParser:
    """
    Method to extract the arguments from the command line.

    :returns: The argument parser.
    :rtype: argparse.ArgumentParser
    """
    parser = argparse.ArgumentParser(
        description="Generates rundeck resources "
                    "file from different API sources")

    parser.add_argument(
        'config', type=str,
        help='Configuration file')
    parser.add_argument(
        '-V', '--version', action='version',
        version='%(prog)s {}'.format(__version__),
        help='Prints version')
    return parser

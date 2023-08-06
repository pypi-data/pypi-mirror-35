from chef import ChefAPI, Search
from .interfaces import ResourcesImporter
from .common import normalize_path


class ChefImporter(ResourcesImporter):
    """
    A Chef node information importer
    """

    def __init__(self, config):
        self.config = config['ChefImporter']

    def get_chef_nodes(self) -> dict:
        """
        Method to get the chef nodes information.
        :returns: The chef nodes information.
        :rtype: dict.
        """
        config = ChefImporter.expand_paths(self.config)
        chef_nodes = ChefImporter.call_chef(config)
        return chef_nodes

    @staticmethod
    def call_chef(config: dict) -> dict:
        """
        Method to query the chef server.
        :param config: The chef configuration.
        :type config: dict.
        :returns: The chef nodes information.
        :rtype: dict.
        """
        with ChefAPI(config['url'],
                     config['user_cert_path'],
                     config['user'],
                     version=config.get('version', '0.10.8'),
                     ssl_verify=config.get('ssl_cert_path', False)):
            return Search('node', 'Node Name:*')

    @staticmethod
    def expand_paths(config: dict) -> dict:
        """
        Method to expand file paths for the user certificate
        and the chef ssl certificate.
        :param config: The chef configuration.
        :type config: dict.
        :returns: The chef configuration with expanded paths.
        :rtype: dict.
        """
        config['user_cert_path'] = normalize_path(config['user_cert_path'])
        config['ssl_cert_path'] = normalize_path(config['ssl_cert_path'])
        return config

    def import_resources(self) -> dict:
        """
        Method to format chef resources into rundeck resources.
        :returns: Rundeck formatted nodes resources.
        :rtype: dict.
        """
        chef_nodes = self.get_chef_nodes()
        nodes = {}
        for node in chef_nodes:
            try:
                _node = {}
                _node[node['name']] = {}
                _node[node['name']]['hostname'] = node['automatic']['fqdn']
                _node[node['name']]['nodename'] = node['automatic']['hostname']
                _node[node['name']]['Environment'] = node['chef_environment']
                _node[node['name']]['osName'] = node['automatic']['platform']
                _node[node['name']]['osFamily'] = \
                    node['automatic']['platform_family']
                _node[node['name']]['osVersion'] = \
                    node['automatic']['platform_version']
                _node[node['name']]['osArch'] = \
                    node['automatic']['kernel']['machine']
                _node[node['name']]['recipes'] = \
                    ','.join(node['automatic']['recipes'])
                _node[node['name']]['roles'] = \
                    ','.join(node['automatic']['roles'])
                _node[node['name']]['tags'] = \
                    ','.join(node['automatic']['recipes'])
                _node[node['name']]['chef_tags'] = \
                    ','.join(node['normal']['tags'])
                _node[node['name']]['description'] = \
                    node['automatic']['lsb']['description']
                _username = self.config.get('rundeck_user_login', None)
                if _username:
                    _node[node['name']]['username'] = _username
            except KeyError:
                continue
            nodes.update(_node)
        return nodes

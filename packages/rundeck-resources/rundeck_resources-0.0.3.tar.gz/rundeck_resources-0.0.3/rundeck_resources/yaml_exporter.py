import yaml
from .interfaces import ResourcesExporter
from .common import normalize_path


class YAMLExporter(ResourcesExporter):
    """
    The YAML rundeck exporter class
    """

    def __init__(self, config: dict = {}):
        self.config = config.get('YAMLExporter', None)

    def export_resources(self, dictionary: dict) -> None:
        """
        Method to save nodes' information into a rundeck
        nodes resources `YAML` file.
        :param dictionary: Rundeck formatted nodes information.
        :type dictionary: dict.
        """
        yaml_file = YAMLExporter.export_path(self.config)
        if yaml_file:
            abs_path = normalize_path(yaml_file)
            with open(abs_path, 'w+') as yfile:
                yaml.dump(dictionary,
                          stream=yfile,
                          explicit_start=True,
                          default_flow_style=False)
        else:
            print(yaml.dump(dictionary,
                            explicit_start=True,
                            default_flow_style=False))

    @staticmethod
    def export_path(config: str) -> str:
        """
        Method to get the rundeck export file in absolute
        path format.
        :param config: The `Rundeck` section of the configuration.
        :type config: str.
        :returns: The file path of rundeck resources to export to.
        :rtype: str.
        """
        if config:
            return config.get('export_path', None)
        return None

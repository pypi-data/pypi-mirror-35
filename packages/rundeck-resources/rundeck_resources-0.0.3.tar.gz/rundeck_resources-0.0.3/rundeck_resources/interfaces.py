from abc import ABCMeta, abstractmethod


class ResourcesImporter(metaclass=ABCMeta):
    """
    ResourcesImporter interface definition
    """

    @abstractmethod
    def import_resources():
        """
        This method is expected to export the
        data into a rundeck data structure that
        can be easily saved
        """
        pass


class ResourcesExporter(metaclass=ABCMeta):
    """
    ResourcesExporter interface definition
    """

    @abstractmethod
    def export_resources():
        """
        This method is expected to save the data
        into a rundeck resources formatted file.
        """
        pass

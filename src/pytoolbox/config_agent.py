from configparser import ConfigParser
import toml


class ConfigAgent():
    """
        A class used to load a timl config file

        For each config section an instance of ConfigSection() is created as a class attribute of ConfigAgent

        Each parameter in a section is set a class attribute of the corresponding ConfigSection()
        ...

        Attributes
        ----------
        config_path : str
            full file path for the config file
        config : ConfigParser
            a dictionary of values, as read with toml

        [loaded_parameters] : [variable]
            parameters loaded from the config file

        Methods
        -------
        get_config()
            Returns the dictionary as read with toml

        add_parameter()
            Manually adds a parameter. Creates a new section if the specified one does not exist

        """

    class ConfigSection():
        def __init__(self, section_name: str):
            self.name = section_name
        

    def __init__(self,
                 config_path: str,
                 section_prefix: str = ''):
        """
        Parameters
        ----------
        config_path : str
            The full path of the config file
        section_prefix : bool, optional
            If True the names of the section objects will be prefixed by the passed string (default is an empty string)

        """
        self.config_path = config_path
        self._read_data(section_prefix)

    def get_config(self) -> ConfigParser:
        return self.config

    def _read_data(self, section_prefix: str):
        self.config = toml.load(self.config_path)
        for section in self.config.items():
            section_name = section_prefix + '_' + section[0] if section_prefix != '' else section[0]
            new_section = self.ConfigSection(section_name)
            for parameter in section[1]:
                parameter_value = section[1][parameter]
                setattr(new_section, parameter, parameter_value)
            setattr(self, section_name, new_section)
    
    def add_parameter(self, section_name: str, parameter: str, parameter_value: type):
        if not hasattr(self, section_name):
            new_section = self.ConfigSection(section_name)
            setattr(new_section, parameter, parameter_value)
            setattr(self, section_name, new_section)
        else:
            section = getattr(self, section_name)
            setattr(section, parameter, parameter_value)


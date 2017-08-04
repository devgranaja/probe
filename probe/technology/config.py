import os
import yaml


class Config(dict):

    def __init__(self):
        super().__init__(self)

    def from_yaml(self, filename):
        """Loads a configuration from a yaml file"""
        try:
            with open(filename) as yaml_file:
                obj = yaml.safe_load(yaml_file)
        except IOError as e:
            e.strerror = 'Unable to load file configuration: {}'.format(e.strerror)
            raise
        except yaml.YAMLError as e:
            if hasattr(e, 'problem_mark'):
                e.strerror = 'Error parsing YAML file at line {}, column {}'.format(e.problem_mark.line, e.problem_mark.column+1)
                raise
            else:
                e.strerror = 'Unknow error parsing YAML file'
                raise
        for (key, value) in obj.items():
            self[key] = value

    def from_envvar(self, variable_name):
        """Loads a configuration from a environment variable pointing a
        yaml file"""
        fn = os.environ.get(variable_name)
        if not fn:
            raise RuntimeError('The environment variable {} isn\'t set.'.format(variable_name))
        self.from_yaml(fn)

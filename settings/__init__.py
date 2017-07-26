from enum import Enum
import yaml


class FileType(Enum):
    UNKNOWN = 'txt'
    YML = 'yml'
    XML = 'xml'
    INI = 'ini'


class Settings(object):
    def __init__(self, filename: str = 'config.yml', filetype: Enum = FileType.YML):
        try:
            file = open(filename, 'r')
        except IOError:
            file = open(filename, 'w')

        self._filename = filename

        if filetype is FileType.YML:
            self._filetype = filetype
            # File may be empty
            try:
                self._config = yaml.load(file)
            except Exception:
                self._config = None
        else:
            # TODO: not implemented
            self._filetype = FileType.UNKNOWN
            raise TypeError('Type not implemented yet')

        if self._config is None:
            self._config = {}

    @property
    def filename(self) -> str:
        return self._filename

    @filename.setter
    def filename(self, filename):
        self._filename = filename

    @property
    def filetype(self) -> FileType:
        return self._filetype

    @filetype.setter
    def filetype(self, filetype):
        self._filetype = filetype

    @property
    def config(self) -> dict:
        return self._config

    @config.setter
    def config(self, config):
        self._config = config

    def save(self):
        if self._filetype is FileType.YML:
            with open(self._filename, 'w') as file:
                yaml.dump(self._config, file, default_flow_style=False)
        else:
            # TODO: not implemented
            raise TypeError('Type not implemented yet')

from settings import Settings
from settings import FileType


if __name__ == '__main__':
    conf = Settings(filetype=FileType.YML)
    sections = [print(x) for x in conf.config]
    conf.config['tree'] = {'branch': 'leaf'}
    print(conf.config['tree']['branch'])
    # conf.filetype = FileType.INI
    conf.save()

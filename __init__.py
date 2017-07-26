from settings import Settings
from settings import FileType


if __name__ == '__main__':
    try:
        conf = Settings(filetype=FileType.YML)
        sections = [print(x) for x in conf.config]
        print(conf.config)
        conf.config['tree'] = {'branch': ['leaf1', 'leaf2', 'leaf3']}
        print(conf.config)
        # conf.filetype = FileType.INI
        # conf.save()
    except Exception as ex:
        print('[Exception]', ex)

# from probe.technology.settings import FileType
# from probe.technology.settings import Settings
# import os.path
# import pytest
#
#
# def test_settings_filewriter():
#     conf = Settings(filename=pytest.filename)
#     assert os.path.isfile(pytest.filename)
#
#
# def test_settings_filetype_yml():
#     mock = Settings(filename=pytest.filename, filetype=FileType.YML)
#     mock.config['tree'] = {'branch': ['leaf1', 'leaf2', 'leaf3']}
#     mock.save()
#
#     conf = Settings(filename=pytest.filename, filetype=FileType.YML)
#     assert repr(conf.config) == "{'tree': {'branch': ['leaf1', 'leaf2', 'leaf3']}}"

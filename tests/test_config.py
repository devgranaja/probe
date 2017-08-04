
import pytest
import yaml
import os
from probe.technology.config import Config


def test_load_from_yaml():
    cfg = Config()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    fn = os.path.join(current_dir, 'files', 'config_1.yml')
    cfg.from_yaml(fn)
    assert len(cfg) > 0


def test_bad_yaml_path():
        cfg = Config()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        fn = os.path.join(current_dir, 'files', 'config_badname.yml')
        with pytest.raises(IOError):
            cfg.from_yaml(fn)


def test_yaml_parser_error():
        cfg = Config()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        fn = os.path.join(current_dir, 'files', 'config_parser_error.yml')
        with pytest.raises(yaml.YAMLError):
            cfg.from_yaml(fn)


def test_load_from_environment_variable_missing():
        cfg = Config()
        env = os.environ
        try:
            os.environ = {}
            with pytest.raises(RuntimeError):
                cfg.from_envvar('PROBE_CONFIG')
        finally:
            os.environ = env


def test_load_from_environment_variable():
        cfg = Config()
        env = os.environ
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            fn = os.path.join(current_dir, 'files', 'config_1.yml')
            os.environ = {'PROBE_CONFIG': fn}
            cfg.from_envvar('PROBE_CONFIG')
            assert len(cfg) > 0
        finally:
            os.environ = env

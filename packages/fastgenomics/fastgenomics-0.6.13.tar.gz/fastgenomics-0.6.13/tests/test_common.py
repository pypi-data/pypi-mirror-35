import logging

import pytest
import pathlib

from fastgenomics import _common, io


def test_paths_are_initialized(local):
    _common.get_paths()


def test_custom_init_paths(app_dir, data_root):
    io.set_paths(app_dir, data_root)
    _common.get_paths()


def test_paths_from_env(fg_env):
    _common.get_paths()


def test_cannot_init_nonexisting_paths():
    with pytest.raises(FileNotFoundError):
        io.set_paths("i_don't_exist", "me_neither")


def test_custom_init_path_within_docker(fake_docker, app_dir, data_root):
    with pytest.warns(None):
        io.set_paths(app_dir, data_root)
        _common.get_paths()


def test_get_app_manifest(local):
    _common.get_app_manifest()


def test_assert_manifest_is_valid(local):
    manifest = _common.get_app_manifest()
    _common.assert_manifest_is_valid({'FASTGenomicsApplication': manifest})


def test_can_get_parameters(local):
    parameters = io.get_parameters()
    assert len(parameters) > 0


def test_get_paramerets_dont_run_into_recursion(monkeypatch, local):
    monkeypatch.setattr("fastgenomics._common.load_parameters_from_manifest", dict)
    monkeypatch.setattr("fastgenomics._common.load_runtime_parameters", dict)
    io.get_parameters()


def test_parameters(local, caplog):
    caplog.set_level(logging.DEBUG)
    parameters = io.get_parameters()

    assert "StrValue" in parameters
    assert parameters["StrValue"] == "hello from parameters.json"

    assert "IntValue" in parameters
    assert parameters["IntValue"] == 150

    assert "FloatValue" in parameters
    assert parameters["FloatValue"] == float(100)

    assert "BoolValue" in parameters
    assert parameters["BoolValue"] is True

    assert "ListValue" in parameters
    assert parameters["ListValue"] == [1, 2, 3]

    assert "DictValue" in parameters
    assert parameters["DictValue"] == {"foo": 42, "bar": "answer to everything"}

    assert "OptionalIntValueConcrete" in parameters
    assert parameters["OptionalIntValueConcrete"] == 4

    assert "OptionalIntValueNull" in parameters
    assert parameters["OptionalIntValueNull"] is None

    assert "EnumValue" in parameters
    assert parameters["EnumValue"] == "X"

    assert any(["Parameters" in x.message for x in caplog.records]), "Parameter logs are not set"


def test_can_get_specific_parameter(local):
    assert io.get_parameter("IntValue") == 150


def test_can_get_null_parameter(local):
    assert io.get_parameter("OptionalIntValueNull") is None


def test_can_have_different_type(local, monkeypatch):
    # patch custom parameter load function
    monkeypatch.setattr("fastgenomics._common.load_runtime_parameters", lambda: {"StrValue": 1})

    # get parameters and compare parameters of different types
    with pytest.warns(None):
        parameters = io.get_parameters()
        assert 1 == parameters["StrValue"]


def test_load_input_file_mapping(local):
    input_file_mapping = _common.load_input_file_mapping()
    assert "some_input" in input_file_mapping


def test_input_file_mapping_to_paths(local):
    ifm_dict = _common.load_input_file_mapping()
    input_file_mapping = _common.str_to_path_file_mapping(ifm_dict)
    assert isinstance(input_file_mapping['some_input'], pathlib.Path)
    assert input_file_mapping['some_input'].exists()


def test_check_input_file_mapping(local):
    ifm_dict = _common.load_input_file_mapping()
    input_file_mapping = _common.str_to_path_file_mapping(ifm_dict)

    # test everything is ok
    _common.check_input_file_mapping(input_file_mapping)

    # test if additional keys trigger warning
    input_file_mapping['unused_key'] = pathlib.Path(".")
    with pytest.warns(None):
        _common.check_input_file_mapping(input_file_mapping)

    # test raises KeyError on missing entry
    with pytest.raises(KeyError):
        _common.check_input_file_mapping({})

    # test raises FileNotFoundError on wrong item
    with pytest.raises(FileNotFoundError):
        _common.check_input_file_mapping({"some_input": pathlib.Path("i_don't_exist")})


def test_load_input_file_mapping_from_env(local, monkeypatch):
    monkeypatch.setenv('INPUT_FILE_MAPPING', '{"some_key_from_env": "some_value"}')
    monkeypatch.setattr('pathlib.Path.exists', lambda self: False if "input_file_mapping.json" in self.name else True)
    input_file_mapping = _common.load_input_file_mapping()
    assert "some_input" not in input_file_mapping, "input_file_mapping from file used instead if env!"
    assert "some_key_from_env" in input_file_mapping
    # test if rest of _common still works
    _ = _common.get_app_manifest()
    _ = io.get_parameters()


def test_get_input_file_mapping(local):
    input_file_mapping = _common.get_input_file_mapping()
    assert "some_input" in input_file_mapping
    assert input_file_mapping['some_input'].exists()


def test_get_input_file_mapping_from_env(local, monkeypatch):
    monkeypatch.setenv('INPUT_FILE_MAPPING', '{"some_input": "input.csv", "some_key_from_env": "input.csv"}')
    input_file_mapping = _common.get_input_file_mapping()
    assert input_file_mapping['some_key_from_env'].exists()

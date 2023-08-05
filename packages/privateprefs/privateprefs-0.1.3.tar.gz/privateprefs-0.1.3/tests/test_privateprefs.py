import pytest
import privateprefs.internal.data_serializer as ds
import privateprefs as prefs

test_key = "test key"
test_value = "test value"
test_dict = {'test key': 'test value'}
test_dict_as_str = "{'test key': 'test value'}"


@pytest.fixture(autouse=True)
def setup_and_teardown():
    # set up
    prefs.delete_all()
    yield
    # tear down
    prefs.delete_all()


def _load_test_file_str():
    with open(ds.path_to_test_file, "r") as file:
        return file.read()


def _save_dict_str_to_file(dict_str):
    with open(ds.path_to_test_file, "w") as file:
        file.write(dict_str)


def test_load():
    _save_dict_str_to_file(test_dict_as_str)
    assert prefs.load(test_key) == test_value


def test_load_default_value_null():
    _save_dict_str_to_file("")
    assert prefs.load(test_key) is None


def test_load_from_empty_file():
    _save_dict_str_to_file("")
    assert prefs.load(test_key) is None


def test_load_dict_filtered():
    _save_dict_str_to_file("{'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}")
    ret = prefs.load_dict(['key1', 'key3'])
    assert ret['key1'] == 'value1' and ret['key3'] == 'value3'


def test_load_dict_not_filtered():
    _save_dict_str_to_file("{'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}")
    ret = prefs.load_dict(None)
    assert ret['key1'] == 'value1' and ret['key2'] == 'value2' and ret['key3'] == 'value3'


def test_load_dict_with_only_key_in_dict_text_file():
    _save_dict_str_to_file("{'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}")
    ret = prefs.load_dict(['key1', 'key4'])
    assert ret['key1'] == 'value1' and "key4" not in ret.keys()


def test_load_dict_from_empty_file():
    _save_dict_str_to_file("")
    assert prefs.load_dict(test_key) == {}


def test_delete_all():
    ds.save(test_key, test_value)
    prefs.delete_all()
    assert prefs.load(test_key) is None


def test_delete():
    ds.save(test_key, test_value)
    ds.save("other test key", "other test value")
    did_save_value = prefs.load(test_key) == test_value
    prefs.delete(test_key)
    did_delete_value = prefs.load(test_key) is None
    did_not_delete_other_test_value = prefs.load("other test key") == "other test value"
    assert all([did_save_value, did_delete_value, did_not_delete_other_test_value])


def test_delete_empty_dict():
    ds.save(test_key, test_value)
    did_save_value = prefs.load(test_key) == test_value
    prefs.delete(test_key)
    did_delete_value = prefs.load(test_key) is None
    assert all([did_save_value, did_delete_value])

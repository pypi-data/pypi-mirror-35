import os

import pyzzy as pz
import commons


pz.set_working_directory(__file__)

data_directory = os.path.join(os.getcwd(), "data")
if not os.path.isdir(data_directory):
    os.mkdir(data_directory)


def test_conf_object():
    datas_src = commons.get_data()
    datas_tmp = pz.dump_conf(datas_src)
    datas_dst = pz.load_conf(datas_tmp)
    datas_dst = pz.data.io_conf.conf2dict(datas_dst, include_default=False)
    assert commons.obj2str(datas_src) == commons.obj2str(datas_dst)


def test_conf_file():
    file_path = "data/data.conf"
    datas_src = commons.get_data()
    pz.dump_conf(datas_src, file_path)
    datas_dst = pz.load_conf(file_path)
    datas_dst = pz.data.io_conf.conf2dict(datas_dst, include_default=False)
    assert commons.obj2str(datas_src) == commons.obj2str(datas_dst)


def test_json_object():
    datas_src = commons.get_data()
    datas_tmp = pz.dump_json(datas_src)
    datas_dst = pz.load_json(datas_tmp)
    assert commons.obj2str(datas_src) == commons.obj2str(datas_dst)


def test_json_file():
    file_path = "data/data.json"
    datas_src = commons.get_data()
    pz.dump_json(datas_src, file_path)
    datas_dst = pz.load_json(file_path)
    assert commons.obj2str(datas_src) == commons.obj2str(datas_dst)


def test_toml_object():
    datas_src = commons.get_data()
    datas_tmp = pz.dump_toml(datas_src)
    datas_dst = pz.load_toml(datas_tmp)
    assert commons.obj2str(datas_src) == commons.obj2str(datas_dst)


def test_toml_file():
    file_path = "data/data.toml"
    datas_src = commons.get_data()
    pz.dump_toml(datas_src, file_path)
    datas_dst = pz.load_toml(file_path)
    assert commons.obj2str(datas_src) == commons.obj2str(datas_dst)


def test_yaml_object():
    datas_src = commons.get_data()
    datas_tmp = pz.dump_yaml(datas_src)
    datas_dst = pz.load_yaml(datas_tmp)
    assert commons.obj2str(datas_src) == commons.obj2str(datas_dst)


def test_yaml_file():
    file_path = "data/data.yaml"
    datas_src = commons.get_data()
    pz.dump_yaml(datas_src, file_path)
    datas_dst = pz.load_yaml(file_path)
    assert commons.obj2str(datas_src) == commons.obj2str(datas_dst)


if __name__ == "__main__":

    tests = (
        ("conf_object", test_conf_object),
        ("conf_file", test_conf_file),
        ("json_object", test_json_object),
        ("json_file", test_json_file),
        ("toml_object", test_toml_object),
        ("toml_file", test_toml_file),
        ("yaml_object", test_yaml_object),
        ("yaml_file", test_yaml_file),
    )

    for name, func in tests:
        print("[*] Testing %s()..." % name)
        func()

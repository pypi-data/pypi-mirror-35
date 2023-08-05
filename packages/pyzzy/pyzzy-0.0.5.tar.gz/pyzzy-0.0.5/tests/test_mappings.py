from pyzzy.utils.mappings import ChainMap, DeepChainMap, merge_dicts


db = {
    "production": "./production.db",
    "development": "./development.db",
}
db_production = {"production": "./production.db"}
db_development = {"development": "./development.db"}


def test_DeepChainMap():
    print("[*] Testing DeepChainMap()...")
    dicts = dict(db_production), dict(db_development)
    assert DeepChainMap(*dicts) == db


def test_DeepChainMap_set():
    print("[*] Testing DeepChainMap_set()...")
    dicts = dict(db_production), dict(db_development)
    dcm = DeepChainMap(*dicts)
    dcm["production"] = "./prod.db"
    dcm["development"] = "./dvpt.db"
    assert dcm == {"production": "./prod.db", "development": "./dvpt.db"}


def test_DeepChainMap_del():
    print("[*] Testing DeepChainMap_del()...")
    dicts = dict(db_production), dict(db_development)
    dcm = DeepChainMap(*dicts)
    del dcm["production"]
    del dcm["development"]
    assert dcm == {}


def test_DeepChainMap_merge():
    print("[*] Testing DeepChainMap_merge()...")
    dicts = dict(db_production), dict(db_development)
    assert DeepChainMap(*dicts).merge() == db


def test_merge_dicts():
    print("[*] Testing merge_dicts()...")
    dicts = dict(db_production), dict(db_development)
    assert db == merge_dicts(*dicts)


def main():
    test_DeepChainMap()
    test_DeepChainMap_set()
    test_DeepChainMap_del()
    test_DeepChainMap_merge()
    test_merge_dicts()


if __name__ == "__main__":
    main()

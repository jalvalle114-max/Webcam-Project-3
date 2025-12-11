import os
from modules.utils import save_pickle, load_pickle

def test_save_load():
    data = {"key": "value"}
    save_pickle("test.pkl", data)
    loaded = load_pickle("test.pkl")
    assert loaded == data
    os.remove("test.pkl")

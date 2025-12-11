import pickle
import os

def save_pickle(filename, data):
    with open(filename, "wb") as f:
        pickle.dump(data, f)

def load_pickle(filename):
    if not os.path.exists(filename):
        return None
    with open(filename, "rb") as f:
        return pickle.load(f)

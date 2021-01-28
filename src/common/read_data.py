"""
    Here, different local data will be loaded
"""
import pickle

from src.common.configuration import *
from src.common.common import *


def load_model(filepath, filename):
    # Loads trained machine learning models
    open_obj = open(absolute_path(filepath, filename), 'rb')
    model = pickle.load(open_obj)
    open_obj.close()

    return model

import pandas as pd
from flask import Flask
import os, sys

from src.common import global_object
from src.common.read_data import *


def app_initialization():
    app = Flask(__name__)

    # Loading model to global object
    global_object.close_price_predictor = load_model(Configuration().get_path_constant('model_path'),
                                                     Configuration().get_file_name('close_price_predictor_model'))
    global_object.sma_predictor = load_model(Configuration().get_path_constant('model_path'),
                                             Configuration().get_file_name('sma_predictor_model'))
    print("Trained models are loaded successfully.")

    @app.route('/', methods=['GET'])
    def home():
        # returns the home page
        return 'Welcome to Happy Stock'

    @app.route('/predict_entry_exit_point/', methods=['GET'])
    def predict_entry_exit_point():
        # It gives back the entry exit point for any stock
        pass

    return app


app = app_initialization()


if __name__ == '__main__':
    app.run()

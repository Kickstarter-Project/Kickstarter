from flask import Flask, render_template, request
import pickle
import numpy as np
from numpy.lib.function_base import quantile
from .model import query_model


def create_app():
    # initializes our app
    app = Flask(__name__)
    app.static_folder = 'static'

    @app.route('/')
    def form():
        return render_template('base.html')

    @app.route('/data/', methods=['POST', 'GET'])
    def data():
        if request.method == 'GET':
            return f"/data is accessed directly. Go to '/' to submit form"
        if request.method == 'POST':
            form_data = request.form
            campaign_name = request.form.get('campaign_name')
            campaign_length = request.form.get('campaign_length')
            percentage_pledged = request.form.get('percentage_pledged')
            currency = request.form.get('currency')
            category = request.form.get('category')
            num_backers = request.form.get('num_backers')
            prediction = query_model(currency, category, campaign_length, percentage_pledged, num_backers)
        return render_template('data.html', form_data=form_data, num_backers=num_backers, campaign_name=campaign_name, campaign_length=campaign_length, percentage_pledged=percentage_pledged, currency=currency, category=category, prediction=prediction)

    return app


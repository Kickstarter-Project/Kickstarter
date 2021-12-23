from flask import Flask, render_template, request
from .model import model
import pandas as pd


def create_app():
    '''Creates the application and displays it

    :returns: the flask appliction
    :rtype: flask app
    '''
    app = Flask(__name__)
    app.static_folder = 'static'

    @app.route('/')
    def form():
        ''' Creates the homepage

        :returns: renders the template for the page
        :rtype: html page via flask application
        '''
        return render_template('base.html', title="Kickstarter campaign")

    @app.route('/data', methods=['POST', 'GET'])
    def data():
        '''Creates the page that takes in user input , feeds through rf_model_pickle_2
           and returns a display of the prediction to the user via html page
        :returns: input outcome
        :rtype: html page
        '''
        if request.method == 'GET':
            return "/data is accessed directly. Go to '/' to submit form"
        if request.method == 'POST':
            form_data = request.form
            campaign_name = request.form.get('campaign_name')
            campaign_name_length = len(campaign_name)
            campaign_length = request.form.get('campaign_length')
            currency = request.form.get('currency')
            category = request.form.get('category')
            goal = request.form.get('goal')
            num_backers = request.form.get('num_backers')
            month = request.form.get('month')

            input_data = pd.DataFrame({'category': [category],
                                       'currency': [currency],
                                       'goal': [goal],
                                       'launched': [month],
                                       'backers': [num_backers],
                                       'campaign_length': [campaign_length],
                                       'name_char_length':
                                       [campaign_name_length]})

            prediction = model(input_data)[0].upper()

        return render_template('data.html',
                               form_data=form_data,
                               goal=goal,
                               month=month,
                               campaign_name_length=campaign_name_length,
                               num_backers=num_backers,
                               campaign_name=campaign_name,
                               campaign_length=campaign_length,
                               currency=currency,
                               category=category,
                               prediction=prediction)

    @app.route('/features')
    def vis():
        '''
        :returns:
        :rtype: html page
        '''
        return render_template('index.html')

    return app

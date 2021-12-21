# WORKING DOCUMENT #
''' This is me trying to understand the input for the model. 

input_currency will not take a string value, nor will input_category

need to reconnect with roger to discuss how to format user inputted data to fit with the model '''

import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))

list_currencies = ['AUD','CAD', 'CHF', 'DKK', 'EUR','GBP', 'HKD', 
                 'JPY', 'MXN','NOK','NZD', 'SEK', 'SGD','USD']
list_categories = ['Art', 'Comics', 'Crafts','Dance', 'Design','Fashion','Film & Video',
                   'Food', 'Games','Journalism','Music', 'Photography',
                   'Publishing', 'Technology','Theater']

def currency_category_select(user_input,list_input):
    for x in range(len(list_input)):
        if list_input[x] == user_input:
            list_input[x] = 1
        else:
            list_input[x] = 0
    return list_input 

# currency = 'HKD'
# category = 'Fashion'
# percentage_pledged = 95
# input_backers = 2000
# input_currency=currency_category_select(currency,list_currencies)
# input_category=currency_category_select(category,list_categories)
# campaign_length = 200
# num_backers = 200

def query_model(currency, category, campaign_length, percentage_pledged, num_backers):
    input_currency=currency_category_select(currency,list_currencies)
    input_category=currency_category_select(category,list_categories)
    model_input = np.array([campaign_length,percentage_pledged,num_backers])
    model_input = np.append(model_input,input_currency)
    model_input = np.append(model_input,input_category).reshape(1, -1)

    if model.predict(model_input)[0] == 1:
        prediction = 'Your kickstarter will be a success!'
    else: 
        prediction = "Your kickstarter will likely fail, try again!"

    return(prediction)



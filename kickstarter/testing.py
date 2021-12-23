import pandas as pd
from model import model
import pickle


# Placeholders to initialize model
category = 'Fashion'
currency = 'USD'
goal = 1000
month = 'july'
num_backers= 10
campaign_length = 20
campaign_name_length = 20


input_data = pd.DataFrame({'category':[category],'currency':[currency],
'goal':[goal],'launched':[month],'backers':[num_backers],
'campaign_length':[campaign_length],'name_char_length':[campaign_name_length]})
prediction = model(input_data)

def model(input_data):
    rf = pickle.load(open('rf_model_pickle_2.pkl', 'rb'))
    pred = rf.predict(input_data)
    return print(pred)

model(input_data)

rf = pickle.load(open('rf_model_pickle_2.pkl', 'rb'))
pred = rf.predict(input_data)




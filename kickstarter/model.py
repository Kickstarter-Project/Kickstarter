
import pickle
import numpy as np


model = pickle.load(open('model.pkl', 'rb'))

campaign_length = 10
percentage_pledged = 20
backers = 20
input_currency = 1
input_category = 0



model_input = np.array([campaign_length,percentage_pledged,backers])
model_input = np.append(model_input,input_currency)
model_input = np.append(model_input,input_category).reshape(1, -1)

if model.predict(model_input)[0] == 1:
    print('Your kickstarter is a success!')
else: 
    print('Your kickstarter failed, try again.')


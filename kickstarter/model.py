import pickle


def model(input_data):
    ''' Takes user input and returns prediciton

    :param input_data:
    :type: pandas dataframe
    :returns: given input data, 1 or 0 based on pickled model
    :rtype: array 1 or 0
    '''
    rf = pickle.load(open('rf_model_pickle_2.pkl', 'rb'))
    pred = rf.predict(input_data)
    return pred

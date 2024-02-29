import  json
import pickle
import numpy as np


__site_location = None
__data_columns = None
__model = None

def get_estimated_price(site_location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(site_location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return  round(__model.predict([x]) [0],2)

def get_location_name():
    return __site_location

def load_save_artifatacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global  __site_location

    with open("./artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __site_location = __data_columns[3:]

    global  __model
    with open("./artifacts/Pune_home_prices_model.pickle",'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")

if __name__ == "__main__":
    load_save_artifatacts()
    print(get_location_name())
    print(get_estimated_price('baner',1500,3,3))
    print(get_estimated_price('baner',1000,2,2))
    print(get_estimated_price('balaji nagar',1500,3,3))
    print(get_estimated_price('dapodi',1000,2,2))

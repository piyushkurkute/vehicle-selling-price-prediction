import numpy as np
import pandas as pd
import pickle
import json

__columns	= None
__predDf	= None
__model		= pickle.load(open('vehicle_selling_price_prediction_model.pkl','rb'))

# data columns: 
# [present_price', 'kms_driven', 'owner', 'no_year', 'fuel_type_diesel',
# 'fuel_type_petrol', 'seller_type_individual', 'transmission_manual']

def loadModelData():
	global __model, __columns

	if __columns == None:
		__columns	= json.load(open('data_columns.json','r'))
		__columns	= __columns['data_columns']

	pass

def setData(request_data):
	global __predDf

	vals = np.zeros(len(__columns)).astype(int).reshape(1,len(__columns))
	__predDf = pd.DataFrame(data=vals, columns=__columns)

	__predDf['present_price'] = float(request_data['present_price']) / 100000
	__predDf['kms_driven'] = int(request_data['kms_driven'])
	__predDf['owner'] = int(request_data['owner'])
	__predDf['no_year'] = int(2020 - int(request_data['year']))

	if request_data['fuel_type'] == 'diesel':
		__predDf['fuel_type_diesel'] = 1

	if request_data['fuel_type'] == 'petrol':
		__predDf['fuel_type_petrol'] = 1

	if request_data['seller_type'] == 'individual':
		__predDf['seller_type_individual'] = 1

	if request_data['transmission_type'] == 'manual':
		__predDf['transmission_manual'] = 1

	pass

def predictSellingPrice(request_data):
	loadModelData()
	setData(request_data)
	predicted_price = __model.predict(__predDf)
	predicted_price = round(float(predicted_price) * 100000)
	return predicted_price
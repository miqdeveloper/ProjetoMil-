from buy_digital import buy_digital_action
import pandas as pd
import json
from joblib import dump, load
from time import strftime
from sklearn.preprocessing import  StandardScaler
#from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import *
from sklearn.metrics import r2_score, mean_squared_error
import time, os
import numpy as np
#from buy import buy
from iqoptionapi.stable_api import IQ_Option

Pkl_Filename = "filename_save1.joblib" 





class reg_linear():
	def __init__(self):
		#import start_bot
		 
		#self.contador = start_bot.main()	
		self.buy_d = buy_digital_action()

		with open("config/program_config.json", "r") as arch:
			self.j = json.loads(arch.read())
			self.ativo = str(self.j['ativo'])
			self.money = int(self.j['money'])
			self.time = int(self.j['time'])
			self.call = str(self.j['call'])
			self.put = str(self.j['put'])




	def calc_reg(self):
		#time.sleep(timer) # Resultado para cada 59 segundos. Altere se quiser
		try:
			self.dataframe = pd.DataFrame()
			self.read = pd.read_csv("iqdataset.csv", delimiter = ";")
			self.dataframe['x'] = self.read["timestamp"] 
			self.dataframe['y'] = self.read["kclose"]

			self.x_values       = np.array(self.dataframe[['x']])
			self.y_values       = np.array(np.log(np.round(self.dataframe[['y']], decimals=5)))
			#y_values = dataframe[['y']]
			self.scaler = StandardScaler().fit(self.y_values)
			self.y_values = self.scaler.transform(self.y_values)

			#x_train, x_test, y_train, y_test = train_test_split(x_values, y_values, train_size=0.80)

			self.model = load(Pkl_Filename)
			self.fit = self.model.fit(self.x_values, self.y_values)
			#dump(self.fit, Pkl_Filename) 

			self.preditx = self.model.predict(self.x_values)

			self.MSE = mean_squared_error(self.y_values, self.preditx)
			self.CED = round(r2_score(self.y_values, self.preditx), 2)


			self.time_day = strftime("%H:%M:%S")
			#print("Row: %i" % i)
			print("chance de Alta r2:| {} || {} |".format(self.CED, self.time_day))
			print("mse:", self.MSE)
			print('')
			#print('Coeficiente -> coef_ -->', self.model.coef_)
			self.y_pred = self.model.predict(self.x_values)
			#self.y_pred_1 = self.y_pred[30]
			self.y_pred_2 = self.y_pred[60]
			#self.y_pred_3 = self.y_pred[60]
			#print(self.y_pred)
			#print(r2_score(y_test, y_pred))
			#print('Preditativa_1 ->', self.y_pred_1)
			#print('Preditativa_2 ->', self.y_pred_2)
			#print(self.str_var)
			if self.CED  >= 0.57:
				#if str(self.y_pred_2[0]) == "-":
				self.buy_d.call_buy_dig(self.ativo, self.money, self.call, self.time)
				#print("pred_put-->", self.y_pred_2)
				print("Compra - Call")
				print('\n')

			else:
				self.buy_d.call_buy_dig(self.ativo, self.money, self.put, self.time)
				#print("pred_call -->", self.y_pred_2)
				print("Venda - Put")
				print('\n')
				#self.contador.lose+=1
				#self.contador.win+=1
				#print("Ganhos e perdas --> {}/{}".format(self.contador.win, self.contador.lose))	
			os.remove("iqdataset.csv")
			print('\n')
		except Exception as error:
			print("Linear.reg_linear --> ", error)

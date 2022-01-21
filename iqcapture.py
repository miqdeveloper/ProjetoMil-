from os import path, remove
from Linear import reg_linear
from time import strftime
from iqoptionapi.stable_api import IQ_Option
from json import loads
from random import randint


class IQ_capture():
	def __init__(self):
		
		self.reg = reg_linear()

		self.file_archive = "iqdataset.csv"
		
		if path.exists(self.file_archive):
			print("Arquivo --> ", self.file_archive)
			with open(self.file_archive, "w+") as file_csv:
				file_csv.write("timestamp;kclose\n")
				file_csv.close()
				print("Arquivo pronto...")

		else:
			print("Criando arquivo...")
			with open(self.file_archive, "w") as create_file:
				create_file.write("timestamp;kclose\n")
				create_file.close()
				print("Arquivo criado...")

		self.file_json = "config/dates_config.json"
		self.program_json = "config/program_config.json"
		#self.file_useragentxt = "http/useragents.txt"
		#self.file_proxy = "http/proxys.txt"

		with open(self.file_json, 'r+') as file_json:
			json_loads = loads(file_json.read())
			self.email = json_loads['email']
			self.passw = json_loads['senha']
			self.account = json_loads['account']

		with open(self.program_json, 'r+') as file_program_json:
			json_program_loads = loads(file_program_json.read())
			self.active = json_program_loads["ativo"]
			self.qdates =  json_program_loads["qdates"]
			self.money = json_program_loads["money"]
			self.time = json_program_loads["time"]

	def IQconnect(self):
		import json		
		try:
			self.iq_ = IQ_Option(self.email, self.passw)
			#self.iq_.set_session(self.header_, self.proxy_)
			self.status, self.x_undefined = self.iq_.connect()
			if self.status:
				print("Conectado...")
				try:
					self.x = 0					
					while self.x <= int(self.qdates):

						self.size = 1
						self.maxdict = 10
						self.iq_.start_candles_stream(self.active, self.size, self.maxdict)

						self.cap_candles = self.iq_.get_realtime_candles(self.active, self.size)
						
						self.time_stamp = [x for x in self.cap_candles]
						self.timeself_x  = int(self.time_stamp[0])
						self.cap_candles[self.timeself_x]			
						
						self.json_load_x = json.dumps(self.cap_candles[self.timeself_x])
						self.load_dates_x = json.loads(self.json_load_x)
						#Dados Close
						#print(x, load_dates_x['close'])
						with open("iqdataset.csv", "a") as file:
							file = file.write("{};{}\n".format(self.timeself_x, self.load_dates_x['close']))
							self.x+=1
					else:
						print("Calculando...")						
						self.reg.calc_reg()
						

				except Exception as error:
						print("Error: Func.IQconnect --> ", error)
						
			else:
				print("Não conectado...")
				#print(x_undefined)
				pass
		except KeyboardInterrupt as e:
			print("Saindo...")
			exit()

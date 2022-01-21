import json

class jsonSerialize():
		def __init__(self):
			self.path = "config/martin.json"
			#self.obj_dict = ["-10", "2"]

		def Dates(self):
			with open(self.path, "r+") as self.file_json:
				self.str_json = json.loads(self.file_json.read())
				self.file_json.close()
				return self.str_json

		def UpdateData(self, mart, loss):

			self.obj  = self.Dates()
			self.mart = mart
			self.loss = loss

			if int(self.obj['loss']) < 1:

				self.obj['mart'] = str(self.mart)
				self.obj['loss'] = str(int(self.obj['loss'])+1)

				with open(self.path, "w+") as self.file_json_w:
					self.dump = json.dump(self.obj, self.file_json_w)
					self.file_json_w.close()
			else:

				self.obj['mart'] = "0"
				self.obj['loss'] = "0"
				with open(self.path, "w+") as self.file_json_w:
					self.dump = json.dump(self.obj, self.file_json_w)
					self.file_json_w.close()


			#return self.dump




#json_= jsonSerialize()

#print("Dado o objeto", json_.Dates())

#print(json_.UpdateData("-50", loss="1"))
#print("novos dados", json_.UpdateData("10", "0"))

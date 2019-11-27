# -*- coding: utf-8 -*-

from os import listdir, getcwd
from json import loads, dumps


default = {
	"extensionList": {
		"images": ['jpg', 'bmp', 'png', 'jpeg', 'gif'],
		"documents": ['doc', 'docx', 'pptx', 'pdf', 'xls', 'xlsx', 'xlsm'],
		"audios": ['ogg', 'mp3'],
		"videos": ['mp4']
	},
	"trackingFolder": "",
	"Aud": "",
	"Doc": "",
	"Img": "",
	"Vid": "",
	"dTrackingFolder": "",
	"dAud": "",
	"dDoc": "",
	"dImg": "",
	"dVid": "",
	"trackingDefState": 0,
	"audDefState": 0,
	"docDefState": 0,
	"imgDefState": 0,
	"vidDefState": 0
}


class JsonHandler:

	def __init__(self):
		self.default = default
		self.generateConfig()


	def read(self, field = None):
		with open("config.json", "r+", encoding="utf-8") as file:
			data = loads(file.read())

		if field is not None and field in data:
			return data[field]
		else:
			return data


	def write(self, field, value):
		data = self.read()

		if field in data:

			if "**default**" in str(value):
				data[field] = self.default[field]

			else:
				if isinstance(data[field], list):
					if isinstance(value, list):
						data[field] = value
					else:
						data[field].append(value)
				else:
					data[field] = value

			with open("config.json", "w", encoding="utf-8") as file:
				file.write(dumps(data, ensure_ascii=False, indent=4))


	def reset(self, field, value):
		data = self.read()

		if field in data:

			if "**default**" in str(value):
				with open("config_copy.json", "w", encoding="utf-8") as file:
					file.write(dumps(data, ensure_ascii=False, indent=4))

				data = self.default

			else:
				if isinstance(data[field], list):
					if isinstance(value, list):
						for value_ in value:
							if value_ in data[field]:
								data[field].remove(value_)
					else:
						if value in data[field]:
							data[field].remove(value)
				else:
					data[field] = value

			with open("config.json", "w", encoding="utf-8") as file:
				file.write(dumps(data, ensure_ascii=False, indent=4))


	def generateConfig(self):
		listDir = listdir(getcwd())

		if "config.json" not in listDir:	
			with open("config.json", "w", encoding="utf-8") as file:
				file.write(dumps(self.default, ensure_ascii=False, indent=4))

		elif "config.json" in listDir:
			data = self.read()

			for k, v in self.default.items():
				if k not in data:
					with open("config.json", "w", encoding="utf-8") as file:
						file.write(dumps(self.default, ensure_ascii=False, indent=4))
						return
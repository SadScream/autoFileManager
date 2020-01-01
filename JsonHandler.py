# -*- coding: utf-8 -*-

from os import listdir, getcwd
from json import loads, dumps


default = {
	"version": 0.3,
	"extensionList": {
		"images": ['jpg', 'jpeg', 'bmp', 'dib', 'png', 'gif', 'tiff', 'tif'],
		"documents": [
			'doc', 'docx', 'docm', 'dotx', 'dotm',
			'xls', 'xlsx', 'xlsm', 'xltx', 'xltm', 'xlsb', 'xlam', 
			'pptx', 'ppt', 'pptm', 'ppsm', 'potx',
			'txt', 'pdf'
			],
		"audios": ['ogg', 'mp3', 'm4r', 'aac', 'aiff', 'wav', 'wma'],
		"videos": ['mp4', 'mpeg', 'avi']
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
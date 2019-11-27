from watchdog.events import FileSystemEventHandler
from re import findall
from time import sleep
import os

import JsonHandler

config = JsonHandler.JsonHandler()


class Event(FileSystemEventHandler):

	def __init__(self, paths):
		# print(paths)
		self.trackingFolder = paths["TrackingFolder"]
		self.destinations = [v for k, v in paths.items()][1:]

	def on_created(self, event):
		sleep(4)
		self.on_moved(event)

	def on_moved(self, event):
		extensionList = config.read("extensionList")

		for filename in os.listdir(self.trackingFolder):
			default = os.path.join(self.trackingFolder, filename)
			new = default

			if any(_ in filename.split('.')[-1] for _ in extensionList["images"]):
				position = 2
			elif any(_ in filename.split('.')[-1] for _ in extensionList["documents"]):
				position = 1
			elif any(_ in filename.split('.')[-1] for _ in extensionList["audios"]):
				position = 0
			elif any(_ in filename.split('.')[-1] for _ in extensionList["videos"]):
				position = 3
			else:
				continue

			if not len(self.destinations[position]):
				continue

			if filename not in os.listdir(self.destinations[position]): # есть ли уже в папке файл с таким названием
				new = os.path.join(self.destinations[position], filename)
			else:
				new = self.processingFile(filename, self.destinations[position])

			if new != default:
				os.rename(default, new)


	def processingFile(self, filename, destination):
		'''
		формирование файла с новым названием, т.к файл с первоначальным названием уже существует
		например: мы скачали изображение hello.jpg, но оно уже есть в конечной папке, значит в конечную папку этот файл перенесется с именем hello_1.jpg
		все последующие файлы с таким названием будут записываться как hello_2.jpg, hello_3.jpg и так далее
		'''

		fileDigit = 1
		fileExtension = filename.split('.')[-1]

		splited = findall(r"_.+", filename)
		splited_file_name = findall(r".+_", filename)

		if len(splited_file_name):
			splited_file_name = splited_file_name[0][:-1]
		else:
			splited_file_name = '.'.join(filename.split('.')[:-1])

		if len(splited):
			splited = splited[0].split('.')

			if len(splited) > 1:
				splited = splited[0].split("_")[-1]

				if splited.isdigit():
					fileDigit = int(splited)

			elif len(splited) == 1:

				for i, letter in enumerate(splited[0]):
					if letter == "_":
						fileDigit = 0

						while splited[0][i+1].isdigit():
							fileDigit += 1
							i += 1
						break
		else:
			filesList = [_ for _ in os.listdir(destination) if ''.join(filename.split(".")[:-1]) in _]
			fileDigit = len(filesList)

		fileName = f"{splited_file_name}_{fileDigit}.{fileExtension}"

		while fileName in os.listdir(destination):
			fileDigit += 1
			fileName = f"{splited_file_name}_{fileDigit}.{fileExtension}"

		return os.path.join(destination, fileName)
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime
from threading import Thread
from getpass import getuser
from time import sleep
from re import findall

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import os
import sys

import JsonHandler
from design import Ui_MainWindow


class Event(FileSystemEventHandler):

	def __init__(self, paths):
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


class Window(QMainWindow, Ui_MainWindow):

	def __init__(self):
		self.init_observer()
		super().__init__()
		self.setupUi(self)
		self.constructor()
		self.show()

	def closeEvent(self, e): # событие нажатия крестик
		self.observer.stop()
		self.observer.join()

		while True:
			if not self.observer.is_alive():
				sys.exit(0)

	def init_observer(self):
		self.observer = Observer()
	

	def constructor(self):
		self.setFocus()

		config.write("dTrackingFolder", f"C:\\Users\\{USER}\\Downloads")
		config.write("dAud", f"C:\\Users\\{USER}\\Music")
		config.write("dDoc", f"C:\\Users\\{USER}\\Documents")
		config.write("dImg", f"C:\\Users\\{USER}\\Pictures")
		config.write("dVid", f"C:\\Users\\{USER}\\Videos")

		# binding check buttons and setting states from config
		self.trackingDef.stateChanged.connect(self.trackingDefStateChanged)
		self.audDef.stateChanged.connect(self.audStateChanged)
		self.docDef.stateChanged.connect(self.docStateChanged)
		self.imgDef.stateChanged.connect(self.imgStateChanged)
		self.vidDef.stateChanged.connect(self.vidStateChanged)

		self.trackingFolder.setText(config.read("trackingFolder"))
		self.Aud.setText(config.read("Aud"))
		self.Doc.setText(config.read("Doc"))
		self.Img.setText(config.read("Img"))
		self.Vid.setText(config.read("Vid"))

		self.trackingDef.setCheckState(config.read("trackingDefState"))
		self.audDef.setCheckState(config.read("audDefState"))
		self.docDef.setCheckState(config.read("docDefState"))
		self.imgDef.setCheckState(config.read("imgDefState"))
		self.vidDef.setCheckState(config.read("vidDefState"))
		#

		# binding folder paths
		self.trackingFolder.textEdited.connect(self.trackingChanged)
		self.Aud.textEdited.connect(self.audChanged)
		self.Doc.textEdited.connect(self.docChanged)
		self.Img.textEdited.connect(self.imgChanged)
		self.Vid.textEdited.connect(self.vidChanged)
		#

		self.startBtn.clicked.connect(self.start)
		self.stopBtn.clicked.connect(self.stopTargeting)


	def start(self):
		paths = self.check_fields()

		if not paths:
			return

		self.widgetsEnabled(False)

		self.init_observer()
		event = Event(paths)
		self.observer.schedule(event, paths["TrackingFolder"], recursive=True)
		self.observer.start()


	def message(self, text):
		self.show_message = QMessageBox(self)
		self.show_message.setWindowIcon(self.icon)
		self.show_message.setIcon(QMessageBox.Information)
		self.show_message.setText(text)
		self.show_message.setWindowTitle("Информация")
		self.show_message.exec_()


	def check_fields(self):
		if not len(config.read("trackingFolder")) or not os.path.isabs(config.read("trackingFolder")):
			self.message("Поле отслеживаемой папки не может быть пустым.")
			return False

		track = ["dTrackingFolder", config.read("trackingFolder"), config.read("trackingDefState")]
		aud = ["dAud", config.read("Aud"), config.read("audDefState")]
		doc = ["dDoc", config.read("Doc"), config.read("docDefState")]
		img = ["dImg", config.read("Img"), config.read("imgDefState")]
		vid = ["dVid", config.read("Vid"), config.read("vidDefState")]

		items = [track, aud, doc, img, vid]
		paths = {}

		for i, item in enumerate(items):
			if item[2] == 2:
				items[i][1] = config.read(items[i][0])

			if os.path.isabs(item[1]) and not os.path.exists(item[1]):
				if item[1] not in ["C:\\", "D:\\", "E:\\", "F:\\", "G:\\", "H:\\"]:
					os.mkdir(item[1])

			paths[item[0][1:]] = item[1]

		return paths


	def trackingChanged(self):
		if os.path.isabs(self.trackingFolder.text()) or "".join(self.trackingFolder.text().split(' ')) == "":
			config.write("trackingFolder", self.trackingFolder.text())

	def audChanged(self):
		if os.path.isabs(self.Aud.text()) or "".join(self.Aud.text().split(' ')) == "":
			config.write("Aud", self.Aud.text())

	def docChanged(self):
		if os.path.isabs(self.Doc.text()) or "".join(self.Doc.text().split(' ')) == "":
			config.write("Doc", self.Doc.text())

	def imgChanged(self):
		if os.path.isabs(self.Img.text()) or "".join(self.Img.text().split(' ')) == "":
			config.write("Img", self.Img.text())

	def vidChanged(self):
		if os.path.isabs(self.Vid.text()) or "".join(self.Vid.text().split(' ')) == "":
			config.write("Vid", self.Vid.text())


	def trackingDefStateChanged(self):
		state = self.trackingDef.checkState()

		config.write("trackingDefState", state)

		if state == 2:
			self.trackingFolder.setText(config.read("dTrackingFolder"))
			self.trackingFolder.setEnabled(False)
		else:
			self.trackingFolder.setText(config.read("trackingFolder"))
			self.trackingFolder.setEnabled(True)

	def audStateChanged(self):
		state = self.audDef.checkState()

		config.write("audDefState", state)

		if state == 2:
			self.Aud.setText(config.read("dAud"))
			self.Aud.setEnabled(False)
		else:
			self.Aud.setText(config.read("Aud"))
			self.Aud.setEnabled(True)

	def docStateChanged(self):
		state = self.docDef.checkState()

		config.write("docDefState", state)

		if state == 2:
			self.Doc.setText(config.read("dDoc"))
			self.Doc.setEnabled(False)
		else:
			self.Doc.setText(config.read("Doc"))
			self.Doc.setEnabled(True)

	def imgStateChanged(self):
		state = self.imgDef.checkState()

		config.write("imgDefState", state)

		if state == 2:
			self.Img.setText(config.read("dImg"))
			self.Img.setEnabled(False)
		else:
			self.Img.setText(config.read("Img"))
			self.Img.setEnabled(True)

	def vidStateChanged(self):
		state = self.vidDef.checkState()

		config.write("vidDefState", state)

		if state == 2:
			self.Vid.setText(config.read("dVid"))
			self.Vid.setEnabled(False)
		else:
			self.Vid.setText(config.read("Vid"))
			self.Vid.setEnabled(True)

	def widgetsEnabled(self, arg):
		self.startBtn.setEnabled(arg)
		self.stopBtn.setEnabled(True if arg==False else False)
		self.groupBox.setEnabled(arg)
		self.trackingFolder.setEnabled(arg)
		self.trackingDef.setEnabled(arg)

	def stopTargeting(self):
		self.observer.stop()
		self.observer.join()
		if not self.observer.is_alive():
			self.widgetsEnabled(True)


if __name__=="__main__":
	USER = getuser()
	config = JsonHandler.JsonHandler()
	app = QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec_())
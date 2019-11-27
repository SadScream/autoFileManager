__version__ = 0.2
__developer__ = False

'''
if __developer__ = true so the default folders fields will contain my personal paths like D:/_Pictures
else it will contains smth like C:/Users/User/Documents
'''

import fix_qt_import_error

from watchdog.observers import Observer
from getpass import getuser
from time import sleep

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import os
import sys

import JsonHandler
from EventHandler import Event
from design import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):

	def __init__(self):
		self.init_observer()

		super().__init__()
		self.setupUi(self)
		self.constructor()
		self.show()

	def closeEvent(self, e): # событие нажатия крестик
		self.observer.stop()
		
		if self.observer.is_alive():
			self.observer.join()

		while True:
			if not self.observer.is_alive():
				sys.exit(0)

	def init_observer(self):
		self.observer = Observer()
	

	def constructor(self):
		self.setFocus()
		self.versionLabel.setText(f"Version: {__version__}")

		if __developer__ == False:
			config.write("dTrackingFolder", f"C:/Users/{USER}/Downloads")
			config.write("dAud", f"C:/Users/{USER}/Music")
			config.write("dDoc", f"C:/Users/{USER}/Documents")
			config.write("dImg", f"C:/Users/{USER}/Pictures")
			config.write("dVid", f"C:/Users/{USER}/Videos")
		else:
			config.write("dTrackingFolder", f"D:/Downloaded")
			config.write("dAud", f"D:/_Audios")
			config.write("dDoc", f"D:/_Documents")
			config.write("dImg", f"D:/_Pictures")
			config.write("dVid", f"D:/_Videos")

		# binding folder buttons
		self.getTrackingPath.clicked.connect(self.openGetTrackingPath)
		self.getAudPath.clicked.connect(self.openGetAudPath)
		self.getDocPath.clicked.connect(self.openGetDocPath)
		self.getImgPath.clicked.connect(self.openGetImgPath)
		self.getVidPath.clicked.connect(self.openGetVidPath)
		#

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

		self.trackingFolder.textChanged.connect(self.trackingChanged)
		self.Aud.textChanged.connect(self.audChanged)
		self.Doc.textChanged.connect(self.docChanged)
		self.Img.textChanged.connect(self.imgChanged)
		self.Vid.textChanged.connect(self.vidChanged)
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
				if item[1] not in ["C:/", "D:/", "E:/", "F:/", "G:/", "H:/"]:
					os.mkdir(item[1])

			paths[item[0][1:]] = item[1]

		return paths


	def openGetTrackingPath(self):
		directory = QFileDialog.getExistingDirectory(None, 'Выберите папку:', self.trackingFolder.text(), QFileDialog.ShowDirsOnly)

		if len(directory):
			self.trackingFolder.setText(directory)

	def openGetAudPath(self):
		directory = QFileDialog.getExistingDirectory(None, 'Выберите папку:', self.Aud.text(), QFileDialog.ShowDirsOnly)

		if len(directory):
			self.Aud.setText(directory)

	def openGetDocPath(self):
		directory = QFileDialog.getExistingDirectory(None, 'Выберите папку:', self.Doc.text(), QFileDialog.ShowDirsOnly)

		if len(directory):
			self.Doc.setText(directory)

	def openGetImgPath(self):
		directory = QFileDialog.getExistingDirectory(None, 'Выберите папку:', self.Img.text(), QFileDialog.ShowDirsOnly)

		if len(directory):
			self.Img.setText(directory)

	def openGetVidPath(self):
		directory = QFileDialog.getExistingDirectory(None, 'Выберите папку:', self.Vid.text(), QFileDialog.ShowDirsOnly)

		if len(directory):
			self.Vid.setText(directory)


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
			self.getTrackingPath.setEnabled(False)
		else:
			self.trackingFolder.setText(config.read("trackingFolder"))
			self.trackingFolder.setEnabled(True)
			self.getTrackingPath.setEnabled(True)			

	def audStateChanged(self):
		state = self.audDef.checkState()

		config.write("audDefState", state)

		if state == 2:
			self.Aud.setText(config.read("dAud"))
			self.Aud.setEnabled(False)
			self.getAudPath.setEnabled(False)
		else:
			self.Aud.setText(config.read("Aud"))
			self.Aud.setEnabled(True)
			self.getAudPath.setEnabled(True)

	def docStateChanged(self):
		state = self.docDef.checkState()

		config.write("docDefState", state)

		if state == 2:
			self.Doc.setText(config.read("dDoc"))
			self.Doc.setEnabled(False)
			self.getDocPath.setEnabled(False)
		else:
			self.Doc.setText(config.read("Doc"))
			self.Doc.setEnabled(True)
			self.getDocPath.setEnabled(True)

	def imgStateChanged(self):
		state = self.imgDef.checkState()

		config.write("imgDefState", state)

		if state == 2:
			self.Img.setText(config.read("dImg"))
			self.Img.setEnabled(False)
			self.getImgPath.setEnabled(False)
		else:
			self.Img.setText(config.read("Img"))
			self.Img.setEnabled(True)
			self.getImgPath.setEnabled(True)

	def vidStateChanged(self):
		state = self.vidDef.checkState()

		config.write("vidDefState", state)

		if state == 2:
			self.Vid.setText(config.read("dVid"))
			self.Vid.setEnabled(False)
			self.getVidPath.setEnabled(False)
		else:
			self.Vid.setText(config.read("Vid"))
			self.Vid.setEnabled(True)
			self.getVidPath.setEnabled(True)


	def message(self, text):
		self.show_message = QMessageBox(self)
		icon = QIcon()
		icon.addPixmap(QPixmap(":/icons/icons/folder.png"), QIcon.Normal, QIcon.Off)
		self.show_message.setWindowIcon(icon)
		self.show_message.setIcon(QMessageBox.Information)
		self.show_message.setText(text)
		self.show_message.setWindowTitle("Информация")
		self.show_message.exec_()


	def widgetsEnabled(self, arg):
		self.startBtn.setEnabled(arg)
		self.stopBtn.setEnabled(True if arg==False else False)
		self.groupBox.setEnabled(arg)
		self.trackingFolder.setEnabled(arg)
		self.trackingDef.setEnabled(arg)
		self.getTrackingPath.setEnabled(arg)


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
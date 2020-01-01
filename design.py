# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

	tray_icon = None

	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.setEnabled(True)
		MainWindow.resize(491, 201)
		MainWindow.setMinimumSize(QtCore.QSize(491, 201))
		MainWindow.setMaximumSize(QtCore.QSize(491, 201))
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/icons/icons/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		MainWindow.setWindowIcon(icon)
		MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: rgb(229, 229, 229);\n"
"}")
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.trackingLabel = QtWidgets.QLabel(self.centralwidget)
		self.trackingLabel.setGeometry(QtCore.QRect(10, 11, 141, 16))
		self.trackingLabel.setStyleSheet("QLabel {\n"
"    font: 13px;\n"
"}")
		self.trackingLabel.setObjectName("trackingLabel")
		self.trackingFolder = QtWidgets.QLineEdit(self.centralwidget)
		self.trackingFolder.setGeometry(QtCore.QRect(153, 10, 201, 20))
		self.trackingFolder.setObjectName("trackingFolder")
		self.trackingDef = QtWidgets.QCheckBox(self.centralwidget)
		self.trackingDef.setGeometry(QtCore.QRect(380, 11, 91, 17))
		self.trackingDef.setObjectName("trackingDef")
		self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBox.setEnabled(True)
		self.groupBox.setGeometry(QtCore.QRect(10, 40, 471, 121))
		self.groupBox.setStyleSheet("")
		self.groupBox.setFlat(False)
		self.groupBox.setObjectName("groupBox")
		self.endImgLabel = QtWidgets.QLabel(self.groupBox)
		self.endImgLabel.setGeometry(QtCore.QRect(20, 67, 91, 16))
		self.endImgLabel.setStyleSheet("QLabel {\n"
"    font: 13px;\n"
"}")
		self.endImgLabel.setObjectName("endImgLabel")
		self.endVidLabel = QtWidgets.QLabel(self.groupBox)
		self.endVidLabel.setGeometry(QtCore.QRect(20, 90, 91, 16))
		self.endVidLabel.setStyleSheet("QLabel {\n"
"    font: 13px;\n"
"}")
		self.endVidLabel.setObjectName("endVidLabel")
		self.endDocLabel = QtWidgets.QLabel(self.groupBox)
		self.endDocLabel.setGeometry(QtCore.QRect(20, 44, 91, 16))
		self.endDocLabel.setStyleSheet("QLabel {\n"
"    font: 13px;\n"
"}")
		self.endDocLabel.setObjectName("endDocLabel")
		self.endAudLabel = QtWidgets.QLabel(self.groupBox)
		self.endAudLabel.setGeometry(QtCore.QRect(20, 21, 91, 16))
		self.endAudLabel.setStyleSheet("QLabel {\n"
"    font: 13px;\n"
"}")
		self.endAudLabel.setObjectName("endAudLabel")
		self.Aud = QtWidgets.QLineEdit(self.groupBox)
		self.Aud.setGeometry(QtCore.QRect(113, 20, 231, 20))
		self.Aud.setStyleSheet("")
		self.Aud.setPlaceholderText("")
		self.Aud.setObjectName("Aud")
		self.Doc = QtWidgets.QLineEdit(self.groupBox)
		self.Doc.setGeometry(QtCore.QRect(113, 43, 231, 20))
		self.Doc.setPlaceholderText("")
		self.Doc.setObjectName("Doc")
		self.Img = QtWidgets.QLineEdit(self.groupBox)
		self.Img.setGeometry(QtCore.QRect(113, 66, 231, 20))
		self.Img.setPlaceholderText("")
		self.Img.setObjectName("Img")
		self.Vid = QtWidgets.QLineEdit(self.groupBox)
		self.Vid.setGeometry(QtCore.QRect(113, 89, 231, 20))
		self.Vid.setPlaceholderText("")
		self.Vid.setObjectName("Vid")
		self.audDef = QtWidgets.QCheckBox(self.groupBox)
		self.audDef.setGeometry(QtCore.QRect(370, 21, 91, 17))
		self.audDef.setObjectName("audDef")
		self.docDef = QtWidgets.QCheckBox(self.groupBox)
		self.docDef.setGeometry(QtCore.QRect(370, 44, 91, 17))
		self.docDef.setObjectName("docDef")
		self.imgDef = QtWidgets.QCheckBox(self.groupBox)
		self.imgDef.setGeometry(QtCore.QRect(370, 67, 91, 17))
		self.imgDef.setObjectName("imgDef")
		self.vidDef = QtWidgets.QCheckBox(self.groupBox)
		self.vidDef.setGeometry(QtCore.QRect(370, 90, 91, 17))
		self.vidDef.setObjectName("vidDef")
		self.getAudPath = QtWidgets.QPushButton(self.groupBox)
		self.getAudPath.setGeometry(QtCore.QRect(347, 19, 20, 21))
		self.getAudPath.setStyleSheet("QPushButton {\n"
"border: none;\n"
"background-color: rgb(229, 229, 229);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(203, 203, 203);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(168, 168, 168);\n"
"}")
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(":/icons/icons/open_folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.getAudPath.setIcon(icon1)
		self.getAudPath.setObjectName("getAudPath")
		self.getDocPath = QtWidgets.QPushButton(self.groupBox)
		self.getDocPath.setGeometry(QtCore.QRect(347, 42, 20, 21))
		self.getDocPath.setStyleSheet("QPushButton {\n"
"border: none;\n"
"background-color: rgb(229, 229, 229);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(203, 203, 203);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(168, 168, 168);\n"
"}")
		self.getDocPath.setIcon(icon1)
		self.getDocPath.setObjectName("getDocPath")
		self.getImgPath = QtWidgets.QPushButton(self.groupBox)
		self.getImgPath.setGeometry(QtCore.QRect(347, 65, 20, 21))
		self.getImgPath.setStyleSheet("QPushButton {\n"
"border: none;\n"
"background-color: rgb(229, 229, 229);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(203, 203, 203);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(168, 168, 168);\n"
"}")
		self.getImgPath.setIcon(icon1)
		self.getImgPath.setObjectName("getImgPath")
		self.getVidPath = QtWidgets.QPushButton(self.groupBox)
		self.getVidPath.setGeometry(QtCore.QRect(347, 88, 20, 21))
		self.getVidPath.setStyleSheet("QPushButton {\n"
"border: none;\n"
"background-color: rgb(229, 229, 229);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(203, 203, 203);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(168, 168, 168);\n"
"}")
		self.getVidPath.setIcon(icon1)
		self.getVidPath.setObjectName("getVidPath")
		self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
		self.horizontalLayoutWidget.setGeometry(QtCore.QRect(140, 164, 211, 31))
		self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
		self.buttonLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
		self.buttonLayout.setContentsMargins(0, 0, 0, 0)
		self.buttonLayout.setObjectName("buttonLayout")
		self.startBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
		self.startBtn.setStyleSheet("QPushButton:hover {\n"
"    color: rgb(42, 42, 42);\n"
"}")
		self.startBtn.setObjectName("startBtn")
		self.buttonLayout.addWidget(self.startBtn)
		self.stopBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
		self.stopBtn.setEnabled(False)
		self.stopBtn.setStyleSheet("QPushButton:hover {\n"
"    color: rgb(42, 42, 42);\n"
"}")
		self.stopBtn.setObjectName("stopBtn")
		self.buttonLayout.addWidget(self.stopBtn)
		self.versionLabel = QtWidgets.QLabel(self.centralwidget)
		self.versionLabel.setGeometry(QtCore.QRect(435, 180, 47, 13))
		self.versionLabel.setStyleSheet("QLabel {\n"
"    font: 9px \"Times New Roman\";\n"
"    color: rgb(139, 139, 139);\n"
"}")
		self.versionLabel.setObjectName("versionLabel")
		self.getTrackingPath = QtWidgets.QPushButton(self.centralwidget)
		self.getTrackingPath.setGeometry(QtCore.QRect(357, 9, 20, 21))
		self.getTrackingPath.setStyleSheet("QPushButton {\n"
"border: none;\n"
"background-color: rgb(229, 229, 229);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(203, 203, 203);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(168, 168, 168);\n"
"}")
		self.getTrackingPath.setIcon(icon1)
		self.getTrackingPath.setObjectName("getTrackingPath")
		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)


	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "FileManager"))
		self.trackingLabel.setText(_translate("MainWindow", "Отслеживаемая папка:"))
		self.trackingDef.setText(_translate("MainWindow", "По умолчанию"))
		self.groupBox.setTitle(_translate("MainWindow", "Конечные папки"))
		self.endImgLabel.setText(_translate("MainWindow", "Изображения:"))
		self.endVidLabel.setText(_translate("MainWindow", "Видео:"))
		self.endDocLabel.setText(_translate("MainWindow", "Документы:"))
		self.endAudLabel.setText(_translate("MainWindow", "Аудио:"))
		self.audDef.setText(_translate("MainWindow", "По умолчанию"))
		self.docDef.setText(_translate("MainWindow", "По умолчанию"))
		self.imgDef.setText(_translate("MainWindow", "По умолчанию"))
		self.vidDef.setText(_translate("MainWindow", "По умолчанию"))
		self.startBtn.setText(_translate("MainWindow", "Запустить"))
		self.stopBtn.setText(_translate("MainWindow", "Остановить"))
		self.versionLabel.setText(_translate("MainWindow", "Version:"))
import res_rc

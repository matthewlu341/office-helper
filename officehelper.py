# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OfficeHelper.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import PyPDF2
import docx2txt
import datetime
import os
import re
import sys
import subprocess
import xlrd
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas

from PyQt5.QtWidgets import QFileDialog, QMessageBox, QTableWidgetItem


class Ui_MainWindow(object):
    def __init__(self):
        self.rootFolder = os.getcwd()  # General variables

        self.regex = ''  # Regex variables
        self.filepath = ''
        self.regRaw = ''
        self.regExtensions = []

        self.cleanupPath = ''  # Cleanup variables
        self.delExtensions = []

        self.encryptionPath = ''  # encryption variables
        self.bits = 0

        self.pdfPath1 = ''  # merging variables
        self.pdfPath2 = ''
        self.pageNum = -1

        self.xlPath = '' #excel variables
        self.csvName = ''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(608, 533)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(-50, -70, 651, 561))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget.setGeometry(QtCore.QRect(50, 70, 611, 491))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 891, 461))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setKerning(True)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setAutoFillBackground(False)
        self.tab_4.setObjectName("tab_4")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_4)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 576, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.regexInput = QtWidgets.QTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.regexInput.sizePolicy().hasHeightForWidth())
        self.regexInput.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.regexInput.setFont(font)
        self.regexInput.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.regexInput.setObjectName("regexInput")
        self.gridLayout.addWidget(self.regexInput, 0, 1, 1, 2)
        self.directoryButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.directoryButton.setObjectName("directoryButton")
        self.gridLayout.addWidget(self.directoryButton, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.fileButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.fileButton.setObjectName("fileButton")
        self.gridLayout.addWidget(self.fileButton, 2, 1, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.pdfCheck = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.pdfCheck.setObjectName("pdfCheck")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pdfCheck)
        self.docxCheck = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.docxCheck.setObjectName("docxCheck")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.docxCheck)
        self.txtCheck = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.txtCheck.setObjectName("txtCheck")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtCheck)
        self.gridLayout.addLayout(self.formLayout, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(10, 220, 581, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(13)
        font.setUnderline(True)
        font.setKerning(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.regexTable = QtWidgets.QTableWidget(self.tab_4)
        self.regexTable.setGeometry(QtCore.QRect(10, 270, 581, 151))
        self.regexTable.setObjectName("regexTable")
        self.regexTable.setColumnCount(2)
        self.regexTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.regexTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.regexTable.setHorizontalHeaderItem(1, item)
        self.searchButton = QtWidgets.QPushButton(self.tab_4)
        self.searchButton.setGeometry(QtCore.QRect(170, 160, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setKerning(True)
        self.searchButton.setFont(font)
        self.searchButton.setObjectName("searchButton")
        self.regexExportButton = QtWidgets.QPushButton(self.tab_4)
        self.regexExportButton.setGeometry(QtCore.QRect(340, 170, 131, 31))
        self.regexExportButton.setObjectName("regexExportButton")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_5)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 10, 591, 210))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setKerning(True)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.cleanupDirectoryButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.cleanupDirectoryButton.setObjectName("cleanupDirectoryButton")
        self.gridLayout_2.addWidget(self.cleanupDirectoryButton, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_4.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_4.addWidget(self.checkBox_3, 1, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_4.addWidget(self.checkBox_2, 2, 0, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_4.addWidget(self.checkBox_4, 1, 1, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_4.addWidget(self.checkBox_5, 0, 1, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout_4.addWidget(self.checkBox_6, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 4, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_5)
        self.label_8.setGeometry(QtCore.QRect(10, 270, 581, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(13)
        font.setUnderline(True)
        font.setKerning(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 320, 571, 101))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_5.setGeometry(QtCore.QRect(200, 220, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_3.setGeometry(QtCore.QRect(0, 0, 601, 461))
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.tab_6)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(60, 10, 501, 131))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setKerning(True)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 2, 0, 1, 1)
        self.cleanupDirectoryButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.cleanupDirectoryButton_2.setObjectName("cleanupDirectoryButton_2")
        self.gridLayout_5.addWidget(self.cleanupDirectoryButton_2, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setKerning(True)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setKerning(True)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setKerning(True)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 3, 0, 1, 1)
        self.textEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout_5.addWidget(self.textEdit_2, 1, 1, 1, 1)
        self.textEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout_5.addWidget(self.textEdit_3, 2, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.gridLayoutWidget_4)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_7.setGeometry(QtCore.QRect(60, 0, 81, 20))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_7.clicked.connect(lambda: self.switchBits(40))
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_8.setGeometry(QtCore.QRect(210, 0, 81, 20))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_8.clicked.connect(lambda: self.switchBits(128))
        self.gridLayout_5.addWidget(self.groupBox_2, 3, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.tab_6)
        self.label_13.setGeometry(QtCore.QRect(10, 170, 581, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(13)
        font.setUnderline(True)
        font.setKerning(True)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_6)
        self.label_14.setEnabled(True)
        self.label_14.setGeometry(QtCore.QRect(10, 270, 581, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(13)
        font.setUnderline(False)
        font.setKerning(True)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab_6)
        self.label_15.setEnabled(True)
        self.label_15.setGeometry(QtCore.QRect(220, 270, 41, 41))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("check.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.label_15.hide()
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 220, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.encrypt)
        self.tabWidget_3.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.tab_7)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 20, 581, 131))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_6.addWidget(self.label_16, 2, 0, 1, 1)
        self.textEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_4.setValidator(QtGui.QIntValidator())
        self.gridLayout_6.addWidget(self.textEdit_4, 2, 2, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setKerning(True)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_6.addWidget(self.label_18, 0, 0, 1, 1)
        self.cleanupDirectoryButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.cleanupDirectoryButton_3.setObjectName("cleanupDirectoryButton_3")
        self.cleanupDirectoryButton_3.clicked.connect(lambda: self.mergeFileHandler(1))
        self.gridLayout_6.addWidget(self.cleanupDirectoryButton_3, 0, 2, 1, 1)
        self.cleanupDirectoryButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.cleanupDirectoryButton_4.setObjectName("cleanupDirectoryButton_4")
        self.cleanupDirectoryButton_4.clicked.connect(lambda: self.mergeFileHandler(2))
        self.gridLayout_6.addWidget(self.cleanupDirectoryButton_4, 1, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setKerning(True)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_6.addWidget(self.label_17, 1, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout_6.addWidget(self.label_19, 3, 0, 1, 1)
        self.textEdit_5 = QtWidgets.QTextEdit(self.gridLayoutWidget_5)
        self.textEdit_5.setObjectName("textEdit_5")
        self.gridLayout_6.addWidget(self.textEdit_5, 3, 2, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.tab_7)
        self.label_20.setGeometry(QtCore.QRect(10, 150, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.tab_7)
        self.label_21.setGeometry(QtCore.QRect(10, 190, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 240, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_22 = QtWidgets.QLabel(self.tab_7)
        self.pushButton_7.clicked.connect(self.merge)
        self.label_22.setEnabled(True)
        self.label_22.setGeometry(QtCore.QRect(10, 300, 581, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(13)
        font.setUnderline(False)
        font.setKerning(True)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.tab_7)
        self.label_23.setEnabled(True)
        self.label_23.setGeometry(QtCore.QRect(210, 300, 41, 41))
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap("check.png"))
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName("label_23")
        self.label_23.hide()
        self.tabWidget_3.addTab(self.tab_7, "")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(70, 40, 441, 71))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout_3.addWidget(self.label_24, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 0, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout_3.addWidget(self.label_25, 1, 0, 1, 1)
        self.textEdit_6 = QtWidgets.QTextEdit(self.gridLayoutWidget_3)
        self.textEdit_6.setObjectName("textEdit_6")
        self.gridLayout_3.addWidget(self.textEdit_6, 1, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.tab_3)
        self.label_26.setGeometry(QtCore.QRect(10, 130, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 190, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_27 = QtWidgets.QLabel(self.tab_3)
        self.label_27.setEnabled(True)
        self.label_27.setGeometry(QtCore.QRect(10, 250, 581, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(13)
        font.setUnderline(False)
        font.setKerning(True)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.tab_3)
        self.label_28.setEnabled(True)
        self.label_28.setGeometry(QtCore.QRect(230, 250, 41, 41))
        self.label_28.setText("")
        self.label_28.setPixmap(QtGui.QPixmap("check.png"))
        self.label_28.setScaledContents(True)
        self.label_28.setObjectName("label_28")
        self.label_28.hide()
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 608, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(1)
        self.tabWidget_3.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.fileButton.clicked.connect(lambda: self.fileDialogHandler('f'))
        self.directoryButton.clicked.connect(lambda: self.fileDialogHandler('d'))
        self.searchButton.clicked.connect(self.search)

    def fileDialogHandler(self, type):
        dialog = QFileDialog()
        if type == 'f':
            dialog.setFileMode(QFileDialog.AnyFile)
            self.toggleReg(True)

        else:
            dialog.setFileMode(QFileDialog.Directory)
            self.toggleReg(False)
        if dialog.exec_():
            self.regexTable.setRowCount(0)
            self.filepath = dialog.selectedFiles()[0]
            self.label_4.setText('Your matches in: ' + self.getFileName(self.filepath))

    def getFileName(self, path):
        i = 0
        for c in reversed(path):
            if c == '/':
                return path[len(path) - i:]
            i += 1

    def getFolderName(self, path):
        return path[:-(len(self.getFileName(path)) + 1)]

    def isRegChecked(self):
        items = []
        for i in range(self.formLayout.count()):
            if self.formLayout.itemAt(i).widget().isChecked():
                items.append(self.formLayout.itemAt(i).widget().text())
        self.regExtensions = items
        return self.pdfCheck.isChecked() or self.docxCheck.isChecked() or self.txtCheck.isChecked()

    def toggleReg(self, bool):
        self.pdfCheck.setDisabled(bool)
        self.txtCheck.setDisabled(bool)
        self.docxCheck.setDisabled(bool)

    def search(self):
        self.regRaw = ''
        self.regex = self.regexInput.toPlainText()
        if self.regex and (self.filepath and (not os.path.isdir(self.filepath)) or (os.path.isdir(self.filepath)
                                                                                    and self.isRegChecked())):
            searchRegex = re.compile(self.regex)
            if os.path.isdir(self.filepath):  # if its a folder
                os.chdir(self.filepath)
                for file in os.listdir():  # iterate through every file
                    if os.path.isfile(file):
                        for ext in self.regExtensions:
                            if file.endswith(ext):
                                self.searchFile(self.filepath + '/' + file, searchRegex)

            else:  # if its a file
                self.searchFile(self.filepath, searchRegex)

        else:
            self.showError('Please make sure the regex and filepath are nonempty, and that at least one file extension '
                           'is selected.')

    def updateTable(self, results, filename):
        for res in results:
            rowPos = self.regexTable.rowCount()
            self.regexTable.insertRow(rowPos)
            self.regexTable.setItem(rowPos, 0, QTableWidgetItem(res))
            self.regRaw += (res + '\n')
            self.regexTable.setItem(rowPos, 1, QTableWidgetItem(filename))

    def searchFile(self, filename, regex):
        if not filename.endswith('.pdf') and not filename.endswith('.docx') and not filename.endswith('.txt'):
            self.showError('Invalid file type')
        else:
            if filename.endswith('.pdf'):
                reader = PyPDF2.PdfFileReader(open(filename, 'rb'))
                for i in range(reader.getNumPages()):
                    results = regex.findall(reader.getPage(i).extractText())
                    self.updateTable(results, filename)

            elif filename.endswith('.docx'):
                docx = docx2txt.process(filename)
                results = regex.findall(docx)
                self.updateTable(results, filename)
            else:
                txt = open(filename)
                results = regex.findall(txt.read())
                self.updateTable(results, filename)
                txt.close()

    def showError(self, msg):
        err = QMessageBox()
        err.setWindowTitle('Regex Search Error')
        err.setText(msg)
        err.setIcon(QMessageBox.Critical)
        err.exec_()

    def saveRaw(self):
        os.chdir(self.rootFolder)
        rawText = ''
        for i in range(self.regexTable.rowCount()):
            rawText += self.regexTable.item(i, 0).text() + '\n'

        if self.rootFolder and rawText:
            os.chdir(self.rootFolder)
            file = open('RegexSearch.txt', 'w+')
            file.write(rawText)
            subprocess.Popen('explorer ' + self.rootFolder + '\\RegexSearch.txt')
            file.close()

    def cleanupFileDialog(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec_():
            self.tableWidget_2.setRowCount(0)
            self.cleanupPath = dialog.selectedFiles()[0]
            self.label_8.setText('Deleting files in: ' + self.getFileName(self.cleanupPath))

    def delCheck(self):
        items = []
        oneChecked = False
        for i in range(self.gridLayout_4.count()):
            if self.gridLayout_4.itemAt(i).widget().isChecked():
                oneChecked = True
                items.append(self.gridLayout_4.itemAt(i).widget().text())

        if self.textEdit.toPlainText():
            oneChecked = True

        self.delExtensions = (items + self.textEdit.toPlainText().split(','))
        self.delExtensions = [ext.strip() for ext in self.delExtensions if ext]
        return oneChecked

    def delete(self):
        files = []
        if self.delCheck() and self.cleanupPath:
            os.chdir(self.cleanupPath)
            for file in os.listdir():
                if os.path.isfile(file):
                    for ext in self.delExtensions:
                        if file.endswith(ext):
                            files.append(file)
            for file in files:
                if os.path.exists(file):
                    os.remove(file)

            self.updateDeleteTable(files)

        else:
            self.showError('Please make sure you selected a filepath and at least one file extension.')

    def updateDeleteTable(self, filenames):
        for file in filenames:
            rowPos = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(rowPos)
            self.tableWidget_2.setItem(rowPos, 0, QTableWidgetItem(file))

    def encryptionDialog(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        if dialog.exec_():
            self.label_14.hide()
            self.label_15.hide()
            self.encryptionPath = dialog.selectedFiles()[0]
            self.label_13.setText('Encrypting PDF: ' + self.getFileName(self.encryptionPath))

    def switchBits(self, bit):
        self.bits = bit
        if bit == 40:
            if self.checkBox_8.isChecked():
                self.checkBox_8.setChecked(False)
                self.checkBox_7.setChecked(True)
        else:
            if self.checkBox_7.isChecked():
                self.checkBox_7.setChecked(False)
                self.checkBox_8.setChecked(True)

    def encrypt(self):
        if self.bits > 0 and self.encryptionPath.endswith('.pdf'):
            os.chdir(self.getFolderName(self.encryptionPath))
            inputPdf = PyPDF2.PdfFileReader(open(self.encryptionPath, 'rb'))
            if not inputPdf.isEncrypted:
                writer = PyPDF2.PdfFileWriter()
                writer.appendPagesFromReader(inputPdf)
                if self.textEdit_2.text() == self.textEdit_3.text() and self.textEdit_2.text() and self.textEdit_3.text():
                    if self.bits == 40:
                        writer.encrypt(self.textEdit_2.text(), self.textEdit_2.text(), False)
                    else:
                        writer.encrypt(self.textEdit_2.text(), self.textEdit_2.text(), True)

                    newFile = open('Encrypted.pdf', 'wb')
                    writer.write(newFile)
                    self.label_14.show()
                    self.label_15.show()
                    newFile.close()
                else:
                    self.showError('Passwords do not match.')

            else:
                self.showError('PDF is already encrypted')
        else:
            self.showError('Please make sure bits and a PDF file are selected.')

    def mergeFileHandler(self, num):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        if dialog.exec_():
            self.label_22.hide()
            self.label_23.hide()
            if num == 1:
                self.pdfPath1 = dialog.selectedFiles()[0]
                self.label_20.setText('Merging: ' + self.getFileName(self.pdfPath1))
                self.label_20.adjustSize()
            else:
                self.pdfPath2 = dialog.selectedFiles()[0]
                self.label_21.setText('With: ' + self.getFileName(self.pdfPath2))
                self.label_21.adjustSize()

    def merge(self):
        os.chdir(self.rootFolder)
        if self.pdfPath1.endswith('.pdf') and self.pdfPath2.endswith('.pdf') and self.textEdit_5.toPlainText().endswith(
                '.pdf'):

            if self.textEdit_5.toPlainText() in os.listdir():
                self.showError('File already exists')
                return 0

            merger = PyPDF2.PdfFileMerger()
            readerPdf = open(self.pdfPath1, 'rb')
            reader = PyPDF2.PdfFileReader(readerPdf)

            pageNum = -1
            if self.textEdit_4.text():
                pageNum = int(self.textEdit_4.text())
                if -1 < pageNum < reader.getNumPages():
                    merger.append(self.pdfPath1)
                    merger.merge(pageNum, self.pdfPath2)
                else:
                    self.showError('Invalid page number')
                    return 0

            else:
                merger.append(self.pdfPath1)
                merger.append(self.pdfPath2)

            merger.write(self.textEdit_5.toPlainText())
            merger.close()
            readerPdf.close()
            self.label_22.show()
            self.label_23.show()
        else:
            self.showError('Please make sure you have 2 PDF files selected and an output in PDF format.')

    def xlDialog(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        if dialog.exec_():
            self.label_27.hide()
            self.label_28.hide()
            self.xlPath = dialog.selectedFiles()[0]
            self.label_26.setText('Converting: ' + self.getFileName(self.xlPath))
            self.label_26.adjustSize()

    def convert(self):
        if self.textEdit_6.toPlainText().endswith('.csv') and self.xlPath.endswith('.xlsx'):
            read_file = pandas.read_excel(self.xlPath)
            read_file.to_csv(self.getFolderName(self.xlPath)+ '/' + self.textEdit_6.toPlainText(), index=None, header=True)
            self.label_27.show()
            self.label_28.show()

        else:
            self.showError('Please make sure your selected file is xlsx and output file is csv.')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Office Helper"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.directoryButton.setText(_translate("MainWindow", "Directory"))
        self.label_3.setText(_translate("MainWindow", "Choose the file types to search:"))
        self.label.setText(_translate("MainWindow", "Type a regex you want to search for:"))
        self.label_2.setText(_translate("MainWindow", "Choose a file or directory to search:"))
        self.fileButton.setText(_translate("MainWindow", "File"))
        self.pdfCheck.setText(_translate("MainWindow", ".pdf"))
        self.docxCheck.setText(_translate("MainWindow", ".docx"))
        self.txtCheck.setText(_translate("MainWindow", ".txt"))
        self.label_4.setText(_translate("MainWindow", "Your matches in:"))
        item = self.regexTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Text"))
        self.regexTable.setColumnWidth(0, 200)
        item = self.regexTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "File"))
        self.regexTable.setColumnWidth(1, 378)
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.regexExportButton.setText(_translate("MainWindow", "Export raw to txt"))
        self.regexExportButton.clicked.connect(self.saveRaw)
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Regex Search"))
        self.label_6.setText(_translate("MainWindow", "Select extensions to delete:"))
        self.cleanupDirectoryButton.setText(_translate("MainWindow", "Directory"))
        self.cleanupDirectoryButton.clicked.connect(self.cleanupFileDialog)
        self.label_5.setText(_translate("MainWindow", "Choose a directory to clean up:"))
        self.checkBox.setText(_translate("MainWindow", ".docx"))
        self.checkBox_3.setText(_translate("MainWindow", ".pptx"))
        self.checkBox_2.setText(_translate("MainWindow", ".png"))
        self.checkBox_4.setText(_translate("MainWindow", ".xlsx"))
        self.checkBox_5.setText(_translate("MainWindow", ".pdf"))
        self.checkBox_6.setText(_translate("MainWindow", ".jpg"))
        self.label_7.setText(_translate("MainWindow", "Other extensions to delete (separated by commas)"))
        self.label_8.setText(_translate("MainWindow", "Deleting files in:"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        self.tableWidget_2.setColumnWidth(0, 608)
        item.setText(_translate("MainWindow", "File"))
        self.pushButton_5.setText(_translate("MainWindow", "Delete"))
        self.pushButton_5.clicked.connect(self.delete)
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Cleanup"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Files"))
        self.label_11.setText(_translate("MainWindow", "Confirm password:"))
        self.cleanupDirectoryButton_2.setText(_translate("MainWindow", "Browse"))
        self.cleanupDirectoryButton_2.clicked.connect(self.encryptionDialog)
        self.label_10.setText(_translate("MainWindow", "Enter a password:"))
        self.label_9.setText(_translate("MainWindow", "Choose a pdf file:"))
        self.label_12.setText(_translate("MainWindow", "Encryption bits:"))
        self.checkBox_7.setText(_translate("MainWindow", "40"))
        self.checkBox_8.setText(_translate("MainWindow", "128"))
        self.label_13.setText(_translate("MainWindow", "Encrypting PDF:"))
        self.label_14.setText(_translate("MainWindow", "Encryption complete!"))
        self.label_14.hide()
        self.pushButton_6.setText(_translate("MainWindow", "Encrypt"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), _translate("MainWindow", "Encryption"))
        self.label_16.setText(_translate("MainWindow", "Specify a page number to insert after (optional)"))
        self.label_18.setText(_translate("MainWindow", "Choose 1st PDF file:"))
        self.cleanupDirectoryButton_3.setText(_translate("MainWindow", "Browse"))
        self.cleanupDirectoryButton_4.setText(_translate("MainWindow", "Browse"))
        self.label_17.setText(_translate("MainWindow", "Choose 2nd PDF file:"))
        self.label_19.setText(_translate("MainWindow", "Output file name:"))
        self.label_20.setText(_translate("MainWindow", "Merging:"))
        self.label_21.setText(_translate("MainWindow", "with:"))
        self.pushButton_7.setText(_translate("MainWindow", "Merge"))
        self.label_22.setText(_translate("MainWindow", "Merging complete!"))
        self.label_22.hide()
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_7), _translate("MainWindow", "Merging"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "PDFs"))
        self.label_24.setText(_translate("MainWindow", "Choose an Excel file:"))
        self.pushButton.setText(_translate("MainWindow", "Browse"))
        self.pushButton.clicked.connect(self.xlDialog)
        self.label_25.setText(_translate("MainWindow", "Output file name:"))
        self.label_26.setText(_translate("MainWindow", "Converting:"))
        self.pushButton_8.setText(_translate("MainWindow", "Convert"))
        self.pushButton_8.clicked.connect(self.convert)
        self.label_27.setText(_translate("MainWindow", "Conversion complete!"))
        self.label_27.hide()
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3),
                                  _translate("MainWindow", "Excel to CSV Conversion"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

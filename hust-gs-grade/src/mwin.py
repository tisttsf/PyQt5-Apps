# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mwin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MWin(object):
    def setupUi(self, MWin):
        MWin.setObjectName("MWin")
        MWin.resize(500, 400)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        MWin.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/smart-hust.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MWin.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(MWin)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.in_cookie = QtWidgets.QToolButton(self.groupBox)
        self.in_cookie.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.in_cookie.setFont(font)
        self.in_cookie.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.in_cookie.setObjectName("in_cookie")
        self.horizontalLayout.addWidget(self.in_cookie)
        self.start = QtWidgets.QToolButton(self.groupBox)
        self.start.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.start.setFont(font)
        self.start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start.setObjectName("start")
        self.horizontalLayout.addWidget(self.start)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.result = QtWidgets.QTextEdit(self.groupBox_2)
        self.result.setObjectName("result")
        self.verticalLayout.addWidget(self.result)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        MWin.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MWin)
        self.statusBar.setObjectName("statusBar")
        MWin.setStatusBar(self.statusBar)

        self.retranslateUi(MWin)
        QtCore.QMetaObject.connectSlotsByName(MWin)

    def retranslateUi(self, MWin):
        _translate = QtCore.QCoreApplication.translate
        MWin.setWindowTitle(_translate("MWin", "华科研究生成绩查询"))
        self.groupBox.setTitle(_translate("MWin", "Buttons"))
        self.in_cookie.setText(_translate("MWin", "Import Cookis"))
        self.start.setText(_translate("MWin", "Query"))
        self.groupBox_2.setTitle(_translate("MWin", "Information"))
        self.groupBox_3.setTitle(_translate("MWin", "Bugs Report"))
        self.label.setText(_translate("MWin", "<html><head/><body><p><a href=\'https://github.com/LewisTian/PyQt5-Apps\'>GitHub/LewisTian/PyQt5-Apps</a></p></body></html>"))

import res_rc

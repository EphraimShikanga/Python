# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'todoklBnQb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(675, 550)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(260, 10, 391, 511))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.listView = QListView(self.verticalLayoutWidget)
        self.listView.setObjectName(u"listView")

        self.verticalLayout.addWidget(self.listView)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 10, 241, 221))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_6 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_2.addWidget(self.pushButton_6)

        self.pushButton_4 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_2.addWidget(self.pushButton_5)

        self.calendarWidget = QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(0, 240, 248, 281))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Edit Task", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Add Tasks", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Get Task", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Delete Task", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"All Tasks", None))
    # retranslateUi


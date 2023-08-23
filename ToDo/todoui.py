from functionality import TaskOperations
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout


class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.MainWindow = QMainWindow()
        self.setupUi(self.MainWindow)
        self.ops = TaskOperations('data.json')
        self.main()

    def main(self):
        self.pushButton.clicked.connect(self.add_task)
        self.pushButton_2.clicked.connect(self.display_all_tasks)
        self.pushButton_3.clicked.connect(self.edit_task)
        self.pushButton_4.clicked.connect(self.get_task)

        list_layout = QHBoxLayout()
        list_layout.addWidget(self.listWidget)
        list_layout.addWidget(self.listWidget_2)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.pushButton)
        button_layout.addWidget(self.pushButton_2)
        button_layout.addWidget(self.pushButton_3)
        button_layout.addWidget(self.pushButton_4)

        main_layout = QVBoxLayout()
        main_layout.addLayout(list_layout)
        main_layout.addLayout(button_layout)

        self.centralwidget.setLayout(main_layout)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 600)
        # MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        MainWindow.setWindowOpacity(0.9)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.centralwidget.setObjectName("centralwidget")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 11, 150, 530))
        self.listWidget.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.listWidget.setStyleSheet("border: none;")
        self.listWidget.setObjectName("listWidget")

        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(165, 11, 300, 530))
        self.listWidget_2.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.listWidget_2.setStyleSheet("border: 3px solid black;")
        self.listWidget_2.setObjectName("listWidget_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 30, 150, 25))
        # make the button resize with the mainwindow
        self.pushButton.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        # self.pushButton.setStyleSheet("border: 1px solid black;")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 60, 150, 25))
        self.pushButton_2.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        # self.pushButton_2.setStyleSheet("border: 1px solid black;")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 90, 150, 25))
        self.pushButton_3.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        # self.pushButton_3.setStyleSheet("border: 1px solid black;")
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 120, 150, 25))
        self.pushButton_4.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        # self.pushButton_4.setStyleSheet("border: 1px solid black;")
        self.pushButton_4.setObjectName("pushButton_4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Add Task"))
        self.pushButton_2.setText(_translate("MainWindow", "All Tasks"))
        self.pushButton_3.setText(_translate("MainWindow", "Edit Task"))
        self.pushButton_4.setText(_translate("MainWindow", "Get Task"))

    def add_task(self):
        pass

    def display_all_tasks(self):
        print('displaying all tasks')
        self.listWidget_2.clear()
        self.ops.load_tasks()

        for task in self.ops.task_list:
            task_item = f"ID: {task.id}\n" \
                        f"Title: {task.title}\n" \
                        f"Status: {task.status.name}\n" \
                        f"Due Date: {task.due_date}"
            self.listWidget_2.addItem(task_item)
            self.listWidget_2.addItem('-' * 50)

    def edit_task(self):
        pass

    def get_task(self):
        pass

    def next_task(self):
        pass

    def previous_task(self):
        pass

from functionality import TaskOperations, TaskStatus, Task
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QDialog, QLabel,
                             QComboBox, QLineEdit, QTextEdit,
                             QPushButton, QVBoxLayout)


class AddTaskDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add Task')
        self.resize(300, 300)

        layout = QVBoxLayout()

        self.title_input = QLineEdit()
        layout.addWidget(QLabel('Title:'))
        layout.addWidget(self.title_input)

        self.description_input = QTextEdit()
        layout.addWidget(QLabel('Description:'))
        layout.addWidget(self.description_input)

        self.due_date_input = QLineEdit()
        layout.addWidget(QLabel('Due Date (DD/MM/YYYY):'))
        layout.addWidget(self.due_date_input)

        self.status_input = QComboBox()
        self.status_input.addItems([status.name for status in TaskStatus])
        layout.addWidget(QLabel('Status:'))
        layout.addWidget(self.status_input)

        self.add_button = QPushButton('Add Task')
        self.add_button.clicked.connect(self.accept)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def get_task(self):
        title = self.title_input.text()
        description = self.description_input.toPlainText()
        due_date = self.due_date_input.text()
        status = TaskStatus[self.status_input.currentText()]

        return title, due_date, description, status


class EditTaskDialog(QtWidgets.QDialog):
    def __init__(self, task, parent=None):
        super(EditTaskDialog, self).__init__(parent)
        self.task = task
        self.setWindowTitle(f"Edit Task: '{self.task.ID}'")
        self.setLayout(QtWidgets.QVBoxLayout())

        self.date_created_input = QtWidgets.QLineEdit(self.task.Date_Created)
        self.date_created_input.setReadOnly(True)
        self.title_input = QtWidgets.QLineEdit(self.task.Title)
        self.description_input = QtWidgets.QTextEdit(self.task.Description)
        self.status_input = QtWidgets.QComboBox()
        self.status_input.addItems([status.name for status in TaskStatus])
        self.status_input.setCurrentText(self.task.Status.name)
        self.due_date_input = QtWidgets.QLineEdit(self.task.Due_Date)

        self.layout().addWidget(QtWidgets.QLabel("Date Created:"))
        self.layout().addWidget(self.date_created_input)
        self.layout().addWidget(QtWidgets.QLabel("Title:"))
        self.layout().addWidget(self.title_input)
        self.layout().addWidget(QtWidgets.QLabel("Description:"))
        self.layout().addWidget(self.description_input)
        self.layout().addWidget(QtWidgets.QLabel("Status:"))
        self.layout().addWidget(self.status_input)
        self.layout().addWidget(QtWidgets.QLabel("Due Date:"))
        self.layout().addWidget(self.due_date_input)

        button_box = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        self.layout().addWidget(button_box)

    def get_edited_task(self):
        edited_task = Task(
            title=self.title_input.text(),
            description=self.description_input.toPlainText(),
            due_date=self.due_date_input.text(),
            task_status=TaskStatus[self.status_input.currentText()],
            task_id=self.task.ID,
            date_created=self.task.Date_Created,
        )
        return edited_task


class GetTaskIdDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(GetTaskIdDialog, self).__init__(parent)
        self.setWindowTitle("Edit Task")
        self.setLayout(QtWidgets.QVBoxLayout())

        self.task_id_input = QtWidgets.QLineEdit()
        self.layout().addWidget(QtWidgets.QLabel("Task ID:"))
        self.layout().addWidget(self.task_id_input)

        button_box = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        self.layout().addWidget(button_box)

    def get_task_id(self):
        return self.task_id_input.text()


class DeleteTasksDialog(QtWidgets.QDialog):
    def __init__(self, task_ids, parent=None):
        super(DeleteTasksDialog, self).__init__(parent)
        self.resize(300, 100)
        self.setWindowTitle("Delete Tasks")
        self.setLayout(QtWidgets.QVBoxLayout())

        self.task_ids_input = QtWidgets.QLineEdit()
        self.task_ids_input.setPlaceholderText(
            "Enter task IDs (comma-separated)")
        self.ok_button = QtWidgets.QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)

        top_section_layout = QtWidgets.QHBoxLayout()
        top_section_layout.addWidget(self.task_ids_input)
        top_section_layout.addWidget(self.ok_button)

        self.delete_all_button = QtWidgets.QPushButton("Delete All Tasks")
        self.delete_all_button.clicked.connect(self.delete_all_clicked)
        self.cancel_button = QtWidgets.QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)

        bottom_section_layout = QtWidgets.QHBoxLayout()
        bottom_section_layout.addWidget(self.delete_all_button)
        bottom_section_layout.addWidget(self.cancel_button)

        self.layout().addLayout(top_section_layout)
        self.layout().addLayout(bottom_section_layout)

        self.task_ids = task_ids
        self.delete_all_tasks = False

    def get_task_ids_to_delete(self):
        if self.result() == QtWidgets.QDialog.Accepted:
            task_ids = self.task_ids_input.text().strip()
            return ([task_id.strip()
                     for task_id in task_ids.split(",") if task_id.strip()])
        return []

    def delete_all_clicked(self):
        self.delete_all_tasks = True
        self.accept()

    def is_delete_all_tasks(self):
        return self.delete_all_tasks


class Ui_MainWindow(object):

    def __init__(self):
        super().__init__()
        self.MainWindow = QMainWindow()
        self.setupUi(self.MainWindow)
        self.ops = TaskOperations('data.json')
        self.main()

    def main(self):
        self.display_all_tasks()
        self.pushButton.clicked.connect(self.display_all_tasks)
        self.pushButton_2.clicked.connect(self.add_task)
        self.pushButton_3.clicked.connect(self.edit_task)
        self.pushButton_4.clicked.connect(self.get_task)
        self.pushButton_5.clicked.connect(self.sort_tasks)
        self.pushButton_6.clicked.connect(self.delete_task)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(725, 658)
        MainWindow.setWindowOpacity(0.9)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout_3 = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout_3.setObjectName("formLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Fira Code SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(True)
        self.pushButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignLeft)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Fira Code SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setMouseTracking(True)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_2.setAutoFillBackground(True)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(
            self.pushButton_2, 0, QtCore.Qt.AlignLeft)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Fira Code SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setMouseTracking(True)
        self.pushButton_3.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton_3.setAutoFillBackground(True)
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(
            self.pushButton_3, 0, QtCore.Qt.AlignLeft)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Fira Code SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setMouseTracking(False)
        self.pushButton_4.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_4.setAutoFillBackground(True)
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(
            self.pushButton_4, 0, QtCore.Qt.AlignLeft)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Fira Code SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setMouseTracking(False)
        self.pushButton_5.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_5.setAutoFillBackground(True)
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setDefault(False)
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(
            self.pushButton_5, 0, QtCore.Qt.AlignLeft)

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Fira Code SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setMouseTracking(False)
        self.pushButton_6.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_6.setAutoFillBackground(True)
        self.pushButton_6.setAutoDefault(False)
        self.pushButton_6.setDefault(False)
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(
            self.pushButton_6, 0, QtCore.Qt.AlignLeft)

        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setMouseTracking(False)
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setHorizontalHeaderFormat(
            QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(
            self.calendarWidget, 0, QtCore.Qt.AlignLeft)

        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listView.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listView.setLineWidth(0)
        self.listView.setMovement(QtWidgets.QListView.Static)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)

        self.formLayout_3.setLayout(
            0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setViewMode(QtWidgets.QListView.ListMode)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro ExtraLight Medi")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.listView_2.setFont(font)
        self.listView_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.listView_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listView_2.setLineWidth(3)
        self.listView_2.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.listView_2.setTabKeyNavigation(True)
        self.listView_2.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.listView_2.setAlternatingRowColors(True)
        self.listView_2.setSelectionMode(
            QtWidgets.QAbstractItemView.MultiSelection)
        self.listView_2.setVerticalScrollMode(
            QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listView_2.setHorizontalScrollMode(
            QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listView_2.setMovement(QtWidgets.QListView.Free)
        self.listView_2.setResizeMode(QtWidgets.QListView.Adjust)
        self.listView_2.setObjectName("listView_2")

        self.model_1 = QtGui.QStandardItemModel(self.centralwidget)
        self.model_2 = QtGui.QStandardItemModel(self.centralwidget)

        self.listView.setModel(self.model_1)
        self.listView_2.setModel(self.model_2)

        self.formLayout_3.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.listView_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Ephraim's de ToDo"))
        self.pushButton.setText(_translate("MainWindow", "All Tasks"))
        self.pushButton_2.setText(_translate("MainWindow", "Add Task"))
        self.pushButton_3.setText(_translate("MainWindow", "Edit Task"))
        self.pushButton_4.setText(_translate("MainWindow", "Get Task"))
        self.pushButton_5.setText(_translate("MainWindow", "Sort Tasks"))
        self.pushButton_6.setText(_translate("MainWindow", "Delete Tasks"))

    def display_all_tasks(self):
        print('displaying all tasks')
        self.model_1.clear()
        self.model_2.clear()
        self.ops.load_tasks()

        for task in self.ops.task_list:
            if (task.Due_Date <= datetime.now().strftime('%a %d, %B %Y')
                    and task.Status.name != 'DONE'):
                task_item = f"Title: {task.Title} - {task.Status.name}\n"\
                            f"Due Date: {task.Due_Date}"
                item = QtGui.QStandardItem(task_item)
                self.model_1.appendRow(item)
                self.model_1.appendRow(QtGui.QStandardItem('-' * 50))

            task_item = f"ID: {task.ID}\n" \
                        f"Title: {task.Title}\n" \
                        f"Status: {task.Status.name}\n" \
                        f"Due Date: {task.Due_Date}"
            item = QtGui.QStandardItem(task_item)
            self.model_2.appendRow(item)
            self.model_2.appendRow(QtGui.QStandardItem('-' * 50))

    def add_task(self):
        add_task_dialog = AddTaskDialog()
        if add_task_dialog.exec_() == QDialog.Accepted:
            title, due_date, description, status = add_task_dialog.get_task()
            task = Task(title, due_date, description, status)
            self.ops.add_task(task)
        self.display_all_tasks()

    def edit_task(self):
        dialog = GetTaskIdDialog(self.MainWindow)
        if not dialog.exec_():
            return

        task_id = dialog.get_task_id()
        task = self.ops.get_task(task_id)
        if not task:
            QtWidgets.QMessageBox.warning(
                self.MainWindow,
                "Task Not Found",
                F"Task with ID '{task_id}' not found!",
                QtWidgets.QMessageBox.Ok,
            )
            return

        edit_dialog = EditTaskDialog(task, self.MainWindow)
        if edit_dialog.exec_():
            edited_task = edit_dialog.get_edited_task()
            self.ops.update_task(
                edited_task.ID,
                new_title=edited_task.Title,
                new_description=edited_task.Description,
                new_due_date=edited_task.Due_Date,
                new_status=edited_task.Status,
            )
            self.display_all_tasks()

    def get_task(self):
        task_id, ok = QtWidgets.QInputDialog.getText(
            self.MainWindow, 'Get Task', 'Enter Task ID:')
        if ok and task_id:
            task = self.ops.get_task(task_id)
            if task:
                task_item = f"ID: {task.ID}\n" \
                            f"Title: {task.Title}\n" \
                            f"Status: {task.Status.name}\n" \
                            f"Date Created: {task.Date_Created}\n" \
                            f"Due Date: {task.Due_Date}\n" \
                            f"Description: {task.Description}"
                item = QtGui.QStandardItem(task_item)
                self.model_2.clear()
                self.model_2.appendRow(item)
            else:
                QtWidgets.QMessageBox.warning(
                    self.MainWindow, 'Error', 'Task not found')

    def sort_tasks(self):
        sort_by, ok = QtWidgets.QInputDialog.getItem(
            self.MainWindow, 'Sort Tasks', 'Sort By:',
            ['ID', 'Title', 'Status', 'Date_Created', 'Due_Date'])
        if ok and sort_by:
            self.ops.sort_tasks(sort_by)
            self.display_all_tasks()

    def delete_task(self):
        dialog = DeleteTasksDialog(self.ops.task_list, self.MainWindow)
        if dialog.exec_() == QDialog.Accepted:
            task_ids_to_delete = dialog.get_task_ids_to_delete()

            if dialog.is_delete_all_tasks():
                self.ops.delete_all_tasks()
            else:
                self.ops.delete_task(task_ids_to_delete)

            self.display_all_tasks()

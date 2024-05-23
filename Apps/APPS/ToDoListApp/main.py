from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
import os


class ToDoListApp(QtWidgets.QMainWindow):
    def SetupUI(self):
        self.setStyleSheet('font-family: MV Boli; font-weight: bold; font-size: 20px; letter-spacing: -1px;')
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(os.getcwd()), 'ICONS', 'ToDoListIcon.ico')))
        self.StartLabel = QtWidgets.QLabel(self)
        self.StartLabel.setText('My ToDo list:')
        self.StartLabel.setGeometry(QtCore.QRect(103, 10, 170, 33))
        self.ListWidget = QtWidgets.QListWidget(self)
        self.ListWidget.setGeometry(QtCore.QRect(20, 50, 400, 390))
        self.AddButton = QtWidgets.QPushButton(self)
        self.AddButton.setText('Add Task')
        self.AddButton.setGeometry(QtCore.QRect(455, 15, 170, 50))
        self.DeleteButton = QtWidgets.QPushButton(self)
        self.DeleteButton.setText('Delete Task')
        self.DeleteButton.setGeometry(QtCore.QRect(455, 80, 170, 50))
        self.CheckButton = QtWidgets.QPushButton(self)
        self.CheckButton.setGeometry(QtCore.QRect(455, 150, 170, 50))
        self.CheckButton.setText('Check All')
        self.UnCheckButton = QtWidgets.QPushButton(self)
        self.UnCheckButton.setText('UnCheck All')
        self.UnCheckButton.setGeometry(QtCore.QRect(455, 220, 170, 50))
        self.setWindowTitle('ToDoListApp')
        self.resize(640, 450)

        self.AddButton.clicked.connect(self.AddTask)
        self.DeleteButton.clicked.connect(self.DeleteTask)
        self.CheckButton.clicked.connect(self.CheckAllTasks)
        self.UnCheckButton.clicked.connect(self.UnCheckAllTasks)

    def AddTask(self):
        TaskText, ok = QtWidgets.QInputDialog.getText(self, 'Add Task', 'Enter task:')
        if ok:
            self.ListWidget.addItem(TaskText)

    def DeleteTask(self):
        SelectedItem = self.ListWidget.currentItem()
        if SelectedItem is not None:
            self.ListWidget.takeItem(self.ListWidget.row(SelectedItem))

    def CheckAllTasks(self):
        for x in range(self.ListWidget.count()):
            Item = self.ListWidget.item(x)
            Item.setCheckState(QtCore.Qt.Checked)

    def UnCheckAllTasks(self):
        for x in range(self.ListWidget.count()):
            Item = self.ListWidget.item(x)
            Item.setCheckState(QtCore.Qt.Unchecked)


APP = QtWidgets.QApplication([])
Window = ToDoListApp()
Window.SetupUI()
Window.show()
APP.exec_()

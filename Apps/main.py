from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
import os


class Apps(QtWidgets.QMainWindow):
    def SetupUI(self):
        self.setStyleSheet('font-family: MV Boli; font-weight: bold; font-size: 20px; letter-spacing: -1px;')
        self.StartLabel = QtWidgets.QLabel(self)
        self.StartLabel.setText('Hello please select App :)')
        self.StartLabel.setGeometry(QtCore.QRect(3, 5, 275, 35))
        self.LalafoButton = QtWidgets.QPushButton(self)
        self.LalafoButton.setText('Lalafo')
        self.LalafoButton.setGeometry(QtCore.QRect(80, 43, 95, 30))
        self.CalculatorButton = QtWidgets.QPushButton(self)
        self.CalculatorButton.setText('Calculator')
        self.CalculatorButton.setGeometry(QtCore.QRect(5, 90, 120, 30))
        self.ToDoListButton = QtWidgets.QPushButton(self)
        self.ToDoListButton.setText('ToDoList')
        self.ToDoListButton.setGeometry(QtCore.QRect(150, 90, 120, 30))
        self.LalafoButton.clicked.connect(self.RunLalafoApp)
        self.CalculatorButton.clicked.connect(self.RunCalculatorApp)
        self.ToDoListButton.clicked.connect(self.RunToDoListApp)
        self.setWindowTitle('SelectApps')
        self.resize(290, 130)

    def RunLalafoApp(self):
        os.system('python ' + os.path.join(os.getcwd(), 'APPS\\LalafoApp\\main.py'))

    def RunCalculatorApp(self):
        os.system('python ' + os.path.join(os.getcwd(), 'APPS\\CalculatorApp\\main.py'))

    def RunToDoListApp(self):
        os.system('python ' + os.path.join(os.getcwd(), 'APPS\\ToDoListApp\\main.py'))


APP = QtWidgets.QApplication([])
Window = Apps()
Window.SetupUI()
Window.show()
APP.exec_()

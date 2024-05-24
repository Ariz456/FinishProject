from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWinExtras import QtWin
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
import os


class CalculatorApp(QtWidgets.QMainWindow):
    def SetupUI(self):
        self.setStyleSheet('font-family: MV Boli; font-weight: bold; font-size: 20px; letter-spacing: -1px; background-color: rgb(15, 15, 15);')
        self.CentralWidget = QtWidgets.QWidget(self)
        self.Layout_1 = QtWidgets.QGridLayout()
        self.Layout_2 = QtWidgets.QGridLayout(self.CentralWidget)

        Buttons = [('1', 2, 0, 1, 1), ('2', 2, 1, 1, 1), ('3', 2, 2, 1, 1), ('4', 3, 0, 1, 1), ('5', 3, 1, 1, 1), ('6', 3, 2, 1, 1), ('7', 4, 0, 1, 1), ('8', 4, 1, 1, 1),('9', 4, 2, 1, 1), ('0', 5, 0, 1, 2), ('.', 5, 2, 1, 1), ('+', 1, 3, 1, 1), ('-', 2, 3, 1, 1), ('*', 3, 3, 1, 1), ('/', 4, 3, 1, 1),('Del', 1, 2, 1, 1), ('Clear', 1, 0, 1, 2), ('=', 5, 3, 1, 1)]

        for text, row, col, rowspan, colspan in Buttons:
            Button = self.create_button(text)
            self.Layout_1.addWidget(Button, row, col, rowspan, colspan)

        self.InputLabel = QtWidgets.QLabel(self.CentralWidget)
        self.InputLabel.setAlignment(QtCore.Qt.AlignLeft)
        self.InputLabel.setStyleSheet('font-family: MV Boli; font-weight: bold; font-size: 50px; letter-spacing: -1px; color: white')
        self.Layout_1.addWidget(self.InputLabel, 0, 0, 1, 4)
        self.Layout_2.addLayout(self.Layout_1, 0, 0, 1, 1)
        self.setCentralWidget(self.CentralWidget)
        QtWin.setCurrentProcessExplicitAppUserModelID('324673567')
        self.setWindowTitle('CalculatorApp')
        self.resize(340, 475)

    def create_button(self, text):
        Button = QtWidgets.QPushButton(text)
        Button.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        Button.setStyleSheet("""
            QPushButton {
                font: 75 20pt "MS Shell Dlg 2";
                color: rgb(255, 255, 255);
                border-radius: 30px;
            }
            QPushButton:hover {
                background-color: rgb(52, 157, 77);
            }
            QPushButton:pressed {
                color: rgb(185, 185, 185);
            }
        """)
        Button.clicked.connect(lambda: self.ButtonClicked(text))
        return Button

    def ButtonClicked(self, text):
        CurrentText = self.InputLabel.text()
        if text == 'Clear':
            self.InputLabel.setText('')
        elif text == 'Del':
            self.InputLabel.setText(CurrentText[:-1])
        elif text == '=':
            self.InputLabel.setText(str(eval(CurrentText)))
        else:
            self.InputLabel.setText(CurrentText + text)


APP = QtWidgets.QApplication([])
Window = CalculatorApp()
Window.SetupUI()
Window.setWindowIcon(QtGui.QIcon(os.path.join(os.getcwd(), 'ICONS', 'CalculatorIcon.ico')))
Window.show()
APP.exec_()

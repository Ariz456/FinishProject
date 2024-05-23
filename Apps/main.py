from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
import os


class Apps(QtWidgets.QMainWindow):
    def SetupUI(self):
        self.setStyleSheet('font-family: MV Boli; font-weight: bold; font-size: 20px; letter-spacing: -1px;')
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(os.getcwd()), 'ICONS', 'SelectIcon.ico')))
        self.StartLabel = QtWidgets.QLabel(self)
        self.StartLabel.setText('Hello please select App :)')
        self.StartLabel.setGeometry(QtCore.QRect(3, 5, 275, 35))
        self.APPSButton = QtWidgets.QPushButton(self)
        self.APPSButton.setText('APPS')
        self.APPSButton.setGeometry(QtCore.QRect(80, 43, 95, 30))
        self.CalculatorButton = QtWidgets.QPushButton(self)
        self.CalculatorButton.setText('Calculator')
        self.CalculatorButton.setGeometry(QtCore.QRect(5, 90, 120, 30))
        self.WeatherButton = QtWidgets.QPushButton(self)
        self.WeatherButton.setText('Weather')
        self.WeatherButton.setGeometry(QtCore.QRect(150, 90, 120, 30))
        self.APPSButton.clicked.connect(self.RunAPPS)
        self.CalculatorButton.clicked.connect(self.RunCalculatorApp)
        self.WeatherButton.clicked.connect(self.RunWeatherApp)
        self.setWindowTitle('SelectApps')
        self.resize(290, 130)

    def RunWeatherApp(self):
        os.system('python ' + os.path.join(os.getcwd(), 'WeatherApp\\main.py'))

    def RunCalculatorApp(self):
        os.system('python ' + os.path.join(os.getcwd(), 'CalculatorApp\\main.py'))

    def RunAPPS(self):
        os.system('python ' + os.path.join(os.getcwd(), 'APPS\\main.py'))


APP = QtWidgets.QApplication([])
Window = Apps()
Window.SetupUI()
Window.show()
APP.exec_()

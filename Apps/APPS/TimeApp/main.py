from PyQt5.QtWidgets import QLabel, QApplication, QWidget
from PyQt5.QtCore import QTimer, QRect
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
import datetime
import os


class TimeApp(QWidget):
    def SetupUI(self):
        self.setStyleSheet('font-family: MV Boli; font-weight: bold; font-size: 230px; letter-spacing: -1px;')
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(os.getcwd()), 'ICONS', 'TimeIcon.ico')))
        self.TimeLabel = QLabel(self)
        self.TimeLabel.setGeometry(QRect(10, 5, 1200, 300))
        self.Timer = QTimer(self)
        self.Timer.timeout.connect(self.UpdateTime)
        self.Timer.start(1000)
        self.resize(1200, 300)
        self.setWindowTitle('TimeApp')

    def UpdateTime(self):
        self.TimeLabel.setText(datetime.datetime.now().strftime('%H:%M:%S'))


APP = QtWidgets.QApplication([])
Window = TimeApp()
Window.SetupUI()
Window.show()
APP.exec_()

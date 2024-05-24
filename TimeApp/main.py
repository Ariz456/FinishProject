from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication
from PyQt5.QtCore import QTimer, QRect
from PyQt5.QtWinExtras import QtWin
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIcon
import datetime


class TimeApp(QtWidgets.QMainWindow):
    def SetupUI(self):
        self.setStyleSheet('font-family: MV Boli; font-weight: bold; font-size: 230px; letter-spacing: -1px;')
        self.setWindowIcon(QtGui.QIcon('D:\\FinishProject\\ICONS\\TimeIcon.ico'))
        self.TimeLabel = QLabel(self)
        self.TimeLabel.setGeometry(QRect(10, 5, 1200, 300))
        self.Timer = QTimer(self)
        self.Timer.timeout.connect(self.UpdateTime)
        self.Timer.start(1000)
        QtWin.setCurrentProcessExplicitAppUserModelID('324673567')
        self.setWindowTitle('TimeApp')
        self.resize(1200, 300)

    def UpdateTime(self):
        self.TimeLabel.setText(datetime.datetime.now().strftime('%H:%M:%S'))


APP = QtWidgets.QApplication([])
Window = TimeApp()
Window.SetupUI()
Window.show()
APP.exec_()

from PyQt5.QtWidgets import QLabel, QApplication
from PyQt5.QtCore import QTimer, QRect
from PyQt5.QtWinExtras import QtWin
from PyQt5 import QtWidgets
from PyQt5 import QtGui
import datetime


class TimeApp(QtWidgets.QMainWindow):
    def SetupUI(self):
        self.setStyleSheet('font-family: MV Boli; font-weight: bold; font-size: 230px; letter-spacing: -1px;')
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
Window.setWindowIcon(QtGui.QIcon(os.path.join(os.getcwd(), 'ICONS', 'TimeIcon.ico')))
Window.show()
APP.exec_()

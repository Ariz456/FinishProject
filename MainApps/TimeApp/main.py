from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication
from PyQt5.QtCore import QTimer, QRect
from PyQt5.QtWinExtras import QtWin
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIcon
import datetime


# Определение класса приложения для отображения времени
class TimeApp(QtWidgets.QMainWindow):
    def SetupUI(self):
        # Установка стилей для текста времени
        self.setStyleSheet('font-family: MV Boli; font-weight: bold; font-size: 230px; letter-spacing: -1px;')
        # Установка иконки окна
        self.setWindowIcon(QtGui.QIcon('D:\\FinishProject\\ICONS\\TimeIcon.ico'))
        # Создание метки для отображения времени
        self.TimeLabel = QLabel(self)
        self.TimeLabel.setGeometry(QRect(10, 5, 1200, 300))
        # Создание таймера для обновления времени каждую секунду
        self.Timer = QTimer(self)
        self.Timer.timeout.connect(self.UpdateTime)
        self.Timer.start(1000)
        # Установка ID приложения для Windows
        QtWin.setCurrentProcessExplicitAppUserModelID('324673567')
        # Установка заголовка и размеров окна
        self.setWindowTitle('TimeApp')
        self.resize(1200, 300)

    # Метод для обновления времени на метке
    def UpdateTime(self):
        self.TimeLabel.setText(datetime.datetime.now().strftime('%H:%M:%S'))


# Создание экземпляра приложения
APP = QtWidgets.QApplication([])
# Создание главного окна приложения и его настройка
Window = TimeApp()
Window.SetupUI()
# Отображение главного окна
Window.show()
# Запуск цикла обработки событий приложения
APP.exec_()

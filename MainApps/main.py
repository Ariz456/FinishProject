from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWinExtras import QtWin
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
import os


# Определение главного окна
class Apps(QtWidgets.QMainWindow):
    def SetupUI(self):
        # Установка стилей для приложения
        self.setStyleSheet('font-family: MV Boli; font-weight: bold; font-size: 20px; letter-spacing: -1px;')
        # Установка иконки приложения
        self.setWindowIcon(QtGui.QIcon('D:\\FinishProject\\ICONS\\SelectIcon.ico'))
        # Создание метки с приветствием
        self.StartLabel = QtWidgets.QLabel(self)
        self.StartLabel.setText('Hello please select App :)')
        self.StartLabel.setGeometry(QtCore.QRect(3, 5, 275, 35))
        # Кнопка для выбора всех приложений
        self.APPSButton = QtWidgets.QPushButton(self)
        self.APPSButton.setText('APPS')
        self.APPSButton.setGeometry(QtCore.QRect(80, 43, 95, 30))
        # Кнопка для запуска погодного приложения
        self.WeatherButton = QtWidgets.QPushButton(self)
        self.WeatherButton.setText('Weather')
        self.WeatherButton.setGeometry(QtCore.QRect(5, 90, 120, 30))
        # Кнопка для запуска приложения с отображением времени
        self.TimeButton = QtWidgets.QPushButton(self)
        self.TimeButton.setText('Time')
        self.TimeButton.setGeometry(QtCore.QRect(150, 90, 120, 30))
        # Подключение обработчиков событий к кнопкам
        self.APPSButton.clicked.connect(self.RunAPPS)
        self.WeatherButton.clicked.connect(self.RunWeatherApp)
        self.TimeButton.clicked.connect(self.RunTimeApp)
        # Установка ID приложения для Windows
        QtWin.setCurrentProcessExplicitAppUserModelID('324673567')
        # Установка заголовка и размеров главного окна
        self.setWindowTitle('SelectApps')
        self.resize(290, 130)

    # Метод для запуска погодного приложения
    def RunWeatherApp(self):
        os.system('python ' + os.path.join(os.getcwd(), 'WeatherApp\\main.py'))

    # Метод для запуска приложения с отображением времени
    def RunTimeApp(self):
        os.system('python ' + os.path.join(os.getcwd(), 'TimeApp\\main.py'))

    # Метод для запуска всех приложений
    def RunAPPS(self):
        os.system('python ' + os.path.join(os.getcwd(), 'APPS\\main.py'))


# Создание объекта приложения и главного окна
APP = QtWidgets.QApplication([])
Window = Apps()
# Настройка пользовательского интерфейса главного окна и его отображение
Window.SetupUI()
Window.show()
# Запуск цикла обработки событий приложения
APP.exec_()

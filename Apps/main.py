from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWinExtras import QtWin
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
import os


# Определение главного окна
class APPS(QtWidgets.QMainWindow):
    def SetupUI(self):
        # Установка стилей для приложения
        self.setStyleSheet('font-family: MV Boli; font-weight: bold; font-size: 20px; letter-spacing: -1px;')
        # Установка иконки приложения
        self.setWindowIcon(QtGui.QIcon(os.path.join(os.getcwd(), 'ICONS', 'SelectIcon.ico')))
        # Создание метки с приветствием
        self.StartLabel = QtWidgets.QLabel(self)
        self.StartLabel.setText('Hello please select App :)')
        self.StartLabel.setGeometry(QtCore.QRect(3, 5, 275, 35))
        # Кнопка для запуска приложения Lalafo
        self.LalafoButton = QtWidgets.QPushButton(self)
        self.LalafoButton.setText('Lalafo')
        self.LalafoButton.setGeometry(QtCore.QRect(80, 43, 95, 30))
        # Кнопка для запуска калькулятора
        self.CalculatorButton = QtWidgets.QPushButton(self)
        self.CalculatorButton.setText('Calculator')
        self.CalculatorButton.setGeometry(QtCore.QRect(5, 90, 120, 30))
        # Кнопка для запуска приложения "Список дел"
        self.ToDoListButton = QtWidgets.QPushButton(self)
        self.ToDoListButton.setText('ToDoList')
        self.ToDoListButton.setGeometry(QtCore.QRect(150, 90, 120, 30))
        # Подключение обработчиков событий к кнопкам
        self.LalafoButton.clicked.connect(self.RunLalafoApp)
        self.CalculatorButton.clicked.connect(self.RunCalculatorApp)
        self.ToDoListButton.clicked.connect(self.RunToDoListApp)
        # Установка ID приложения для Windows
        QtWin.setCurrentProcessExplicitAppUserModelID('324673567')
        # Установка заголовка и размеров главного окна
        self.setWindowTitle('SelectApps')
        self.resize(290, 130)

    # Метод для запуска приложения Lalafo
    def RunLalafoApp(self):
        os.system('python ' + os.path.join(os.getcwd(), ''))  # Нужно указать путь к приложению Lalafo

    # Метод для запуска калькулятора
    def RunCalculatorApp(self):
        os.system('python ' + os.path.join(os.getcwd(), 'APPS', 'CalculatorApp', 'main.py'))

    # Метод для запуска приложения "Список дел"
    def RunToDoListApp(self):
        os.system('python ' + os.path.join(os.getcwd(), 'APPS', 'ToDoListApp', 'main.py'))


# Создание объекта приложения и главного окна
APP = QtWidgets.QApplication([])
Window = APPS()
# Настройка пользовательского интерфейса главного окна и его отображение
Window.SetupUI()
Window.show()
# Запуск цикла обработки событий приложения
APP.exec_()

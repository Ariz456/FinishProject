from PyQt5.QtWidgets import QCalendarWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWinExtras import QtWin
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
from time import sleep
from random import *
import configparser
import requests
import json
import os


# Определение класса приложения Lalafo
class LalafoApp(QtWidgets.QMainWindow):
    def SetupUI(self):
        # Установка стилей для приложения
        self.setStyleSheet('font-family: MV Boli; font-weight: bold; font-size: 20px; letter-spacing: -1px;')
        # Установка иконки приложения
        self.setWindowIcon(QtGui.QIcon('D:\\FinishProject\\ICONS\\LalafoIcon.ico'))
        # Создание и настройка изображения
        self.StartImage = QtWidgets.QLabel(self)
        self.StartImage.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(), 'APPS\\LalafoApp\\Image.png')))
        self.StartImage.setGeometry(QtCore.QRect(10, 10, 150, 150))
        self.StartImage.setScaledContents(True)
        # Создание кнопок
        self.StartButton = QtWidgets.QPushButton(self)
        self.StartButton.setText('Start')
        self.StartButton.setGeometry(QtCore.QRect(165, 20, 100, 30))
        self.CalendarButton = QtWidgets.QPushButton(self)
        self.CalendarButton.setText('Calendar')
        self.CalendarButton.setGeometry(QtCore.QRect(165, 70, 100, 30))
        self.TimeButton = QtWidgets.QPushButton(self)
        self.TimeButton.setText('Time')
        self.TimeButton.setGeometry(QtCore.QRect(165, 120, 100, 30))
        # Создание прогресс-бара
        self.ProgressBar = QtWidgets.QProgressBar(self)
        self.ProgressBar.setProperty('value', 0)
        self.ProgressBar.setGeometry(QtCore.QRect(10, 170, 250, 25))
        # Привязка событий кнопок к соответствующим методам
        self.StartButton.clicked.connect(self.GetStartProcess)
        self.CalendarButton.clicked.connect(self.GetOpenCalendar)
        self.TimeButton.clicked.connect(self.RunTimeApp)
        # Установка ID приложения для Windows
        QtWin.setCurrentProcessExplicitAppUserModelID('324673567')
        # Установка заголовка и размеров окна
        self.setWindowTitle('LalafoApp')
        self.resize(280, 200)

    # Метод для открытия календаря
    def GetOpenCalendar(self):
        self.calendar = QCalendarWidget()
        self.calendar.setGeometry(800, 350, 310, 250)
        self.calendar.setWindowTitle('Calendar')
        self.calendar.show()

    # Метод для выполнения процесса
    def GetStartProcess(self):
        # Чтение конфигурационного файла
        Config = configparser.ConfigParser()
        Config.read('config.ini', encoding='utf-8-sig')

        # URL-адреса для запросов
        AuthUrl = 'https://lalafo.kg/api/auth/login'
        AdsUrl = 'https://lalafo.kg/api/search/v3/feed/my/active?&page=1&expand=url&status_id_not[]=11'
        AdUpdateUrl = 'https://lalafo.kg/api/catalog/v32/posting-ads/'

        # Данные для аутентификации
        AuthPayload = json.dumps({
            'mobile': Config.get('auth', 'phone'),
            'password': Config.get('auth', 'password')
        })

        # Заголовки для запросов
        Headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'ru-RU,ru;q=0.9',
            'authorization': 'Bearer',
            'content-type': 'application/json',
            'country-id': '12',
            'device': 'pc',
            'language': 'ru_RU',
            'origin': 'https://lalafo.kg',
            'referer': 'https://lalafo.kg/',
            'user-agent': 'Mozilla/5.0 (Linux; U; Linux x86_64) AppleWebKit/600.40 (KHTML, like Gecko) Chrome/52.0.2333.255 Safari/603'
        }

        # Аутентификация
        AuthResponse = requests.post(AuthUrl, headers=Headers, data=AuthPayload).json()
        Token = AuthResponse.get('token')
        Headers['authorization'] = 'Bearer ' + Token

        # Получение списка объявлений и их обновление
        AdsResponse = requests.get(AdsUrl, headers=Headers).json()
        AdsItems = AdsResponse.get('items')

        for index, item in enumerate(AdsItems):
            AdId = str(item['id'])
            UpdateData = json.dumps({
                'currency': item['currency']
            })
            UpdateUrl = AdUpdateUrl + AdId
            requests.put(UpdateUrl, headers=Headers, data=UpdateData).json()
            self.ProgressBar.setValue(int((index + 1) * 100 / len(AdsItems)))

            if index != len(AdsItems) - 1:
                sleep(randint(1, 5))

    # Метод для запуска временного приложения
    def RunTimeApp(self):
        os.system('python ' + os.path.join(os.path.join(os.getcwd(), 'TimeApp\\main.py')))


# Создание экземпляра приложения
APP = QtWidgets.QApplication([])
# Создание главного окна приложения и его настройка
Window = LalafoApp()
Window.SetupUI()
# Установка иконки окна с использованием пути к иконке
Window.setWindowIcon(QtGui.QIcon(os.path.join(os.getcwd(), 'ICONS', 'LalafoIcon.ico')))
# Отображение главного окна
Window.show()
# Запуск цикла обработки событий приложения
APP.exec_()

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


class LalafoApp(QtWidgets.QMainWindow):
    def SetupUI(self):
        self.setStyleSheet('font-family: MV Boli; font-weight: bold; font-size: 20px; letter-spacing: -1px;')
        self.StartImage = QtWidgets.QLabel(self)
        self.StartImage.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(), 'APPS\\LalafoApp\\Image.png')))
        self.StartImage.setGeometry(QtCore.QRect(10, 10, 150, 150))
        self.StartImage.setScaledContents(True)
        self.StartButton = QtWidgets.QPushButton(self)
        self.StartButton.setText('Start')
        self.StartButton.setGeometry(QtCore.QRect(165, 20, 100, 30))
        self.CalendarButton = QtWidgets.QPushButton(self)
        self.CalendarButton.setText('Calendar')
        self.CalendarButton.setGeometry(QtCore.QRect(165, 70, 100, 30))
        self.TimeButton = QtWidgets.QPushButton(self)
        self.TimeButton.setText('Time')
        self.TimeButton.setGeometry(QtCore.QRect(165, 120, 100, 30))
        self.ProgressBar = QtWidgets.QProgressBar(self)
        self.ProgressBar.setProperty('value', 0)
        self.ProgressBar.setGeometry(QtCore.QRect(10, 170, 250, 25))
        self.StartButton.clicked.connect(self.GetStartProcess)
        self.CalendarButton.clicked.connect(self.GetOpenCalendar)
        self.TimeButton.clicked.connect(self.RunTimeApp)
        QtWin.setCurrentProcessExplicitAppUserModelID('324673567')
        self.setWindowTitle('LalafoApp')
        self.resize(280, 200)


    def GetOpenCalendar(self):
        self.calendar = QCalendarWidget()
        self.calendar.setGeometry(800, 350, 310, 250)
        self.calendar.setWindowTitle('Calendar')
        self.calendar.show()

    def GetStartProcess(self):
        Config = configparser.ConfigParser()
        Config.read('config.ini', encoding='utf-8-sig')

        AuthUrl = 'https://lalafo.kg/api/auth/login'
        AdsUrl = 'https://lalafo.kg/api/search/v3/feed/my/active?&page=1&expand=url&status_id_not[]=11'
        AdUpdateUrl = 'https://lalafo.kg/api/catalog/v32/posting-ads/'

        AuthPayload = json.dumps({
            'mobile': Config.get('auth', 'phone'),
            'password': Config.get('auth', 'password')
        })

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

        AuthResponse = requests.post(AuthUrl, headers=Headers, data=AuthPayload).json()
        Token = AuthResponse.get('token')
        Headers['authorization'] = 'Bearer ' + Token
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

    def RunTimeApp(self):
        os.system('python ' + os.path.join(os.path.join(os.getcwd(), 'TimeApp\\main.py')))


APP = QtWidgets.QApplication([])
Window = CalculatorApp()
Window.SetupUI()
Window.setWindowIcon(QtGui.QIcon(os.path.join(os.getcwd(), 'ICONS', 'LalafoIcon.ico')))
Window.show()
APP.exec_()

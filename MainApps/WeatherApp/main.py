from bs4 import BeautifulSoup as bs4
from PyQt5.QtWinExtras import QtWin
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
from requests import *
import os


# Определение класса приложения погоды
class WeatherApp(QtWidgets.QMainWindow):
    def SetupUI(self):
        # Установка стилей для приложения
        self.setStyleSheet('font-family: MV Boli; font-weight: bold; font-size: 20px; letter-spacing: -1px;')
        # Установка иконки приложения
        self.setWindowIcon(QtGui.QIcon('D:\\FinishProject\\ICONS\\WeatherIcon.ico'))
        # Создание меток для отображения информации о погоде
        self.StartLabel = QtWidgets.QLabel(self)
        self.StartLabel.setText('Hello in app you will learn about the weather :)')
        self.StartLabel.setGeometry(QtCore.QRect(10, 10, 480, 25))
        self.TemperatureLabel = QtWidgets.QLabel(self)
        self.TemperatureLabel.setGeometry(QtCore.QRect(10, 85, 240, 25))
        self.DescriptionLabel = QtWidgets.QLabel(self)
        self.DescriptionLabel.setGeometry(QtCore.QRect(10, 50, 480, 25))
        self.WindSpeedLabel = QtWidgets.QLabel(self)
        self.WindSpeedLabel.setGeometry(QtCore.QRect(270, 120, 250, 25))
        self.Humiditylabel = QtWidgets.QLabel(self)
        self.Humiditylabel.setGeometry(QtCore.QRect(270, 85, 250, 25))
        self.Visibilitylabel = QtWidgets.QLabel(self)
        self.Visibilitylabel.setGeometry(QtCore.QRect(10, 120, 250, 25))
        # Установка ID приложения для Windows
        QtWin.setCurrentProcessExplicitAppUserModelID('324673567')
        # Установка заголовка и размеров окна
        self.setWindowTitle('WeatherApp')
        self.resize(500, 160)

    # Метод для поиска информации о погоде и ее отображения
    def SearchWeather(self):
        # Отправка запроса на сайт с погодой и получение HTML-кода страницы
        Response = get('https://weather.com/ru-KG/weather/today/l/KGXX0001').content
        # Создание объекта BeautifulSoup для парсинга HTML
        Soup = bs4(Response, "html.parser")
        # Поиск элементов с информацией о погоде на странице
        TodayDetails = Soup.select_one('#todayDetails').select_one('.TodayDetailsCard--detailsContainer--2yLtL')
        WindSpeed = TodayDetails.select_one(
            '[data-testid=WeatherDetailsListItem]:nth-of-type(2) [data-testid=wxData] span').text.strip()
        WindSpeed = ''.join(filter(lambda x: x.isdigit(), WindSpeed))  # Извлечение числовой информации из строки
        Humidity = TodayDetails.select_one(
            '[data-testid=WeatherDetailsListItem]:nth-of-type(3) [data-testid=wxData] span').text.strip()
        Visibility = TodayDetails.select_one(
            '[data-testid=WeatherDetailsListItem]:nth-of-type(7) [data-testid=wxData] span').text.strip()
        Temperature = Soup.select_one('[data-testid="TemperatureValue"]').text.strip()
        Description = Soup.select_one('[data-testid="wxPhrase"]').text.strip()

        # Обновление меток информацией о погоде
        self.TemperatureLabel.setText('Temperature: ' + Temperature)
        self.WindSpeedLabel.setText('WindSpeed: ' + WindSpeed + ' km/h')
        self.DescriptionLabel.setText('Description: ' + Description)
        self.Humiditylabel.setText('Humidity: ' + Humidity)
        self.Visibilitylabel.setText('Visibility: ' + Visibility)


# Создание экземпляра приложения
APP = QtWidgets.QApplication([])
# Создание главного окна приложения и его настройка
Window = WeatherApp()
Window.SetupUI()
# Поиск информации о погоде и отображение ее
Window.SearchWeather()
# Отображение главного окна
Window.show()
# Запуск цикла обработки событий приложения
APP.exec_()

from bs4 import BeautifulSoup as bs4
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from requests import *
  
  
class WeatherApp(QtWidgets.QMainWindow):  
    def SetupUI(self):  
        self.setStyleSheet('font-family: MV Boli; font-weight: bold; font-size: 20px; letter-spacing: -1px;')
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
        self.setWindowTitle('WeatherApp')  
        self.resize(500, 160)  
  
    def SearchWeather(self):
        Response = get('https://weather.com/ru-KG/weather/today/l/KGXX0001').content
        Soup = bs4(Response, "html.parser")
        TodayDetails = Soup.select_one('#todayDetails').select_one('.TodayDetailsCard--detailsContainer--2yLtL')
        WindSpeed = TodayDetails.select_one('[data-testid=WeatherDetailsListItem]:nth-of-type(2) [data-testid=wxData] span').text.strip()  
        WindSpeed = ''.join(filter(lambda x: x.isdigit(), WindSpeed))  
        Humidity = TodayDetails.select_one('[data-testid=WeatherDetailsListItem]:nth-of-type(3) [data-testid=wxData] span').text.strip()
        Visibility = TodayDetails.select_one('[data-testid=WeatherDetailsListItem]:nth-of-type(7) [data-testid=wxData] span').text.strip()
        Temperature = Soup.select_one('[data-testid="TemperatureValue"]').text.strip()
        Description = Soup.select_one('[data-testid="wxPhrase"]').text.strip()
  
        self.TemperatureLabel.setText('Temperature: ' + Temperature)
        self.WindSpeedLabel.setText('WindSpeed: ' + WindSpeed + ' km/h')
        self.DescriptionLabel.setText('Description: ' + Description)
        self.Humiditylabel.setText('Humidity: ' + Humidity)
        self.Visibilitylabel.setText('Visibility: ' + Visibility)
  
  
APP = QtWidgets.QApplication([])
Window = WeatherApp()
Window.SetupUI()
Window.SearchWeather()
Window.show()
APP.exec_()

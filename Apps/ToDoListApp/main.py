from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWinExtras import QtWin
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
import os


class ToDoListApp(QtWidgets.QMainWindow):
    def SetupUI(self):
        # Установка стилей для приложения
        self.setStyleSheet('font-family: MV Boli; font-weight: bold; font-size: 20px; letter-spacing: -1px;')
        # Установка иконки приложения
        self.setWindowIcon(QtGui.QIcon('D:\\FinishProject\\ICONS\\ToDoListIcon.ico'))
        # Создание и настройка метки "My ToDo list:"
        self.StartLabel = QtWidgets.QLabel(self)
        self.StartLabel.setText('My ToDo list:')
        self.StartLabel.setGeometry(QtCore.QRect(103, 10, 170, 33))
        # Создание виджета списка задач
        self.ListWidget = QtWidgets.QListWidget(self)
        self.ListWidget.setGeometry(QtCore.QRect(20, 50, 400, 390))
        # Создание кнопки "Add Task" и привязка к ней метода
        self.AddButton = QtWidgets.QPushButton(self)
        self.AddButton.setText('Add Task')
        self.AddButton.setGeometry(QtCore.QRect(455, 15, 170, 50))
        self.AddButton.clicked.connect(self.AddTask)
        # Создание кнопки "Delete Task" и привязка к ней метода
        self.DeleteButton = QtWidgets.QPushButton(self)
        self.DeleteButton.setText('Delete Task')
        self.DeleteButton.setGeometry(QtCore.QRect(455, 80, 170, 50))
        self.DeleteButton.clicked.connect(self.DeleteTask)
        # Создание кнопки "Check All" и привязка к ней метода
        self.CheckButton = QtWidgets.QPushButton(self)
        self.CheckButton.setGeometry(QtCore.QRect(455, 150, 170, 50))
        self.CheckButton.setText('Check All')
        self.CheckButton.clicked.connect(self.CheckAllTasks)
        # Создание кнопки "UnCheck All" и привязка к ней метода
        self.UnCheckButton = QtWidgets.QPushButton(self)
        self.UnCheckButton.setText('UnCheck All')
        self.UnCheckButton.setGeometry(QtCore.QRect(455, 220, 170, 50))
        self.UnCheckButton.clicked.connect(self.UnCheckAllTasks)
        # Установка ID приложения для Windows
        QtWin.setCurrentProcessExplicitAppUserModelID('324673567')
        # Установка заголовка и размеров окна
        self.setWindowTitle('ToDoListApp')
        self.resize(640, 450)

    # Метод для добавления задачи
    def AddTask(self):
        TaskText, ok = QtWidgets.QInputDialog.getText(self, 'Add Task', 'Enter task:')
        if ok:
            self.ListWidget.addItem(TaskText)

    # Метод для удаления задачи
    def DeleteTask(self):
        SelectedItem = self.ListWidget.currentItem()
        if SelectedItem is not None:
            self.ListWidget.takeItem(self.ListWidget.row(SelectedItem))

    # Метод для отметки всех задач как выполненных
    def CheckAllTasks(self):
        for x in range(self.ListWidget.count()):
            Item = self.ListWidget.item(x)
            Item.setCheckState(QtCore.Qt.Checked)

    # Метод для снятия отметки со всех задач
    def UnCheckAllTasks(self):
        for x in range(self.ListWidget.count()):
            Item = self.ListWidget.item(x)
            Item.setCheckState(QtCore.Qt.Unchecked)


# Создание экземпляра приложения
APP = QtWidgets.QApplication([])
# Создание главного окна приложения и его настройка
Window = ToDoListApp()
Window.SetupUI()
# Отображение главного окна
Window.show()
# Запуск цикла обработки событий приложения
APP.exec_()

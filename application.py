from ui.main_app_ui import *
from PyQt6.QtWidgets import QWidget
from PyQt6 import QtWidgets
from PyQt6.QtCore import QDate
import json
from popup import Popup


def format_qdate(qdate):
    return f'{qdate.month()}-{qdate.day()}-{qdate.year()}'


class MyApplication(QWidget):
    def __init__(self):
        super().__init__()

        self.data = None

        # set up ui file
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # give button functionality
        self.ui.pushButton.clicked.connect(self.make_popup)

        # load the current data. if there is no data file, create it.
        # set the minimum date of the dateEdit to the date that the widget was created
        self.load_data()

        # set default opening date of date edit to the current date
        self.ui.dateEdit.setDate(QDate.currentDate())
        self.ui.dateEdit.dateChanged.connect(self.populate_screen)

        # create scene and font
        self.scene = QtWidgets.QGraphicsScene(self)
        self.ui.graphicsView.setScene(self.scene)
        self.font = QtGui.QFont()
        self.font.setPointSize(16)

        # populate current day on opening app
        self.populate_screen()

    def load_data(self):
        try:
            with open('data.json', 'r') as data_file:
                self.data = json.load(data_file)
        except FileNotFoundError:
            self.data = {
                'min_date': (QDate.currentDate().year(), QDate.currentDate().month(), QDate.currentDate().day()),
                'data': {}
            }
            with open('data.json', 'w') as data_file:
                json.dump(self.data, data_file, indent=2)
        finally:
            self.ui.dateEdit.setMinimumDate(QDate(*self.data['min_date']))

    def make_popup(self):
        self.popup = Popup(self)
        self.popup.show()

    def item_added(self, text):
        # add item from popup to the data file for the current date
        date = format_qdate(self.ui.dateEdit.date())
        date_data = self.data['data'].get(date, None)

        if not date_data:
            self.data['data'][date] = [[text, False]]
        else:
            self.data['data'][date].append([text, False])

        self.update_json()

    def update_json(self):
        with open('data.json', 'w') as data_file:
            json.dump(self.data, data_file)

    def populate_screen(self):
        # add all text to the graphics view
        self.scene.clear()
        self.scene.addText(' ')

        date = format_qdate(self.ui.dateEdit.date())
        date_data = self.data['data'].get(date, None)

        if date_data:
            for index, task in enumerate(date_data):
                task, completion_status = task[0], task[1]
                checkbox = QtWidgets.QCheckBox()
                checkbox.index = index
                checkbox.toggled.connect(self.checkbox_clicked)
                checkbox.setChecked(completion_status)
                item = self.scene.addWidget(checkbox)
                item.setPos(75 - self.ui.graphicsView.width(), 65 - self.ui.graphicsView.height() + 50 * index)

                text = self.scene.addText(task, font=self.font)
                text.setPos(100 - self.ui.graphicsView.width(), 50 - self.ui.graphicsView.height() + 50 * index)

    def checkbox_clicked(self):
        cbox = self.sender()
        self.data['data'][format_qdate(QDate().currentDate())][cbox.index][1] = cbox.isChecked()
        self.update_json()
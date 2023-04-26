from ui.pop_up import *
from PyQt6.QtWidgets import QWidget


class Popup(QWidget):
    def __init__(self, parent):
        super(Popup, self).__init__()
        # add main application as parent of the popup window
        self.parent = parent

        # set up ui
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # give button functionality
        self.ui.pushButton.clicked.connect(self.button_pressed)

    def button_pressed(self):
        text = self.ui.plainTextEdit.toPlainText()
        if text:
            self.parent.item_added(text)
            self.parent.populate_screen()
        self.close()

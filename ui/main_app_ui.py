# Form implementation generated from reading ui file 'main_app_ui.ui'
#
# Created by: PyQt6 UI code generator 6.4.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 600)
        self.dateEdit = QtWidgets.QDateEdit(parent=Form)
        self.dateEdit.setGeometry(QtCore.QRect(120, 70, 120, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(195, 10, 110, 41))
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.graphicsView = QtWidgets.QGraphicsView(parent=Form)
        self.graphicsView.setGeometry(QtCore.QRect(10, 110, 480, 480))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(270, 70, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "To Do"))
        self.pushButton.setText(_translate("Form", "Add Item"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())

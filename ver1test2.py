# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiver1.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 60, 531, 371))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 1, 0, 1, 1)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.gridLayout.addWidget(self.plainTextEdit_2, 2, 1, 1, 1)
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.gridLayout.addWidget(self.plainTextEdit_3, 1, 2, 1, 1)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.gridLayout)
        self.pushButton.clicked.connect(self.decrypt)
        self.pushButton_3.clicked.connect(self.encrypt)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "History"))
        self.label.setText(_translate("Form", "Input"))
        self.pushButton.setText(_translate("Form", "Decrypt"))
        self.label_2.setText(_translate("Form", "Output"))
        self.label_4.setText(_translate("Form", "Key"))
        self.pushButton_3.setText(_translate("Form", "Encrypt"))

    def encrypt(self):
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

        message = self.plainTextEdit.toPlainText()

        # self.label_3.setText(message)
        # self.lineEdit.textChanged.connect(self.update_label)

        key = self.plainTextEdit_2.toPlainText()

        translated_message = ''
        encrypt = "E"
        mode = "E"
        index = 0
        for character in message:  # encryption/decryption method

            if character in letters:
                number = letters.find(character)

                if mode in encrypt:
                    number = number + (ord(key[index]) - ord('a'))

                index = index + 1
                index = index % len(key)

                if number >= len(letters):
                    number = number - len(letters)
                elif number < 0:
                    number = number + len(letters)

                translated_message = translated_message + letters[number]
            else:
                translated_message = translated_message + character
            self.plainTextEdit_3.setPlainText(translated_message)

        return translated_message

    def decrypt(self):
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

        message = self.plainTextEdit.toPlainText()

        # self.label_3.setText(message)
        # self.lineEdit.textChanged.connect(self.update_label)

        key = self.plainTextEdit_2.toPlainText()

        translated_message = ''
        decrypt = "D"
        mode = "D"
        index = 0
        for character in message:  # encryption/decryption method
            if character in letters:
                number = letters.find(character)

                if mode in decrypt:
                    number = number - (ord(key[index]) - ord('a'))

                index = index + 1
                index = index % len(key)

                if number >= len(letters):
                    number = number - len(letters)
                elif number < 0:
                    number = number + len(letters)

                translated_message = translated_message + letters[number]



            else:
                translated_message = translated_message + character

            self.plainTextEdit_3.setPlainText(translated_message)
        return translated_message




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

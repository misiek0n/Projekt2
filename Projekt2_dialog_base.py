# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Projekt2_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Projekt2DialogBase(object):
    def setupUi(self, Projekt2DialogBase):
        Projekt2DialogBase.setObjectName("Projekt2DialogBase")
        Projekt2DialogBase.resize(634, 538)
        self.button_box = QtWidgets.QDialogButtonBox(Projekt2DialogBase)
        self.button_box.setGeometry(QtCore.QRect(280, 500, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.label_wynik = QtWidgets.QLabel(Projekt2DialogBase)
        self.label_wynik.setGeometry(QtCore.QRect(380, 450, 231, 31))
        self.label_wynik.setText("")
        self.label_wynik.setObjectName("label_wynik")
        self.label_wynik_obl = QtWidgets.QLabel(Projekt2DialogBase)
        self.label_wynik_obl.setGeometry(QtCore.QRect(20, 30, 73, 16))
        self.label_wynik_obl.setObjectName("label_wynik_obl")
        self.comboBox_obliczenie = QtWidgets.QComboBox(Projekt2DialogBase)
        self.comboBox_obliczenie.setGeometry(QtCore.QRect(20, 48, 142, 16))
        self.comboBox_obliczenie.setObjectName("comboBox_obliczenie")
        self.comboBox_obliczenie.addItem("")
        self.comboBox_obliczenie.addItem("")
        self.radioButton_m2 = QtWidgets.QRadioButton(Projekt2DialogBase)
        self.radioButton_m2.setGeometry(QtCore.QRect(30, 410, 113, 17))
        self.radioButton_m2.setObjectName("radioButton_m2")
        self.radioButton_ar = QtWidgets.QRadioButton(Projekt2DialogBase)
        self.radioButton_ar.setGeometry(QtCore.QRect(30, 433, 40, 17))
        self.radioButton_ar.setObjectName("radioButton_ar")
        self.radioButton_ha = QtWidgets.QRadioButton(Projekt2DialogBase)
        self.radioButton_ha.setGeometry(QtCore.QRect(30, 456, 61, 17))
        self.radioButton_ha.setObjectName("radioButton_ha")
        self.label_jedn_pole = QtWidgets.QLabel(Projekt2DialogBase)
        self.label_jedn_pole.setGeometry(QtCore.QRect(30, 391, 131, 16))
        self.label_jedn_pole.setObjectName("label_jedn_pole")
        self.comboBox_uklad = QtWidgets.QComboBox(Projekt2DialogBase)
        self.comboBox_uklad.setGeometry(QtCore.QRect(20, 94, 142, 16))
        self.comboBox_uklad.setObjectName("comboBox_uklad")
        self.comboBox_uklad.addItem("")
        self.comboBox_uklad.addItem("")
        self.label_wybor_wsp = QtWidgets.QLabel(Projekt2DialogBase)
        self.label_wybor_wsp.setGeometry(QtCore.QRect(20, 76, 142, 16))
        self.label_wybor_wsp.setObjectName("label_wybor_wsp")

        self.retranslateUi(Projekt2DialogBase)
        self.button_box.accepted.connect(Projekt2DialogBase.accept) # type: ignore
        self.button_box.rejected.connect(Projekt2DialogBase.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Projekt2DialogBase)

    def retranslateUi(self, Projekt2DialogBase):
        _translate = QtCore.QCoreApplication.translate
        Projekt2DialogBase.setWindowTitle(_translate("Projekt2DialogBase", "Projekt2"))
        self.label_wynik_obl.setText(_translate("Projekt2DialogBase", "Wybór obliczeń"))
        self.comboBox_obliczenie.setItemText(0, _translate("Projekt2DialogBase", "Różnica wysokości"))
        self.comboBox_obliczenie.setItemText(1, _translate("Projekt2DialogBase", "Pole powierzchni"))
        self.radioButton_m2.setText(_translate("Projekt2DialogBase", "Metry kwadratowe"))
        self.radioButton_ar.setText(_translate("Projekt2DialogBase", "Ary"))
        self.radioButton_ha.setText(_translate("Projekt2DialogBase", "Hektary"))
        self.label_jedn_pole.setText(_translate("Projekt2DialogBase", "Jednostka pola powierzchni"))
        self.comboBox_uklad.setItemText(0, _translate("Projekt2DialogBase", "PL-2000"))
        self.comboBox_uklad.setItemText(1, _translate("Projekt2DialogBase", "PL-1992"))
        self.label_wybor_wsp.setText(_translate("Projekt2DialogBase", "Wybór układu współrzędnych"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Projekt2DialogBase = QtWidgets.QDialog()
    ui = Ui_Projekt2DialogBase()
    ui.setupUi(Projekt2DialogBase)
    Projekt2DialogBase.show()
    sys.exit(app.exec_())

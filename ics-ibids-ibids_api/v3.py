# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alert.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

##strings for alert ###
found_msg_1 = "is ground truth task cycle but "
same_msg = "Ground Truth and inferred truth are the same"
error_msg = "Measurements are Inconclusive"
############
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_dialogAlert(object):
    def setupUi(self, dialogAlert):
        dialogAlert.setObjectName(_fromUtf8("dialogAlert"))
        dialogAlert.resize(721, 482)
        self.lblFound = QtGui.QLabel(dialogAlert)
        self.lblFound.setGeometry(QtCore.QRect(30, 20, 81, 17))
        self.lblFound.setObjectName(_fromUtf8("lblFound"))
        self.label1 = QtGui.QLabel(dialogAlert)
        self.label1.setGeometry(QtCore.QRect(20, 60, 131, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setObjectName(_fromUtf8("label1"))
        self.label2 = QtGui.QLabel(dialogAlert)
        self.label2.setGeometry(QtCore.QRect(400, 60, 191, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label2.setFont(font)
        self.label2.setObjectName(_fromUtf8("label2"))
        self.lblSame = QtGui.QLabel(dialogAlert)
        self.lblSame.setGeometry(QtCore.QRect(30, 110, 121, 17))
        self.lblSame.setObjectName(_fromUtf8("lblSame"))
        self.lblError = QtGui.QLabel(dialogAlert)
        self.lblError.setGeometry(QtCore.QRect(30, 200, 121, 17))
        self.lblError.setObjectName(_fromUtf8("lblError"))
        self.btnUpdate = QtGui.QPushButton(dialogAlert)
        self.btnUpdate.setGeometry(QtCore.QRect(40, 290, 98, 27))
        self.btnUpdate.setObjectName(_fromUtf8("btnUpdate"))
        self.btnClose = QtGui.QPushButton(dialogAlert)
        self.btnClose.setGeometry(QtCore.QRect(150, 290, 98, 27))
        self.btnClose.setObjectName(_fromUtf8("btnClose"))
        self.txtSame = QtGui.QPlainTextEdit(dialogAlert)
        self.txtSame.setGeometry(QtCore.QRect(30, 140, 391, 41))
        self.txtSame.setObjectName(_fromUtf8("txtSame"))
        self.txtError = QtGui.QPlainTextEdit(dialogAlert)
        self.txtError.setGeometry(QtCore.QRect(30, 230, 391, 41))
        self.txtError.setObjectName(_fromUtf8("txtError"))
        self.txtAlert = QtGui.QPlainTextEdit(dialogAlert)
        self.txtAlert.setGeometry(QtCore.QRect(160, 50, 231, 41))
        self.txtAlert.setObjectName(_fromUtf8("txtAlert"))

        self.statusLabel = QtGui.QLabel(dialogAlert)
        self.statusLabel.setGeometry(QtCore.QRect(50, 350, 301, 61))
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))

        self.retranslateUi(dialogAlert)
        QtCore.QMetaObject.connectSlotsByName(dialogAlert)
        QtCore.QObject.connect(self.btnClose, QtCore.SIGNAL(_fromUtf8("clicked()")), dialogAlert.close)
        QtCore.QObject.connect(self.btnUpdate, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.updateMsg)

    def retranslateUi(self, dialogAlert):
        dialogAlert.setWindowTitle(_translate("dialogAlert", "Alerts and Notifications", None))
        self.lblFound.setText(_translate("dialogAlert", "FoundAlert", None))
        self.label1.setText(_translate("dialogAlert", "<Ground truth ns>", None))
        self.label2.setText(_translate("dialogAlert", "<inferred ns> was inferred", None))
        self.lblSame.setText(_translate("dialogAlert", "Same Inferrence", None))
        self.lblError.setText(_translate("dialogAlert", "Error", None))
        self.btnUpdate.setText(_translate("dialogAlert", "Update", None))
        self.btnClose.setText(_translate("dialogAlert", "Close", None))
        self.statusLabel.setText(_translate("dialogAlert", "Press Update to change alert message", None))

        import front
        self.txtSame.setPlainText(_translate("dialogAlert", error_msg, None))
        self.txtError.setPlainText(_translate("dialogAlert", same_msg, None))
        self.txtAlert.setPlainText(_translate("dialogAlert", found_msg_1, None))

    def updateMsg(self):
        import front
        found_msg_1 = self.txtAlert.toPlainText()
        same_msg = self.txtSame.toPlainText()
        error_msg = self.txtError.toPlainText()
        self.statusLabel.setText("Update to Alert message done")


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    dialogAlert = QtGui.QDialog()
    ui = Ui_dialogAlert()
    ui.setupUi(dialogAlert)
    dialogAlert.show()
    sys.exit(app.exec_())

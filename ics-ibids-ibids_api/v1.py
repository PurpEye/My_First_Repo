# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_stux.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1013, 659)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.profileBtn = QtGui.QPushButton(self.centralwidget)
        self.profileBtn.setGeometry(QtCore.QRect(90, 80, 98, 27))
        self.profileBtn.setObjectName(_fromUtf8("profileBtn"))

        self.statusLabel = QtGui.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(330, 10, 541, 411))
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))

        self.btnAlert = QtGui.QPushButton(self.centralwidget)
        self.btnAlert.setGeometry(QtCore.QRect(90, 280, 98, 27))
        self.btnAlert.setObjectName(_fromUtf8("btnAlert"))

        self.monitor_button = QtGui.QPushButton(self.centralwidget)
        self.monitor_button.setGeometry(QtCore.QRect(90, 150, 148, 27))
        self.monitor_button.setObjectName(_fromUtf8("monitor_button"))

        self.lblRobo = QtGui.QLabel(self.centralwidget)
        self.lblRobo.setGeometry(QtCore.QRect(710, 10, 201, 131))
        self.lblRobo.setText(_fromUtf8(""))
        self.lblRobo.setPixmap(QtGui.QPixmap(_fromUtf8("img/RoboCop.jpg")))
        self.lblRobo.setScaledContents(True)
        self.lblRobo.setObjectName(_fromUtf8("lblRobo"))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.hostTxt = QtGui.QPlainTextEdit(self.centralwidget)
        self.hostTxt.setGeometry(QtCore.QRect(60, 220, 191, 31))
        self.hostTxt.setObjectName(_fromUtf8("hostTxt"))

        self.monitor_button_1 = QtGui.QRadioButton(self.centralwidget)
        self.monitor_button_1.setGeometry(QtCore.QRect(300, 300, 116, 22))
        self.monitor_button_1.setObjectName(_fromUtf8("monitor_button_1"))
        self.monitor_button_1.setChecked(True)

        self.monitor_button_2 = QtGui.QRadioButton(self.centralwidget)
        self.monitor_button_2.setGeometry(QtCore.QRect(300, 330, 116, 22))
        self.monitor_button_2.setObjectName(_fromUtf8("monitor_button_2"))

        self.monitor_button_3 = QtGui.QRadioButton(self.centralwidget)
        self.monitor_button_3.setGeometry(QtCore.QRect(400, 300, 116, 22))
        self.monitor_button_3.setObjectName(_fromUtf8("monitor_button_3"))

        self.monitor_button_4 = QtGui.QRadioButton(self.centralwidget)
        self.monitor_button_4.setGeometry(QtCore.QRect(400, 330, 116, 22))
        self.monitor_button_4.setObjectName(_fromUtf8("monitor_button_4"))

        self.monitor_button_5 = QtGui.QRadioButton(self.centralwidget)
        self.monitor_button_5.setGeometry(QtCore.QRect(400, 360, 116, 22))
        self.monitor_button_5.setObjectName(_fromUtf8("monitor_button_5"))
        # self.btnStop = QtGui.QPushButton(self.centralwidget)
        # self.btnStop.setGeometry(QtCore.QRect(190, 140, 131, 27))
        # self.btnStop.setObjectName(_fromUtf8("btnStop"))

        self.lblStart = QtGui.QLabel(self.centralwidget)
        self.lblStart.setGeometry(QtCore.QRect(80, 20, 371, 31))

        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lblStart.setFont(font)
        self.lblStart.setObjectName(_fromUtf8("label_2"))

        self.lblScada = QtGui.QLabel(self.centralwidget)
        self.lblScada.setGeometry(QtCore.QRect(720, 150, 181, 121))
        self.lblScada.setText(_fromUtf8(""))
        self.lblScada.setPixmap(QtGui.QPixmap(_fromUtf8("img/rtu.jpg")))
        self.lblScada.setScaledContents(True)
        self.lblScada.setObjectName(_fromUtf8("lblScada"))

        self.lblOutput = QtGui.QLabel(self.centralwidget)
        self.lblOutput.setGeometry(QtCore.QRect(90, 360, 661, 201))
        self.lblOutput.setText(_fromUtf8(""))
        self.lblOutput.setObjectName(_fromUtf8("lblOutput"))

        self.lblOHead = QtGui.QLabel(self.centralwidget)
        self.lblOHead.setGeometry(QtCore.QRect(90, 320, 66, 17))
        self.lblOHead.setObjectName(_fromUtf8("lblOHead"))

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        #        QtCore.QObject.connect(self.profileBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButton_3.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow",
                                             "Industrial Control Systems Inference-based Intrusion Detection System (ICS-iBIDS)",
                                             None))
        self.profileBtn.setText(_translate("MainWindow", "Profile", None))
        self.btnAlert.setText(_translate("MainWindow", "Alert", None))
        self.lblOHead.setText(_translate("MainWindow", "Output:", None))
        self.lblStart.setText(_translate("MainWindow", "ICS-iBIDS CPU Usage COP", None))
        #self.btnStop.setText(_translate("MainWindow", "Stop Monitoring", None))

        self.monitor_button.setText(_translate("MainWindow", "Monitor Mode", None))

        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.statusLabel.setText(_translate("MainWindow",
                                            "<html><head/><body><p>-Click Profile to create profiles</p><p>-Click Train Button to train classifier</p><p>-Monitor to switch to IDS mode</p><p>-Enter host and task cycle in text box as following format : <p>hostname;taskcycle(ns) Eg 192.168.1.1;50</p> </p> </body></html>",
                                            None))
        self.monitor_button_1.setText(_translate("MainWindow", "Mode 1", None))
        self.monitor_button_2.setText(_translate("MainWindow", "Mode 2", None))
        self.monitor_button_3.setText(_translate("MainWindow", "Mode 3", None))
        self.monitor_button_4.setText(_translate("MainWindow", "Mode 4", None))
        self.monitor_button_5.setText(_translate("MainWindow", "Mode 5 (EXPT)", None))



if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

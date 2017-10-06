# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prof_dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import os, sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import txt2csv as t2csv
import glob, os, re
from measurements import perform_filter

OWNER = 'rn'
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


class Ui_profileDialog(object):
    def setupUi(self, profileDialog):
        profileDialog.setObjectName(_fromUtf8("profileDialog"))
        profileDialog.resize(492, 428)
        profileDialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        profileDialog.setAutoFillBackground(True)
        self.buttonBox = QtGui.QDialogButtonBox(profileDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 220, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.p1text = QtGui.QPlainTextEdit(profileDialog)
        self.p1text.setGeometry(QtCore.QRect(50, 50, 104, 21))
        self.p1text.setPlainText(_fromUtf8(""))
        self.p1text.setObjectName(_fromUtf8("p1text"))
        self.profilebtn1 = QtGui.QPushButton(profileDialog)
        self.profilebtn1.setGeometry(QtCore.QRect(330, 50, 98, 27))
        self.profilebtn1.setObjectName(_fromUtf8("profilebtn1"))

        self.choice_icmp = QtGui.QRadioButton(profileDialog)
        self.choice_icmp.setGeometry(QtCore.QRect(330, 80, 198, 27))
        self.choice_icmp.setObjectName(_fromUtf8("choice_icmp"))
        self.choice_icmp.setChecked(True)

        self.choice_tcp = QtGui.QRadioButton(profileDialog)
        self.choice_tcp.setGeometry(QtCore.QRect(330, 100, 198, 27))
        self.choice_tcp.setObjectName(_fromUtf8("choice_tcp"))

        self.label = QtGui.QLabel(profileDialog)
        self.label.setGeometry(QtCore.QRect(0, 200, 81, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.statusLabel = QtGui.QLabel(profileDialog)
        self.statusLabel.setGeometry(QtCore.QRect(60, 100, 281, 61))
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.label_2 = QtGui.QLabel(profileDialog)
        self.label_2.setGeometry(QtCore.QRect(60, 10, 221, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        # Train button
        self.pushButton_2 = QtGui.QPushButton(profileDialog)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 270, 98, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.setEnabled(True)

        self.hostText = QtGui.QTextEdit(profileDialog)
        self.hostText.setGeometry(QtCore.QRect(80, 190, 101, 31))
        self.hostText.setObjectName(_fromUtf8("hostText"))

        # Dropdown Menu
        self.cmbUsage = QtGui.QComboBox(profileDialog)
        self.cmbUsage.setGeometry(QtCore.QRect(80, 50, 151, 27))
        self.cmbUsage.setObjectName(_fromUtf8("cmbUsage"))
        self.cmbUsage.addItem(_fromUtf8(""))
        self.cmbUsage.addItem(_fromUtf8(""))
        self.cmbUsage.addItem(_fromUtf8(""))
        self.cmbUsage.addItem(_fromUtf8(""))
        self.cmbUsage.addItem(_fromUtf8(""))

        self.retranslateUi(profileDialog)
        self.pushButton_2.clicked.connect(self.trainbutton)
        QtCore.QObject.connect(self.profilebtn1, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.msgbtn)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), profileDialog.close)
        #        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), profileDialog.close)
        QtCore.QMetaObject.connectSlotsByName(profileDialog)

    def retranslateUi(self, profileDialog):
        profileDialog.setWindowTitle(_translate("profileDialog", "Dialog", None))
        self.profilebtn1.setText(_translate("profileDialog", "profile", None))
        self.label.setText(_translate("profileDialog", "Host Name", None))
        self.statusLabel.setText(_translate("profileDialog", "Enter the host name", None))
        self.label_2.setText(_translate("profileDialog", "Enter usage % of device", None))

        self.pushButton_2.setText(_translate("profileDialog", "Train", None))  # Train button

        # Set DropDown Menu
        self.cmbUsage.setItemText(0, _translate("profileDialog", "15% Usage 100ns", None))
        self.cmbUsage.setItemText(1, _translate("profileDialog", "30% Usage 40ns", None))
        self.cmbUsage.setItemText(2, _translate("profileDialog", "50% Usage 30ns", None))
        self.cmbUsage.setItemText(3, _translate("profileDialog", "70% Usage 20ns", None))
        self.cmbUsage.setItemText(4, _translate("profileDialog", "99% Usage(stuxnet) 99ns", None))
        self.choice_icmp.setText(_translate("MainWindow", "ICMP Profile", None))
        self.choice_tcp.setText(_translate("MainWindow", "TCP Profile", None))

    def assign_details(self, txt):
        if txt == 0 or txt == 15:
            return "15;100"
        elif txt == 1 or txt == 30:
            return "30;40"
        elif txt == 2 or txt == 50:
            return "50;30"
        elif txt == 3 or txt == 70:
            return "70;20"
        elif txt == 4 or txt == 99:
            return "99;99"

    def msgbtn(self):
        self.pushButton_2.setEnabled(True)
        txt_index = self.cmbUsage.currentIndex()
        txt = self.assign_details(txt_index)
        host = self.hostText.toPlainText()
        usage = txt.split(';')[0]
        task_cycle = txt.split(';')[1]
        print usage
        if host != "" and usage != "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("The Profiling will take approxmiately 2 minutes,")
            msg.setInformativeText("Click OK to start profiling, Popup will let you know once it is done!")
            msg.setWindowTitle("Profiler")
            msg.setDetailedText(
                "Due to our Machine Learning algorithm requiring a large dataset, we require that you profile the SCADA"
                " at specific usage for 2 minutes to get most accurate reuslts during detection")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            if self.choice_tcp.isChecked():
                os.system('hping3 -c 10000 %s -i u10000 &' % host)  ##REAL HPING command
                os.system(
                    'timeout 5m tcpdump -i enp0s3 -w pcap/capture_%s_%s.pcap' % (usage, host))  # REAL tcpdump command

            if self.choice_icmp.isChecked():
                os.system('hping3 -c 10000 %s -i u10000 --icmp &' % host)  ##REAL HPING command
                os.system(
                    'timeout 5m tcpdump -i enp0s3 -w pcap/capture_%s_%s.pcap' % (usage, host))  # REAL tcpdump command
            d = QDialog()
            b1 = QPushButton("Profiling Done!, Click X", d)
            b1.move(175, 75)
            d.setWindowTitle("Completion")
            d.setWindowModality(Qt.ApplicationModal)
            d.exec_()
        else:
            print "\n Enter host! / or usage "

    def retreive_pcaps(self):
        files = os.listdir('pcap')
        # Crappy regex TODO: regex implementation ; Function retrieves list of all training pcap ;111 excluded
        # Reason being 111 -> test data set
        filtered = [f for f in files if '.pcap' in f]
        filtered = [x for x in filtered if not ('capture_111' in x)]
        return filtered

    def trainbutton(self):
        # Filter data & save frame delta response time to txt file for further calculations
        if self.choice_icmp.isChecked():
            flag = 'icmp'
            # TODO ; fix this import issue
            training_pcap_list = self.retreive_pcaps()
            for i, item in enumerate(training_pcap_list):
                perform_filter(item, 'icmp')
            t2csv.ignite(trainer='icmp')

        if self.choice_tcp.isChecked():
            os.system("chown " + OWNER + ":" + OWNER + " pcap/*;su -c 'bash filter_tcp.sh' -s /bin/sh rn")
            t2csv.ignite(trainer='tcp')

        self.statusLabel.setText("Dumping Frametime delta done \n Calculating Features Now...")

        flabel = open("label_train", "w")  # Open file to write labels into
        fdata = open("data_train", "w")  # Open file to consolidate all training data from profiles
        for file in glob.glob("csv/capture_*.csv"):

            # find CPU usage % from file name for label in classifier
            #               result = re.search('ip_(.*)_RespTimeDeltaOut.csv',file)

            #               usage = result.group(1) #Usage percentage with Regular exp
            usage = file.split('_')[1]
            if usage == 111:
                break
            no_of_labels = file_len(file)  # Determine number of labels
            if usage == "stux" or usage == "st":
                usage = str(99)
            f = open(file, "r")
            fdata.write(f.read().replace(',', ''))  # write csv files into master training file
            flabel.write(str(usage + ' ') * no_of_labels)
            f.close()

        flabel.close()
        fdata.close()
        print "\n Done writing Data set and labels"
        self.statusLabel.setText("All Training data saved into files csv/data_train !")


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    profileDialog = QtGui.QDialog()
    ui = Ui_profileDialog()
    ui.setupUi(profileDialog)
    profileDialog.show()
    sys.exit(app.exec_())

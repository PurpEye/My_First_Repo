#!/usr/bin/env python

import logging

import numpy as np
import os, sys
import time
from v3 import Ui_dialogAlert, found_msg_1, same_msg, error_msg
from PyQt4 import QtGui

import listener_module
import txt2csv as t2csv
import tweepy
from datetime import datetime
import pandas as pd
from sklearn import svm
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_score

from v1 import Ui_MainWindow
from v2 import Ui_profileDialog
from write_cluster import cluster_data

################GLOBAL VARIABLES########################
threshold = 51
host_name = "blank"
c_monitor = 'yes'

# Twitter API information for @RoboCOP

cfg = {
    "consumer_key": "n1xWqNR1UL41xjUJebAamnovx",
    "consumer_secret": "PEAATS0xDl3DLN701pmxlzYUTbqXFp1rNubnfXc4sLRSiOHGVW",
    "access_token": "733996388640534528-eFPK6SqubrZafr96RwtHisNYb3RrBTi",
    "access_token_secret": "uFK2uFj1qA3wNgNcdEc1EBLjnxNbkr4g5KfuxLUmiWx2B"
}


def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)


class Form1(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.profileBtn.clicked.connect(self.handleButton)
        self.monitor_button.clicked.connect(self.monitor_main)
        self.btnAlert.clicked.connect(self.alertButton)  # alert button function
        # self.btnStop.clicked.connect(self.mStopButton)  # stop monitor button function
        self.window2 = None
        self.window3 = None

    def mStopButton(self):
        print "hi"
        c_monitor = False

    def host_split_validate(self, txt_value):
        print "validate"
        if ";" in txt_value:
            host_name = txt_value.split(';')[0]
            task_cycle = txt_value.split(';')[1]
            return host_name, task_cycle
        else:
            self.statusLabel.setText("Use Correct format - Usage -> hostname;taskcycle")
            return -1, -1

    def perform_filter(self, file_to_filter, flag_val):
        if flag_val == 'tcp':

            os.system(
                "tshark -r pcap/%s -T fields -e frame.time_delta > txt/%s_FrameTimeDelta.txt" % (
                    file_to_filter, file_to_filter))  # pcap to txt file

        if flag_val == 'icmp':
            os.system(
                "tshark -r pcap/%s -Y icmp.type==0 -T fields -e frame.time_delta > txt/%s_FrameTimeDelta.txt" % (
                    file_to_filter, file_to_filter))  # pcap to txt file

    def host_measure(self, host, cycle, flag):
        self.statusLabel.setText("Monitoring Device now")

        if flag == 'icmp':
            '''
            os.system('hping3 -c 10000 %s -i u10000 --icmp &' % host)
            os.system('timeout 5m tcpdump -i enp0s3 -w pcap/capture_111_%s.pcap' % host)
            '''
            self.statusLabel.setText("Packet capture done, starting analysis for test monitor at %s" % time.ctime())
            ftest = str("capture_111_" + host + ".pcap")  # filename of pcap file
            self.perform_filter(ftest, flag)
            test_file = 'txt/' + ftest + '_FrameTimeDelta.txt'  # Monitor txt file name to pass to featurecalc()
            print test_file

        # TODO : Remove from Main code, even flags
        '''
        if flag == 'tcp':
            self.statusLabel.setText("Packet capture done, starting analysis for test monitor at %s" % time.ctime())
            ftest = str("capture_111_" + host + ".pcap")  # filename of pcap file
            self.perform_filter(ftest, flag)
            test_file = 'txt/' + ftest + '_FrameTimeDelta.txt'  # Monitor txt file name to pass to featurecalc()
            print test_file
        '''

        self.lblOutput.setText("\n Analyzing Data now...Please wait...")
        return test_file

    def file_len(self, fname):
        with open(fname) as f:
            for i, l in enumerate(f):
                pass
        return i + 1

    def calculations(self, cfile_name):
        file1 = open(cfile_name, 'r')
        values = []
        count = 0
        setCount = 1
        line = '1'
        line_temp = 0

        while line != '':
            try:
                line = (file1.readline())
                sys.stdout.write(line)
                # line = line.rstrip()
                if count > 99:
                    # print "Count became greater than 999, calling featureCalc"
                    print cfile_name.replace('txt/', '')
                    t2csv.featureCalc(values, cfile_name.replace('txt/', ''))
                    count = 0
                    values = []
                    setCount += 1
                    if line == '' and setCount > 99:
                        break
                if not line == '\n':
                    line_temp = float(line)
                if not line_temp == 0:
                    values.append(line_temp)
                    # Debug info            print count
                    #            print setCount
                    count += 1

            except:
                print "Found a non number %s " % line
        if count > 0:
            t2csv.featureCalc(values, cfile_name.replace('txt/', ''))

        else:
            print "Please input host name"

        print "analyze time"
        tflabel = open("label_test", "w")  # Open file to write labels into
        tfdata = open("data_test", "w")  # Open file to consolidate all training data from profiles

        test_file = str('csv/' + cfile_name.replace('txt/', '') + '.csv')
        print test_file
        usage = test_file.split('_')[1]
        # usage = usage.replace('txt/','')
        print usage
        no_of_labels = self.file_len(test_file)  # Determine number of labels
        f = open(test_file, "r")  ##
        tfdata.write(f.read().replace(',', ''))  # write csv files into master training file
        tflabel.write(str(usage + ' ') * no_of_labels)
        f.close()

        tflabel.close()
        tfdata.close()
        print "\n Done writing Data set and labels"
        self.statusLabel.setText("All testing data saved into files csv/data_train !")

    def load_dataset(self):
        X_train = np.genfromtxt("data_train")
        y_train = np.loadtxt("label_train")
        X_test = np.loadtxt("data_test")
        y_test = np.loadtxt("label_test")
        return X_train, y_train, X_test, y_test

    def monitor_main(self):
        try:
            txt = self.hostTxt.toPlainText()
            if txt != '':
                host, cycle = self.host_split_validate(txt_value=txt)
                if host != -1:
                    # Check if Mode 1 / Mode 2, then assign ICMP mode
                    if self.monitor_button_1.isChecked() or self.monitor_button_2.isChecked():
                        flag = 'icmp'

                        text_ips = self.host_measure(host, cycle, flag)

                        self.lblOutput.setText("\n Measurement Done, Proceeding with calculations..")
                        self.calculations(cfile_name=text_ips)
                        if self.monitor_button_1.isChecked():
                            training_data, training_label, testing_data, testing_label = self.load_dataset()
                            self.random_check(X_train=training_data, y_train=training_label, X_test=testing_data,
                                              y_test=testing_label, task_c=cycle)
                        if self.monitor_button_2.isChecked():
                            training_data, training_label, testing_data, testing_label = self.load_dataset()
                            self.svm_check(X_train=training_data, y_train=training_label, X_test=testing_data,
                                           y_test=testing_label)

                    # Check if Mode 3/4 then assign TCP
                    if self.monitor_button_3.isChecked() or self.rbm4.isChecked():
                        flag = 'tcp'
                        # New code -->
                        file_from_listen_module = listener_module.node_traffic_capture(node_ip=host)
                        if file_from_listen_module != -1:

                            self.perform_filter(file_to_filter=file_from_listen_module, flag_val=flag)
                            txt_ips = 'txt/' + file_from_listen_module + '_FrameTimeDelta.txt'  # Monitor txt file name to pass to featurecalc()
                            #  Proceed with Clustering for TCP
                            # text_ips = 'txt/capture_111_127.0.0.1.pcap_FrameTimeDelta.txt'
                            clustered_file_name = cluster_data(txt_ips)
                            self.lblOutput.setText("\n Clustering Done, Proceeding with ML")
                            # End-Clustering Block

                            self.calculations(cfile_name=clustered_file_name)
                            if self.monitor_button_3.isChecked():
                                training_data, training_label, testing_data, testing_label = self.load_dataset()
                                self.random_check(X_train=training_data, y_train=training_label, X_test=testing_data,
                                                  y_test=testing_label, task_c=cycle)
                            if self.monitor_button_4.isChecked():
                                training_data, training_label, testing_data, testing_label = self.load_dataset()
                                self.svm_check(X_train=training_data, y_train=training_label, X_test=testing_data,
                                               y_test=testing_label)

                        # START BLOCK for Condition -> In case listener_module returns -1, which fails over to ICMP
                        # Same as normal ICMP with few mods
                        else:
                            print "Start ICMP procedures--"
                            flag = 'icmp'
                            text_ips = self.host_measure(host, cycle, flag)
                            self.lblOutput.setText("\n Proceeding with ICMP since TCP data is not sufficient")
                            self.calculations(cfile_name=text_ips)
                            # In case the User monitored TCP with RandomForest, use the same; else use SVM

                            if self.monitor_button_3.isChecked():
                                training_data, training_label, testing_data, testing_label = self.load_dataset()
                                self.random_check(X_train=training_data, y_train=training_label, X_test=testing_data,
                                                  y_test=testing_label, task_c=cycle)

                            if self.rbM4isChecked():
                                training_data, training_label, testing_data, testing_label = self.load_dataset()
                                self.svm_check(X_train=training_data, y_train=training_label, X_test=testing_data,
                                               y_test=testing_label)

                    if self.monitor_button_5.isChecked():
                        flag = 'icmp'
                        text_ips = self.host_measure(host, cycle, flag)
                        self.lblOutput.setText("\n Measurement Done, Proceeding with calculations..")
                        self.calculations(cfile_name=text_ips)
                        # random_check() returns 1 for detection, else -1
                        training_data, training_label, testing_data, testing_label = self.load_dataset()

                        rf_status_icmp = self.random_check(X_train=training_data, y_train=training_label,
                                                           X_test=testing_data,
                                                           y_test=testing_label, task_c=cycle)

                        if rf_status_icmp != -1:
                            # TODO add sequence -> ICMP + TCP + RULE - IN CASE no alert for both etc...MODIFY ?
                            flag = 'tcp'
                            file_from_listen_module = listener_module.node_traffic_capture(node_ip=host)
                            if file_from_listen_module != -1:
                                self.perform_filter(file_to_filter=file_from_listen_module, flag_val=flag)
                                txt_ips = 'txt/' + file_from_listen_module + '_FrameTimeDelta.txt'  # Monitor txt file name to pass to featurecalc()

                                #  Proceed with Clustering for TCP
                                # text_ips = 'txt/capture_111_127.0.0.1.pcap_FrameTimeDelta.txt'
                                clustered_file_name = cluster_data(txt_ips)
                                self.lblOutput.setText("\n Clustering Done, Proceeding with ML")
                                # End-Clustering Block

                                self.calculations(cfile_name=clustered_file_name)
                                rf_status_TCP = self.random_check(self.load_dataset())

                                if rf_status_TCP != -1:
                                    self.lblOutput.setText("\n ICMP & TCP data shows that Device ")

                                else:
                                    self.lblOutput.setText("\n Seems Fine...")


        except Exception, e:
            logging.error(e, exc_info=True)

    def random_check(self, X_train, y_train, X_test, y_test, task_c):
        logging.debug('Inside Rcheck')
        match_rf = -1
        classifier = RandomForestClassifier(n_estimators=100)

        y_pred = classifier.fit(X_train, y_train).predict(X_test)

        classifier_test = RandomForestClassifier(n_estimators=100)
        scores = cross_val_score(classifier_test, X_train, y_train, cv=10)
        print("\n Accuracy comaprision against self : %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
        # Compute confusion matrix
        cm = confusion_matrix(y_test, y_pred)
        np.set_printoptions(precision=2)
        print('Confusion matrix, without normalization')
        print("Confusion matrix:\n%s" % cm)

        # Normalize the confusion matrix by row (i.e by the number of samples
        # in each class)
        cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized Confusion matrix:\n%s" % cm_normalized)
        result_matrix = pd.crosstab(y_test, y_pred, rownames=['True'], colnames=['Predicted States'], margins=True)
        print result_matrix
        #        self.statusLabel.setText("Profile Analyzed \n Results are as follows \n\n %s" %result_matrix )
        pv = []
        flag = 0
        task_cycle = task_c
        tweet = ''
        print "--" * 20
        total = result_matrix.tail(1)['All'][-1]
        for column in result_matrix.tail(1):
            inferred = (result_matrix[column][-1] / float(total))
            if .51 < inferred < 1.0:

                # TODO Determine usage
                match_rf = 1
                import v3

                detect_time = str(datetime.now().strftime('%H:%M:%S %m-%d-%Y'))
                flag = 1
                print inferred
                inf_usage = column
                inf_cycle = str(assign_details(inf_usage)).split(';')[1]
                if task_cycle != inf_cycle:
                    self.statusLabel.setText("%s ns %s %s ns was inferred" % (task_cycle, v3.found_msg_1, inf_cycle))
                    tweet = tweet.join([str(task_cycle), v3.found_msg_1, inf_cycle, detect_time])
                    tweet += str(' was found')
                    self.lblOutput.setText("Malicious activity detected !!  %s \n Tweet Sent out!" % detect_time)
                    api = get_api(cfg)
                    status = api.update_status(status=tweet)
                elif task_cycle == inf_cycle:
                    self.statusLabel.setText(v3.same_msg)
                break

        if flag == 0:
            from v3 import error_msg
            print error_msg
            self.statusLabel.setText(v3.error_msg)

        return match_rf

        stux_value = result_matrix.tail(1)[99.0][-1]  # Stuxnet predictions

        '''
        #Debugging
        print stux_value
        print total
        print "-------"
        '''
        ###

    def svm_check(self, X_train, y_train, X_test, y_test):
        clf = svm.OneClassSVM()

        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)

        # classifier_test = svm.OneClassSVM()
        # scores = cross_val_score(classifier_test, X_train, y_train, cv=10)
        # print("\n Accuracy comaprision against self : %0.2f (+/- %0.2f)"% (scores.mean(), scores.std()*2))

        cm = confusion_matrix(y_test, y_pred)
        np.set_printoptions(precision=2)
        print('Confusion matrix, without normalization')
        print("Confusion matrix:\n%s" % cm)

        # Normalize the confusion matrix by row (i.e by the number of samples
        # in each class)
        result_matrix = pd.crosstab(y_test, y_pred, rownames=['True'], colnames=['Predicted States'], margins=True)
        print result_matrix
        pv = []
        print "--" * 20
        for column in result_matrix.tail(1):
            print (result_matrix[column][-1])
            pv.append(result_matrix[column][-1])

        total = pv[-1]  # Total entries
        pv.pop(-1)  # only show list of integers
        deviant_value = result_matrix.tail(1)[-1][-1]  # Stuxnet predictions
        average = (deviant_value / float(total)) * 100
        print "*---\n"
        print deviant_value
        print average
        if average > 51:
            print "Deviation from Normal behavior"

        detect_time = str(datetime.now().strftime('%H:%M:%S %m-%d-%Y'))
        if average > threshold:
            tweet = "Possibility of malicious actitivity :" + str(average) + "% at - " + str(detect_time)
            self.lblOutput.setText(
                "Malicious activity detected !!  %s at %s\n Tweet Sent out!" % (average, detect_time))
            api = get_api(cfg)
            status = api.update_status(status=tweet)

        else:
            self.lblOutput.setText(
                "Device seems safe !! Probability:  %s at , Detected at %s!" % (average, detect_time))

    def handleButton(self):
        if self.window2 is None:
            self.window2 = Form2(self)
        self.window2.show()

    def alertButton(self):
        if self.window3 is None:
            self.window3 = Form3(self)
        self.window3.show()


class Form2(QtGui.QDialog, Ui_profileDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)


class Form3(QtGui.QDialog, Ui_dialogAlert):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)


def assign_details(txt):
    if txt == 0 or txt == 15:
        return "15;100"
    elif txt == 1 or txt == 30:
        return "30;40"
    elif txt == 2 or txt == 50 or txt == 55:
        return "50;30"
    elif txt == 3 or txt == 70:
        return "70;20"
    elif txt == 99:
        return "99;99"


if __name__ == '__main__':
    logging.basicConfig(filename='logs/' + datetime.now().strftime("%y-%m-%d-%H-%M-%S") + '.log', level=logging.DEBUG)

    app = QtGui.QApplication(sys.argv)
    window = Form1()
    window.show()
    sys.exit(app.exec_())

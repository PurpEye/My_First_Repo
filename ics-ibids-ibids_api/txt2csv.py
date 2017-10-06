#!/usr/bin/env python

import numpy as np
import math, os
import sys, glob
from write_cluster import cluster_data

boost = 1  # Boosting statistical data


# foutname = 'blank'

def gmean(a, axis=0, dtype=None):
    if not isinstance(a, np.ndarray):  # if not an ndarray object attempt to convert it
        log_a = np.log(np.array(a, dtype=dtype))
    elif dtype:  # Must change the default dtype allowing array type
        if isinstance(a, np.ma.MaskedArray):
            log_a = np.log(np.ma.asarray(a, dtype=dtype))
        else:
            log_a = np.log(np.asarray(a, dtype=dtype))
    else:
        log_a = np.log(a)
    return np.exp(log_a.mean(axis=axis))


# Calculate feature values for a batch of 100 samples
def featureCalc(values, fo_name):
    foutname = fo_name
    len1 = len(values)
    mean = np.mean(values, dtype=float) * boost
    stdev = np.std(values) * boost

    var = '{:.15f}'.format(float(np.var(values, dtype=np.float64)) * 1000)
    har_mean = (len1 / np.sum(1.0 / val for val in values)) * boost
    geo_mean = gmean(values) * 1000
    print foutname
    fcsv = open('csv/%s.csv' % foutname, "a")
    fcsv.write(str(mean) + ', ' + str(stdev) + ', ' + str(var) + ', ' + str(har_mean) + ', ' + str(geo_mean) + '\n')
    fcsv.close()
    # Debugging info
    '''
	print 'Mean: ', mean
	print 'Std Dev: ', stdev
	print 'Variance: ', var
	print 'Harmonic Mean: ', har_mean
	print 'Geometric Mean: ', geo_mean
	'''
    return


# The following code will split the file in batches of 100 and will calculate the feature
# values on them
# The function featureCalc does this part
# Once 100 values are read, they are fed to featureCalc which calculates the values and
# Once this is done, the array is flushed and the count is reset.

def generate_stuff(file):
    print file
    foutname = file.replace('txt/', '')
    print foutname
    if foutname.split('_')[1] == "111":
        print "Ignoring test values"
    # break
    file1 = open(file, 'r')

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
                featureCalc(values, foutname)
                count = 0
                values = []
                setCount += 1
            if line == '' and setCount > 99:
                break
            if not line == '\n':
                line_temp = float(line)
                if not line_temp == 0:
                    values.append(line_temp)
                    # Debug info		            print count
                    #		            print setCount
                    count += 1
        except:
            print "Found a non number %s " % line
    if count > 0:
        # clustered_file = cluster_data(foutname)
        featureCalc(values, foutname)


def ignite(trainer):
    #	os.chdir("txt/")
    print "wadduP"
    if trainer == 'tcp':
        for file in glob.glob("txt/*_cluster.txt"):
            generate_stuff(file)

    if trainer == 'icmp':
        for file in glob.glob("txt/*.txt"):
            generate_stuff(file)


if __name__ == "__main__":
    print "Runn from main!"
# ignite()

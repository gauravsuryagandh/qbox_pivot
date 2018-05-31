#!/usr/bin/python

import os
from os import listdir
from os.path import isfile, join

################################################################################
# Function : get_last_file()
# This function returns the most recent file from the given dir
# Arguments: 
#   - path of the directory
#   - count 
# Returns : list of file names 
################################################################################
def get_last_file(dirname, count):
    list_dir = []
    if not os.path.isdir(dirname):
        print "Directory does not exist"
        return list_dir

    onlyfiles = [f for f in listdir(dirname) if isfile(join(dirname, f))]
    list_dir = sorted(onlyfiles, reverse=True)[0:count]
    return list_dir

################################################################################
# Function: get_list_of_fno
# This function reads fno.csv file from meta directory and generates a list of 
# scrips which are allowed in F&O
################################################################################
def get_list_of_fno():
    fno = []
    f_path = "meta/fno.csv" #TODO: make it constant

    fp = open(f_path)
    for each in fp:
        l = each.strip().split(',')
        fno.append(l[2])
    return fno



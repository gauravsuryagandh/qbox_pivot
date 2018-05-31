#!/usr/bin/python

#system wide imports
import os
import sys

#local imports
import utils



################################################################################
# Function : main()
# Main routine for the entire program. This is where the program gets started
################################################################################
def main():
    print "Executing qbox with pivot based trading"
    
    fno_list = utils.get_list_of_fno()

    f_list = utils.get_last_file("bhavcopy", 1)

    f_name = "bhavcopy/" + f_list[0]

    fp = open(f_name)
    for each in fp:
        l = each.strip().split(',')
        if l[1] != "EQ":
            continue
        if l[0] in fno_list:
            print l
'''
    calling main function
'''
if __name__ == "__main__":
    main()

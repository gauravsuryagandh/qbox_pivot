#!/usr/bin/python

import sys
import os
import re
import zipfile
import commands
import utils


month_dict = {
    'JAN' : '01',
    'FAB' : '02',
    'MAR' : '03',
    'APR' : '04',
    'MAY' : '05',
    'JUN' : '06',
    'JUL' : '07',
    'AUG' : '08',
    'SEP' : '09',
    'OCT' : '10',
    'NOV' : '11',
    'DEC' : '12',
        }

def main():
    print "Extracting passed file ..."
    if len(sys.argv) != 2:
        print "Invalid number of command line arguments"
        print "python extract_bhavcopy.py <bhavcopy file>"
        return

    f_path = sys.argv[1]
    if not os.path.isfile(f_path):
        print "File dose not exists. Check file path"
        return 

    zip_ref = zipfile.ZipFile(f_path, 'r')
    zip_ref.extractall()
    zip_ref.close()

    f_name = os.path.basename(f_path)

    ret = re.match(r'cm(.*?)bhav', f_name)
    if ret:
        s = ret.groups()[0]
        match = re.match(r"([0-9]+)([a-z]+)([0-9]+)", str(s), re.I)
        if match:
            dd = match.groups()[0]
            mm = month_dict[match.groups()[1]]
            yyyy = match.groups()[2]
            tgt_file_name = str(yyyy) + str(mm) + str(dd) + ".csv"
            print tgt_file_name
            
    cmd = "mv " + f_name.split('.')[0] + ".csv " + "bhavcopy/" + tgt_file_name
    print cmd
    ret, status = commands.getstatusoutput(cmd)
    
    utils.get_last_file("bhavcopy", 2)

if __name__ == "__main__":
    main()

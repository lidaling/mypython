__author__ = 'lidl'
import os
import pexpect

csv_path='/Users/lidl/Documents/location.csv'
for line in open(csv_path):
    country,province,city,county,code = line.split(",")
    os.system('echo '+county+'>> /Users/lidl/Documents/provincecity.txt');
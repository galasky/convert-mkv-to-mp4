#!/usr/bin/python

from subprocess import call
import os
import time
import codecs
import re

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def without_extension(file):
    s = file.split('.')
    i = 0
    str = ""

    while i < len(s) - 1:
        str += s[i]
        i += 1
        if i < len(s) - 1:
            str += "."
        
    return str

def not_convert(list, file_test):
    print bcolors.OKBLUE + "check : " + file_test + bcolors.ENDC
    for file in list:
        extension = file[len(file) - 4:len(file)]
        if extension == ".mp4" and without_extension(file) == without_extension(file_test):
            print bcolors.WARNING + "already converted : " + file + bcolors.ENDC
            return False
    return True
            
        

list = os.listdir("./")
for file in list:
    extension =  file[len(file) - 4:len(file)]
    if extension == ".mkv" and not_convert(list, file):
        call(["avconv", "-i", file, "-codec", "copy", without_extension(file) + ".mp4"])

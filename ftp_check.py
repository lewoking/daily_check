#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-05 11:09:19
# @Author  : guozi 
# @Link    : https://github.com/lewoking/
# @Version : $Id$

import os
import time
import sys
import ftplib





pypath = os.getcwd()
with open(pypath +'\host.ini', 'r') as host_info:
    for line in host_info.readlines():

        items = line.split("#")

    server=items[0]
    user=items[1]
    password=items[2]
    check_dir=items[3]
    file_head =items[4]
    file_end =items[5]
    gap = items[6]
    sp = ""

    ftp = ftplib.FTP(server)
    ftp.login(user,password)
    if gap == "10":
        mtime = [ str(x).zfill(2) + str(y).zfill(2) for x in range(0,24) for y in range(0,60,10)]
    elif gap =="5":
        mtime = [ str(x).zfill(2) + str(y).zfill(2) for x in range(0,24) for y in range(0,60,5)]
    else:
        print ('time error')

    for z in mtime:
        sp = sp + file_head + time.strftime('%Y%m%d',time.localtime(time.time()))+ z + file_end +" "
    need_file = sp.split()

    files = []
    ftp.cwd(check_dir)
    files = ftp.nlst()



def diff(listA, listB):
    # 求交集的两种方式

    retB = list(set(listA).intersection(set(listB)))


    print("Completed : ", retB)

    # 求差集，在B中但不在A中
    retD = list(set(listB).difference(set(listA)))
    print ("Being : ", retD)

def main():
    listA = files
    listB = need_file
    diff(listA, listB)

if __name__ == '__main__':
    main()
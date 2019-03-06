#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-05 11:09:19
# @Author  : liujg (lewoking@gmail.com)
# @Link    : http://liujg.tk/
# @Version : $Id$

import os
import time
import sys
import ftplib



pypath = os.getcwd()
with open(pypath +'\host.ini', 'r') as host_info:
    for line in host_info.readlines():
        if line[0:1] == '#':continue
        items = line.split()
        run_command(items)

def run_command(items):
    server=items[0]
    user=items[1]
    password=items[2]
    check_dir=items[3]
    file_head =items[4]
    file_end =items[5]
    gap = items[5]

    ftp = ftplib.FTP(server)
    ftp.login(user,password)
    if gap == 10 :
        mtime = [0,10.20,30,40,50]
    else:
        mtime = [0,5,10,15,20,25,30,35,40,45,50,55]
    ntime = [time.strftime('%Y%m%d',time.localtime(time.time()))+ str(x).zfill(2) for x in range(0,23) ]
    ntime = [ntime + str(mtime).zfill(2) for mtime in mtime]
    need_file = [ntime+ filename for ntime in ntime]
    files = []
    ftp.cwd(check_dir)
    files = ftp.nlst()
    ftp.quit()


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
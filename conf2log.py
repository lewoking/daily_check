# 运行 python3.5 Regular_visit.py

# -*- coding:utf-8 -*-
# author: neo
# date: 2017-05-31

import paramiko
import os
import sys
import time


def run(text):
    for line in text.readlines():
        if line[0:1] == '#':continue
        items = line.split()
        run_command(items)

def run_command(item):
    host,user,passwd,port,type = item
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host,int(port),user,passwd,timeout=5,look_for_keys=False,allow_agent=False,compress=False)
        print ('host connect success :',host)
        # command = "display current-configuration"
        # command=command.encode('utf-8')
        ssh_con=ssh.invoke_shell()
        ssh_con.send("screen-length 0 temporary\n")
        ssh_con.send("display current-configuration\n")
        time.sleep(2)
        # print(ssh_con.recv(5000).decode('utf-8'))  #只能读取一次  必须注释掉
        output=ssh_con.recv(5000).decode('utf-8')
        ssh.close()
        # stdin, stdout, stderr = ssh.exec_command('display current-configuration \n')
        # return_info = stdout.read().strip()
        with open("%s.log"%(item[0]),"a+") as f:
            # f.write("--\n")
            f.write("%s"%output)
        print ('host command success :',host)
    except:
        print ("ssh connect timeout,please check network connect.",item[0])
        with open("error.log","a") as fe:
            fe.write("\n-------------------------------------分割线-----------------------------------------\n")
            fe.write("ssh connect timeout,please check network connect.%s"%(item[0]))
    ssh.close()
    


if __name__ == '__main__':
    host_info = open('./conf/host_info.ini','r',encoding='utf-8')
    run(host_info)
    host_info.close()
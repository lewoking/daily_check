#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-07 11:17:12
# @fork  : liujg (lewoking@gmail.com)
# @Link    : http://liujg.tk/
# @Version : $Id$

import os
import telnetlib


def do_telnet(Host, username, password, finish, commends):

    tn = telnetlib.Telnet(Host, port=23, timeout=10)

    tn.set_debuglevel(2)

    # login input username

    tn.read_until('Username:')  # 期待回复

    tn.write(username+'\n')

    # input password

    tn.read_until('Password:')  # 期待回复

    tn.write(password+'\n')

    # finish login input commend

    tn.read_until(finish)

    forcommend in commnds:

        tn.write("%s\n" % commend)

    tn.read_until(finish)

    tn.close()


if __name__ == '__main__':

    Host = "192.168.10.100"

    username = "yerik"

    password = "1111"

    finish = "R1>"  # 命令提示符（标识着上一条命令已执行完毕）

    commends = ['enable', '2222', 'showip route']  # 相关指令

    do_telnet(Host, username, password, finish, commends)

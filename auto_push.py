#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 blueyi <blueyi@blueyi-lubuntu>
#
# Distributed under terms of the MIT license.

"""

"""
import subprocess
import os
import datetime

error_log_file = 'auto.log'
error_log = open(error_log_file, 'a')


now_time = datetime.date.today().strftime('%Y%m%d')

def print_to_file(tmsg='', file_opened=error_log):
    msg = tmsg + ' --' + now_time
    print(msg)
    file_opened.write(str(msg) + '\n')


def run_cmd(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    toutput = p.communicate()[0]
    print_to_file(toutput)
    if p.returncode != 0:
        print_to_file('<<< ' + cmd + ' >>> run failed!')
    return toutput


def run_cmd_nolog(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    toutput = p.communicate()[0]
    print(toutput)
    if p.returncode != 0:
        print('<<< ' + cmd + ' >>> run failed!')
    return toutput


def git_push():
    commit_msg = now_time + '_bak'
    run_cmd_nolog('git add .')
    run_cmd_nolog('git commit -m ' + commit_msg)
    run_cmd_nolog('git push')


sql_user = 'root'
sql_pass = 'blueyiniu'
sql_file_name = 'shadowsocks_' + now_time + '.sql'
sql_bak_cmd = 'mysqldump -u ' + sql_user + ' -p' + sql_pass + ' shadowsocks > ' + sql_file_name
run_cmd(sql_bak_cmd)

error_log.close()

git_push()






# -*- coding: UTF-8 -*-
#!/usr/bin/env python
#!/usr/bin/env python3

# CGI处理模块
import cgi
import shutil
import site


# 引入时间模块
import time
import sys
from subprocess import call,check_output
import os
from sys import argv

def kill_process_by_name(name):
    cmd = "ps -e | grep %s" % name
    f = os.popen(cmd)
    txt = f.readlines()
    if len(txt) == 0:
        pass
    else:
        for line in txt:
            colum = line.split()
            pid = colum[0]
            print(pid)
            cmd2 = "kill -9 %d" % int(pid)
            call(cmd2,shell=True)

def is_python3():
    return sys.version > '3'

def kill_process_by_shell(port):
    try:
        cmd = "lsof -i:"+port+""" | awk '$1=="Python" {print $2}' | xargs kill -9"""
        call(cmd,shell=True)
    except:
        raise Exception("Do not kill Python process")

    
def start_server_with_port(port):
    try:
        kill_process_by_shell(port)
    except Exception as err:
        print("\033[31m "+str(err)+"\033[0m")

    try:
        if is_python3():
            call(["python3","-m","http.server","--cgi",port])
        else:
            call(["python","-m","CGIHTTPServer",port])
    except:
        print("\033[31m service open failed \033[0m")

def find_cgi():
    pcg_dir = site.getsitepackages()
    for dir_name in pcg_dir:
        cgi_dir = dir_name+"/cgi-bin"
        if os.path.exists(cgi_dir):
            return cgi_dir

def index():
    args = argv
    cgi_dir = find_cgi()
    newdir = os.getcwd()+"/cgi-bin"
    if (len(args) == 3) and (args[1] == "-port") and (args[2].isdigit()):
        if os.path.exists(newdir):
            start_server_with_port(args[2])
            print("\033[32m service has opening.... \033[0m")
        else:
            print("\033[31m 请先使用 yali_server init 初始化cgi环境  \n \033[0m")

    elif (len(args) == 2) and (args[1].lower() == "init"):
        try:
            shutil.copytree(cgi_dir,newdir,False)
            call("chmod 777 %s" % newdir+"/log_record.py",shell=True)
            call("chmod -R 777 %s" % newdir,shell=True)
            print("\033[32m  初始化 cgi 环境完成 \n \033[0m")
        except:
            print("\033[31m  本地有同名文件夹 cgi-bin 需删除或者已经完成初始化 \n \033[0m")
    
    elif (len(args) == 2) and (args[1].lower() == "help" or args[1] == "-h") or (len(args) == 1):
        print("\033[32m  yali_server init 初始化cgi环境 \n \033[0m")
        print("\033[32m  yali_server -port 8800 开启服务 \n \033[0m")
    else:
        print("\033[32m  yali_server help 查看用法 \n \033[0m")






# -*- coding: UTF-8 -*-
#!/usr/bin/env python

# CGI处理模块
import cgi
import time
import os

def index():
    # 创建 FieldStorage 的实例化
    form = cgi.FieldStorage()

    # 获取日志数据
    if form.getvalue('log'):
        log_text = form.getvalue('log')
    else:
        log_text = "---------terminal error----------"

    file_name= os.getcwd()+"/cgi-bin/"+time.strftime("%Y-%m-%d",time.localtime(time.time()))+".txt"

    try:
        with open(file_name,"a+") as f:
            f.write(log_text+"\n")
    except:
        print("\033[32m open fail.... \033[0m")

index()










#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time    : 2019/3/1 8:52
# @Author  : Aries
# @Site    : 
# @File    : GetIP.py
# @Software: PyCharm

import socket
import platform
import requests
import re


# 获取本地内网IP
def getLocalIP():
    """获取Linux系统IP"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('www.wukong.com', 0))
        ip = s.getpeername()[0]
    except (Exception) as s:
        ip = '0.0.0.0'
    finally:
        s.close()
    return ip

# 获取外网IP
def getExportIP():
    text=requests.get('http://txt.go.sohu.com/ip/soip').text
    ip=re.findall('\d+.\d+.\d+.\d+', text)
    return ip[0]

if __name__ == "__main__":
    sys_type = platform.system()  # 获取系统类型
    # if sys_type in ("Windows" , "Darwin")
    if sys_type == "Windows" or sys_type == "Darwin":
        ip_address = socket.gethostbyname(socket.gethostname())
        print("主机名：%s" % socket.gethostname())
        print("本机内网IP地址：%s" % ip_address)
        print("本机外网IP地址：%s" % getExportIP())
    elif sys_type == "Linux":
        ip_address = getLocalIP()
        print("本机内网IP地址：%s" % ip_address)
        print("本机外网IP地址：%s" % getExportIP())
    else:
        print("其他操作系统")
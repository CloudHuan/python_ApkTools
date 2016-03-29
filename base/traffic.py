#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from baseUtils import *

pkg = 'com.togic.livevideo'
ctool = C_Utils()
def getTraffic():
    """"""
    #_adb = "adb shell cat /proc/net/xt_qtaguid/stats |grep -iE '10095' | awk '{count_rx=$6+count_rx;count_tx=$8+count_tx}END{print count_rx','count_tx}'"
    _adb = "adb shell cat /proc/net/xt_qtaguid/stats |grep -iE '10095'|awk '{print $6','$8}'"
    userID = ctool.getUID(pkg)
    result = ctool.execADB(_adb)
    result = result.split('\n')[0:-2]  #去除localhost流量
    count_rx = 0    #接收流量
    count_tx = 0    #发送流量
    for i in result:
        count_rx = int(i.split(" ")[0]) + count_rx
        count_tx = int(i.split(" ")[1]) + count_tx
    ctime = ctool.getCurrentTime()
    ctool.writeCSV(map(lambda x:str(x), [ctime,count_rx/1000.0,count_tx/1000.0]))
    print '\n  时间    接收KB  发送kb'
    print ctime,count_rx/1000.0,count_tx/1000.0
    
def main():
    """"""
    while True:
        key = raw_input('回车键打印并记录流量值，写入csv文件,输入q回车结束')
        if key == 'q' or key == 'Q':
            exit()
        getTraffic()
        
    
    

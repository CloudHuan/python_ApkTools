#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import os
import time
from baseUtils import C_Utils

ctool = C_Utils()
pkg = ctool.readSetting()[0]
activity_name = ctool.readSetting()[1]


def printMem():
    """"""
    _adb = "adb shell dumpsys meminfo %s | grep -iE 'Dalvik Heap' | awk 'BEGIN{print 'Allocat,Pencent'}{print $8','$8/128000}'"%pkg
    _adbGC = 'adb shell am start -n %s/%s'%(pkg,activity_name)
    ctool.execADB(_adbGC)
    time.sleep(3)
    ctime = ctool.getCurrentTime()
    result = ctool.execADB(_adb)
    result = result.split(" ")
    result.insert(0,ctime)
    print '\n时间  内存  占用比'
    print result
    ctool.writeMemCSV(result)
    
def main():
    """"""
    while True:
        key = raw_input('回车键触发GC机制(需要源码支持),并获取内存数据，然后写入csv文件-->输入q退出')
        if key == 'q' or key == 'Q':
            ctool.writeMemCSV(['-','-','-'])
            exit()
        printMem()

    
        
        
    
    
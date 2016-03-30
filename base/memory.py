#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import os
import time
from baseUtils import C_Utils

pkg = 'com.togic.livevideo'
ctool = C_Utils()

def printMem():
    """"""
    _adb = "adb shell dumpsys meminfo com.togic.livevideo | grep -iE 'Dalvik Heap' | awk 'BEGIN{print 'Allocat,Pencent'}{print $8','$8/128000}'"
    _adbGC = 'adb shell am start -n com.togic.livevideo/com.togic.launcher.GcActivity'
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
        key = raw_input('回车键打印并记录内存值，写入csv文件,输入q回车结束')
        if key == 'q' or key == 'Q':
            ctool.writeMemCSV(['-','-','-'])
            exit()
        printMem()

    
        
        
    
    
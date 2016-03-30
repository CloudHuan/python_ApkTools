#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from baseUtils import *
import os

pkg = 'com.togic.livevideo'
ctool = C_Utils()

def getDelay():
    """"""
    _adb = "adb shell dumpsys gfxinfo %s | grep -A 128 'Execute'  | grep -v '[a-Z]' "%pkg
    result = ctool.execADB(_adb)
    result = result.split('\r\n')
    print '\n打印总绘制时长：'
    for i in result:
        l_result = i.split('\t')[-3:]
        f_sum = 0
        for j in l_result:
            try:
                f_sum += float(j)
                print f_sum
            except Exception:
                print '没有读到数据，请滑动屏幕'
                return     
        l_result.append('%.2f'%f_sum)
        ctool.writeGFXCSV(l_result)
    ctool.writeGFXCSV(['我是','分','割','线'])
        
def getDisplayed():
    ''''''
    _adb = "adb logcat | grep -iE 'displayed' > %s"%os.path.join(os.getcwd(),'displayed.txt')
    print _adb
    print ctool.execADB(_adb)
    
def main():
    """"""
    while True:
        key = raw_input('回车键打印并记录流畅度，写入csv文件,输入q回车结束')
        if key == 'q' or key == 'Q':
            exit()
        getDelay()    
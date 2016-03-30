#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import os
import re
import time
import csv

########################################################################
class C_Utils():
        
    def execADB(self,_adb):
        """"""
        return os.popen(_adb).read().strip()    
    
    def adb_con(self,ip):
        """"""
        _adb = 'adb connect %s'%ip
        self.execADB(_adb)
    
    def adb_check(self):
        """"""
        _adb = 'adb get-state'
        adb_result = self.execADB(_adb)
        if adb_result == 'device':
            return True
        else:
            return False
        
    def getPropInfo(self,propName):
        """"""
        _adb = "adb shell getprop | grep -iE %s | awk -F ':' '{print $2}'"%propName
        adb_result = self.execADB(_adb)
        adb_result = adb_result.split(']')
        adb_result = adb_result[0].split('[')
        return adb_result[1]

    def getUID(self,pkg):
        """"""
        _adb = 'adb shell dumpsys package %s'%pkg
        adb_result = self.execADB(_adb)
        adb_result = re.findall(u'userId=(\d+)',adb_result)[0]
        return adb_result
    
    def getCurrentTime(self):
        return time.strftime('%H-%M-%S',time.localtime(time.time()))
    
    def writeTrafficCSV(self,d_list,abs_path = os.path.join(os.getcwd(),'traffic.csv')):
        """"""
        if not os.path.exists(abs_path):
            f = file(abs_path,'w+')
            _writer = csv.writer(f)
            _writer.writerow(['时间','接收流量KB','发送流量KB'])
            f.close()
        f = file(abs_path,'a+')
        _writer = csv.writer(f)
        _writer.writerow(d_list)
        f.close()
    
    def writeMemCSV(self,d_list,abs_path = os.path.join(os.getcwd(),'meminfo.csv')):
        """"""
        if not os.path.exists(abs_path):
            f = file(abs_path,'w+')
            _writer = csv.writer(f)
            _writer.writerow(['时间','分配内存','占用百分比'])
            f.close()
        f = file(abs_path,'a+')
        _writer = csv.writer(f)
        _writer.writerow(d_list)
        f.close()
    
    def writeGFXCSV(self,d_list,abs_path = os.path.join(os.getcwd(),'GFX.csv')):
        """"""
        if not os.path.exists(abs_path):
            f = file(abs_path,'w+')
            _writer = csv.writer(f)
            _writer.writerow(['Draw(ms)','Process(ms)','Execute(ms)','总时间<16ms'])
            f.close()
        f = file(abs_path,'a+')
        _writer = csv.writer(f)
        _writer.writerow(d_list)
        f.close()     

if __name__ == '__main__':
    print C_Utils().writeCSV(['15-15-15','151','1515'])
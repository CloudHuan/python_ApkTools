#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import os
import time
from baseUtils import C_Utils

#----------------------------------------------------------------------
def printMem():
    """"""
    while True:
        _adb = "adb shell dumpsys meminfo com.togic.livevideo | grep -iE 'Dalvik Heap' | awk 'BEGIN{print 'Allocat,Pencent'}{print $8','$8/128000}'"
        adb_result = os.popen(_adb).read().strip()
        time.sleep(1)
        print adb_result    

    
        
        
    
    
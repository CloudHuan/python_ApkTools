#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from base import traffic,memory,delay

#----------------------------------------------------------------------
def run():
    """"""
    print '\n\n\n\n\n'
    print '--------------------------------'
    print u'本工具的github地址:https://github.com/CloudHuan/Test_Tools'
    print '--------------------------------'
    print u'\n\n\n\n1.内存\n2.流量\n3.时延\n4.启动速度'
    select_num = raw_input('启动的序号，回车键结束-->')
    if select_num == '1':
        memory.main()  
    elif select_num == '2':
        traffic.main()
    elif select_num == '3':
        delay.main()
    elif select_num == '4':
        print "直接adb logcat | grep -iE 'displayed'直接看到，这里不支持啦"    

if __name__ == '__main__':
    run()
    

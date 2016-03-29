#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from base import traffic

#----------------------------------------------------------------------
def run():
    """"""
    print u'1.内存(维护中)\n2.流量\n3.时延'
    select_num = raw_input('启动的序号，回车键结束-->')
    if select_num == '1':
        trace_memory.printMem()  
    elif select_num== '2':
        traffic.main()

if __name__ == '__main__':
    run()
    

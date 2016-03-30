这是一个集成的性能专项python脚本，支持内存，流量和时延的专项数值的统计。

使用方法
setting.txt目录输入两行,第一行输入测试的包名，第二行输入插入的activity名字(流量)
cd到项目目录，运行python run.py

内存：为了adb自动触发GC，需要在源码添加一个activity，并在onCreate()方法执行GC命令。

流量：读取xt_qtagui的值，很多软件都是读取这个的

流畅度：需要先打开开发者调试的GPU呈现模式分析的gfxinfo

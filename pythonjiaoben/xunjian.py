# -*- coding: UTF-8 -*-
#!/usr/bin/env python

from pyh import *
import os
import requests
import json
import subprocess
ip="161.189.20.101"
url1="http://"+ip+":1988/proc/kernel/version"
url2="http://"+ip+":1988/proc/kernel/hostname"
url3="http://"+ip+":1988/system/date"
url4="http://"+ip+":1988/page/system/uptime"
url5="http://"+ip+":1988/proc/cpu/num"
url6="http://"+ip+":1988/page/cpu/usage"
url7="http://"+ip+":1988/page/diskio"
url8="http://"+ip+":1988/page/memory"
url9="http://"+ip+":1988/page/df"
data = requests.get(url1)
hostname=requests.get(url2)
time=requests.get(url3)
uptime=requests.get(url4)
cpunum=requests.get(url5)
cpuinfo=requests.get(url6)
diskio=requests.get(url7)
memory=requests.get(url8)
df=requests.get(url9)
diskcmd='ssh {} df -h|grep dev'.format(ip)
cpucmd='ssh {}  ps -eo pid,ppid,cmd,%cpu --sort=-%cpu | head'.format(ip) 
memcmd='ssh {}  ps -eo pid,ppid,cmd,%mem --sort=-%mem | head'.format(ip) 
cputop=subprocess.check_output(cpucmd,shell=True)
memtop=subprocess.check_output(memcmd,shell=True)
disktop=subprocess.check_output(diskcmd,shell=True)
   
page = PyH('巡检报告')
page.addCSS('myStylesheet1.css', 'myStylesheet2.css')
page.addJS('myJavascript1.js', 'myJavascript2.js')


page << h1('------------------亚信云天巡检报告----------------------')
page << br()
page << p('本次被巡检主机地址: '+ip,style='color:red;')
page << br()
page << h2('主机信息', cl='center')
page << div(id='myDiv1')
page.myDiv1 << p('kernel: '+ data.json()['data'])
page.myDiv1 << p('hostname: '+ hostname.json()['data'])
page.myDiv1 << p('date: '+ time.json()['data'])
page.myDiv1 << p('uptime: '+ uptime.json()['data'])


page << br()
page << h2('CPU', cl='center')
page << div(id='myDiv2')
page.myDiv2 << p('cpu.idle: '+ cpuinfo.json()['data'][0][0] )
page.myDiv2 << p('cpu.busy: '+ cpuinfo.json()['data'][0][1] )
page.myDiv2 << p('cpu.user: '+ cpuinfo.json()['data'][0][2] )
page.myDiv2 << p('cpu.nice: '+ cpuinfo.json()['data'][0][3] )
page.myDiv2 << p('cpu.system: '+ cpuinfo.json()['data'][0][4] )

page << br()
page << h2('磁盘信息', cl='center')
page << div(id='myDiv3')
page.myDiv3 << p(disktop,style="white-space: pre-wrap;")
#page.myDiv3 << p('Disk Filesystem: '+df.json()['data'][0][0])
#page.myDiv3 << p('Disk Size: '+df.json()['data'][0][1])
#page.myDiv3 << p('Disk Used: '+ df.json()['data'][0][2])
#page.myDiv3 << p('Disk Avail: '+ df.json()['data'][0][3])
#page.myDiv3 << p('Disk Used%: '+df.json()['data'][0][4])
#page.myDiv3 << p('Disk Mount: '+df.json()['data'][0][5])

page << br()
page << h2('内存信息', cl='center')
page << div(id='myDiv4')
page.myDiv4 << p('Memory Total: ' + str(memory.json()['data'][0])+' MB' )
page.myDiv4 << p('Memory Used: ' + str(memory.json()['data'][1])+ ' MB' )
page.myDiv4 << p('Memory Free: ' + str(memory.json()['data'][2])+ ' MB')


page << br()
page << h2('进程CPU使用率TOP10', cl='center')
page << div(id='myDiv5')
page.myDiv5 << p(cputop,style="white-space: pre-wrap;")



page << br()
page << h2('进程内存使用率TOP10', cl='center')
page << div(id='myDiv6')
page.myDiv6 << p(memtop,style="white-space: pre-wrap;")



page.printOut() 


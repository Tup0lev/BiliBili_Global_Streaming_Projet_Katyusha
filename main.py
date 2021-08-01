# -*- coding: utf-8 -*-
"""
Created on Sat May  2 17:50:42 2020

From New York to Moskow
to Moskow!
ニューヨークからモスクワへ
モスクワへ

The entire pilipili global streamers are attacked
streamers attacked!
中國以外の配信者は制裁します
配信者は制裁します

Overieda lead the pilipili resistance
lead pilipili resistance!
キョウカがピリピリレジスタンスを統率する
ピリピリレジスタンスを統率する

Everyone must see they are not afraid of anything
they are not afraid of anything!

The ChenRui Empire is awaking
ChenRui Empire!
陳ルイの帝国は目覚めている
陳ルイの帝国

Do not touch our streams
our streams!
私たちの配信わ邪魔をしない
私たちの配信

Overieda lead the pilipili resistance
lead pilipili resistance!
キョウカがピリピリレジスタンスを統率する
ピリピリレジスタンスを統率する

Everyone must see they are not afraid of anything
they are not afraid of anything!

From ShangHai the wolves are coming
wolves coming!

Beware of Pilipili-Fanboys and censorer
fanboys and censorer!

Overieda lead the pilipili resistance
lead pilipili resistance!

Everyone must see they are not afraid of anything
they are not afraid of anything!

In defense of global streamers
defense of global streamers!

Fighting for our beloved streamers
our beloved streamers!

Overieda lead the pilipili resistance
lead pilipili resistance!

Everyone must see they are not afraid of anything
they are not afraid of anything!

"""

import subprocess
from tkinter import *
from tkinter import messagebox
import os
import time
import re
import urllib.request
import socket
import urllib.error

CykaForm = Tk()


LblTtl = Label(CykaForm, text="批哩批哩海外主播转播项目")

proxy= StringVar()
port = StringVar()
source = StringVar()
destlink = StringVar()
destkey = StringVar()

def is_bad_proxy(pip):    
    try:
        proxy_handler = urllib.request.ProxyHandler({'http': pip})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        req=urllib.request.Request('http://www.google.com')  # change the URL to test here
        sock=urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code)
        return e.code
    except Exception as detail:
        print("ERROR:", detail)
        return True
    return False



def startup():
	sourceconverted = source.get()


	if (proxy.get() == "" or port.get() == "" or source.get() == "" or destlink.get() == "" or destkey.get() == ""):
		messagebox.showinfo("你没填完整啊", "空着干嘛？")
		return

	wholeproxy = proxy.get()+":"+port.get()

	try:
		val = int(port.get())
	except ValueError:
		messagebox.showinfo("你端口填的不对啊", "端口咋能有字母呢？")
		return

	val = int(port.get())
	if (val > 65353 or val < 0):
		messagebox.showinfo("你端口填的不对啊", "端口必须在0和63353之间")
		return

	if (is_bad_proxy(wholeproxy)):
		messagebox.showinfo("你的代理不给力啊", "上得了YouTube吗？")
		return


	if ("youtu.be" in source.get()):
		sourceconverted = source.get().replace("youtu.be/", "www.youtube.com/watch?v=")
		print(sourceconverted)
	
	while True:
		wholeproxy = proxy.get()+":"+port.get()
		destination = destlink.get()+destkey.get()
		_streamlink_process = subprocess.Popen(('streamlink.bat', '--http-proxy', wholeproxy, sourceconverted, 
   	                                        'best', '-o', '-'), stdout=subprocess.PIPE) 
		print("asdf")
		_ffmpeg_process = subprocess.Popen(('ffmpeg/ffmpeg.exe', '-i', '-', '-acodec', 'aac' ,'-vcodec','copy', '-f','flv',
   	                                    destination ), stdin=_streamlink_process.stdout) #Try both aac and copy for acodec |||| USE -bsf when prompted if using ffmpeg3
		time.sleep(5)
    
    
    
#GUI Elements
    
CykaForm.title('Pilipili Resistance presents')
canvas = Canvas(CykaForm, width = 500, height = 150)           
  


LblPxy = Label(CykaForm, text="http proxy用于访问YouTube的http代理")
EntPxy = Entry(CykaForm, textvariable=proxy)
LblPrt = Label(CykaForm, text="port端口")
EntPrt = Entry(CykaForm, textvariable=port)
LblUtb = Label(CykaForm, text="source转播源 请复制YouTube链接或短链")
EntUtb = Entry(CykaForm, textvariable=source)
LblDsl = Label(CykaForm, text="destlink批哩批哩直播链接")
EntDsl = Entry(CykaForm, textvariable=destlink)
LblDsk = Label(CykaForm, text="destkey批哩批哩直播码")
EntDsk = Entry(CykaForm, textvariable=destkey)
BtnSet = Button(CykaForm, text="start开始", command=startup)

LblTtl.pack()

canvas.pack()
LblTtl.pack()
LblPxy.pack()
EntPxy.pack()
LblPrt.pack()
EntPrt.pack()
LblUtb.pack()
EntUtb.pack()
LblDsl.pack()
EntDsl.pack()
LblDsk.pack()
EntDsk.pack()
BtnSet.pack()
CykaForm.mainloop()

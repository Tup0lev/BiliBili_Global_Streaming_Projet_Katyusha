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
import os
import time

CykaForm = Tk()


LblTtl = Label(CykaForm, text="批哩批哩海外主播转播项目")

proxy= StringVar()
port = StringVar()
source = StringVar()
destlink = StringVar()
destkey = StringVar()

def startup():

	while true:

    	wholeproxy = proxy.get()+":"+port.get()
    	destination = destlink.get()+destkey.get()
    	_streamlink_process = subprocess.Popen(('streamlink', '--http-proxy', wholeproxy, source.get(), 
                                            'best', '-o', '-'), stdout=subprocess.PIPE) 
   		_ffmpeg_process = subprocess.Popen(('ffmpeg', '-i', '-', '-acodec', 'aac' ,'-vcodec','copy', '-f','flv',
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

LblTtl.grid(row=0, column=0)



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

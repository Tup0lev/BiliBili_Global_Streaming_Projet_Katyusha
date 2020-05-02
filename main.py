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


#define variables
destination = "<RTMP SERVER>/<KEY>" #DESTINATION
proxy = "ip_addr:port" #MUST BE HTTP PROXY
youtube = "URL" #YOUTUBE SOURCE URL

#core processes
_streamlink_process = subprocess.Popen(('streamlink', '--http-proxy', proxy, youtube, 'best', '-o', '-'), stdout=subprocess.PIPE) 
_ffmpeg_process = subprocess.Popen(('ffmpeg', '-i', '-', '-acodec', 'aac' ,'-vcodec', 'copy', '-f','flv', destination ), stdin=_streamlink_process.stdout) #Try both aac and copy for audio codec in case one of them doesn't work 

#TODO: add options to change parameters

'''

'''



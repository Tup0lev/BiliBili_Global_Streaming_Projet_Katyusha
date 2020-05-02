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

Beware of PiXiaoJiang and censorer
PiXiaoJiang and censorer!

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

#define parameters
destination = "rtmp://js.live-send.acg.tv/live-js/?streamname=live_218408251_44562509&key=aa839afbd05edd2b7f48e409a3f83d30"
proxy = "127.0.0.1:7890"
youtube = "https://www.youtube.com/watch?v=3s8iJRdqa3s"

#core processes
_streamlink_process = subprocess.Popen(('streamlink', '--http-proxy', proxy, youtube, 'best', '-o', '-'), stdout=subprocess.PIPE)
_ffmpeg_process = subprocess.Popen(('ffmpeg', '-i', '-', '-acodec', 'aac' ,'-vcodec', 'copy', '-f','flv', destination ), stdin=_streamlink_process.stdout)

#TODO: add options to change parameters

'''

'''



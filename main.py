# -*- coding: utf-8 -*-
"""
Created on Sat May  2 17:50:42 2020


From New York to Moskow
to Moskow

The entire pilipili global streamers are attacked
streamers attacked

Overieda lead the pilipili resistance
lead pilipili resistance

Everyone must see they are not afraid of anything
they are not afraid of anything

"""

import subprocess

#define variables
destination = "rtmp://js.live-send.acg.tv/live-js/?streamname=live_218408251_44562509&key=aa839afbd05edd2b7f48e409a3f83d30"
proxy = "127.0.0.1:7890"
youtube = "https://www.youtube.com/watch?v=3s8iJRdqa3s"

#core processes
_streamlink_process = subprocess.Popen(('streamlink', '--http-proxy', proxy, youtube, 'best', '-o', '-'), stdout=subprocess.PIPE)
_ffmpeg_process = subprocess.Popen(('ffmpeg', '-i', '-', '-acodec', 'aac' ,'-vcodec', 'copy', '-f','flv', destination ), stdin=_streamlink_process.stdout)


'''

'''



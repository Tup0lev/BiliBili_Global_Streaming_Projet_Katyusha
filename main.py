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
destination = "<RTMP SERVER>/<KEY>" #DESTINATION
proxy = "ip_addr:port" #MUST BE HTTP PROXY
youtube = "URL" #YOUTUBE SOURCE URL

#core processes
_streamlink_process = subprocess.Popen(('streamlink', '--http-proxy', proxy, youtube, 'best', '-o', '-'), stdout=subprocess.PIPE) 
_ffmpeg_process = subprocess.Popen(('ffmpeg', '-i', '-', '-acodec', 'aac' ,'-vcodec', 'copy', '-f','flv', destination ), stdin=_streamlink_process.stdout) #Try both aac and copy for audio codec in case one of them doesn't work 


'''

'''



# BiliBili_Global_Streaming_Project_Katyusha
解决海外主播无法在哔哩哔哩直播的“系统升级中”问题  

解决海外主播无法在批哩批哩直播的问题  
“Remove ChenRui Resistance Stronk”  
  
硬件需求：不那么老的PC，转播MAN必须肉身在中国墙内（港澳台等批哩批哩不让你播的地方是不可以的）  
软件依赖：不老掉牙的Windows, Mac OS X 或Linux（小 心 a p t）,只要能运行 Python3, Streamlink1.3.1+, ffmpeg4+就行 连接速度10Mbps以上 丢包低的梯子  
  
主播的准备工作  
	注册一个youtube账号并申请直播，直播间选择Normal Latency并关闭DVR， 在obs/Xsplit中填入youtube的直播链接和直播码（不支持批哩批哩直播鸡），向YouTube推流，并将YouTube直播间链接、你的批哩批哩直播链接、你的批哩批哩直播码告诉转播MAN  
  
  
  
转播MAN的工作  
  
首次运行前的配置工作——好事多磨，别嫌烦  
下载本项目为zip并解压缩  
安装python 3  
	打开 https://www.python.org/downloads/ 下载一个和你操作系统相符的python 3  
  
安装streamlink  
	打开https://github.com/streamlink/streamlink/releases/tag/1.4.1 下载streamlink  
安装FFMPEG  
	打开https://ffmpeg.zeranoe.com/builds/ 下载ffmpeg  
	解压下载好的zip，打开并前往bin文件夹，将ffmpeg.exe复制粘贴到本项目的文件夹里  
配置工作完毕  
  
每次转播时的工作  
  
运行你用来看YouTube的梯子，并找到你梯子的http代理地址和端口（如果是本机则地址是http://127.0.0.1)  
打开本项目文件夹，双击main.py运行  
在相应的地方填好代理地址和端口  
在相应的地方填好主播给你的YouTube直播间链接、批哩批哩直播链接、批哩批哩直播码  

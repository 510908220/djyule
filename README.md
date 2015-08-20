# Dj Music 

##介绍
这是一个dj音乐下载的web小工具.可以在线听并且下载DJ歌曲.
##目的
**平时喜欢听一些dj音乐,遇到好听的想下载，不仅要登录还得有金币之类的虚拟货币.而且广告超多**于是就研究了一下dj娱乐网web版的歌曲地址获取方式：
- 根据flash播放器的反汇编得到歌曲下载地址生成的规则,这这[DjBoxDownloader](https://github.com/510908220/DjBoxDownloader.git)有说明的.
- 使用移动设备打开[dj娱乐网](http://www.djyule.com/)的方式，可以分析静态页面得到下载地址.

##使用
- 启动mongodb
- 运行```djyule\handler\crawler.py```会进行dj歌曲的抓取.目前还未考虑并发下载.
- 运行djyule.py，根据端口在浏览器打开即可.默认端口是9999.会出现如下界面:
![](http://7xk7ho.com1.z0.glb.clouddn.com/djyule.png)

##设想改进点
- 在web页面增加配置，设置抓取规则，比如根据人气、下载榜、登上来的等。
- 由于是本地服务器，可以设置下载目录，一键下载指定歌曲到执行目录
- 在抓取是基本都是网络io，所以多采用多线程即可
- 可以设置一些选择歌曲的算法，根据人气、时长、关键字等下载歌曲
- 设置抓取脚本，比如可以定期抓取歌曲
- 创建一个bat脚本，点击即可开始操作了
- 增加收藏功能，这样在下载时可以只下载收藏的歌曲
- 可以增加分享功能，觉得好听了可以分享地址给好友

##设想改进后
- 开机启动后，点击bat，可以查看最近人气高的歌曲进行试听，如果喜欢的话可以下载或收藏.
- 定时自动跟新歌曲列表，这样每次打开时都是最新的
- ....

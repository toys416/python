# python

pyUtil/apk_install.py
@工具用途：此工具主要用来做apk各渠道包的基本安装测试，可以依次自动安装给定目录下的apk到手机，启动该apk，并在给定时间内关闭并卸载apk
@使用方法：
  @前提：电脑预装adb, python并将Android手机与电脑连接
  @脚本运行： python apk_install.py arg1 arg2   其中arg1为apk文件的存放路径，必须提供，脚本将在该路径下寻找所有apk进行安装测试， arg2为脚本安装并启动apk后的暂停时间，可以不提供，默认为10秒，10秒后卸载该apk

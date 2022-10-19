# -*- encoding=utf8 -*-
__author__ = "蒋星"

import os
import time

#APP类
class CommonFunction(object):
    def __init__(self):
        self.content=""
        self.startTime="0"
        global packageName
        global activityName
        #adb shell dumpsys activity
        packageName = "com.toy.toonblast.royalmatching.puzzle"
        activityName = ".AppActivity t3"
        self.apkName = "CubeBlastAudroid_Cube1.0.2-release.apk"

    def GetPackageName(self):
        return packageName

    # 安装app
    def InstallAPP(self):
        try:
            os.system("adb install D://appLocation//{}".format(self.apkName))
            print("安装完成")
            time.sleep(5)
        except Exception as e:
            print(e)
        
    # monkey启动APP 
    def MonkeyStartApp(self):
        cmd = 'adb shell monkey -p {} -v 100'.format(packageName)
        #adb shell monkey -p "com.toy.toonblast.royalmatching.puzzle" -v 100
        self.content=os.popen(cmd) #执行cmd,并将执行结果赋值给变量 content

    # 正常启动APP 
    def LaunchApp(self):
        cmd = 'adb shell am start -W -n {}/{}'.format(packageName,activityName)
        self.content = os.popen(cmd) #执行cmd,并将执行结果赋值给变量 content
        time.sleep(1)
    
    # 正常停止APP，用于冷启动的APP
    def StopApp(self):
        cmd = 'adb shell am force-stop {}'.format(packageName)
        os.popen(cmd) #执行cmd
        time.sleep(1)

    # 停止APP，用于热启动的APP
    # def StopApp(self):
        # cmd='adb shell input keyevent 3'#触发手机上的back键，实现退出
        # os.popen(cmd) #执行cmd

    # 获取当前的时间戳
    def GetCurrentTime(self):
        currentTime = time.localtime()
        return currentTime

    # 转换时间戳
    def TransferTime(self,time1):
        return time.strftime("%Y-%m-%d %H:%M:%S",time1)

    def GetCPUStatus(self):
        self.cpu = 0
        result = os.popen('adb shell dumpsys cpuinfo | find "{}" '.format(packageName))
        #adb shell dumpsys cpuinfo | find "com.toy.toonblast.royalmatching.puzzle"
        for line in result.readlines():
            self.cpu = line.split('%')[0]
        return self.cpu

    def GetDevice(self):
        deivceList = os.popen('adb devices').read()
        device = deivceList.split('\n')[1].split('\t')[0]
        return device
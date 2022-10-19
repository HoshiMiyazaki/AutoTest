# -*- encoding=utf8 -*-
__author__ = "蒋星"
__title__ = "方块消消乐"

from airtest.core.api import *

from poco.drivers.unity3d import UnityPoco

from airtest.report.report import simple_report

import sys
sys.path.append('../AutoTestLibrary/CommonFunction')
from CommonFunction import CommonInterface

auto_setup(__file__,logdir = True)

class FixtureStarBox():
    appName = "com.toy.toonblast.royalmatching.puzzle"
    appName_CN = "方块消消乐"
    
    def ClickStarbox():
        poco('Area_button').click() 
        sleep(5)

    def Fixture():
        poco("FixtureItem(Clone)")[0].child("Button").click()
        sleep(8)

    def GetRewardAndUnlock():
        if poco('Text_Open').exists():
            poco('Text_Open').click()
            sleep(15)  
            if poco('UnlockBtn').exists():
                poco('UnlockBtn').click()
                sleep(5)
                print("当前为第{}次装修".format(index))
#                 sleep(60)
                if exists(Template(r"tpl1664191310927.png", record_pos=(0.43, -0.82), resolution=(540, 960))):

                    touch(Template(r"tpl1664191310927.png", record_pos=(0.43, -0.82), resolution=(540, 960)))
    
    try:    
        global poco #实例化poco
        poco = CommonInterface.getUnityPoco()
        appName = "com.toy.toonblast.royalmatching.puzzle"
        CommonInterface.StartAPP(appName) #启动游戏
        
        if poco('Title').exists():
            poco('CloseBtn').click() #点击关闭购买弹窗
        sleep(2)
        
        if poco('tipTxt').exists():
            print("进入装修引导")
        
        global index 
        index = 0
        while(index < 100):
            if poco('$Text_open').exists():
                ClickStarbox()
                sleep(5)
                GetRewardAndUnlock()
            ClickStarbox()
            if poco("FixtureItem(Clone)")[0].child("title").get_text() == "Recharge" :
                print("进入充能阶段，测试完毕")
                break
            Fixture()
            if poco('Text_EARNSTARS').exists():
                poco('Button_close').click() #关闭继续游戏界面
                print("星星不够了")
                break
            index += 1
        
    finally:
        # 打印报告
        CommonInterface.CreateReport(appName_CN)

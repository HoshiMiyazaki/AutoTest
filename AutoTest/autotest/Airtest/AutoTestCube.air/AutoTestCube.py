# -*- encoding=utf8 -*-
__author__ = "蒋星"
__title__ = "方块消消乐"

from airtest.core.api import *

from poco.drivers.unity3d import UnityPoco

from airtest.report.report import simple_report

import sys
sys.path.append('../AutoTestLibrary/CommonFunction')
sys.path.append('../PlayGame')
from CommonFunction import CommonInterface
from PlayGame import PG
# from FixtureStarbox import FixtureStarBox


auto_setup(__file__,logdir = True)

class AutoTestCube():
    
    pakageName = "CubeBlastAudroid_Cube1.1.2-debug.apk"
    appName = "com.toy.toonblast.royalmatching.puzzle"
    appName_CN = "方块消消乐"

    # 第一关新手引导
    def Round1():
        poco('tip').wait_for_appearance(timeout=60)
        poco("GameBoard(Clone)").offspring("block5").child("BlockItem0")[3].click()
        sleep(2)
        poco("GameBoard(Clone)").offspring("block9").child("BlockItem0")[1].click()
        sleep(2)
        poco("GameBoard(Clone)").offspring("block9").child("BlockItem0")[1].click()
        sleep(2)
        
            
    def GuideHand():
        if poco('arrowpDown').exists(): 
            print("进入level2强制引导")
        elif poco('hand').exists(): 
            print("手指弱引导")
                  
        poco('Bg_button').click()
        sleep(2)
        poco('MiddleBtns').offspring('Bg_button').click()
        sleep(8)
        
        if poco('BoosterBtn').exists():
            poco('Bg_button').click()
            sleep(2)
            poco('MiddleBtns').offspring('Bg_button').click()
            sleep(8)
        
    def GuideInRound():
        if poco('tip').exists():
            if poco('tip').child('Text').attr('text') == 'Match 5 cubes to create a Rocket!':
                poco("GameBoard(Clone)").offspring("block5").child("BlockItem0")[3].click()
                sleep(2)
            elif poco('tip').child('Text').attr('text') == 'Match 7 cubes to create a Bomb!':
                poco("GameBoard(Clone)").offspring("block7").child("BlockItem0")[4].click()
                sleep(2)
                poco("GameBoard(Clone)").offspring("block8").child("BlockItem0")[4].click()
                sleep(2)
            elif poco('tip').child('Text').attr('text') == 'Match 9 cubes to create a Color Destroyer!':
                poco("GameBoard(Clone)").offspring("block7").child("BlockItem253")[4].click()
                sleep(3)
                poco('ColorBomb580').click()
                sleep(2)
            elif poco('tip').child('Text').attr('text') == 'Tap on 2 super elements to create a combo!':
                sleep(3)
                poco('rocketImg').click()
                sleep(5)
                poco('rocketImg').click()
                sleep(5)
                poco('rocketImg').click()
                sleep(5)
            PG()
            
        
    def GuideOfFixture():
        if poco('tipTxt').exists():
            assert_equal(poco('tipTxt').get_text(),'You can open your task list from here.',"进入装修引导成功")
            poco('AreaBtn').click()
            sleep(2)
            poco("FixtureItem1").child("Button").click()
            sleep(2)
            poco("StartLevelBtn").click()
            sleep(1)
            if poco('StartLevelBtn', text='Play').exists():
                poco("Menu").offspring("StartLevelDialog(Clone)").offspring("StartLevelBtn").click()
                sleep(3)
        
    
    try:    
#         # 安装
#         CommonInterface.InstallAPP(pakageName,appName)
#         # 启动
#         CommonInterface.StartAPP(appName)
        # 实例化poco
        global poco
        poco = CommonInterface.getUnityPoco()
        # 首次进游戏
        Round1()
        PG()
        sleep(5)
        
        for i in range(5):
            GuideHand()
            GuideInRound()
            PG()
            if poco('TimeOfferBtn').exists():
                poco('TimeOfferDialog(Clone)').offspring('CloseBtn').click()
                GuideOfFixture()
            i++
                
        
#         if int(poco('$Stars').get_text()) < 3: # 如果星星数不足以装修
#             print('星星数不足')
#         GuideOfFixture()

        # 看广告
#         CommonInterface.SkipAd()

        # 中途退出
#         Dropout()
        
        # 大退游戏
        # EndGame()

    finally:
        # 打印报告
        CommonInterface.CreateReport(appName_CN)

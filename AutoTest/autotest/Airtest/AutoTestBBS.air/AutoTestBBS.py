# -*- encoding=utf8 -*-
__author__ = "蒋星"
__title__ = "泡泡龙射手"

from airtest.core.api import *
from airtest.report.report import simple_report
from poco.drivers.cocosjs import CocosJsPoco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import sys
sys.path.append('../AutoTestLibrary/CommonFunction')
from CommonFunction import CommonInterface
auto_setup(__file__,logdir = True)

    
class AutoTestBBS():
    
    pakageName = "ble.pop.bubbl-v1.0.1-api_19_31-git_84121c9-2022.08.15.11.08.25-debug.apk"
    appName = "com.matching.bubble.pop.bubble.shooter"
    appName_CN = "泡泡龙射手"

    # 首次进入触发新手引导
    def FirstOpenGame():
        poco('bg', type='Sprite').wait(timeout=60)
    #     assert_equal(poco('_lab', type='LabelOutline').get_text(), '消除所有泡泡', '进入第一关失败')
        sleep(3)
        
        if assert_equal(poco('figer', type='Sprite').exists(), True, "新手引导触发成功."):
            poco('figer', type='Sprite').click()
            sleep(3)
            assert_not_exists(poco('figer'), "新手引导跳过成功")
            sleep(3)
        else:
            print("无新手引导")


    # 进入第一关
    def JoinRound1():
        # 进入游戏
        poco('ndBtnStartLevel', type='Button').wait_for_appearance(timeout=20)
        poco(text='1').click()
        sleep(2)
        poco('New Label', type='LabelShadow').click()
        sleep(3)
        poco('set', type='Sprite').wait_for_appearance(timeout=20)  #默认超时是120秒


    # 验证通关成功
    def GameSuccess():
        # 进行游戏
        touch([200,900])
        sleep(3)
        assert_equal(poco(node='[0, 0, 1, 0, 4, 3, 74, 12]').exists(), False, "第1次消除成功")
        touch([450,900])
        sleep(3)
        assert_equal(poco(node='[0, 0, 1, 0, 4, 3, 78, 12]').exists(), False, "第2次消除成功")
        touch([700,900])
        sleep(3)
        assert_equal(poco(node='[0, 0, 1, 0, 4, 3, 83, 12]').exists(), False, "第3次消除成功")
        touch([450,900])
        sleep(3)
        assert_equal(poco(node='[0, 0, 1, 0, 4, 3, 47, 12]').exists(), False, "第4次消除成功")
        touch([450,900])
        sleep(3)
        assert_equal(poco(node='[0, 0, 1, 0, 4, 3, 26, 12]').exists(), False, "第5次消除成功")

        # 返回主界面
        poco('New Label', type='LabelShadow', text='下一关').wait_for_appearance(timeout=20)
        sleep(3)
        poco('_btClose', type='Widget').click()
        sleep(3)
        assert_equal(poco('ndBtnStartLevel', type='Button').exists(),True, "通关后返回主界面成功.")

    # 验证通关失败+购买金币
    def GameFail():
        # 进行游戏
        for i in range(30):
            touch([700,900])
            sleep(2)

        step = int(poco('_leftShot', type='LabelOutline').get_text())
        if step > 0 :
            for m in range(step):
                touch([700,900])
                sleep(3)

        # 游戏失败
        assert_equal(poco('_labTitle1', type='LocalizedLabel').get_text(), '没有发射机会了！', "弹出首次失败界面成功.")

        # 购买步数
        poco('_btBuy', type='Widget').click()
        sleep(5)
        assert_equal(poco('_leftShot', type='LabelOutline').get_text(), '5', "金币购买步数成功.")

        # 失败界面
        for i in range(5):   
            touch([700,900])
            sleep(2)

        step = int(poco('_leftShot', type='LabelOutline').get_text())
        if step > 0 :
            for m in range(step):
                touch([700,900])
                sleep(3)

        assert_equal(poco('New Label', type='LabelShadow').get_text(), '再试一次', "弹出关卡失败界面成功.")

        # 再试一次
        poco(text='再试一次', type='LabelShadow').click()
        assert_equal(poco('_leftShot', type='LabelOutline').get_text(), '30', "再试一次成功.") 

        # 观看广告
        for i in range(30):
            touch([700,900])
            sleep(2)

        step = int(poco('_leftShot', type='LabelOutline').get_text())
        if step > 0 :
            for m in range(step):
                touch([700,900])
                sleep(3)    

        poco('_btWatch', type='Button').click()
        sleep(20)

        
    #     touch([1024,40])



    # 游戏中途退出
    def Dropout():
        poco("set").click()
        sleep(2)
        poco("_btBack").click()
        sleep(2)
        poco("_btQuit").click()
        sleep(2)
        assert_equal(poco('ndHP', type='Sprite').exists(), True, "中途退出时返回主界面成功.")


    try:    
        # 安装
        CommonInterface.InstallAPP(pakageName,appName)
        # 启动
        CommonInterface.StartAPP(appName)
        # 实例化poco
        global poco
        poco = CommonInterface.getPoco()
        # 首次进游戏
        FirstOpenGame()
        # 成功
        GameSuccess()
        # 进第一关
        JoinRound1()
        # 失败
        GameFail()
        # 看广告
        CommonInterface.SkipAd()
        # 中途退出
        Dropout()
        
        # 大退游戏
        # EndGame()

    finally:
        # 打印报告
        CommonInterface.CreateReport(appName_CN)

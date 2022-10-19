# -*- encoding=utf8 -*-
__author__ = "蒋星"
__title__ = "泡泡龙射手"

from airtest.core.api import *
from airtest.report.report import simple_report
from poco.drivers.cocosjs import CocosJsPoco
from poco.drivers.unity3d import UnityPoco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
auto_setup(__file__,logdir = True)

class CommonInterface():

    pakageName = ""
    appName = ""
    global poco
    
    # 实例化poco
    def getPoco():
        global poco
        poco = CocosJsPoco() #这个代码顺序不能改
        sleep(3)
        return poco
    
   # 实例化poco-2
    def getUnityPoco():
        global poco
        poco = UnityPoco() #这个代码顺序不能改
        sleep(3)
        return poco
    
    # 安装
    def InstallAPP(pakageName,appName):
        try:
            device().check_app(appName)
            uninstall(appName)
        except Exception as e:
            print(e)
        install("D://appLocation//" + pakageName)
    
    # 启动
    def StartAPP(appName):
        start_app(appName)
        sleep(8)

    # 广告流程
    def SkipAd():
        poco_android = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False) 
        sleep(3)
        touch(Template(r"tpl1660205173186.png", record_pos=(0.449, -1.016), resolution=(1080, 2280)))
        sleep(3)
        touch(Template(r"tpl1660290006696.png", record_pos=(0.004, 0.166), resolution=(1080, 2280)))
        sleep(3)
#         assert_equal(poco_android("android.widget.ImageView", type='android.widget.ImageView').exists(),True, "进入商店失败")
        keyevent("BACK")   
        sleep(3)
#         poco_android('android.widget.Image', type='android.widget.Image', text='btn').click()
        touch(Template(r"tpl1660289167044.png", record_pos=(0.45, -1.016), resolution=(1080, 2280)))
        sleep(3)
        assert_equal(poco('_leftShot', type='LabelOutline').get_text(), '3', "观看广告获得步数成功.")
        
    # 关闭客户端
    def EndGame():
        poco("ndBtnClose").click()
        keyevent("BACK")
    
    # 生成报告
    def CreateReport(appName_CN):
        simple_report(__file__,logpath=True,output="..\{}.html".format(appName_CN))
        print("test over")


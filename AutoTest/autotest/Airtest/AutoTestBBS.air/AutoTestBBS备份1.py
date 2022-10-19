# -*- encoding=utf8 -*-
__author__ = "蒋星"
__title__ = "泡泡龙射手"

from airtest.core.api import *
from airtest.report.report import simple_report
from poco.drivers.cocosjs import CocosJsPoco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
auto_setup(__file__,logdir = True)


# 安装
def InstallAPP():
    try:
        device().check_app("com.matching.bubble.pop.bubble.shooter")
        uninstall("com.matching.bubble.pop.bubble.shooter")
    except Exception as e:
        print(e)
    pakageName = "ble.pop.bubbl-v1.0.0-api_19_31-git_e512c3f-2022.08.11.10.29.29-release.apk"
    install("D://appLocation//" + pakageName)
    
# 启动
def StartAPP():
    start_app("com.matching.bubble.pop.bubble.shooter")
    sleep(5)
    
# 首次进入触发新手引导
def FirstOpenGame():
    poco('_content', type='Widget').wait(timeout=60)
#     assert_equal(poco('_lab', type='LabelOutline').get_text(), '消除所有泡泡', '进入第一关失败')
    sleep(5)
    try:
#         ae = assert_equal(poco('figer').exists(),True,"无新手引导")
        ae = assert_exists(poco('figer'), "新手引导触发失败")
        if ae == True:
            poco('figer', type='Sprite').click()
            sleep(5)
            assert_not_exists(poco('figer'), "新手引导跳过失败")
            sleep(5)
    except Exception as e:
        print(e)    
    

# 进入第一关
def JoinRound1():
    # 进入游戏
    poco('ndBtnStartLevel', type='Button').wait_for_appearance(timeout=20)
    poco('lab', type='Widget', text='1').click()
    sleep(2)
    poco('New Label', type='LabelShadow').click()
    sleep(3)
    poco('set', type='Sprite').wait_for_appearance(timeout=20)  #默认超时是120秒
        

# 验证通关失败
def GameSuccess():
    # 进行游戏
    touch([200,900])
    sleep(5)
    
    touch([200,900])
    sleep(5)
    assert_equal(poco(node='[0, 0, 1, 0, 4, 3, 74, 12]').exists(), False, "第1次消除失败")
    touch([450,900])
    sleep(5)
    assert_equal(poco(node='[0, 0, 1, 0, 4, 3, 78 12]').exists(), False, "第2次消除失败")
    touch([700,900])
    sleep(5)
    assert_equal(poco(node='[0, 0, 1, 0, 4, 3, 83 12]').exists(), False, "第3次消除失败")
    touch([450,900])
    sleep(5)
    assert_equal(poco(node='[0, 0, 1, 0, 4, 3, 47, 12]').exists(), False, "第4次消除失败")
    touch([450,900])
    sleep(5)
    assert_equal(poco(node='[0, 0, 1, 0, 4, 3, 26, 12]').exists(), False, "第5次消除失败")

    # 游戏失败
    try:
        poco('New Label', type='LabelShadow', text='下一关').wait_for_appearance(timeout=20)
    except Exception as e:
        print(e)
    sleep(5)
    poco('_btClose', type='Widget').click()
    sleep(5)
    assert_equal(poco('ndBtnStartLevel', type='Button').exists(),True, "返回主界面失败.")
    
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
            sleep(5)
        
    # 游戏失败
    assert_equal(poco('_labTitle1', type='LocalizedLabel').get_text(), '没有发射机会了！', "弹出首次失败界面失败.")
    
    # 购买步数
    poco('_btBuy', type='Widget').click()
    sleep(2)
    assert_equal(poco('_leftShot', type='LabelOutline').get_text(), '5', "金币购买步数失败.")
    
    # 失败界面
    for i in range(5):   
        touch([700,900])
        sleep(2)
    
    step = int(poco('_leftShot', type='LabelOutline').get_text())
    if step > 0 :
        for m in range(step):
            touch([700,900])
            sleep(5)
            
    assert_equal(poco('New Label', type='LabelShadow').get_text(), '再试一次', "弹出关卡失败界面失败.")
    
    # 再试一次
    poco(text='再试一次', type='LabelShadow').click()
    assert_equal(poco('_leftShot', type='LabelOutline').get_text(), '30', "再试一次失败.") 
    
    # 观看广告
    for i in range(30):
        touch([700,900])
        sleep(2)
        
    step = int(poco('_leftShot', type='LabelOutline').get_text())
    if step > 0 :
        for m in range(step):
            touch([700,900])
            sleep(5)    
            
    poco(text="观看").click()
    sleep(20)
    
    poco_android = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

#     sleep(2)
#     assert_equal(poco_android("android.widget.ImageView", type='android.widget.ImageView').exists(),True, "进入商店失败")
#     sleep(2)
#     keyevent("BACK")
#     sleep(2)
#     touch([1024,40])
    sleep(2)
    touch(Template(r"tpl1660205173186.png", record_pos=(0.449, -1.016), resolution=(1080, 2280)))
    sleep(5)
    poco_android('overlayBtn', type='android.widget.TextView', text='GET').click()
    sleep(5)
    assert_equal(poco_android("android.widget.ImageView", type='android.widget.ImageView').exists(),True, "进入商店失败")
    keyevent("BACK")   
    sleep(5)
#     poco_android('android.widget.Image', type='android.widget.Image', text='btn').click()
    touch(Template(r"tpl1660207079985.png", record_pos=(0.452, -1.014), resolution=(1080, 2280)))
    sleep(2)
    assert_equal(poco("_leftShot", type='LabelOutline').get_text(), '3', "观看广告获得步数失败.") 
    
# 游戏中途退出
def Dropout():
    poco("set").click()
    sleep(2)
    poco("_btBack").click()
    sleep(2)
    poco("_btQuit").click()
    sleep(2)
    assert_equal(poco('ndBtnStartLevel', type='Button').exists(),True, "返回主界面失败.")
    
# 关闭客户端
def EndGame():
    poco("ndBtnClose").click()
    keyevent("BACK")
    
# 生成报告
def CreateReport():
    simple_report(__file__,logpath=True,output="..\BBSLog.html")
    print("test over")

try:
    InstallAPP()
    StartAPP()
    poco = CocosJsPoco()    #这个代码顺序不能改
    sleep(5)
    FirstOpenGame()
    GameSuccess()
    JoinRound1()
    GameFail()
    Dropout()
    # EndGame()
# except Exception as e:
#     print(e)
finally:
    CreateReport()

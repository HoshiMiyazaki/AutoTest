# -*- encoding=utf8 -*-
__author__ = "蒋星"
__title__ = "方块消消乐"

from airtest.core.api import *

from poco.drivers.unity3d import UnityPoco

from airtest.report.report import simple_report

auto_setup(__file__,logdir = True)

poco = UnityPoco()


# 消除玩法
def PG():
    col = 3
    while(col < 10):
        row = 0
        if poco("GameBoard(Clone)").offspring("Content").exists():
            while(row < 7):
                if poco('rocketImg').exists(): # 如果同时存在多个火箭，点击最上面最左边的
                    poco('rocketImg').click()
                    sleep(2)
                elif poco('Image').exists():
                    poco('Image').click() 
                    sleep(2)
                if poco("GameBoard(Clone)").offspring("Content").child("gridView").child("block{}".format(col)).child("BlockItem0")[row] :
                    aim = poco("GameBoard(Clone)").offspring("Content").child("gridView").child("block{}".format(col)).child("BlockItem0")[row]
                    loc = aim.get_position()
                    poco.click(loc)
                    sleep(2)
                    click([500,1000])
                    sleep(2)
                if poco('Button_continue').exists(): # 如果continue按钮出现，说明游戏通过了
                    poco('Button_continue').click()
                    sleep(3)
                    break
                row = row + 1 
            col = col + 1
        else:
            break    

            

    
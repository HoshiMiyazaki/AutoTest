import os,time,xlwt
import TestLibrary

# 可以直接在cmd中使用的命令
if __name__== '__main__':
    cmd = "adb shell monkey -p com.toy.toonblast.royalmatching.puzzle --pct-syskeys 100 --ignore-crashes --ignore-timeouts --monitor-native-crashes -v -v 10000 > D:\WorkspaceVS\Monkey\Report\monkey_log.txt"
    os.popen(cmd)


#--pct-touch点击（down+up）
#--pct-motion动作（down+伪随机事件+up）
#--pct-trackball轨迹（一个及以上的移动+点击）
#--pct-nav方向输入（上下左右）
#--pct-majornav主要导航事件（中间键、回退键、菜单键）
#--pct-syskeys系统按键（Home、Back、接挂电话、音量加减）有的设备只能加减音量
#--pct-anyevent其他事件
#--ignore-crashes 忽略崩溃和异常
#--ignore-timeouts忽略超时错误
#--ignore-security-exceptions忽略许可错误

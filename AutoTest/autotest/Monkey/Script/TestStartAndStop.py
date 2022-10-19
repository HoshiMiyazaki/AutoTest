# -*- encoding=utf8 -*-
__author__ = "蒋星"


import time,xlwt
import TestLibrary
    
#控制类
class Controller(object):
    def __init__(self,count):
        self.com = TestLibrary.CommonFunction()
        self.count = count
        self.start = ["开始时间"]
        self.end = ["结束时间"]
        self.interval = ["间隔时间"]
        
        
    #单次测试过程
    def testprocess(self):
        self.com.LaunchApp()
        startTime = self.com.GetCurrentTime()
        self.com.StopApp()
        endTime = self.com.GetCurrentTime()

        #startTime = self.com.GetCurrentTime()
        #self.com.MonkeyStartApp()
        #endTime = self.com.GetCurrentTime()

        if endTime.tm_min != startTime.tm_min:
            intervalTime = 60 + float(endTime.tm_sec) - float(startTime.tm_sec)
        else:
            intervalTime = float(endTime.tm_sec) - float(startTime.tm_sec)
        
        #将时间戳存到数组里
        self.start.append(self.com.TransferTime(startTime))
        self.end.append(self.com.TransferTime(endTime))
        self.interval.append(intervalTime)
        

    #多次执行测试过程。用while循环,现在__init__里定义执行次数的参数，每执行一次，自减1 直到完成
    def run(self):
        while self.count>0:
            print("开始倒数第{}次执行".format(self.count))
            self.testprocess()
            print("结束倒数第{}次执行".format(self.count))
            self.count -= 1

            
    #数据的存储
    def SaveDataToXls(self):
        self.workbook = xlwt.Workbook(encoding='utf-8')# 创建一个workbook 并设置编码
        self.worksheet = self.workbook.add_sheet('sheet1',cell_overwrite_ok=True) # 创建工作表，并设置可以重写单元格内容
        c = 0
        while(c < excTimes+1):
            self.worksheet.write(0,c,self.start[c])
            self.worksheet.write(1,c,self.end[c])
            self.worksheet.write(2,c,self.interval[c])
            self.worksheet.col(c).width = 256*20
            self.worksheet.row(c).set_style(xlwt.easyxf('font:height 720;'))      # 36pt,类型小初的字号
            c += 1
        self.workbook.save("Report/on_off_report.xls")
    

if __name__=='__main__':
    # 调整次数
    global excTimes
    excTimes = 5
    controller = Controller(excTimes)
    TestLibrary.CommonFunction().InstallAPP()
    # 调用run方法
    controller.run()
    # 保存结果为xls文件
    controller.SaveDataToXls()
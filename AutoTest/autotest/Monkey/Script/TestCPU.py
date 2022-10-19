import time,xlwt
import TestLibrary

#控制类
class Controller(object):
    def __init__(self,count):
        self.com = TestLibrary.CommonFunction()
        self.count = count
        self.recordTime = ["记录时间"]
        self.cpuStatus = ["CPU情况"]
        
    #单次测试过程
    def testprocess(self):
        cpu = self.com.GetCPUStatus()
        self.cpuStatus.append(cpu)
        currenttime = self.com.GetCurrentTime()
        self.recordTime.append(self.com.TransferTime(currenttime))

        
    def run(self):
        while self.count>0:
            print("开始倒数第{}次执行".format(self.count))
            self.testprocess()
            print("结束倒数第{}次执行".format(self.count))
            self.count -= 1
            time.sleep(3)
        self.com.StopApp()

            
    #数据的存储
    def SaveDataToXls(self):
        self.workbook = xlwt.Workbook(encoding='utf-8')# 创建一个workbook 并设置编码
        self.worksheet = self.workbook.add_sheet('sheet1',cell_overwrite_ok=True) # 创建工作表，并设置可以重写单元格内容
        c = 0
        while(c < excTimes+1):
            self.worksheet.write(0,c,self.recordTime[c])
            self.worksheet.write(1,c,self.cpuStatus[c])
            self.worksheet.col(c).width = 256*20
            self.worksheet.row(c).set_style(xlwt.easyxf('font:height 720;'))      # 36pt,类型小初的字号
            c += 1
        self.workbook.save("Report/cpu_report.xls")
        
if __name__== '__main__':
    global excTimes
    excTimes = 3 # 执行次数
    controller = Controller(excTimes)
    TestLibrary.CommonFunction().LaunchApp()
    time.sleep(5)
    controller.run()
    controller.SaveDataToXls()
import os,time,xlwt
import TestLibrary

# ����ֱ����cmd��ʹ�õ�����
if __name__== '__main__':
    cmd = "adb shell monkey -p com.toy.toonblast.royalmatching.puzzle --pct-syskeys 100 --ignore-crashes --ignore-timeouts --monitor-native-crashes -v -v 10000 > D:\WorkspaceVS\Monkey\Report\monkey_log.txt"
    os.popen(cmd)


#--pct-touch�����down+up��
#--pct-motion������down+α����¼�+up��
#--pct-trackball�켣��һ�������ϵ��ƶ�+�����
#--pct-nav�������루�������ң�
#--pct-majornav��Ҫ�����¼����м�������˼����˵�����
#--pct-syskeysϵͳ������Home��Back���ӹҵ绰�������Ӽ����е��豸ֻ�ܼӼ�����
#--pct-anyevent�����¼�
#--ignore-crashes ���Ա������쳣
#--ignore-timeouts���Գ�ʱ����
#--ignore-security-exceptions������ɴ���

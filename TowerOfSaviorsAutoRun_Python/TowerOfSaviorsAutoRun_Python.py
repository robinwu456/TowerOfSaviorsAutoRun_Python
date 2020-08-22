# !/usr/bin/python
# coding:utf-8

import sys  
import os  
import re  
import time
from com.dtmilano.android.viewclient import ViewClient

def run():  
    stageRound = 6

    device, serialno = ViewClient.connectToDeviceOrExit()  
    ##vc = ViewClient(device, serialno)         

    while True:
        print("click btn choose attributes")
        device.touch(993, 439, 0)
        time.sleep(1)

        print("choose light")
        device.touch(474, 849, 0)
        time.sleep(1)

        print("choose demon")
        device.touch(225, 1007, 0)
        time.sleep(1)

        print("click btn confirm")
        device.touch(366, 1529, 0)
        time.sleep(1)

        print("choose ally (index=1)")
        device.touch(580, 700, 0)
        time.sleep(1)

        print("click btn choose ally confirm")
        device.touch(544, 1218, 0)
        time.sleep(1)

        print("entering stage...")
        device.touch(945, 2223, 0)
        time.sleep(20)

        print("turning beads ...")
        #device.touch(991, 1396, 0) # 右上第1顆
        #device.touch(1004, 1751, 0) # 右上第3顆
        for i in range(0, stageRound * 15):
            print("turn count: " + str(i))
            device._AdbClient__send("shell:input swipe 991 1396 991 1751", checkok=True, reconnect=True)
            time.sleep(0.5)
        
        time.sleep(30)

        print("exposure battle results")
        device.touch(564, 1043, 0)
        time.sleep(3)

        print("battle again")
        device.touch(897, 1207, 0)
        time.sleep(5)

if __name__ ==  '__main__':  
    #run(int(sys.argv[1]))
    run()









     # 按HOME键  
    #device.press('KEYCODE_HOME')  
    #time.sleep( 3)  
    # # 找到微信图标  
    #vc.dump()      
    #weixin_button = vc.findViewWithTextOrRaise(u'美人的心計')
    #weixin_button = vc.findViewWithTextOrRaise(u'天界的門廊')
    #weixin_button = vc.findViewByIdOrRaise("id/no_id/2")
    ## 点击微信图标  
    #weixin_button.touch()  
    #time.sleep( 10)  
    ## 找到第一个联系人/群  
    ## 可以使用UI Automator Viewer查看到对应第一个联系人/群的resource-id为"com.tencent.mm:id/auj"  
    #vc.dump()  
    #group_button = vc.findViewByIdOrRaise( "com.tencent.mm:id/auj")  
    # # 点击进群  
    #group_button.touch()  
    #time.sleep( 5)  
    # # 找到输入框并输入当前时间  
    #vc.dump()  
    #vc.findViewByIdOrRaise( "com.tencent.mm:id/aep").setText( 'Now:{}'.format(time.strftime( '%Y-%m-%d %H:%M:%S')))  
    #time.sleep( 3)  
    # # 点击发送按钮  
    #vc.dump()  
    #vc.findViewWithTextOrRaise(u '发送').touch()   
    #
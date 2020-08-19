encoding="utf-8"

import sys  
import os  
import re  
import time
from com.dtmilano.android.viewclient import ViewClient

def run():  
    stageRound = 6

     # 連接手機
    device, serialno = ViewClient.connectToDeviceOrExit()  
    ##vc = ViewClient(device, serialno)         

    while True:
        # 點擊"選擇屬性"
        print("點擊 選擇屬性")
        device.touch(993, 439, 0)
        time.sleep(1)

        # 選擇屬性(光)
        print("選擇屬性(光)")
        device.touch(474, 849, 0)
        time.sleep(1)

        # 選擇魔族
        print("選擇魔族")
        device.touch(225, 1007, 0)
        time.sleep(1)

        # 按確定
        print("按確定")
        device.touch(366, 1529, 0)
        time.sleep(1)

        # 選擇隊友(index=1)
        print("選擇隊友(index=1)")
        device.touch(580, 700, 0)
        time.sleep(1)

        # 點擊"選擇"
        print("點擊 選擇")
        device.touch(544, 1218, 0)
        time.sleep(1)

        # 點擊"進入戰鬥"
        print("進入戰鬥...")
        device.touch(945, 2223, 0)
        time.sleep(20)

        # 轉珠
        print("轉珠...")
        #device.touch(991, 1396, 0) # 右上第1顆
        #device.touch(1004, 1751, 0) # 右上第3顆
        for i in range(0, stageRound * 15):
            print("轉珠次數" + str(i))
            device._AdbClient__send("shell:input swipe 991 1396 991 1751", checkok=True, reconnect=True)
            time.sleep(0.5)
        
        # 等待結算畫面
        time.sleep(30)

        # 隨便點畫面
        print("隨便點畫面")
        device.touch(564, 1043, 0)
        time.sleep(3)

        # 點擊"再次挑戰"
        print("點擊 再次挑戰")
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
__author__ = 'bj'
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

device = MonkeyRunner.waitForConnection()
ACTION_CLICK = "DOWN_AND_UP"
GREEN_COLOR = [-1, 69, 192, 26]
WHITE_COLOR = [-1, 255, 255, 255]
BUTTON_GREEN= [-1, 69, 192, 26]
menu_x_2 = 456
menu_y_2 = 291
width = 720;


def click(x, y):
    device.touch(x, y, "DOWN_AND_UP")
    MonkeyRunner.sleep(2)


def toMain():
    runComponent = "com.tencent.mm/com.tencent.mm.ui.LauncherUI"
    device.startActivity(component=runComponent, flags=0x00008000)
    MonkeyRunner.sleep(3)


def clickMenu():
    device.press('KEYCODE_MENU', ACTION_CLICK)
    MonkeyRunner.sleep(2)


def clickRightCorner():
    click(680, 90)
    MonkeyRunner.sleep(2)


def clickFirstMenu():
    device.touch(456, 240, ACTION_CLICK)
    MonkeyRunner.sleep(2)


def clickThirdMenu():
    device.touch(456, 340, ACTION_CLICK)
    MonkeyRunner.sleep(2)


def clickSecondMenu():
    device.touch(456, 290, ACTION_CLICK)
    MonkeyRunner.sleep(2)


def toQrod():
    toMain()
    clickMenu()
    clickThirdMenu()


def moveVertify(y):
    if y > 10:
        while y > 800:
            start = (100, 800 + 300)
            end = (100, 300)
            device.drag(start, end, 0.5, 10)
            y -= 800
        start = (100, y + 300)
        end = (100, 300)
        device.drag(start, end, 0.5, 10)


def clickBack():
    device.press('KEYCODE_BACK', ACTION_CLICK)
    MonkeyRunner.sleep(2)


def scanQrode(start_x, start_y, per_x, move_y_dis, startI, endI):
    for i in range(startI, endI):
        toQrod()
        clickMenu()
        clickSecondMenu()
        moveVertify((i / 3) * move_y_dis)
        device.touch(start_x + (i % 3) * per_x, start_y, ACTION_CLICK)
        MonkeyRunner.sleep(5)
        clickBack()


def sendMessage(idx):
    clickX = 360
    click_y = 475
    num_conv = 9
    height_conv = 115
    if (idx < num_conv):
        device.touch(clickX, click_y + height_conv * idx, ACTION_CLICK)
    else:
        while idx >= num_conv:
            moveVertify(height_conv)
            idx = idx - 1;
        device.touch(clickX, click_y + height_conv * (num_conv - 1), ACTION_CLICK)
    MonkeyRunner.sleep(3)
    device.touch(550, 840, ACTION_CLICK)
    MonkeyRunner.sleep(5)


def clickAva(idx):
    count_per_pagse = 25;


def isNeedAddFrend():
    return True


def doAdd():
    return True


def isNeedSendAddFrendMessage():
    return True


def sendAddFriendMessage():
    return True


def addFrend(idx):
    clickAva(idx)
    if isNeedAddFrend():
        doAdd()
        if isNeedSendAddFrendMessage():
            sendAddFriendMessage()
        else:
            clickBack()
    else:
        clickBack()


def isSomeColor(x, y, basepixe):
    newimage = device.takeSnapshot()
    pixel = newimage.getRawPixel(x, y)
    gateValue = 10
    for i in range(1, 4):
        if abs(basepixe[i] - pixel[i]) > gateValue:
            return False
    return True


def addFrendHelp(idx):
    click(115 + (idx % 4) * 160, 270 + idx / 4 * 200)
    startX = [256,256,256,256]
    startY = [580,716,830, 900]
    for y in startY:
        if (isSomeColor(200, y, BUTTON_GREEN) and isSomeColor(256, y, WHITE_COLOR)):
            click(width / 2, y)
            if isSomeColor(682, 79, GREEN_COLOR):
                clickRightCorner()
                break
    clickBack()



def addGroupOwner(idx):
    startX = width / 2
    startY = 210
    if (idx < 8):
        click(startX, startY)
        clickRightCorner()
        addFrendHelp(0)

# for i in range(1,2):
# toQrod()
# clickMenu()
# clickSecondMenu()
# MonkeyRunner.sleep(3)
# for i in range(1,3):
# toQrod()
# clickMenu()
# clickSecondMenu()
# for i in range(1,10):
# i = 1
# device.touch(start_x + (i % 3) * per_x, start_y, ACTION_CLICK)
# idx = 0
# addGroupOwner(idx)
# addFrendHelp(6)
# print(isSomeColor(256,830,WHITE_COLOR))
# print(isSomeColor(682, 79,GREEN_COLOR))
# newimage = device.takeSnapshot()
# pixel = newimage.getRawPixel(682, 79)
# print(pixel)
# for i in range(3,10):
# addFrendHelp(10)
newimage = device.takeSnapshot()
# for y in range(680,780):
#     pixel = newimage.getRawPixel(256,y)
#     if (pixel[1]  == 255 and pixel[2] == 255):
#         print(y)
#         break
# print('end')
# print(isSomeColor(682, 79, GREEN_COLOR))
addFrendHelp(10)
# MonkeyRunner.sleep(3)  # device.touch(start_x + (i % 3) * per_x, start_y + (i / 3) * per_y, "MOVE")
# device.touch(start_x + (i % 3) * per_x, start_y + (i / 3) * per_y+100, "MOVE")

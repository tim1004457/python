__author__ = 'bj'
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

device = MonkeyRunner.waitForConnection()

menu_x_2 = 456
menu_y_2 = 291


def toMain():
    runComponent = "com.tencent.mm/com.tencent.mm.ui.LauncherUI"
    device.startActivity(component=runComponent, flags=0x00008000)
    MonkeyRunner.sleep(3)


def clickMenu():
    device.press('KEYCODE_MENU', "DOWN_AND_UP")
    MonkeyRunner.sleep(2)


def clickFirstMenu():
    device.touch(456, 240, "DOWN_AND_UP")
    MonkeyRunner.sleep(2)


def clickThirdMenu():
    device.touch(456, 340, "DOWN_AND_UP")
    MonkeyRunner.sleep(2)


def clickSecondMenu():
    device.touch(456, 290, "DOWN_AND_UP")
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
    device.press('KEYCODE_BACK', "DOWN_AND_UP")
    MonkeyRunner.sleep(2)


def scanQrode(start_x, start_y, per_x, move_y_dis, startI, endI):
    for i in range(startI, endI):
        toQrod()
        clickMenu()
        clickSecondMenu()
        moveVertify((i / 3) * move_y_dis)
        device.touch(start_x + (i % 3) * per_x, start_y, "DOWN_AND_UP")
        MonkeyRunner.sleep(5)
        clickBack()


def sendMessage(idx):
    clickX = 360
    click_y = 475
    num_conv=9
    height_conv=115
    if (idx < num_conv):
            device.touch(clickX, click_y + height_conv * idx, "DOWN_AND_UP")
    else :
        while idx >= num_conv:
            moveVertify(height_conv)
            idx=idx-1;
        device.touch(clickX, click_y + height_conv * (num_conv-1) , "DOWN_AND_UP")
    MonkeyRunner.sleep(3)
    device.touch(550,840,"DOWN_AND_UP")
    MonkeyRunner.sleep(5)



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
# device.touch(start_x + (i % 3) * per_x, start_y, "DOWN_AND_UP")
width = 720
height = 1280
start_x = width / 6
start_y = 300
per_x = width / 3
for i in range(0,9):
    clickMenu()
    clickFirstMenu()
    sendMessage(i)
# MonkeyRunner.sleep(3)  # device.touch(start_x + (i % 3) * per_x, start_y + (i / 3) * per_y, "MOVE")
# device.touch(start_x + (i % 3) * per_x, start_y + (i / 3) * per_y+100, "MOVE")

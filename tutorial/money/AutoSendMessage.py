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
    start = (100, y + 300)
    end = (100, 300)
    device.drag(start, end, 1, 10)


width = 720
height = 1280
start_x = width / 6
start_y = 200
per_x = width / 3

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
for i in range(1, 10):
    # toQrod()
    # clickMenu()
    # clickSecondMenu()
    print(i)
    moveVertify((i / 3) * 260)
    device.touch(start_x + (i % 3) * per_x, start_y, "DOWN_AND_UP")
    MonkeyRunner.sleep(5)
# MonkeyRunner.sleep(3)
# device.touch(start_x + (i % 3) * per_x, start_y + (i / 3) * per_y, "MOVE")
# device.touch(start_x + (i % 3) * per_x, start_y + (i / 3) * per_y+100, "MOVE")

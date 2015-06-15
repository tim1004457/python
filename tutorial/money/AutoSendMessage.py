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
    device.touch(653, 105, "DOWN_AND_UP")
    MonkeyRunner.sleep(3)


def clickThirdMenu():
    device.touch(456, 340, "DOWN_AND_UP")
    MonkeyRunner.sleep(3)


def clickSecondMenu():
    device.touch(456, 290, "DOWN_AND_UP")
    MonkeyRunner.sleep(3)


def toQrod():
    toMain()
    clickMenu()
    clickThirdMenu()


width = 720
height = 1280
start_x = width / 6
start_y = 200
per_x = width / 3
per_y = height / 5

# for i in range(1,2):
# toQrod()
# clickMenu()
# clickSecondMenu()
# MonkeyRunner.sleep(3)
i = 1
print(start_x + (i % 3) * per_x)
print(start_y + (i / 3) * per_y)
# device.touch(start_x + (i % 3) * per_x, start_y + (i / 3) * per_y, "DOWN_AND_UP")
# MonkeyRunner.sleep(5)
newimage = device.takeSnapshot()
pixel_int = newimage.getRawPixelInt(214, 739)

raw_pixel_int = newimage.getRawPixelInt(494, 739)
green = -16466430
print(raw_pixel_int)
print ((pixel_int == raw_pixel_int and pixel_int == green))
# if pixel_int == raw_pixel_int and pixel_int == green:
print('yes')
device.touch(366, 736, "DOWN")
MonkeyRunner.sleep(1)
device.touch(366, 736, "UP")

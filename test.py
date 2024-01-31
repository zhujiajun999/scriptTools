import os
from time import sleep
import pyautogui
import sys
# import tesserocr
# from PIL import Image

# image = Image.open('.png')
# result = tesserocr.image_to_text(image)
# print(result)

# 案例一,使用osascript在cmd运行
# cmd = """
# osascript -e 'tell application "System Events" to keystroke "nihao" ' 
# """
# # using {command down}
# # minimize active window

# sleep(5)
# os.system(cmd)
# https://stackoverflow.com/questions/136734/key-presses-in-python
# 案例二,使用pyautogui
# pyautogui.typewrite('any text you want to type')
# sleep(5)
# pyautogui.keyDown('abc')

def test(times):
    print(times)


def main():
    times = sys.argv[1]


if __name__ == '__main__':
    test()
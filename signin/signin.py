from asyncio import exceptions
import datetime
import os
import random
import subprocess
import sys
import time
from unittest import expectedFailure
from interval import Interval
from selenium import webdriver
from selenium.webdriver.common.by import By
from settings import *
import pyautogui
import getpass


# import pyautogui as pag


def sigin(starTimes):
    starTimes = starTimes[0:2] + ':' + starTimes[2:]
    print('脚本执行时间：' + starTimes)

    while True:
        # 当前时间
        now_localtime = time.strftime("%H:%M:%S", time.localtime())  # 18:00:00
        # 当前时间（以时间区间的方式表示）
        now_time = Interval(now_localtime, now_localtime)
        print('当前时间：' + now_localtime)
        time_interval = Interval(f'{starTimes}:00', f'{starTimes}:59')  # 脚本执行时间是否在这个区间

        # width, height = pyautogui.size() # 屏幕的宽度和高度
        # print(width, height)

        if now_time in time_interval:
            driver = webdriver.Chrome()
            # driver.maximize_window()  # 最大化
            driver.get(url)
            time.sleep(2)
            # 登录
            driver.find_element(By.ID, 'username').send_keys(username)
            driver.find_element(By.ID, 'password_input').send_keys(password)
            time.sleep(2)
            driver.find_element(By.ID, 'login_button').click()
            time.sleep(2)
            # 签入签出
            try:
                driver.find_element(By.ID, 'checkin_btn')
                driver.find_element(By.ID, 'checkin_btn').click()
            except:
                driver.find_element(By.ID, 'checkout_btn').click()
            time.sleep(3)
            numbers = 1  # 站位,验证码元素
            if numbers == 1:
                # 直接签出
                # driver.find_element(By.CSS_SELECTOR, '.btn-primary > span').click()  # 确定
                driver.find_element(By.CSS_SELECTOR, '.btn:nth-child(2) > span').click()  # 取消
                time.sleep(2)
            else:  # 识别验证码，后续补充
                numbers = 0

            time.sleep(3)
            if driver.find_element(By.CLASS_NAME, 'ui-dialog-titlebar') != None:
                break
        else:
            pyautogui.moveTo(x=random.randint(1000,1500),y=random.randint(500,800), duration=1)
            time.sleep(60)

    # # print(pag.position())
    print('签到成功,结束时间：' + now_localtime)
    driver.close()  # 关闭浏览器
    os.system("pmset displaysleepnow")  # 锁屏
    # 关机 需要密码 无法 os.sys输出  调试中
    # os.system("sudo shutdown -n 1")
    # time.sleep(1)
    # password = getpass.getpass("Password:")
    # print("您输入的密码是：", password)


def main():
    if len(sys.argv) < 2:
        print("python3 sigin.py 1800\n")
        sys.exit()

    starTimes = sys.argv[1]
    sigin(starTimes)


if __name__ == '__main__':
    main()

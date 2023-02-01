import os
import time
from interval import Interval
from selenium import webdriver
from selenium.webdriver.common.by import By
from settings import *
import pyautogui as pag


class sigin():
    while True:
        # 当前时间
        now_localtime = time.strftime("%H:%M:%S", time.localtime())
        # 当前时间（以时间区间的方式表示）
        now_time = Interval(now_localtime, now_localtime)
        print(now_time)
        time_interval = Interval(starTimes, endTimes)

        # width, height = pyautogui.size() # 屏幕的宽度和高度
        # print(width, height)

        if now_time in time_interval:
            driver = webdriver.Chrome()
            # driver.maximize_window()  # 最大化
            driver.get(url)
            time.sleep(2)
            # 登录
            driver.find_element(By.NAME, 'data[Login][name]').send_keys(username)
            driver.find_element(By.NAME, 'data[Login][password]').send_keys(password)
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="login_button"]').click()
            time.sleep(2)
            # 签出
            driver.find_element(By.ID, 'checkout_btn').click()
            time.sleep(3)
            numbers = 1  # 站位,验证码元素
            if numbers == 1:
                # 直接签出
                driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/a[1]/span').click()  # 确定
                # driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/a[2]').click()  # 取消
                time.sleep(2)
            else:  # 识别验证码，后续补充
                numbers = 0
            
            time.sleep(3)
            if driver.find_element(By.CLASS_NAME, 'ui-dialog-titlebar') != None:
                break
        else:
            time.sleep(60)

    # print(pag.position())
    driver.close()  # 关闭浏览器
    # pag.moveTo(0, 1050, duration=2)  # 自己电脑设置左下角触发角锁屏
    os.system("pmset displaysleepnow")  # 锁屏


if __name__ == '__main__':
    sigin()


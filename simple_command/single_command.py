# import pandas as pd #用于数据输出
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

# from datetime import datetime

driver=webdriver.Edge() # 选择Chrome浏览器
driver.get('http://192.168.100.254/litepoint/') # 打开网站
driver.maximize_window() #最大化谷歌浏览器

#0417驱动
runpath="cd E:/xiechao/Git/IQ test/exe/8800d80/win10_x64 && "
steptime=1000
#0704驱动
runpath="cd E:/xiechao/Git/IQ test/exe/8800d80/win10_x64 && "
steptime=500

#0630驱动
runpath="cd E:/xiechao/Git/IQ test/exe/8800d80/win10_x64 && "
steptime=500


i=0
while i<14:
    os.system(runpath+"aicrf_test.exe set_tx "+str(i+1)+" 0 0 0 1024 1000")
    time.sleep(1)
    i=i+2




# os.system("cd C:/Users/JYWX/Desktop/M80射频摸底/aic8800_windows_rftest_2024_0417/exe/8800d80/win10_x64/ && aicrf_test.exe set_txstop")
time.sleep(1)
#txstop
os.system(runpath+"aicrf_test.exe set_txstop")
#基准功率表
os.system(runpath+"aicrf_test.exe rdwr_pwrlvl")
#校准补偿
os.system(runpath+"aicrf_test.exe rdwr_efuse_pwrofst")
#11b
os.system(runpath+"aicrf_test.exe set_tx 1 0 0 0 1024 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(2412);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

os.system(runpath+"aicrf_test.exe set_tx 13 0 0 0 1024 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(2472);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)
#功率设置
os.system(runpath+"aicrf_test.exe set_power 22")

os.system(runpath+"aicrf_test.exe set_power 21")

os.system(runpath+"aicrf_test.exe set_power 20")

os.system(runpath+"aicrf_test.exe set_power 19")

os.system(runpath+"aicrf_test.exe set_power 18")

os.system(runpath+"aicrf_test.exe set_power 17")

os.system(runpath+"aicrf_test.exe set_power 16")

os.system(runpath+"aicrf_test.exe set_power 15")

os.system(runpath+"aicrf_test.exe set_power 14")

os.system(runpath+"aicrf_test.exe set_power 13")
#11ax 40M MCS11   2.4G
# os.system(runpath+"aicrf_test.exe set_txstop");time.sleep(2);os.system(runpath+"aicrf_test.exe set_tx 3 0 0 11 1024 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(2422);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

# os.system(runpath+"aicrf_test.exe set_txstop");time.sleep(2);os.system(runpath+"aicrf_test.exe set_tx 7 0 0 11 1024 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(2442);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

# os.system(runpath+"aicrf_test.exe set_txstop");time.sleep(2);os.system(runpath+"aicrf_test.exe set_tx 11 0 0 11 1024 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(2462);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)


os.system(runpath+"aicrf_test.exe set_txstop");time.sleep(5);os.system(runpath+"aicrf_test.exe set_tx 3 1 5 11 8192 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(2422);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

os.system(runpath+"aicrf_test.exe set_txstop");time.sleep(5);os.system(runpath+"aicrf_test.exe set_tx 7 1 5 11 8192 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(2442);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

os.system(runpath+"aicrf_test.exe set_txstop");time.sleep(5);os.system(runpath+"aicrf_test.exe set_tx 11 1 5 11 8192 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(2462);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)
#11ax 80M MCS11  5G
os.system(runpath+"aicrf_test.exe set_txstop");time.sleep(5);os.system(runpath+"aicrf_test.exe set_tx 36 2 5 11 16000 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5180);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

os.system(runpath+"aicrf_test.exe set_txstop");time.sleep(5);os.system(runpath+"aicrf_test.exe set_tx 42 2 5 11 16000 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5210);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

os.system(runpath+"aicrf_test.exe set_txstop");time.sleep(5);os.system(runpath+"aicrf_test.exe set_tx 58 2 5 11 16000 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5290);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

os.system(runpath+"aicrf_test.exe set_txstop");time.sleep(5);os.system(runpath+"aicrf_test.exe set_tx 106 2 5 11 16000 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5530);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

os.system(runpath+"aicrf_test.exe set_txstop");time.sleep(5);os.system(runpath+"aicrf_test.exe set_tx 122 2 5 11 16000 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5610);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

os.system(runpath+"aicrf_test.exe set_txstop");time.sleep(5);os.system(runpath+"aicrf_test.exe set_tx 138 2 5 11 16000 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5690);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

os.system(runpath+"aicrf_test.exe set_txstop");time.sleep(5);os.system(runpath+"aicrf_test.exe set_tx 155 2 5 11 16000 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5775);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

#6M
os.system(runpath+"aicrf_test.exe set_txstop");os.system(runpath+"aicrf_test.exe set_tx 36 2 5 0 16000 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5180);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

os.system(runpath+"aicrf_test.exe set_tx 42 2 5 0 16000 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5210);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

os.system(runpath+"aicrf_test.exe set_tx 58 2 5 0 16000 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5290);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

os.system(runpath+"aicrf_test.exe set_tx 106 2 5 0 16000 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5530);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

os.system(runpath+"aicrf_test.exe set_tx 122 2 5 0 16000 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5610);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

os.system(runpath+"aicrf_test.exe set_tx 138 2 5 0 16000 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5690);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

os.system(runpath+"aicrf_test.exe set_tx 155 2 5 0 16000 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5775);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)



#11n 20M MCS7

os.system(runpath+"aicrf_test.exe set_tx 42 0 2 7 4096 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5210);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

os.system(runpath+"aicrf_test.exe set_tx 58 0 2 7 4096 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5290);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

os.system(runpath+"aicrf_test.exe set_tx 106 0 2 7 4096 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5530);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

os.system(runpath+"aicrf_test.exe set_tx 122 0 2 7 4096 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5610);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

os.system(runpath+"aicrf_test.exe set_tx 138 0 2 7 4096 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5690);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

os.system(runpath+"aicrf_test.exe set_tx 155 0 2 7 4096 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5775);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

#11ac 80M MCS9
os.system(runpath+"aicrf_test.exe set_tx 36 2 4 9 16000 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5180);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

os.system(runpath+"aicrf_test.exe set_tx 42 2 4 9 16000 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5210);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

os.system(runpath+"aicrf_test.exe set_tx 58 2 4 9 16000 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5290);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

os.system(runpath+"aicrf_test.exe set_tx 106 2 4 9 16000 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5530);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

os.system(runpath+"aicrf_test.exe set_tx 122 2 4 9 16000 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5610);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

os.system(runpath+"aicrf_test.exe set_tx 138 2 4 9 16000 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5690);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

os.system(runpath+"aicrf_test.exe set_tx 155 2 4 9 16000 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5775);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

#11ac 40M MCS9
os.system(runpath+"aicrf_test.exe set_tx 42 1 4 9 8192 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5210);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

os.system(runpath+"aicrf_test.exe set_tx 58 1 4 9 8192 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5290);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

os.system(runpath+"aicrf_test.exe set_tx 106 1 4 9 8192 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5530);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

os.system(runpath+"aicrf_test.exe set_tx 122 1 4 9 8192 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5610);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

os.system(runpath+"aicrf_test.exe set_tx 138 1 4 9 8192 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5690);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

os.system(runpath+"aicrf_test.exe set_tx 1 4 9 8192 "+str(steptime));driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a');driver.find_element(By.ID,'Frequency_inp').send_keys(5775);driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)

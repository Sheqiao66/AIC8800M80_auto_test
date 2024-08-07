import pandas as pd #用于数据输出
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from datetime import datetime


#环境配置
# chromedriver = "C:\Program Files (x86)\Microsoft\Edge\Application"
# os.environ["webdriver.ie.driver"] = chromedriver
 
driver=webdriver.Edge() # 选择Chrome浏览器
driver.get('http://192.168.100.254/litepoint/') # 打开网站
driver.maximize_window() #最大化谷歌浏览器

curtime=datetime.now()
runpath="cd E:/xiechao/Git/IQ test/exe/8800d80/win10_x64 && "
savepath='E:/xiechao/1data/'

filename=str(curtime.year)+'_'+str(curtime.month)+'_'+str(curtime.day)+'_'+str(curtime.hour)+'_'+str(curtime.minute)+'_'+str(curtime.second)+'_'
filename=filename+'_rx_scan_11ax改进_0704软件_#2.csv'


#配置文件——测试项
data1 = pd.read_csv('configure_rx_scan_11ax.csv',encoding='GB2312')

# print(data1)

data1['mode'] = data1['mode'].astype(str)

mode=data1['mode']

fre=data1['fre']
ch=data1['ch']
bw=data1['bw']
level=data1['level']
levelstop=data1['levelstop']
data1['wave_xpath'] = data1['wave_xpath'].astype(str)
wave_xpath=data1['wave_xpath']

i=0
receive_sensitive=[]
fcsok=[]
total=[]
step=0.5

modeout=[]
chout=[]
levelout=[]
fcsokout=[]
totalout=[]


#指令处理


vsg_xpath='/html/body/div[1]/div[2]/div[1]/div[1]/label[2]/span'

time.sleep(10)
# time.sleep(1)
driver.find_element(By.ID,'techBtn').click()
time.sleep(1)
driver.find_element(By.ID,'wifisiso').click()
time.sleep(1)
# driver.find_element(By.ID,'ui-id-2').click()
# time.sleep(1)

driver.find_element(By.XPATH,vsg_xpath).click()
time.sleep(1)

driver.find_element(By.ID,'ui-id-73').click()
time.sleep(1)

driver.find_element(By.ID,'ui-id-75').click()
time.sleep(1)


driver.find_element(By.ID,'counterEnable').click()
time.sleep(1)

#设置发包长度
driver.find_element(By.ID,'counterInfo').send_keys(Keys.CONTROL,'a')
driver.find_element(By.ID,'counterInfo').send_keys(1000)
driver.find_element(By.ID,'counterInfo').send_keys(Keys.ENTER)
time.sleep(1)

driver.find_element(By.ID,'runBtn').click()
time.sleep(1)

# #加载波形文件
driver.find_element(By.ID,'VsgWaveLoadBtn').click()
# print('请加载波形文件，等待20s')
time.sleep(2)

user_xpath='/html/body/div[71]/div[2]/div[2]/ul/div[508]/img[1]'

driver.find_element(By.XPATH,user_xpath).click()
time.sleep(1)

driver.find_element(By.XPATH,wave_xpath[i]).click()
time.sleep(1)

driver.find_element(By.ID,'SelectWave').click()
time.sleep(1)





# set_rx='aicrf_test.exe set_rx '


rx_result='aicrf_test.exe get_rx_result'
rx_stop='aicrf_test.exe set_rxstop'

play_xpath='/html/body/div[1]/div[2]/div[3]/div/div[1]/div[2]/div[2]/div/div[3]/div[3]/span[2]/label[2]/span'




while i<len(ch):
    
    
    if i>0:
        
        if mode[i]!=mode[i-1]:
            #加载波形文件
            print('-----------mode_change_to ',mode[i]+'-----------------')
            driver.find_element(By.ID,'VsgWaveLoadBtn').click()
            # print('请加载波形文件，等待20s')
            time.sleep(2)
            driver.find_element(By.XPATH,user_xpath).click()
            time.sleep(1)
    
            driver.find_element(By.XPATH,wave_xpath[i]).click()
            time.sleep(1)
    
            driver.find_element(By.ID,'SelectWave').click()
            time.sleep(1)
            
            
            time.sleep(6)
#----------------------------------------------------------------------------------------------------        
        
    # level_send=float(level[i])
    level_send=-61
    #vsg_freq 设置
    driver.find_element(By.ID,'vsg_freq_inp').send_keys(Keys.CONTROL,'a')
    driver.find_element(By.ID,'vsg_freq_inp').send_keys(str(fre[i]))
    driver.find_element(By.ID,'vsg_freq_inp').send_keys(Keys.ENTER)
    time.sleep(1)
    os.system(runpath+rx_stop)
    print(rx_stop)

    
    while level_send<=0:
        
        if (level_send>=-50)&(level_send<-10):
            step=5
        elif (level_send>=-56)&(level_send<-50):
            step=2
        elif (level_send>=-6)&(level_send<0):
            step=2
        else:    
            step=0.5
        # os.system(rx_stop)
        time.sleep(0.5)
        set_rx='aicrf_test.exe set_rx '+str(ch[i])+' '+str(bw[i])
        print(set_rx)
        os.system(runpath+set_rx)
        
        
        #灵敏度设置
        driver.find_element(By.ID,'VsgPowerLevel').send_keys(Keys.CONTROL,'a')
        driver.find_element(By.ID,'VsgPowerLevel').send_keys(str(level_send))
        # print(level_send)
        driver.find_element(By.ID,'VsgPowerLevel').send_keys(Keys.ENTER)
        time.sleep(1)
        
        driver.find_element(By.XPATH,play_xpath).click()
        time.sleep(6)
        
        re=os.popen(runpath+rx_result)
        print(rx_result)
        
        text=re.readlines()
        t=str(text)
        
        print(t)
        print('------------'+mode[i]+'------------------')
        a1=t.find('fcsok=')
        a2=t.find('total=')
        a=t.find(',',a1,len(t))

        b=t.find('done',a2,len(t))

        # print(b)
        fcs=int(t[a1+6:a])
        tot=int(t[a2+6:b-6])
        
        print(fcs,tot,' level_send:',level_send)
        
        if (fcs>1020)|(tot>1020):
            print('-------error--------')
            os.system(runpath+rx_stop)
            driver.find_element(By.ID,'stopPlayWave').click()
            time.sleep(3)
            # level_send=level_send-step
            continue
            # time.sleep(3)
        # else:
        #     print(level_send,'-------pass--------')
        #     receive_sensitive.append(level_send)
            
        #     os.system(runpath+rx_stop)
        #     time.sleep(2)
        #     print('receive_sensitive:',receive_sensitive)
        #     fcsok.append(fcs)
        #     total.append(tot)
        #     break
        # fcs1=fcs
        # tot1=tot
        
        modeout.append(mode[i])
        chout.append(ch[i])
        levelout.append(level_send)
        fcsokout.append(fcs)
        totalout.append(tot)
        
        level_send=level_send+step
        
#----------------------------------------------------------------------------------------------------        
        
    i=i+1
    test=pd.DataFrame({'mode':modeout,'ch':chout,'level':levelout,
                       'fcsok':fcsokout,'total':totalout})
    test.to_csv(savepath+filename,index=False) #数据存入csv,存储位置及文件名称











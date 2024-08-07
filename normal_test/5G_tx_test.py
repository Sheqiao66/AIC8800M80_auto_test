import pandas as pd #用于数据输出
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from datetime import datetime

#先安装pywin32，才能导入下面两个包
#环境配置
# chromedriver = "C:\Program Files (x86)\Microsoft\Edge\Application"
# os.environ["webdriver.ie.driver"] = chromedriver
 
driver=webdriver.Edge() # 选择Chrome浏览器
driver.get('http://192.168.100.254/litepoint/') # 打开网站
driver.maximize_window() #最大化谷歌浏览


#打开VSA


# time.sleep(30)
# time.sleep(1)

time.sleep(8)
# time.sleep(1)
driver.find_element(By.ID,'techBtn').click()
# time.sleep(1)
driver.find_element(By.ID,'wifisiso').click()
# time.sleep(1)
driver.find_element(By.ID,'ui-id-2').click()
time.sleep(1)


#Results

element_to_drag=driver.find_element(By.ID,'wifi_siso_item1')
# time.sleep(1)
target_element =driver.find_element(By.ID,'Row11')
# time.sleep(1)
actions = ActionChains(driver)#拖拽
actions.drag_and_drop(element_to_drag, target_element).perform()
time.sleep(1.5)

element_to_drag=driver.find_element(By.ID,'wifi_siso_item6')
# time.sleep(1)
target_element =driver.find_element(By.ID,'Row12')
# time.sleep(1)
actions = ActionChains(driver)#拖拽
actions.drag_and_drop(element_to_drag, target_element).perform()
time.sleep(1.5)

element_to_drag=driver.find_element(By.ID,'wifi_siso_item20')
time.sleep(1)
target_element =driver.find_element(By.ID,'Row21')
# time.sleep(1)
actions = ActionChains(driver)#拖拽
actions.drag_and_drop(element_to_drag, target_element).perform()
# time.sleep(1)

element_to_drag=driver.find_element(By.ID,'wifi_siso_item8')
time.sleep(1)
target_element =driver.find_element(By.ID,'Row22')
# time.sleep(1)
actions = ActionChains(driver)#拖拽
actions.drag_and_drop(element_to_drag, target_element).perform()
# time.sleep(1)



driver.find_element(By.ID,'ui-id-1').click()
# time.sleep(1)
driver.find_element(By.ID,'ui-id-7').click()
time.sleep(1)

driver.find_element(By.ID,'refLevel').send_keys(Keys.CONTROL,'a')
driver.find_element(By.ID,'refLevel').send_keys(30)
driver.find_element(By.ID,'refLevel').send_keys(Keys.ENTER)
time.sleep(1)

driver.find_element(By.ID,'captureLen').send_keys(Keys.CONTROL,'a')
driver.find_element(By.ID,'captureLen').send_keys(10)
driver.find_element(By.ID,'captureLen').send_keys(Keys.ENTER)
time.sleep(1)

driver.find_element(By.ID,'ui-id-9').click()
time.sleep(1)

VIDeo_xpath='/html/body/div[7]/ul/li[3]'

driver.find_element(By.ID,'trigSrcCombo-button').click()
time.sleep(0.5)

driver.find_element(By.XPATH,VIDeo_xpath).click()
time.sleep(0.5)
# driver.find_element(By.ID,'ui-id-27').click()
time.sleep(0.5)

driver.find_element(By.ID,'runBtn').click()

# print(command[0])
# os.system(command[0])


runpath="cd E:/xiechao/Git/IQ test/exe/8800d80/win10_x64 && "

# os.system(runpath+'aicrf_test.exe set_tx 106 0 5 11 4096 500')
savepath='E:/xiechao/1data/'
curtime=datetime.now()

#文件名

filename=str(curtime.year)+'_'+str(curtime.month)+'_'+str(curtime.day)+'_'+str(curtime.hour)+'_'+str(curtime.minute)+'_'+str(curtime.second)+'_'
filename=filename+'_test_U11pro_5G_all_#6.csv'

timestep=1000

#指令处理

#配置文件——测试项
data1 = pd.read_csv('configure_test_U11pro_5G_all.csv')

#print(data1)

data1['mode'] = data1['mode'].astype(str)

mode=data1['mode']

fre=data1['fre']
ch=data1['ch']
bw=data1['bw']
md_n=data1['md_n']
rate=data1['rate']
p_len=data1['p_len']
target_power=data1['target_power']



#初始化


i=0
command=[]
power_margin=[]


ch_n=0

power=[]
evm=[]

j=0

#tx set

# print(len(mode))
while i<len(mode):
    command.append('aicrf_test.exe set_tx '+str(ch[i])+' '+str(bw[i])+' '+str(md_n[i])+' '+str(rate[i])+' '+str(p_len[i])+' '+str(timestep))
    
    #print(command[i])
    i=i+1
# print(command[0]) 
# os.system(command[0])

txstop='aicrf_test.exe set_txstop '




xpath_power='/html/body/div[1]/div[2]/div[4]/div/div[1]/div[1]/div/div[2]/div[1]/div/div[1]/div/div[1]/table/tbody/tr[1]/td[2]'
xpath_evm='/html/body/div[1]/div[2]/div[4]/div/div[1]/div[1]/div/div[2]/div[2]/div/div[1]/div/div[1]/table/tbody/tr[1]/td[2]'

#运行
# mm=4
# j=mm
while j<len(mode):
# while j<mm+4:
    print(fre[j])
    print(command[j])
    print('---------------'+str(mode[j])+'------------')
    os.system(runpath+command[j])
    print('---------------command------------')
    time.sleep(1)
    
    driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a')
    # a=driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'c')
    # print(fre[j])
    
    driver.find_element(By.ID,'Frequency_inp').send_keys(int(fre[j]))
    print('---------------fre ------------')
    driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)
    
    print('---------------fre changed------------')
    time.sleep(6)
    
    test_power1=driver.find_element(By.XPATH,xpath_power).text
    test_evm1=driver.find_element(By.XPATH,xpath_evm).text
    print('power1:',test_power1,'evm1:',test_evm1)
    time.sleep(1)
    test_power2=driver.find_element(By.XPATH,xpath_power).text
    test_evm2=driver.find_element(By.XPATH,xpath_evm).text
    print('power2:',test_power2,'evm2:',test_evm2)
    time.sleep(1)
    
    test_power3=driver.find_element(By.XPATH,xpath_power).text
    test_evm3=driver.find_element(By.XPATH,xpath_evm).text
    print('power3:',test_power3,'evm3:',test_evm3)
    
    
    test_power=max(float(test_power1), float(test_power2), float(test_power3))
    if test_evm1=='--':
        test_evm=test_evm1
    else:
        test_evm=min(float(test_evm1), float(test_evm2), float(test_evm3))
    print('power:',test_power,'evm:',test_evm)
    
    
    
    
    # test_power=driver.find_element(By.XPATH,xpath_power).text
    # test_evm=driver.find_element(By.XPATH,xpath_evm).text
    # print('power:',test_power,'evm:',test_evm)
    
    
    print('target_power:',target_power[j])
    pm=float(test_power)-float(target_power[j])
    pm=round(pm,2)
    
    print('power_margin:',pm)
    power_margin.append(pm)
    
    power.append(test_power)
    evm.append(test_evm)
    # print('list1:',power)
    # print('list2:',evm)
    

    
    os.system(runpath+txstop)
    time.sleep(0.5)
    if int(fre[j])==5775:
        print('-----------------拔插一下，等待8s-----------')
        time.sleep(12)
    j=j+1
    
    test=pd.DataFrame({'mode':mode[0:j],'ch':ch[0:j],'power':power[0:j],'evm':evm[0:j]
                       ,'target_power':target_power[0:j],'power_margin':power_margin[0:j]})
    test.to_csv(savepath+filename,index=False) #数据存入csv,存储位置及文件名称
    
    
    
    
 
# #test=pd.DataFrame({'power':power,'evm':evm})
# test=pd.DataFrame({'mode':mode,'fre':fre,'ch':ch,'bw':bw,'power':power,'evm':evm,'target_power':target_power,'power_margin':power_margin,'result':result})
# test.to_csv(filename,index=False) #数据存入csv,存储位置及文件名称









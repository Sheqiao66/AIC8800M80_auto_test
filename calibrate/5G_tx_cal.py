import pandas as pd #用于数据输出
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from datetime import datetime


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
time.sleep(1)

element_to_drag=driver.find_element(By.ID,'wifi_siso_item6')
# time.sleep(1)
target_element =driver.find_element(By.ID,'Row12')
# time.sleep(1)
actions = ActionChains(driver)#拖拽
actions.drag_and_drop(element_to_drag, target_element).perform()
time.sleep(1)

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
curtime=datetime.now()
savepath='E:/xiechao/1data/'
#文件名

filename=str(curtime.year)+'_'+str(curtime.month)+'_'+str(curtime.day)+'_'+str(curtime.hour)+'_'+str(curtime.minute)+'_'+str(curtime.second)+'_'
filename=filename+'_cal_U11Pro_#13.csv'

#指令处理

#配置文件——测试项
data1 = pd.read_csv('configure_cal_U11Pro_tiaogao_11ax.csv')

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
of1=data1['of1']
of2=data1['of2']
of3=data1['of3']



#初始化
timestep=1000

i=0
command=[]
power_margin=[]

offset=[]

result=[]
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

# #清除校准数据
# while j<len(mode):
    
    
#     of_reset='aicrf_test.exe rdwr_efuse_pwrofst '+str(of1[j])+' '+str(of2[j])+' '+str(of3[j])+' 0'
#     print(of_reset)
#     os.system(runpath+of_reset)
#     time.sleep(2)
#     j=j+1

j=0
while j<len(mode):

    
    
    
    print(fre[j])
    print(command[j])
    print('---------------'+str(mode[j])+'-------------')
    os.system(runpath+command[j])
    print('---------------'+mode[j]+'------------')
    time.sleep(2)
    
    driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'a')
    # a=driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.CONTROL,'c')
    # print(fre[j])
    
    driver.find_element(By.ID,'Frequency_inp').send_keys(int(fre[j]))
    print('---------------fre ------------')
    driver.find_element(By.ID,'Frequency_inp').send_keys(Keys.ENTER)
    
    print('---------------fre changed------------')
    time.sleep(10)
    
    test_power=driver.find_element(By.XPATH,xpath_power).text
    print('power:',test_power)
    test_evm=driver.find_element(By.XPATH,xpath_evm).text
    print('evm:',test_evm)
    print('target_power:',target_power[j])
    pm=float(test_power)-float(target_power[j])
    
    pm=round(pm,2)
    print('power_margin:',pm)
    power_margin.append(pm)
    
    power.append(test_power)
    evm.append(test_evm)
    # print('list1:',power)
    # print('list2:',evm)
    
    offset.append(round(2*-pm))
    
    if int(pm>3.9)|int(pm<-3.9):
        print('------------error power abnormal----------')
        result.append('fail')
        
        os.system(runpath+txstop)
        time.sleep(1)
        j=j+1
        
        test=pd.DataFrame({'mode':mode[0:j],'fre':fre[0:j],'ch':ch[0:j],'bw':bw[0:j],'power':power[0:j],'evm':evm[0:j]
                           ,'target_power':target_power[0:j],'power_margin':power_margin[0:j],'result':result[0:j],'offset':offset[0:j]})
        test.to_csv(filename,index=False) #数据存入csv,存储位置及文件名称
        continue
    
    result.append('pass')
    of_cmd='aicrf_test.exe rdwr_efuse_pwrofst '+str(of1[j])+' '+str(of2[j])+' '+str(of3[j])+' '+str(offset[j])
    print(of_cmd)
    os.system(runpath+of_cmd)
    print('---------------set offset------------')
    time.sleep(3)
    
    os.system(runpath+txstop)
    time.sleep(1)
    
    j=j+1
    
    test=pd.DataFrame({'mode':mode[0:j],'fre':fre[0:j],'ch':ch[0:j],'bw':bw[0:j],'power':power[0:j],'evm':evm[0:j]
                       ,'target_power':target_power[0:j],'power_margin':power_margin[0:j],'result':result[0:j],'offset':offset[0:j]})
    test.to_csv(savepath+filename,index=False) #数据存入csv,存储位置及文件名称
    
    
    
    
 
# #test=pd.DataFrame({'power':power,'evm':evm})
# test=pd.DataFrame({'mode':mode,'fre':fre,'ch':ch,'bw':bw,'power':power,'evm':evm,'target_power':target_power,'power_margin':power_margin,'result':result})
# test.to_csv(filename,index=False) #数据存入csv,存储位置及文件名称









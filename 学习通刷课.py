from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
wd = webdriver.Edge(r'D:\msedgedriver.exe')
wd.maximize_window()
wd.implicitly_wait(10)# 设置最大等待时长为5秒
wd.get('https://mooc1-2.chaoxing.com/mycourse/studentstudy?chapterId=478246040&courseId=220218514&clazzid=46577396&enc=4b8f6b1ccf3ac97e55cd8e7b5fd3e984')#打开网址
element=wd.find_element_by_class_name('ipt-tel')
element.send_keys('212503027')
element = wd.find_element_by_class_name('ipt-pwd')
element.send_keys('WL.+.09163035')
time.sleep(1)
wd.find_element_by_id('loginBtn').click()#点击登录
wd.find_element_by_css_selector('#alert_dialog_wrapper > div.alert_close_btn').click()#点击取消弹窗
wd.find_element_by_css_selector('#group_container > div > div.group-main > div:nth-child(3) > div > img').click()#点击预约教室
print(wd.title)
for handle in wd.window_handles:
    wd.switch_to.window(handle)
    if '智能教室预约' in wd.title:
        break
print(wd.title)
ActionChains(wd).move_to_element(wd.find_elements_by_xpath('/html/body/div/div/div[2]/div[1]/div[3]/div[1]')).click().perform()
# element = wd.find_element_by_css_selector('#main_content > div > div.calendar > div.room_date > div.next_date > div.next_icon')
# wd.execute_script("arguments[0].click();", element)
# time.sleep(3)
# sum1=0
# elements = wd.find_elements_by_css_selector('.time_table>table>table>tbody>tr')
# for element in elements:
#     sum1+=1
#     print(element.get_attribute('date-reactid'))
# print(sum1)
wd.quit()
# wd.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div[3]/div[1]').click()

# time.sleep(3)
# wd.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div[3]/div[1]').click()
# time.sleep(2)
# wd.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div[3]/div[1]').click()
# time.sleep(2)
# elements=wd.find_elements_by_xpath('/html/body/div/div/div[2]/div[2]/table/tbody/tr[8]/td[2]/div[4]/div[1]/div[2]')
# for element in elements:             #测试并退出
#    print('------------------------')
#    print(element.text)
#    print(element.get_attribute('outerHTML'))
# wd.quit()
#main_content > div > div.calendar > div.room_date > div.normal_date > div:nth-child(1) > div.data_inf_day_sel
#main_content > div > div.calendar > div.room_date > div.normal_date > div:nth-child(1) > div.data_inf_day_sel
#main_content > div > div.calendar > div.time_table > table > tbody > tr:nth-child(8) > td:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div.order_btn
#main_content > div > div.calendar > div.time_table > table > tbody > tr:nth-child(8) > td:nth-child(3) > div:nth-child(4) > div:nth-child(1) > div.order_btn
#main_content > div > div.calendar > div.time_table > table > tbody > tr:nth-child(8) > td:nth-child(4) > div:nth-child(4) > div:nth-child(1) > div.order_btn
#main_content > div > div.calendar > div.time_table > table > tbody > tr:nth-child(8) > td:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div.order_btn
# element = wd.find_element_by_css_selector('#main_content > div > div.top > div.search > div > input')
# element.send_keys('A509\n')
# for element in elements:             #测试并退出
#    print('------------------------')
#    print(element.get_attribute('outerHTML'))
# wd.quit()




# for element in elements:             #测试并退出
#    print('------------------------')
#    print(element.get_attribute('outerHTML'))
# wd.quit()


# element = wd.find_element_by_id('kw')
# element.send_keys('黑羽魔巫宗')
# wd.find_element_by_id('su').click()#点击百度一下
# element = wd.find_element_by_id('1')
# print (element.text)#打印文本

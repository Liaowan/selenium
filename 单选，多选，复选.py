from selenium import webdriver
wd = webdriver.Edge(r'D:\msedgedriver.exe')
wd.implicitly_wait(5)# 设置最大等待时长为5秒
wd.get('http://cdn1.python3.vip/files/selenium/test2.html')
#单选（radio）
# element=wd.find_element_by_css_selector('#s_radio input[value="小雷老师"]')
# element.click()
# print('当前选中的是: ' + element.get_attribute('value'))
# wd.quit()

#多选（checkbox）
#先把已经选中的选项全部取消
#elements = wd.find_elements_by_css_selector('#s_checkbox input[checked="checked"]')
#for element in elements:
#element.click()
#开始多选
#elements=wd.find_elements_by_css_selector('#s_checkbox input[value="小雷老师"],#s_checkbox input[value="小江老师"]')
#for element in elements:
#element.click()
#打印所选
#for element in elements:
#print('当前选中的是: ' + element.get_attribute('value'))
#wd.quit()

#下拉列表单选（ss_single）
# element=wd.find_element_by_css_selector('#ss_single option[value="小雷老师"]')
# element.click()
# print('当前选中的是: ' + element.get_attribute('value'))
# wd.quit()

#下拉复选框(ss_multi)
from selenium.webdriver.support.ui import Select # 导入Select类
select = Select(wd.find_element_by_id("ss_multi")) # 创建Select对象
select.deselect_all()# 创建Select对象
select.select_by_visible_text("小雷老师")
select.select_by_visible_text("小凯老师")
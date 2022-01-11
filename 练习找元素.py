# -------------------------------
# '.class'
# '#id'
# 'span'或'div'
#'[href*='gov.cn']'      #href中包含的部分单词
# -------------------------------
from selenium import webdriver
wd = webdriver.Edge(r'D:\msedgedriver.exe')
wd.implicitly_wait(5)# 设置最大等待时长为5秒
wd.get('https://cn.bing.com/search?q=%E7%99%BE%E5%BA%A6&cvid=b3917aae501a41d3aa2ebb5e66944dcd&aqs=edge..69i57j0l6.918j0j1&FORM=ANNTA1&PC=NMTS')

elements=wd.find_elements_by_css_selector('#sb_form_q')
for element in elements:             #测试并退出
    print('------------------------')
    print(element.get_attribute('outerHTML'))
elements.send_keys('123\n')
# element = wd.find_elements_by_css_selector('#searchtext')
# element.send_keys('你好')

for element in elements:             #测试并退出
    print('------------------------')
    print(element.get_attribute('outerHTML'))

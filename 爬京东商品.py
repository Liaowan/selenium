from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def spider(url,keywords):
  try:

    wd = webdriver.Edge(r'D:\msedgedriver.exe')
    wd.minimize_window()
    wd.implicitly_wait(5)  # 设置最大等待时长为5秒
    wd.get(url)
    element = wd.find_element_by_id('key')
    element.send_keys(keywords)
    element.send_keys(Keys.ENTER)
    get_goods(wd)
  finally:
    wd.close()

def get_goods(wd):
    goods = wd.find_elements_by_class_name('gl-item')
    sum1 = 0
    for good in goods:
       sum1+=1
       mainWindow = wd.current_window_handle
       p_name = good.find_element_by_class_name('p-name').text.replace("京东超市\n",'')
       p_price = good.find_element_by_css_selector('i').text

       p_comentweb = good.find_element_by_css_selector('.p-commit a')
       p_comentweb.click()
       for handle in wd.window_handles:
           # 先切换到该窗口
           wd.switch_to.window(handle)
           if p_comentweb.get_attribute('href') in wd.title:
               # 如果网址标题有关键词bing，跳出循环
               break
       element=wd.find_element_by_css_selector('.comment-item p')
       p_coment = element.text
       time.sleep(2)
       wd.switch_to.window(mainWindow)
       p_html = good.find_element_by_tag_name('a').get_attribute('href')
       msg = '''
       商品名字：%s
       价格：%s
       评论：%s
       网址：%s
       '''%(p_name,p_price,p_coment,p_html)
       f = open('./文档.text', mode='w', encoding='UTF-8')
       f.write(msg)
    print(sum1)
spider('https://www.jd.com/','口罩')

from selenium import webdriver
import time
def find(keywords):
  try:
    wd = webdriver.Edge(r'D:\msedgedriver.exe')
    wd.minimize_window()
    wd.implicitly_wait(5)  # 设置最大等待时长为5秒
    wd.get('https://kns.cnki.net/KNS8/DefaultResult/Index?dbcode=SCDB&kw=%E5%85%89%E5%9C%BA%E6%B7%B1%E5%BA%A6%E8%8E%B7%E5%8F%96&korder=SU')
    element = wd.find_element_by_class_name('search-input')
    time.sleep(1)
    element.clear()
    element.send_keys(keywords)
    wd.find_element_by_class_name('search-btn').click()
    time.sleep(1)
    mainWindow = wd.current_window_handle
    elements = wd.find_elements_by_class_name('odd')
    for i in elements:
       m = i.find_element_by_css_selector('td.operat > a.downloadlink.icon-download')
       wd.execute_script("arguments[0].click();", m)
       time.sleep(2)
       wd.switch_to.window(mainWindow)
  finally:
       wd.close()
find('光场深度获取')
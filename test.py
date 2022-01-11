from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
profile = webdriver.EdgeProfile()

profile.set_preference("browser.download.folderList", 2)

profile.set_preference("browser.download.manager.showWhenStarting", False)

profile.set_preference("browser.download.dir", 'PATH TO DESKTOP')

profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

driver = webdriver.Edge(Edgefile=profile)

driver.get("Name of web site I'm grabbing from")

driver.find_element_by_xpath("//a[contains(text(), 'DEV.tgz')]").click()
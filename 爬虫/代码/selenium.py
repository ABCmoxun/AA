
#selenium

from selenium import webdriver
import time

driver=webdriver.Chrome()
# brower=webdriver.FireFox()

driver.find_elment_by_id('').send_keys('')

# driver.find_elment_by_classname('').send_keys('')
# driver.find_elment_by_name('').send_keys('')
# driver.find_elment_by_xpath('').send_keys('')
driver.find_elment_by_id('').click()

demo=driver.page_source


time.sleep(5)

driver.quit()
driver.close()

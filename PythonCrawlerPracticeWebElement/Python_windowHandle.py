from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

#
search_windows = driver.current_window_handle

#driver.find_element_by_link_text('更多产品').click()
#driver.find_element_by_link_text("立即注册").click()

#
all_handles = driver.window_handles

for handle in all_handles:
    if handle != search_windows:
        driver.switch_to.window(handle)
        print('now regiester window:')
        #driver.find_element_by_name("account").send_keys('username')
        #driver.find_element_by_name('password').send_keys('password')
        time.sleep(2)


for handle in all_handles:
    if handle == search_windows:
        driver.switch_to.window(handle)
        print('now search window')
        #driver.find_element_by_id('TANGRAM__PSP_2__closeBtn').click()
        driver.find_element_by_id('kw').send_keys('selenium')
        driver.find_element_by_id('su').click()
        time.sleep(2)

driver.quit()

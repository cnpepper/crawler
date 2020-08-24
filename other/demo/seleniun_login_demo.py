from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://xxx.cn/#/")

input_list = driver.find_elements_by_class_name('el-input__inner')
input_list[0].send_keys("")
input_list[1].send_keys("")
input_list[2].send_keys("")

buttons = driver.find_elements_by_tag_name('button')

buttons[1].click()

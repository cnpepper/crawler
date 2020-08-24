from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# https://httpbin.org/headers

# Chrome无GUI模式
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--user-agent=%s' % user_agent)
driver = webdriver.Chrome(chrome_options=chrome_options)
print('程序启动...', end="\n")
first_url = 'https://httpbin.org/headers'
driver.get(first_url)
print(driver.page_source)
driver.close()

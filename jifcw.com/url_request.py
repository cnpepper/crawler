import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Chrome无GUI模式
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
chrome_options.add_argument('--user-agent=%s' % user_agent)
driver = webdriver.Chrome(chrome_options=chrome_options)
print('程序启动...', end="\n")
first_url = 'http://jifcw.com/jn_web_dremis_dev/web_house_dir/Show_GoodsHouse_More.aspx'
driver.get(first_url)
time.sleep(3)
print('打开页面...', end="\n")
content_html = driver.page_source
# 解析所有的项目按钮


def content_parser(html):
    p = re.compile(
        "<a id=\"(ctl00_ContentPlaceHolder2_DataList2_ctl\d+_LinkButton1)\".*?href=\"javascript:__doPostBack\('.*?',''\)\">", re.S)
    return re.findall(p, html)


print('获取按钮列表...', end="\n")
button_list = content_parser(content_html)


def detail_save(num, file_name, content):
    print('保存详情...', end="\n")
    with open('./'+str(num)+'_'+str(file_name)+'.txt', 'w') as f:
        f.write(content)


# 总页数
page_count = 23
for page_no in range(0, page_count):
    print('获取第'+str(page_no)+'页...', end="\n")
    time.sleep(3)
    # len(button_list)
    for index in range(0, len(button_list)):
        # 选取要点击的详情按钮
        button = driver.find_element_by_id(button_list[index])
        button.click()
        time.sleep(3)
        # 保存详情页面
        file_name = button_list[index]
        detail_save(page_no, file_name, driver.page_source)
        # 回退
        time.sleep(1)
        driver.back()
    # 进行下一页
    button_next = driver.find_element_by_link_text('下一页')
    button_next.click()

import os
import pandas as pd
from bs4 import BeautifulSoup

# 扫描目录中的文件
file_list = []
file_dir = './html'
for root, dirs, files in os.walk(file_dir):
    file_list = files


def htm_get(path):
    content = ''
    with open(path) as f:
        content = f.read()
    return content


'''
项目名称 ctl00_ContentPlaceHolder2_lb_item_name
开发商 ctl00_ContentPlaceHolder2_lb_enter_name
项目位置 ctl00_ContentPlaceHolder2_lb_item_seat
建设规模 ctl00_ContentPlaceHolder2_lb_item_area
总面积 ctl00_ContentPlaceHolder2_lb_area
竣工时间 ctl00_ContentPlaceHolder2_lb_item_ew_date
用地规划许可 ctl00_ContentPlaceHolder2_lb_program_pcode
建设施工许可 ctl00_ContentPlaceHolder2_lb_jg
工程规划许可 ctl00_ContentPlaceHolder2_lb_gh
土地使用许可 ctl00_ContentPlaceHolder2_lb_td
售楼电话 ctl00_ContentPlaceHolder2_lb_item_tel
开盘时间 ctl00_ContentPlaceHolder2_lb_item_open_date
绿化率 ctl00_ContentPlaceHolder2_lb_item_green_rate

已售面积 ctl00_ContentPlaceHolder2_Web_recentitem_count1_lb_y_area
已售套数 ctl00_ContentPlaceHolder2_Web_recentitem_count1_lb_y_num
已售价格 ctl00_ContentPlaceHolder2_Web_recentitem_count1_lb_z_price
已售均价 ctl00_ContentPlaceHolder2_Web_recentitem_count1_lb_j_price

可售面积 ctl00_ContentPlaceHolder2_lb_k_area
可售套数 ctl00_ContentPlaceHolder2_lb_k_num
总面积 ctl00_ContentPlaceHolder2_lb_z_area
总套数 ctl00_ContentPlaceHolder2_lb_z_num
已售面积 ctl00_ContentPlaceHolder2_lb_y_area
已售套数 ctl00_ContentPlaceHolder2_lb_y_num
已售价格 ctl00_ContentPlaceHolder2_lb_z_price
已售均价 ctl00_ContentPlaceHolder2_lb_j_price
公交路线 ctl00_ContentPlaceHolder2_lb_environment_over_route
公交站名 ctl00_ContentPlaceHolder2_lb_environment_over_name
教育环境 ctl00_ContentPlaceHolder2_lb_environment_edu
医疗卫生 ctl00_ContentPlaceHolder2_lb_environment_treatment
商业环境 ctl00_ContentPlaceHolder2_lb_environment_business
休闲娱乐 ctl00_ContentPlaceHolder2_lb_environment_amuse
'''


def htm_parser(html):
    soup = BeautifulSoup(html, 'html.parser')
    item_info = []
    # 项目名称 ctl00_ContentPlaceHolder2_lb_item_name
    item_name = soup.find(id="ctl00_ContentPlaceHolder2_lb_item_name")
    item_info.append(item_name.text)
    # 开发商 ctl00_ContentPlaceHolder2_lb_enter_name
    enter_name = soup.find(id="ctl00_ContentPlaceHolder2_lb_enter_name")
    item_info.append(enter_name.text)
    # 项目位置 ctl00_ContentPlaceHolder2_lb_item_seat
    item_seat = soup.find(id="ctl00_ContentPlaceHolder2_lb_item_seat")
    item_info.append(item_seat.text)
    # 建设规模 ctl00_ContentPlaceHolder2_lb_item_area
    item_area = soup.find(id="ctl00_ContentPlaceHolder2_lb_item_area")
    item_info.append(item_area.text)
    # 总面积 ctl00_ContentPlaceHolder2_lb_area
    area = soup.find(id="ctl00_ContentPlaceHolder2_lb_area")
    item_info.append(area.text)
    # 竣工时间 ctl00_ContentPlaceHolder2_lb_item_ew_date
    item_ew_date = soup.find(id="ctl00_ContentPlaceHolder2_lb_item_ew_date")
    item_info.append(item_ew_date.text)

    item_ew_date = soup.find(id="ctl00_ContentPlaceHolder2_lb_program_pcode")
    item_info.append(item_ew_date.text)

    item_ew_date = soup.find(id="ctl00_ContentPlaceHolder2_lb_jg")
    item_info.append(item_ew_date.text)

    item_ew_date = soup.find(id="ctl00_ContentPlaceHolder2_lb_gh")
    item_info.append(item_ew_date.text)

    item_ew_date = soup.find(id="ctl00_ContentPlaceHolder2_lb_td")
    item_info.append(item_ew_date.text)

    item_ew_date = soup.find(id="ctl00_ContentPlaceHolder2_lb_item_tel")
    item_info.append(item_ew_date.text)

    item_ew_date = soup.find(id="ctl00_ContentPlaceHolder2_lb_item_open_date")
    item_info.append(item_ew_date.text)

    # 绿化率 ctl00_ContentPlaceHolder2_lb_item_green_rate
    item_green_rate = soup.find(
        id="ctl00_ContentPlaceHolder2_lb_item_green_rate")
    item_info.append(item_green_rate.text)

    item_ew_date = soup.find(
        id="ctl00_ContentPlaceHolder2_Web_recentitem_count1_lb_y_area")
    item_info.append(item_ew_date.text)

    item_ew_date = soup.find(
        id="ctl00_ContentPlaceHolder2_Web_recentitem_count1_lb_y_num")
    item_info.append(item_ew_date.text)

    item_ew_date = soup.find(
        id="ctl00_ContentPlaceHolder2_Web_recentitem_count1_lb_z_price")
    item_info.append(item_ew_date.text)

    item_ew_date = soup.find(
        id="ctl00_ContentPlaceHolder2_Web_recentitem_count1_lb_j_price")
    item_info.append(item_ew_date.text)

    # 可售面积 ctl00_ContentPlaceHolder2_lb_k_area
    k_area = soup.find(id="ctl00_ContentPlaceHolder2_lb_k_area")
    item_info.append(k_area.text)
    # 可售套数 ctl00_ContentPlaceHolder2_lb_k_num
    k_num = soup.find(id="ctl00_ContentPlaceHolder2_lb_k_num")
    item_info.append(k_num.text)

    k_num = soup.find(id="ctl00_ContentPlaceHolder2_lb_z_area")
    item_info.append(k_num.text)

    k_num = soup.find(id="ctl00_ContentPlaceHolder2_lb_z_num")
    item_info.append(k_num.text)

    k_num = soup.find(id="ctl00_ContentPlaceHolder2_lb_y_area")
    item_info.append(k_num.text)

    k_num = soup.find(id="ctl00_ContentPlaceHolder2_lb_y_num")
    item_info.append(k_num.text)

    k_num = soup.find(id="ctl00_ContentPlaceHolder2_lb_z_price")
    item_info.append(k_num.text)

    k_num = soup.find(id="ctl00_ContentPlaceHolder2_lb_j_price")
    item_info.append(k_num.text)

    k_num = soup.find(id="ctl00_ContentPlaceHolder2_lb_environment_over_route")
    item_info.append(k_num.text)

    k_num = soup.find(id="ctl00_ContentPlaceHolder2_lb_environment_over_name")
    item_info.append(k_num.text)

    k_num = soup.find(id="ctl00_ContentPlaceHolder2_lb_environment_edu")
    item_info.append(k_num.text)

    k_num = soup.find(id="ctl00_ContentPlaceHolder2_lb_environment_treatment")
    item_info.append(k_num.text)

    k_num = soup.find(id="ctl00_ContentPlaceHolder2_lb_environment_business")
    item_info.append(k_num.text)

    k_num = soup.find(id="ctl00_ContentPlaceHolder2_lb_environment_amuse")
    item_info.append(k_num.text)

    return item_info


# df.to_csv('my_csv.csv', mode='a', header=False)
result = []
for name in file_list:
    # 打开文件读取页面
    html = htm_get('./html/'+str(name))
    # 解析html页面
    result.append(htm_parser(html))
    # 保存到csv文件

header_name = ['项目名称', '开发商', '项目位置', '建设规模', '总面积', '竣工时间', '用地规划许可', '建设施工许可', '工程规划许可', '土地使用许可', '售楼电话', '开盘时间', '绿化率',
               '已售面积', '已售套数', '已售价格', '已售均价',
               '可售面积', '可售套数', '总面积', '总套数', '已售面积', '已售套数', '已售价格', '已售均价', '公交路线', '公交站名', '教育环境', '医疗卫生', '商业环境', '休闲娱乐'
               ]

df = pd.DataFrame(result, columns=header_name)
df.to_csv('./data.csv')

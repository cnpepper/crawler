from bs4 import BeautifulSoup
import pandas as pd


def parser_html(num):
    with open("./ctl00_ContentPlaceHolder2_DataList2_ctl"+str(num).zfill(2)+"_LinkButton1", "r") as f:
        html = f.read()

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
    # 绿化率 ctl00_ContentPlaceHolder2_lb_item_green_rate
    item_green_rate = soup.find(
        id="ctl00_ContentPlaceHolder2_lb_item_green_rate")
    item_info.append(item_green_rate.text)
    # 可售面积 ctl00_ContentPlaceHolder2_lb_k_area
    k_area = soup.find(id="ctl00_ContentPlaceHolder2_lb_k_area")
    item_info.append(k_area.text)
    # 可售套数 ctl00_ContentPlaceHolder2_lb_k_num
    k_num = soup.find(id="ctl00_ContentPlaceHolder2_lb_k_num")
    item_info.append(k_num.text)
    # 已售套数 ctl00_ContentPlaceHolder2_lb_y_num
    y_num = soup.find(id="ctl00_ContentPlaceHolder2_lb_y_num")
    item_info.append(y_num.text)
    # 已售均价 ctl00_ContentPlaceHolder2_lb_j_price
    j_price = soup.find(id="ctl00_ContentPlaceHolder2_lb_j_price")
    item_info.append(j_price.text)
    return item_info


all_list = []
for index in range(0, 20):
    res = parser_html(index)
    all_list.append(res)

print(all_list)
df = pd.DataFrame(all_list)

df.to_csv("./1.csv")

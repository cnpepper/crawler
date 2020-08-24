import requests
import re


def request_dandan():
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-1'
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:79.0) Gecko/20100101 Firefox/79.0"
    }
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            return res.text
    except requests.RequestException:
        return None


html = request_dandan()
print(html)
pattern = re.compile(
    '<li.*?list_num.*?(\d+).</div>.*?title="(.*?)">.*?price_r">(.*?)</span>', re.S)

items = re.findall(pattern, html)
print(items)

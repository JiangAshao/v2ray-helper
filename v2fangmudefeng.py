import requests
import json
import time
import random

# 加入随机延时
time.sleep(random.randint(1,30))

fromdata = {}
if fromdata == {}:
    fromdata['email'], fromdata["passwd"], sckey = input().strip().split(",")

# 微信推送
def send_wechat(content):
    # title and content must be string.
    title = "v2流量签到通知"                                   
    url = 'https://sc.ftqq.com/' + sckey + '.send'
    data = {'text':title,'desp':content}
    result = requests.post(url,data)
    return(result) 

def main():
    headers = {
        'authority': 'www.youneed.win',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        'sec-ch-ua-platform': '"macOS"',
        'origin': 'https://www.youneed.win',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.youneed.win/free-v2ray',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cookie': 'gothamadblock_last_visit_time=1'
    }
    url = f'https://www.youneed.win/wp-admin/admin-ajax.php'
    try:
        r0 = requests.post(url, headers=headers, timeout=15)
    except requests.exceptions.RequestException as e:
        print(e)
        print("请求异常" + e)
        return
    if r0.status_code == 200:
        t = json.loads(r0.text)
        print(f"返回:{t['success']}")
    else:
        print(r0.text)
        print("获取失败")


if __name__ == "__main__":
    main()

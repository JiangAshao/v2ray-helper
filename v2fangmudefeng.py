import requests
import json
import time
import random
from bs4 import BeautifulSoup
import sys
sys.setrecursionlimit(3000)
import os
# 加入随机延时
# time.sleep(random.randint(1,30))

# 钉钉机器人
if os.environ['DD_BOT_TOKEN'] != "":
  DD_BOT_TOKEN = os.environ['DD_BOT_TOKEN']
if os.environ['DD_BOT_SECRET'] != "":
  DD_BOT_SECRET = os.environ['DD_BOT_SECRET']

# 钉钉推送
def dingNotify(self, text):
    if DD_BOT_TOKEN != '':
        url = 'https://oapi.dingtalk.com/robot/send?access_token=' + DD_BOT_TOKEN
        data = {
            "msgtype": "text",
            "text": {
                'content': text
            }
        }
        headers = {
            'Content-Type': 'application/json;charset=utf-8'
        }
        if DD_BOT_SECRET != '':
            timestamp = str(round(time.time() * 1000))
            secret = DD_BOT_SECRET
            secret_enc = secret.encode('utf-8')
            string_to_sign = '{}\n{}'.format(timestamp, secret)
            string_to_sign_enc = string_to_sign.encode('utf-8')
            hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
            sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
            url = 'https://oapi.dingtalk.com/robot/send?access_token=' + DD_BOT_TOKEN + '&timestamp=' + timestamp + '&sign=' + sign
        response = requests.post(url=url, data=json.dumps(data), headers=headers).text
        if json.loads(response)['errcode'] == 0:
            print('\n钉钉发送通知消息成功\n')
        else:
            print('\n钉钉发送通知失败！！\n')
    else:
        print('\n您未提供钉钉的有关数据，取消钉钉推送消息通知\n')
        pass

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
    data = {
            "action": "validate_input",
            "nonce": "ca7eb6eec1",
            "captcha": "success",
            "post_id": "563",
            "type": "captcha",
            "protection": ""
        }
    try:
        r0 = requests.post(url, data, headers=headers)
    except requests.exceptions.RequestException as e:
        print(e)
        print("请求异常" + e)
        return
    if r0.status_code == 200:
        t = json.loads(r0.text)
        print(f"返回:{t['success']}")
        content = t['content']
        soup = BeautifulSoup(content, 'html.parser')  # 将读取到的网页代码用指定解析器html.parser进行解析
        v2ray = soup.find_all("td", class_="v2ray", limit=10)
        for v2 in v2ray:
          data_raw = v2.find('a')["data-raw"]
          dingNotify(data_raw.replace('\\',''),"\n")
    else:
        print(r0.text)
        print("获取失败")


if __name__ == "__main__":
    main()

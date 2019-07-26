#!/usr/bin/python
#-*- coding:utf8 -*-

import json
#import urllib.request
import requests
import sys

def dingT(text):
    url="https://oapi.dingtalk.com/robot/send?access_token=3bd088169244a56f55cd3e24287cf1b3fb245a770028d14a2544f906a33dc6b4"
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    data = {
        "msgtype": "text",
        "text": {
            "content": text
        },
        "at": {
             "isAtAll": True
            #"atMobiles":"13515961024"
        }
    }
    sendData = json.dumps(data)
    sendData = sendData.encode("utf-8")
    request = requests.post(url=url,data=sendData,headers=header)
    print(request.text)
if __name__ == "__main__":
    dingT(sys.argv[1])

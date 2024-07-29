# -*- encoding: utf-8 -*-
# https://market.aliyun.com/apimarket/detail/cmapi00035384?spm=5176.730005.result.32.1e6c3524ufvtzf

# AK: 24842496
# AS: e0b6809ebfa6574ad8a4d5d4a97bd2c2
# AC: 141c262e8ed64fe9abeda7a4de1ece30

import requests
import json

# url = "https://iweather.market.alicloudapi.com/address?needday=1&prov=浙江&city=杭州&area=西湖"
url = "https://iweather.market.alicloudapi.com/address?needday=1&prov=浙江&city=杭州"

payload = {}
headers = {
  'Authorization': 'APPCODE 141c262e8ed64fe9abeda7a4de1ece3'
}

response = requests.request("GET", url, headers=headers, data=payload)

weather_content = response.text.encode('utf-8').decode('unicode_escape')

weather_json = json.loads(weather_content)

now_detail = weather_json['data']['now']['detail']

# print("当前日期: ", now_detail['date'])
# print("当前时间: ", now_detail['time'])
# print("当前天气: ", now_detail['weather'])
# print("当前温度: ", now_detail['temperature'])
# print("当前湿度: ", now_detail['humidity'])
# print("当前风向：", now_detail['wind_direction'])
# print("当前风速: ", now_detail['wind_speed'])

# 将上面的数据整合到一起

weather = (now_detail['date'] + " " + now_detail['time'] + "，天气：" + now_detail['weather'] + " ，温度：" + now_detail['temperature']
           + " ，湿度：" + now_detail['humidity'] + " ，风向：" + now_detail['wind_direction'] + " ，风速：" + now_detail['wind_speed'])
print(weather)



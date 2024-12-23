from mocked_information import *
def get_destination_recommendation(query):
    return destination
def get_attraction_recommendation(city):
    return attraction
def get_dining_recommendation(city):
    return dining
def get_life_tips(city):
    return life_tips
def get_local_customs(city):
    return local_customs
def get_current_date():
    return "今天"
def get_weather(location, date=""):
    if date == "":
        date = get_current_date()
    weathers = [
         '雨',
         '阴',
         '阴转多云',
         '晴转多云',
         '晴'
        ]
    # 随机选择一个天气
    # 使用随机数
    import random
    weather = random.choice(weathers)
    return date + "日，天气是 " + weather
    # return date + "日，天气是 " + "晴天"
def get_current_location():
    return "北京"
def get_path_recommendation(destination, start='', recommendation=False):
    return "建议通过飞机从" + start + "到" + destination + "\n以下是航班信息\n" + flight

def get_weather_by_city(location,date=""):
    import requests
    import json

    url = f"https://iweather.market.alicloudapi.com/address?needday=1&prov=浙江&city={location}"

    payload = {}
    headers = {
        'Authorization': 'APPCODE 141c262e8ed64fe9abeda7a4de1ece30'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    weather_content = response.text.encode('utf-8').decode('unicode_escape')

    weather_json = json.loads(weather_content)

    now_detail = weather_json['data']['now']['detail']

    # 将上面的数据整合到一起

    weather = (now_detail['date'] + " " + now_detail['time'] + "，天气：" + now_detail['weather'] + " ，温度：" +
               now_detail['temperature']
               + " ，湿度：" + now_detail['humidity'] + " ，风向：" + now_detail['wind_direction'] + " ，风速：" + now_detail[
                   'wind_speed'])
    return weather

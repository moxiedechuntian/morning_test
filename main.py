from datetime import date, datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random

today = datetime.now()
start_date = os.environ['START_DATE']

city_cq = os.environ['CITY_cq']
city_xa = os.environ['CITY_xa']
city_bj = os.environ['CITY_bj']

birthday_wkh = os.environ['BIRTHDAY_wkh']
birthday_mqy = os.environ['BIRTHDAY_mqy']
birthday_lcj = os.environ['BIRTHDAY_lcj']
birthday_zhy = os.environ['BIRTHDAY_zhy']
birthday_zzy = os.environ['BIRTHDAY_zzy']
birthday_ty = os.environ['BIRTHDAY_ty']
birthday_jj = os.environ['BIRTHDAY_jj']

app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

user_id_test = os.environ["USER_ID_test"]
# user_id_wkh = os.environ["USER_ID_wkh"]
# user_id_mqy = os.environ["USER_ID_mqy"]
# user_id_lcj = os.environ["USER_ID_lcj"]
# user_id_zhy = os.environ["USER_ID_zhy"]
# user_id_zzy = os.environ["USER_ID_zzy"]
# user_id_ty = os.environ["USER_ID_ty"]
# user_id_jj = os.environ["USER_ID_jj"]

template_id = os.environ["TEMPLATE_ID"]


def get_weather_cq():
  url_cq = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city_cq
  res_cq = requests.get(url_cq).json()
  weather_cq = res_cq['data']['list'][0]
  return weather_cq['weather'], math.floor(weather_cq['temp'])

def get_weather_xa():
  url_xa = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city_xa
  res_xa = requests.get(url_xa).json()
  weather_xa = res_xa['data']['list'][0]
  return weather_xa['weather'], math.floor(weather_xa['temp'])

def get_weather_bj():
  url_bj = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city_bj
  res_bj = requests.get(url_bj).json()
  weather_bj = res_bj['data']['list'][0]
  return weather_bj['weather'], math.floor(weather_bj['temp'])


def get_count():
  delta = today - datetime.strptime(start_date, "%Y-%m-%d")
  return delta.days

def get_birthday_wkh():
  next_wkh = datetime.strptime(str(date.today().year) + "-" + birthday_wkh, "%Y-%m-%d")
  if next_wkh < datetime.now():
    next_wkh = next_wkh.replace(year=next_wkh.year + 1)
  return (next_wkh - today).days

def get_birthday_mqy():
  next_mqy = datetime.strptime(str(date.today().year) + "-" + birthday_mqy, "%Y-%m-%d")
  if next_mqy < datetime.now():
    next_mqy = next_mqy.replace(year=next_mqy.year + 1)
  return (next_mqy - today).days

def get_birthday_lcj():
  next_lcj = datetime.strptime(str(date.today().year) + "-" + birthday_lcj, "%Y-%m-%d")
  if next_lcj < datetime.now():
    next_lcj = next_lcj.replace(year=next_lcj.year + 1)
  return (next_lcj - today).days

def get_birthday_zhy():
  next_zhy = datetime.strptime(str(date.today().year) + "-" + birthday_zhy, "%Y-%m-%d")
  if next_zhy < datetime.now():
    next_zhy = next_zhy.replace(year=next_zhy.year + 1)
  return (next_zhy - today).days

def get_birthday_zzy():
  next_zzy = datetime.strptime(str(date.today().year) + "-" + birthday_zzy, "%Y-%m-%d")
  if next_zzy < datetime.now():
    next_zzy = next_zzy.replace(year=next_zzy.year + 1)
  return (next_zzy - today).days

def get_birthday_ty():
  next_ty = datetime.strptime(str(date.today().year) + "-" + birthday_ty, "%Y-%m-%d")
  if next_ty < datetime.now():
    next_ty = next_ty.replace(year=next_ty.year + 1)
  return (next_ty - today).days

def get_birthday_jj():
  next_jj = datetime.strptime(str(date.today().year) + "-" + birthday_jj, "%Y-%m-%d")
  if next_jj < datetime.now():
    next_jj = next_jj.replace(year=next_jj.year + 1)
  return (next_jj - today).days

def get_words():
  words = requests.get("https://api.shadiao.pro/chp")
  if words.status_code != 200:
    return get_words()
  return words.json()['data']['text']

def get_random_color():
  return "#%06x" % random.randint(0, 0xFFFFFF)


client = WeChatClient(app_id, app_secret)

wm = WeChatMessage(client)

wea_cq, temperature_cq = get_weather_cq()
wea_xa, temperature_xa = get_weather_xa()
wea_bj, temperature_bj = get_weather_bj()

data = {"weather_cq":{"value":wea_cq},"temperature_cq":{"value":temperature_cq},
        "weather_xa":{"value":wea_xa},"temperature_xa":{"value":temperature_xa},
        "weather_bj":{"value":wea_bj},"temperature_bj":{"value":temperature_bj},
        "love_days":{"value":get_count()},
        "birthday_left_wkh":{"value":get_birthday_wkh()},
        "birthday_left_mqy":{"value":get_birthday_mqy()},
        "birthday_left_lcj":{"value":get_birthday_lcj()},
        "birthday_left_zhy":{"value":get_birthday_zhy()},
        "birthday_left_zzy":{"value":get_birthday_zzy()},
        "birthday_left_ty":{"value":get_birthday_ty()},
        "birthday_left_jj":{"value":get_birthday_jj()},
        "words":{"value":get_words(), "color":get_random_color()}}

# name=['user_id_test','user_id_wkh','user_id_mqy','user_id_lcj','user_id_zhy','user_id_zzy','user_id_ty','user_id_jj']
# for i in name:
res = wm.send_template(user_id_test, template_id, data)
print(res)

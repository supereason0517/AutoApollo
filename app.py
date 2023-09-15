from playwright.sync_api import Playwright, sync_playwright, expect
from datetime import datetime
import pandas as pd
import requests
import config
import time


def GetNowTime():
    nowtime = time.time()
    struct_time = time.localtime(nowtime)  # 轉成時間元組
    timeString = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)  # 轉成字串
    return timeString


token = config.Line
LoginMessage = GetNowTime()+"Login CloudRiches-Apollo"
CheckMessage = GetNowTime()+"Apollo Checked"
DayOffMessage = GetNowTime()+"Day Off"
FailedMessage = GetNowTime()+"失敗了R,手動吧老哥"


def CheckHoliday():
  df = pd.read_csv('date.csv')
  today = int(datetime.strftime(datetime.today(),'%Y%m%d'))
  date = df[df['西元日期'] == today]["是否放假"].values[0]
  if date == 0:
    print('平日')
    return True
  else:
    print('好耶放假')
    return False
  
def gettime():
    nowtime = datetime.now()
    print(nowtime.hour)
    if nowtime.hour < 10:
        print('on duty')
        return "上班"
    else:
        print('clock out')
        return "下班"

def LineNotifly(message):
    headers = { "Authorization": "Bearer " + token}
    data = { "message": message }
    requests.post("https://notify-api.line.me/api/notify",
        headers = headers, data = data)

def LineNotifyImage():
    headers = { "Authorization": "Bearer " + token}
    data = {'message':'照片來啦！'}     # 設定 LINE Notify message ( 不可少 )
    image = open('screenshot.png', 'rb')    # 以二進位方式開啟圖片
    imageFile = {'imageFile' : image}
    requests.post("https://notify-api.line.me/api/notify",
        headers = headers,data = data,files=imageFile)

def check():
    try:
        if CheckHoliday():
            LineNotifly(LoginMessage)
            with sync_playwright() as playwright:
                run(playwright)
            LineNotifly(CheckMessage)
            LineNotifyImage()
        else:
            print('dayoff')
            LineNotifly(DayOffMessage)
    except:
        print('Mission failed')
        LineNotifly(FailedMessage)


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://asiaauth.mayohr.com/HRM/Account/Login")
    page.get_by_placeholder("公司代碼").fill("cloudriches")
    page.get_by_placeholder("工號").fill(config.User)
    page.get_by_placeholder("請輸入您的密碼").fill(config.Password)
    page.get_by_role("button", name="登入").click()
    page.get_by_role("link", name="我要打卡").click()
    time.sleep(5)
    page.get_by_role("button", name=gettime()).click()
    time.sleep(5)
    page.goto("https://apollo.mayohr.com/ta/personal/checkin/checkinrecords/workrecords")
    time.sleep(5)
    page.screenshot(path="screenshot.png")


    # ---------------------
    context.close()
    browser.close()

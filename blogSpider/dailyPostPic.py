#! python3
from base64 import b64encode
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json
import datetime

def autoPost():
    with open('./data.json') as f:
        data = json.load(f)
        gID = data["groupID"]
        access_token = data["at"]
        paletteUrl = data["designseedUrl"]
        imageUrl = "https://www.design-seeds.com/wp-content/uploads/2015/09/LandingPage7.png"
        with open('./url.json') as u:
                urldata = json.load(u)
                imageUrl = urldata["url"]

                now = datetime.datetime.now()
                photoCaps = f"""🙌{now.month}/{now.day} 打卡區🙌「今天我也有做事喔！」

當天有小創作的，或是只是想分享一下創作進度的都可以在這裡打卡！

不知道該創作什麼的可以以 design seed 當日色票或照片為靈感

{paletteUrl}

防長草用，閒聊也歡迎！

🍅一起蕃茄鐘🍅利用方式請看公告

https://www.roundee.io/pomodorobuddy

歡迎留言預計利用時段揪伴！"""

                postPhotoUrl = f"https://graph.facebook.com/{gID}/photos"
        
                curlParam = urlencode(
                        dict(
                                url=imageUrl,
                                caption=photoCaps,
                                access_token=access_token)
                ).encode('utf-8')
                response = urlopen(Request(postPhotoUrl, curlParam))
                
                print(response.info())
                print(response.read().decode())
autoPost()
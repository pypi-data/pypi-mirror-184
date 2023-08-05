'''
Name: Code.
Author: Monarchdos
Date: 2022-12-27
'''
from nonebot import on_command
from nonebot.plugin import on_regex
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, Message, MessageSegment, GroupMessageEvent
from nonebot.plugin import PluginMetadata
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests
import random
import json
__plugin_meta__ = PluginMetadata(
    name = "云签到",
    description = "云端签到积分系统",
    usage = "发送'功能'查看",
)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
url = "https://cloudsign.ayfre.com/"
def get_at(data: str) -> list:
    qq_list = []
    data = json.loads(data)
    try:
        for msg in data['message']:
            if msg['type'] == 'at':
                qq_list.append(int(msg['data']['qq']))
        return qq_list
    except Exception:
        return []

qd = on_regex("^签到$|^积分$|^挖矿$|^我的背包$|^钓鱼$|^我的鱼篓$|^功能$|^领取积分补助$|^机器人状态$|^排行榜$|^(抽奖) (\d+)$|^(转账) (\d+)$")
@qd.handle()
async def qd_(bot: Bot, event: GroupMessageEvent):
    s = str(event.get_message()).strip()
    username = str(event.sender.nickname)
    try:
        ats = get_at(event.json())[0]
    except Exception:
        ats = event.user_id
    
    data = {
        "command": s,
        "at": ats,
        "qq": event.user_id,
        "qun": event.group_id,
        "botqq": event.self_id,
        "platform": "qq"
    }
    if event.user_id != "80000000": 
        res = "\n" + str(requests.post(url=url, data=data, verify=False).text)
        await qd.send(message=Message(res), at_sender=True)
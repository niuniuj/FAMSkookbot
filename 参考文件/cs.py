# home.py
# py模块
from khl import Bot, Message,MessageTypes ## kook机器人(khl.py)模块
from khl.card import Card, CardMessage, Module, Types, Element, Struct ##kook卡片(khl.py)模块
from khl import EventTypes, Event ##kook监听(khl.py)模块
import json ##json文件模块
import aiohttp
import asyncio

# 导入支线文件
import 参考文件.comm as comm

# kook机器人连接
## 读取json文件
with open('config.json') as f:
    data = json.load(f)
## 获取token值
token = data['token']
## 创建机器人实例
bot = Bot(token=token)

async def create_game():
    url="https://www.kookapp.cn/api/v3/game/create"
    headers={f'Authorization': f"Bot {botoken}"}
    params = {
  "s": 0,
  "d": {
    "channel_type": "GROUP",
    "type": 255,
    "target_id": "xxx",
    "author_id": "1",
    "content": "[系统消息]",
    "extra": {
      "type": "added_role",
      "body": {
        "role_id": 11111,
        "name": "新角色",
        "color": 0,
        "position": 5,
        "hoist": 0,
        "mentionable": 0,
        "permissions": 142924296
      }
    },
    "msg_id": "c804a6a6-xxxx-e041ec3bb887",
    "msg_timestamp": 1613998615411,
    "nonce": "",
    "verify_token": "xxxx"
  },
  "sn": 186
}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=params,headers=headers) as response:
                ret =json.loads(await response.text())
                print(ret)

# 这样编写是因为我们直接调用了一个async函数
# 如果是在async函数中，直接await create_game()调用即可。
loop = asyncio.get_event_loop()
tasks = [create_game(), ]
loop.run_until_complete(asyncio.wait(tasks))

print("bot已启动")
# 机器人运行
if __name__ == '__main__':
    bot.run()
    
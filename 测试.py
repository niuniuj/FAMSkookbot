# py模块
from khl import Bot, Message,MessageTypes ## kook机器人(khl.py)模块
from khl.card import Card, CardMessage, Module, Types, Element, Struct ##kook卡片(khl.py)模块
from khl import EventTypes, Event ##kook监听(khl.py)模块
import requests,json##json文件模块

# kook机器人连接
## 读取json文件
with open('key.json') as f:
    data = json.load(f)
## 获取token值
token = data['token']
## 创建机器人实例
bot = Bot(token=token)

@bot.command(name='ping')
async def bot_ping(msg:Message):
    # 方法1，都使用ID
    guild = await bot.client.fetch_guild("83594105")
    await guild.grant_role("3503751958","30807834") # 第二个参数是角色id
    # 方法2，使用用户ID
    guild = await bot.client.fetch_guild("83594105")
    guild_user = await guild.fetch_user("3503751958")
    await guild.grant_role(guild_user,30807834) # 第二个参数是角色id




# 程序运行
if __name__ == "__main__":
    bot.run() ## khl.py机器人运行

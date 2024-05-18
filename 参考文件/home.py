# home.py
# py模块
from khl import Bot, Message,MessageTypes ## kook机器人(khl.py)模块
from khl.card import Card, CardMessage, Module, Types, Element, Struct ##kook卡片(khl.py)模块
from khl import EventTypes, Event ##kook监听(khl.py)模块
import json ##json文件模块

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

# help插件运行
@bot.on_startup
async def bot_init(bot: Bot):
	comm.init(bot)
     
# 主botping运行
@bot.on_startup
async def bot_init(bot: Bot):
	init(bot)

# 主botping函数执行
def init(bot:Bot):
    @bot.command(name="ping")
    async def world_cmd(msg: Message):
        await ping(msg)
      
# ping
async def ping(msg:Message):
    ch = await bot.client.fetch_public_channel("1038117411797245") ### 指定频道收取发送

    ping_back = [
         {
    "type": "card",
    "theme": "secondary",
    "size": "lg",
    "modules": [
      {
        "type": "header",
        "text": {
          "type": "plain-text",
          "content": "调试返回"
        }
      },
      {
        "type": "section",
        "text": {
          "type": "plain-text",
          "content": "返回值：pong!!"
        }
      },
      {
        "type": "divider"
      },
      {
        "type": "context",
        "elements": [
          {
            "type": "image",
            "src": "https://i.mcmod.cn/play/favicon/20187418.png?r=JnEv"
          },
          {
            "type": "plain-text",
            "content": "FAMS"
          }
        ]
      }
    ]
  }
  ]
    await msg.reply(ping_back,type=MessageTypes.CARD) ### 发送ping返回卡片

print("bot已启动")
# 机器人运行
if __name__ == '__main__':
    bot.run()
    
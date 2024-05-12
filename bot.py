# 注释解释
### #为板块名称 ##为代码解释 ##/为代码解释大纲 ###为其他类型解释
### 编写解释时请在#后加上空格，建议给每个模块、代码体加上解释，以便后续或其他人编辑

# 模块
import os ## 文件模块
import datetime ## 时间模块
## khl.py模块
from khl import Bot, Message,MessageTypes ## 主模块
from khl.card import Card, CardMessage, Module, Types, Element, Struct ## 卡片=模块
from khl import EventTypes, Event ## 监听模块
import json ##json文件模块

# 日志模块(def)
## 获取当前时间
current_time = datetime.datetime.now()
## 格式化时间为 "年-月-日-时-分"
time_str = current_time.strftime("%Y-%m-%d-%H-%M")
## 创建文件夹名
folder_name = f"{time_str}_logs"
## 初始化logs变量
logs = 0
    
## 检查logs文件夹是否存在
if not os.path.exists("logs"):
# 如果不存在，则创建logs文件夹
    os.makedirs("logs")
    logs = "false"
    
## 在logs文件夹中创建以当前时间命名的.txt文件
file_name = os.path.join("logs", f"{time_str}.txt")
with open(file_name, "a",encoding="utf-8") as f:
    ## logs文件夹是否存在日志写入
    if logs == "false":
        f.write("[日志]未检测到日志文件夹，已自动创建日志文件夹\n")
    ## 写入日志文本
    f.write("[日志]创建日志成功\n")

# kook机器人连接
## 读取key.josn文件的token
with open('key.json') as f:
    token = json.load(f)
## 获取token值
token = token['token']
## 创建机器人实例
bot = Bot(token=token)

##/ 编写日志
with open(file_name, "a",encoding="utf-8") as f:
    ##/ 日志正文
    f.write("[bot]token：\n".format(token))
    f.write("[bot]实例创建成功\n")

# 主程序ping
@bot.command(name='ping')
async def bot_ping(msg:Message):
    with open(file_name, "a",encoding="utf-8") as f:
        f.write("[bot]用户发送了ping指令\n")
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
    await msg.reply(ping_back,type=MessageTypes.CARD) ## 发送卡片
    with open(file_name, "a",encoding="utf-8") as f:
        f.write("[bot]返回ping\n")
    


# 程序运行
if __name__ == "__main__":
    bot.run() ## khl.py机器人运行

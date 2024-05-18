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

# 程序函数注册
def init(bot:Bot):
    ##/ 获取logs文件名
    with open('logs/logs.txt', 'r', encoding='utf-8') as file:
        file_name = file.read()
    with open(file_name, "a",encoding="utf-8") as f:
        f.write("[menu]读取txt目录：{}\n".format(file_name))

# 程序ping
    @bot.command(name='menu-ping')
    async def menu_ping(msg:Message):
        with open(file_name, "a",encoding="utf-8") as f:
            f.write("[menu]用户发送了ping指令\n")
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
            "content": "[menu]调试返回"
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
            f.write("[menu]返回ping\n")
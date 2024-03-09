# py模块
from khl import Bot, Message,MessageTypes ## kook机器人(khl.py)模块
from khl.card import Card, CardMessage, Module, Types, Element, Struct ##kook卡片(khl.py)模块
from khl import EventTypes, Event ##kook监听(khl.py)模块
import json ##json文件模块

# kook机器人连接
## 读取json文件
with open('config.json') as f:
    data = json.load(f)
## 获取token值
token = data['token']
## 创建机器人实例
bot = Bot(token=token)

#指令操作
##菜单
@bot.command(name='help',aliases=['comm','帮助'],prefixes=['/',''])
async def help_comm(msg: Message):
    await help(msg)
##ping
@bot.command(name='ping')
async def ping_comm(msg: Message):
    await ping(msg)
##help-ping
@bot.command(name='plugins-help-ping')
async def help_ping_comm(msg: Message):
    await helpping(msg)


@bot.on_event(EventTypes.MESSAGE_BTN_CLICK)
async def btn_click_event(b: Bot, e: Event):
    print(e.target_id)
    print(e.body,"\n")
    value = e.body['value']
    print(value)
    
    if value == 'ping':
        print("ping执行")
        async def help_comm(msg: Message):
            await ping_help(msg)


# help
async def help(msg: Message):
    ch = await bot.client.fetch_public_channel("1038117411797245") ### 指定频道收取发送
    help_card_1 = Card(
    Module.Header("欢迎来到FAMS服务器！"),
    color='#DC143C'
    ) ### 标题卡片
    help_card_1.append(Module.Divider()) ### help_card_1分隔符

    help_card_2 = Card(
    Module.Header("指令菜单|command"), ### 文本显示
    Module.ActionGroup(Element.Button("ping",value='ping',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO)), ### 执行主文件ping指令
    color='#00FFFF' ### 卡片边颜色
    )

    help_card_3 = Card(
    Module.Header("常用链接|URL"), 
    Module.ActionGroup(Element.Button("帮助开发机器人",value='https://github.com/niuniuj/FAMSkookbot',click=Types.Click.LINK,theme=Types.Theme.SECONDARY)), 
    color='#00FFFF'
    )
    ### 发送卡片
    await msg.reply(CardMessage(help_card_1,help_card_2,help_card_3),use_quote=False)

#help-ping
async def helpping(msg: Message):
    ch = await bot.client.fetch_public_channel("1038117411797245") ### 指定频道收取发送
    
    ping_help_back = [
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
          "content": "ping指令：/plugins help ping"
        }
      },
      {
        "type": "section",
        "text": {
          "type": "plain-text",
          "content": "插件名称：help"
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
    ### ping返回卡片
    await msg.reply(ping_help_back,type=MessageTypes.CARD,use_quote=False)


#ping-help-comm
async def ping_help(msg: Message):
    ping_help_card_1 = Card(
    Module.Header("ping指令"),
    color='#DC143C'
    ) ### 标题卡片

    ping_help_card_2 = Card(
    Module.Header("指令菜单|command"), ### 文本显示
    Module.Section("机器人ping|/ping"),
    Module.Section("插件ping|plugins [插件名称] ping"),
    color='#00FFFF' ### 卡片边颜色
    )### 执行主文件ping指令
            
    ### 发送卡片
    await msg.reply(CardMessage(ping_help_card_1,ping_help_card_2),use_quote=False)


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
    await msg.reply(ping_back,type=MessageTypes.CARD,use_quote=False) ### 发送ping返回卡片


# 机器人运行
if __name__ == '__main__':
    bot.run()
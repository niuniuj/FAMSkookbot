# py模块
from khl import Bot, Message,MessageTypes ## kook机器人(khl.py)模块
from khl.card import Card, CardMessage, Module, Types, Element, Struct ##kook卡片(khl.py)模块
from khl import EventTypes, Event ##kook监听(khl.py)模块
import json ##json文件模块

#kook机器人连接
## 读取json文件
with open('config.json') as f:
    data = json.load(f)
## 获取token值
token = data['token']
## 创建机器人实例
bot = Bot(token=token)

#条件激活指令模块
##菜单
@bot.command(name="help",aliases=['指令'])
async def help(msg:Message):
    help_card_1 = Card(
        Module.Header("欢迎来到FAMS服务器！"),
        color='#DC143C') ### 标题卡片
    help_card_1.append(Module.Divider()) ### help_card_1分隔符

    help_card_2 = Card(
        Module.Section("快捷指令"), 
        Module.ActionGroup(Element.Button("帮助开发机器人",value='https://khl-py.eu.org/',click=Types.Click.LINK,theme=Types.Theme.SECONDARY)), 
        color='#0000FF'
        )
    
    help_card_3 = Card(
        Module.ActionGroup(
            Element.Button("按钮文字1",value='按钮值1',click=Types.Click.RETURN_VAL,theme=Types.Theme.INFO),
            Element.Button("按钮文字2",value='按钮值2',click=Types.Click.RETURN_VAL,theme=Types.Theme.DANGER),
            Element.Button("按钮文字3",value='https://khl-py.eu.org/',click=Types.Click.LINK,theme=Types.Theme.SECONDARY)
        )
    ) ### 在这里补充卡片消息的内容（空卡片消息无法发送）
    ### 发送卡片
    await msg.reply(CardMessage(help_card_1,help_card_2))

##ping
@bot.command(name="ping") 
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
]### ping返回卡片
    await msg.reply(ping_back,type=MessageTypes.CARD) ### 发送ping返回卡片

## 菜单-ping按钮执行
@bot.on_event(EventTypes.MESSAGE_BTN_CLICK)
async def btn_click_event(b:Bot,e:Event):
    """按钮点击事件"""
    print(e.target_id)
    print(e.body,"\n")


# 机器人运行
if __name__ == '__main__':
    bot.run()

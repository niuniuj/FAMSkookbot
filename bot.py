# 注释解释
### #为板块名称 ##为代码解释 ###为其他类型解释
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
def create_logs_folder():
    ## 获取当前时间
    current_time = datetime.datetime.now()
    ## 格式化时间为 "年-月-日-时-分"
    time_str = current_time.strftime("%Y-%m-%d-%H-%M")
    ## 创建文件夹名
    folder_name = f"{time_str}_logs"
    
    ## 检查logs文件夹是否存在
    if not os.path.exists("logs"):
        # 如果不存在，则创建logs文件夹
        os.makedirs("logs")
        logs = "false"
    
    ## 在logs文件夹中创建以当前时间命名的.txt文件
    file_name = os.path.join("logs", f"{time_str}.txt")
    with open(file_name, "a",encoding="utf-8") as f:
        ## 获取当前时间
        current_time = datetime.datetime.now()
        ## 格式化时间为 "年-月-日-时-分"
        time_str = current_time.strftime("%Y-%m-%d-%H-%M")
        ## logs文件夹是否存在日志写入
        if logs == "false":
            f.write("[{}]".format(time_str) + "[日志]未检测到日志文件夹，已自动创建日志文件夹\n")
        ## 写入日志文本
        f.write("[{}]".format(time_str) + "[日志]创建日志成功\n")

# kook机器人连接
## 读取key.josn文件的token
with open('config.json') as f:
    token = json.load(f)
## 获取token值
token = token['token']
## 创建机器人实例
bot = Bot(token=token)

# 程序运行
if __name__ == "__main__":
    create_logs_folder() ## 日志模块运行
    bot.run() ## khl.py机器人运行

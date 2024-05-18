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

import requests,json ##json文件模块

# 程序函数注册
def init(bot:Bot):
    ##/ 获取logs文件名
    with open('logs/logs.txt', 'r', encoding='utf-8') as file:
        file_name = file.read()
    with open(file_name, "a",encoding="utf-8") as f:
        f.write("[power]读取txt目录：{}\n".format(file_name))

    ## 读取key.josn文件的token
    with open('key.json') as f:
        token = json.load(f)
    ## 获取token值
    token = token['token']

# 权限组名单录入
    @bot.command(regex=r'^(?:添加验证)(.+)')
    async def key_add(msg: Message, key: str):
        user_power = 'user_power.json'  ## 权限组文件路径

        ## 记录管理员添加密钥操作
        with open(file_name, "a", encoding="utf-8") as f:
            f.write(f"[power]管理员添加密钥 {key}\n")

        ## 验证文件是否存在
        if not os.path.exists(user_power):
            with open(user_power, 'w', encoding='utf-8') as f:
                json.dump({'keys': []}, f, ensure_ascii=False, indent=4)
        else:
            try:
                with open(user_power, 'r', encoding='utf-8') as f:
                    json.load(f)  ## 尝试读取以确保内容有效
            except (json.JSONDecodeError, FileNotFoundError):
                with open(user_power, 'w', encoding='utf-8') as f:
                    json.dump({'keys': []}, f, ensure_ascii=False, indent=4)

        ## 加载文件
        try:
            with open(user_power, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            data = {'keys': []}

        ## 确保密钥列表是列表类型
        if not isinstance(data.get('keys'), list):
            data['keys'] = list(data.get('keys', []))

        ## 检查密钥是否存在
        if key in data['keys']:
            await msg.reply(f"密钥已存在")
            with open(file_name, "a", encoding="utf-8") as f:
                f.write("[power]密钥已存在，拒绝添加\n")
        else:
            ## 添加新密钥
            data['keys'].append(key)
            try:
                with open(user_power, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
                await msg.reply(f"密钥 {key} 已添加")
                with open(file_name, "a", encoding="utf-8") as f:
                    f.write("[power]密钥已添加\n")
            except IOError as e:
                await msg.reply(f"写入文件时出错: {str(e)}")
                with open(file_name, "a", encoding="utf-8") as f:
                    f.write(f"[power]写入文件时出错: {str(e)}\n")

# 权限组检查
    @bot.command(regex=r'^(?:验证)(.+)')
    async def key_find(msg: Message, key: str):
        user_power = 'user_power.json'  ## 权限组文件路径

        ## 记录用户验证邀请码操作
        with open(file_name, "a", encoding="utf-8") as f:
            f.write(f"[power]用户验证邀请码: {key}\n")

        ## 加载 JSON 文件中的密钥
        try:
            with open(user_power, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            data = {'keys': []}

        ## 确保密钥列表是列表类型
        if not isinstance(data.get('keys'), list):
            data['keys'] = list(data.get('keys', []))

        ## 检查密钥是否存在
        if key in data['keys']:
            ## 删除并返回密钥
            data['keys'].remove(key)
            try:
                with open(user_power, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
                await msg.reply(f"验证通过，按我服规定，已给予对应权限组")
                # 发送添加角色POST请求
                url = 'https://www.kaiheila.cn/api/v3/guild-role/grant'  # 确认API地址
                headers = {
                    'Authorization': f'Bot {token}',
                    'Content-Type': 'application/json'  # 添加 Content-Type 头
                }
                payload = {
                    'guild_id': '83594105',  # 服务器ID
                    'user_id': str(msg.author_id),  # 玩家ID
                    'role_id': '30807834'  # 角色ID
                }
                POST_back = requests.post(url, headers=headers, json=payload)

                with open(file_name, "a", encoding="utf-8") as f:
                    f.write(f"[power]验证通过，已给予 {msg.author_id} 权限\n")
                    f.write(f"[power]POST返回:{POST_back}\n")
            except IOError as e:
                await msg.reply(f"写入文件时出错: {str(e)}")
                with open(file_name, "a", encoding="utf-8") as f:
                    f.write(f"[power]写入文件时出错: {str(e)}\n")
        else:
            await msg.reply(f"验证失败，请检查邀请码是否经过管理员录入或者是否有效")
            with open(file_name, "a", encoding="utf-8") as f:
                f.write("[power]验证失败\n")

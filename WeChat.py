# coding:utf8
from AutoPersual import wechat_check_essay
import itchat
import time
import json

config = {u'英文自动审阅系统': wechat_check_essay}
active_func = []
UserActiveState = dict()
is_active = False


def Nothing():
    pass


def match_command(msg):
    if active_func:
        itchat.send(u'正在处理，请耐心等待...', msg['FromUserName'])
        func = active_func[0]
        result = func(msg['Text'])
        itchat.send(''.join(result), msg['FromUserName'])
        return
    if msg['Text'] in config:
        active_func.append(config[msg['Text']])
        func = config[msg['Text']]
        itchat.send(u'开启 ' + msg['Text'], msg['FromUserName'])
    else:
        itchat.send(u'不懂你说什么哦，请~请~下达命令，主人...现在有以下几种服务：', msg['FromUserName'])
        itchat.send(';\n'.join(config.keys()), msg['FromUserName'])


def command_mode(func):
    def wraps(*args, **kwargs):
        if args:
            msg = args[0]
        elif 'msg' in kwargs:
            msg = kwargs['msg']
        else:
            print('command_mode way is invalid!')
            return func(*args, **kwargs)

        if msg['FromUserName'] not in UserActiveState:
            UserActiveState[msg['FromUserName']] = False

        if msg['Text'] == u'进入命令模式':
            UserActiveState[msg['FromUserName']] = True
            itchat.send(u'成功开启命令模式，请输入命令...', msg['FromUserName'])
            itchat.send(u'现在有以下几个可用命令服务：\n' + '\n'.join(config.keys()), msg['FromUserName'])
            return Nothing
        elif msg['Text'] == u'退出命令模式':
            UserActiveState[msg['FromUserName']] = False
            itchat.send(u'成功退出命令模式，谢谢您的使用~', msg['FromUserName'])
            return Nothing
        return func(*args, **kwargs)

    return wraps


@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing'])
@command_mode
def text_reply(msg):
    if UserActiveState[msg['FromUserName']]:
        match_command(msg)
        time.sleep(1)


@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
def download_files(msg):
    print(msg)
    fileDir = '%s%s' % (msg['Type'], int(time.time()))
    msg['Text'](fileDir)
    itchat.send('%s received' % msg['Type'], msg['FromUserName'])
    itchat.send('@%s@%s' % ('img' if msg['Type'] == 'Picture' else 'fil', fileDir), msg['FromUserName'])


itchat.auto_login(enableCmdQR=2)
itchat.run()

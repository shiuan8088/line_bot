from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('dIkclmiqB5XUU+1Y00NCYtbmhVvUKJcPXR7+Oh0x5hN1F9Fd9Aa0V+2yGNYMR8IxpTnqDxYvvsEqqks9j1GG5OJFxEre+0dOd5eZZiMzZfqSFOCl7lZiSAe8F3ygGUTUG2s0webF0LNv/f4hYWZEWAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ec56d616a0dcd9911ac6c0dd96bce4dc')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    

    if msg in ['hi', 'Hi']:
        r = '嗨~小助手來和妳請安囉!!'
    elif msg == '小胖好難揪':
        r = '對阿~小胖怎麼這麼難揪:"('
    elif msg in '是誰':
        r = '我是Liam的好夥伴'
    elif msg in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'i', 'n']:
        r = '不要說英文，小助手還在學習英文'
    elif msg == '不要耍白癡':
        r = '對阿~小心變阿ㄎ一ㄤ!!!'
    elif msg == '小助手上~':
        r = 'Yes sir 請問到底甚麼時候要出來聚?'
    else:
        return

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()
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
    r = '@Lin 好難揪'


    if msg == 'hi':
        r = '嗨'
    elif msg == '小胖好難揪':
        r = '對阿~小胖怎麼這麼難揪'
        
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()
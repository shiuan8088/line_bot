from flask import Flask, request, abort

from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)

app = Flask(__name__)

line_bot_api = LineBotApi('0ggj78as0ojdhigsldkupns / muqp05bl8x22hnlz4i9clkivuex + irhpt7py / xzptnqdxyvvseqks9j1gg5ojfxere + 0dod5ezzimzzimzzfq4fenxtdwr + d7urp1gn7lv9xbwiawof2tts0d1tytgwdb04t89 / 1o / w1cdnyilfu =')
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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
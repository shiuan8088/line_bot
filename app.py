from flask import Flask, request, abort
 from linebot import (
     LineBotApi, WebhookHandler
 )
 from linebot.exceptions import (
     InvalidSignatureError
 )
 from linebot.models import *
 app = Flask(name)
 Channel Access Token
 line_bot_api = LineBotApi('0ggj78as0ojdhigsldkupns / muqp05bl8x22hnlz4i9clkivuex + irhpt7py / xzptnqdxyvvseqks9j1gg5ojfxere + 0dod5ezzimzzimzzfq4fenxtdwr + d7urp1gn7lv9xbwiawof2tts0d1tytgwdb04t89 / 1o / w1cdnyilfu =')
 Channel Secret
 handler = WebhookHandler('ec56d616a0dcd9911ac6c0dd96bce4dc')
 監聽所有來自 /callback 的 Post Request
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
         abort(400)
     return 'OK'
 處理訊息
 @handler.add(MessageEvent, message=TextMessage)
 def handle_message(event):
     message = TextSendMessage(text=event.message.text)
     line_bot_api.reply_message(event.reply_token, message)
 @app.route('/')
 def index():
     return 'Hello World'
 import os
 if name == "main":
     port = int(os.environ.get('PORT', 5000))
     app.run(host='0.0.0.0', port=port)
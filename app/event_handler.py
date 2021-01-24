from linebot import WebhookHandler, LineBotApi
from linebot.models import MessageEvent
from linebot.models.messages import TextMessage
from linebot.models.send_messages import TextSendMessage

from app.config import LINE_CHANNEL_SECRET, LINE_CHANNEL_TOKEN

handler = WebhookHandler(LINE_CHANNEL_SECRET)


@handler.add(MessageEvent, TextMessage)
def handle_text_message(event: MessageEvent):
    """
    Echo the same message
    """

    line_bot_api = LineBotApi(LINE_CHANNEL_TOKEN)
    line_bot_api.reply_message(
        event.reply_token, TextSendMessage(event.message.text)
    )

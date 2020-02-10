# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import CardFactory, TurnContext, MessageFactory
from botbuilder.core.teams import TeamsActivityHandler, TeamsInfo
from botbuilder.schema import CardAction, HeroCard, Mention, ConversationParameters
from botbuilder.schema._connector_client_enums import ActionTypes

from tools.weather import weather

class TeamsConversationBot(TeamsActivityHandler):
    def __init__(self, app_id: str, app_password: str):
        self._app_id = app_id
        self._app_password = app_password

    async def on_message_activity(self, turn_context: TurnContext):
        TurnContext.remove_recipient_mention(turn_context.activity)
        #turn_context.activity.text = turn_context.activity.text.strip()
        text = turn_context.activity.text.strip()



        if text == "TestA":        
            await turn_context.send_activity(
                MessageFactory.text("Ending conversation from the skillA...")
            )
            return 

        if text == "TestB":        
            await turn_context.send_activity(
                MessageFactory.text("Ending conversation from the skillB...")
            )
            return 
            await turn_context.send_activity(
             MessageFactory.text(content)
            )
            return 0

##########***天氣預報***#########  

        if text == "!天氣預報":
            content = "請輸入欲查詢地點\n(目前限台灣本島+離島)\n\n使用方式如下(已設有防呆):\n!台北市\n!臺北市\n!台北\n!臺北\n!taipei"
            await turn_context.send_activity(
             MessageFactory.text(content)
            )
            return 0

        if text == "!台北市" or text == "!臺北市" or text == "!台北" or text == "!臺北" or text == "!taipei":
            content = weather(L=0)
            await turn_context.send_activity(
             MessageFactory.text(content)
            )
            return 0
        if text == "!新北市" or text == "!新北" or text == "!new taipei":
            content = weather(L=1)
            await turn_context.send_activity(
             MessageFactory.text(content)
            )
            return 0
        if text == "!桃園市" or text == "!taoyuan":
            content = weather(L=2)
            await turn_context.send_activity(
             MessageFactory.text(content)
            )
            return 0
        if text == "!台中市" or text == "!臺中市" or text == "!台中" or text == "!臺中" or text == "!taichung":
            content = weather(L=3)
            await turn_context.send_activity(
             MessageFactory.text(content)
            )
            return 0
        if text == "!台南市" or text == "!臺南市" or text == "!台南" or text == "!臺南" or text == "!tainan":
            content = weather(L=4)
            await turn_context.send_activity(
             MessageFactory.text(content)
            )
            return 0
        if text == "!高雄市" or text == "!高雄" or text == "!kaohsiung":
            content = weather(L=5)
            await turn_context.send_activity(
             MessageFactory.text(content)
            )
            return 0
        if text == "!基隆市" or text == "!基隆" or text == "!keelung":
            content = weather(L=6)
            await turn_context.send_activity(
             MessageFactory.text(content)
            )
            return 0
        if text == "!新竹縣" or text == "!hsinchu county":
            content = weather(L=7)
            await turn_context.send_activity(
             MessageFactory.text(content)
            )
            return 0
        if text == "!新竹市" or text == "!hsinchu city":
            content = weather(L=8)
            await turn_context.send_activity(
             MessageFactory.text(content)
            )
            return 0
        if text == "!苗栗縣" or text == "!苗栗" or text == "!miaoli":
            content = weather(L=9)
            await turn_context.send_activity(
             MessageFactory.text(content)
            )
            return 0
        if text == "!彰化縣" or text == "!彰化" or text == "!changhua":
            content = weather(L=10)
            await turn_context.send_activity(
             MessageFactory.text(content)
            )
            return 0
        if text == "!南投縣" or text == "!南投" or text == "!nantou":
            content = weather(L=11)
            await turn_context.send_activity(
             MessageFactory.text(content)
            )
            return 0
        if text == "!雲林縣" or text == "!雲林" or text == "!yunlin":
            content = weather(L=12)
            await turn_context.send_activity(
             MessageFactory.text(content)
            )
            return 0
        if text == "!嘉義縣" or text == "!chiayi county":
            content = weather(L=13)
            await turn_context.send_activity(
             MessageFactory.text(content)
            )
            return 0
        if text == "!嘉義市" or text == "!chiayi city":
            content = weather(L=14)
            await turn_context.send_activity(
             MessageFactory.text(content)
            )
            return 0
        if text == "!屏東縣" or text == "!屏東" or text == "!pingtung":
            content = weather(L=15)
            await turn_context.send_activity(
             MessageFactory.text(content)
            )
            return 0
        if text == "!宜蘭縣" or text == "!宜蘭" or text == "!ilan":
            content = weather(L=16)
            await turn_context.send_activity(
             MessageFactory.text(content)
            )
            return 0
        if text == "!花蓮縣" or text == "!花蓮" or text == "!hualien":
            content = weather(L=17)
            await turn_context.send_activity(
             MessageFactory.text(content)
            )
            return 0
        if text == "!臺東縣" or text == "!台東" or text == "!taitung":
            content = weather(L=18)
            await turn_context.send_activity(
             MessageFactory.text(content)
            )
            return 0
        if text == "!澎湖縣" or text == "!澎湖" or text == "!penghu":
            content = weather(L=19)
            await turn_context.send_activity(
             MessageFactory.text(content)
            )
            return 0
        if text == "!金門縣" or text == "!金門" or text == "!jinmen":
            content = weather(L=20)
            await turn_context.send_activity(
             MessageFactory.text(content)
            )
            return 0
        if text == "!連江縣" or text == "!連江" or text == "!lianjiang":
            content = weather(L=21)
            await turn_context.send_activity(
             MessageFactory.text(content)
            )
            return 0


    ##########***隱藏專區(需權限)***#########  




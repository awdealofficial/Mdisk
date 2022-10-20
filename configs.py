# (c) @KGN_OFFICIAL

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", "9411723"))
    API_HASH = os.environ.get("API_HASH", "30fa091455c0548d77dc254f0bb705b0")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5496693865:AAEsyCi-tFpsDID-0X0zFrZjfK_DqF-1n08")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQAiPieGy4ZpSyj2Oc7o_Z8UEr6OAwecAH2ay2s3Z8T3vPm9ReQrd-NT1NcbOBcEjOGwUebGuqfJNSrTw677fP-LVvx0bTMP4rWQh9RBtgGxdFZFq-3hmZjAjRxvdzSKmJMcsrEqaSnpoFH6OBd3rr0j6ejjY2qNXmTwtJ4m36KcHubj65TydwBLMbbv1Z0KySyNESF30HAhe-NiY3OOXpvZvKkoJGAClEzSYL98NFfRGGnf0BRveiU7rCmP-LNh-BryWmWVq03M2Ganb6vFHYCKy7s4J5c_H90uCNmNOfcZcjmk_IXeDcaOW2eA95jKI4VT2pNPlQOTTDHZrOtV7OnvAAAAADQzMu0A")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001668318959"))
    BOT_USERNAME = os.environ.get("BOT_USERNAME" , "Mdisksearch_Tgbot")
    BOT_OWNER = int(os.environ.get("BOT_OWNER" ,"875770605"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL"),( None)
    ABOUT_BOT_TEXT = """<b>This is Mdisk Search Bot.

🤖 My Name: <a href='https://t.me/Hollywood_in_HindiHD'>Mdisk Search Robot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

👨‍💻 Created By: <a href='https://t.me/AmanReDX'>AmanReDX</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Developer : <a href='https://t.me/AmanReDX'>AmanReDX</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm Mdisk Search Robot.🤖</a>

I Can Search!🔍 What You Want? YOU KNOW WHAT I MEAN 😜

<a>Made With ❤ By @AmanReDX</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm Mdisk Search Robot.🤖</a>

I Can Search!🔍 What You Want?😜

<a>Made With ❤ By @AmanReDX</a></b>
"""



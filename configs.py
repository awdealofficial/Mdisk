# (c) @KGN_OFFICIAL

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", "9411723"))
    API_HASH = os.environ.get("API_HASH", "30fa091455c0548d77dc254f0bb705b0")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5496693865:AAEsyCi-tFpsDID-0X0zFrZjfK_DqF-1n08")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "1BVtsOLYBu10DHe1oenVf24BuFwWW_UhDOGKf9dkH-o4Lo26LrjpQiUXvrsgAKh7vJWfZAVKgie5lt81plYCgEQFc7gjL5ra22HxJ-TbUq6Hj-kw2YipZsadyEFwJB1Zs50PkgRRnMJ9Nzs9db5RYyEfSUxY5Ejz-NfXWIQjyqX1wMXwJ9AJWZXFk7d993EimJvNeSBRrLmXRoS_ABgA81hsHdkSo-nN4_tKQqjaS1Ddf6PswMPJHd1z_UjMk34pIOtelj1AMqewLHksXWp82obJD6SPs392iNekM3Cu5gUnEp5J9Je3BxG90Q3v27GDN8vA1fal1MqR4LY0e5x-TaDqnesSoQ6E")
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



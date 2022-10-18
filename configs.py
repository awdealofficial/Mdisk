# (c) @KGN_OFFICIAL

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", "9411723"))
    API_HASH = os.environ.get("API_HASH", "30fa091455c0548d77dc254f0bb705b0)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5477733402:AAHLAfB4vF1PVtFzCHEy_OhwJZvAaw0cYgE")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "1BVtsOHkBu1tToP-XwodSsUyBzjxhTlT4DADFRV4d6pOv0R195eL2LI5r5BWzfY-1WpAaZYC0mypoGQdQQdsQZNpIAdC4geybfZQqtC9EkODCxFmafd6WlKV1VRrT9TiVrFqWCz_-6LLiSPEpEFI3xLWR8qK_6yiI_SAnmkp24BtiKlSksXb7AmgjpwmXPC1FbJcUfg70GHK5KRJ70wdejgHP10P4wfBv_bPRj0FGbvCHNz-oX7i9DAWQl0-L4XkvScjAmYV6z3vcf59gVtEL7R92I9ZRmcDe3n_7_YM6dOM8-302guO_94TfaLU0_fe4XHQRah9rj1mQE4rIyLtQe-R8z0-P-Rs=")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001668318959"))
    BOT_USERNAME = os.environ.get("BOT_USERNAME" , "File_to_Link_TGBOT")
    BOT_OWNER = int(os.environ.get("BOT_OWNER" ,"875770605"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL"),( None)
    ABOUT_BOT_TEXT = """<b>This is Mdisk Search Bot.

🤖 My Name: <a href='https://t.me/Official_Movies_Group'>Mdisk Search Robot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

👨‍💻 Created By: <a href='https://t.me/Am_RoBots'>ᎯℕUℛᎯᎶ</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Developer : <a href='https://t.me/Am_RoBots'>ᎯℕUℛᎯᎶ</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm Mdisk Search Robot.🤖</a>

I Can Search!🔍 What You Want?😜

<a>Made With ❤ By @Am_RoBots</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm Mdisk Search Robot.🤖</a>

I Can Search!🔍 What You Want?😜

<a>Made With ❤ By @Am_RoBots</a></b>
"""



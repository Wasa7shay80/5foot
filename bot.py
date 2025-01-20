from aiohttp import web
from plugins import web_server

import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL2, CHANNEL_ID, PORT

name = """
    ,-·-.          ,'´¨;                    ,.,   '                   ,. -,          .·¨'`;        ,.·´¨;\   
    ';   ';\      ,'´  ,':\'                ;´   '· .,            ,.·'´,    ,'\        ';   ;'\       ';   ;::\  
     ;   ';:\   .'   ,'´::'\'             .´  .-,    ';\      ,·'´ .·´'´-·'´::::\'      ;   ;::'\      ,'   ;::'; 
     '\   ';::;'´  ,'´::::;'             /   /:\:';   ;:'\'   ;    ';:::\::\::;:'       ;  ;::_';,. ,.'   ;:::';°
       \  '·:'  ,'´:::::;' '           ,'  ,'::::'\';  ;::';   \·.    `·;:'-·'´        .'     ,. -·~-·,   ;:::'; '
        '·,   ,'::::::;'´         ,.-·'  '·~^*'´¨,  ';::;    \:`·.   '`·,  '        ';   ;'\::::::::;  '/::::;  
         ,'  /::::::;'  '         ':,  ,·:²*´¨¯'`;  ;::';      `·:'`·,   \'          ;  ';:;\;::-··;  ;::::;   
       ,´  ';\::::;'  '           ,'  / \::::::::';  ;::';       ,.'-:;'  ,·\         ':,.·´\;'    ;' ,' :::/  '  
       \`*ª'´\\::/‘             ,' ,'::::\·²*'´¨¯':,'\:;   ,·'´     ,.·´:::'\         \:::::\    \·.'::::;     
        '\:::::\';  '            \`¨\:::/          \::\'    \`*'´\::::::::;·'‘          \;:·´     \:\::';      
          `*ª'´‘                 '\::\;'            '\;'  '   \::::\:;:·´                          `·\;'       
            '                      `¨'                        '`*'´‘                                 '        

"""

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN,
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        # Handle FORCE_SUB_CHANNEL2
        if FORCE_SUB_CHANNEL2:
            try:
                link = (await self.create_chat_invite_link(chat_id=FORCE_SUB_CHANNEL2, creates_join_request=True)).invite_link
                self.invitelink2 = link
            except Exception as e:
                self.LOGGER(__name__).warning(e)
                self.LOGGER(__name__).warning("Bot can't export join request link from FORCE_SUB_CHANNEL2!")
                self.LOGGER(__name__).warning(f"Please double-check the FORCE_SUB_CHANNEL2 value and ensure the bot is admin with 'Invite Users via Link' permission. Value: {FORCE_SUB_CHANNEL2}")
                self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/Animetalks0 for support")
                sys.exit()

        # Handle FORCE_SUB_CHANNEL
        if FORCE_SUB_CHANNEL:
            try:
                link = (await self.create_chat_invite_link(chat_id=FORCE_SUB_CHANNEL, creates_join_request=True)).invite_link
                self.invitelink = link
            except Exception as e:
                self.LOGGER(__name__).warning(e)
                self.LOGGER(__name__).warning("Bot can't export join request link from FORCE_SUB_CHANNEL!")
                self.LOGGER(__name__).warning(f"Please double-check the FORCE_SUB_CHANNEL value and ensure the bot is admin with 'Invite Users via Link' permission. Value: {FORCE_SUB_CHANNEL}")
                self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/Apatheticyash for support")
                sys.exit()

        # Handle Database Channel
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Ensure the bot is admin in the DB Channel and check CHANNEL_ID. Value: {CHANNEL_ID}")
            self.LOGGER(__name__).info("\nBot Stopped. talk to https://t.me/Apatheticyash for support")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"Bot Running..!\n\nCreated by \nhttps://t.me/Animes_Xyz")
        self.LOGGER(__name__).info(name)

        self.username = usr_bot_me.username

        # Web server setup
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")

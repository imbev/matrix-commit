import os
import simplematrixbotlib as botlib

HOMESERVER = os.getenv("HOMESERVER")
USERNAME = os.getenv("USERNAME")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ROOM_ID = os.getenv("ROOM_ID")
MESSAGE = os.getenv("MESSAGE")

print(MESSAGE)

creds = botlib.Creds(homeserver=HOMESERVER, username=USERNAME, access_token=ACCESS_TOKEN)
bot = botlib.Bot(creds=creds)

@bot.listener.on_startup
async def send_message(joined_room_id: str) -> None:
    if ROOM_ID and ROOM_ID != joined_room_id:
        return

    await bot.api.send_markdown_message(
        room_id=joined_room_id, 
        message=MESSAGE, 
        msgtype="m.notice")
        
    exit()

bot.run()

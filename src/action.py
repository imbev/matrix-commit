import os
import time
import simplematrixbotlib as botlib
import git

HOMESERVER = os.getenv("HOMESERVER")
USERNAME = os.getenv("USERNAME")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ROOM_ID = os.getenv("ROOM_ID")
MESSAGE = os.getenv("MESSAGE") or "Commit:"
BRANCH = os.getenv("BRANCH")
 
repo = git.Repo('.')
if BRANCH:
    repo.git.checkout(BRANCH)
    commit = repo.commit(BRANCH)
else:
    commit = repo.commit('HEAD')

creds = botlib.Creds(homeserver=HOMESERVER, username=USERNAME, access_token=ACCESS_TOKEN)
bot = botlib.Bot(creds=creds)

@bot.listener.on_startup
async def send_message(joined_room_id: str) -> None:
    if ROOM_ID and ROOM_ID != joined_room_id:
        return

    message = f"""
{MESSAGE}
Author: {commit.author.name}
Branch: {repo.active_branch}
Timestamp: {time.asctime(time.gmtime(commit.committed_date))}
Message: {commit.message}
"""

    await bot.api.send_markdown_message(
        room_id=joined_room_id, 
        message=message, 
        msgtype="m.notice")
        
    exit()

bot.run()

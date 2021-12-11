import os

homeserver = os.getenv("HOMESERVER")
username = os.getenv("USERNAME")
access_token = os.getenv("ACCESS_TOKEN")
room_id = os.getenv("ROOM_ID")
message = os.getenv("MESSAGE")

print(homeserver)
print(username)
print(access_token)
print(room_id)
print(message)
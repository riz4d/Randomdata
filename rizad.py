import asyncio
import requests
import os
import logging
import time
import string
import random
import html

# for fake dats.
from faker import Faker
from faker.providers import internet

# telethon
from telethon import events, Button, TelegramClient
from telethon.tl import functions, types
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location

logging.basicConfig(level=logging.INFO)

try:
    API_ID = int(os.environ.get("API_ID", 6))
    API_HASH = os.environ.get("API_HASH", None)
    TOKEN = os.environ.get("TOKEN", None)
except ValueError:
    print("You forgot to fix or written all vars")
    print("Ping your Issue at https://telegram.me/riz4d ,Now Bot is Exiting.!")
    exit()
except Exception as e:
    print(f"Bug - {str(e)}")
    print("Ping your Issue at https://telegram.me/riz4d ,Now Bot is Exiting.!")
    exit()
except ApiIdInvalidError:
    print("API_ID or API_HASH Are Invalid.")
    print("Ping your Issue at https://telegram.me/riz4d ,Now Bot is Exiting.!")
    exit()

bot = TelegramClient('rizad', API_ID, API_HASH)
rizad = bot.start(bot_token=TOKEN)


# Copyright @riz4d
async def is_admin(event, user):
    try:
        sed = await event.client.get_permissions(event.chat_id, user)
        if sed.is_admin:
            is_mod = True
        else:
            is_mod = False
    except:
        is_mod = False
    return is_mod

@rizad.on(events.NewMessage(pattern="/fakedb"))
async def hi(event):
    if event.fwd_from:
        return
    if event.is_group:
        if not await is_admin(event, event.message.sender_id):
            await event.reply("`This Action Not Allowed. It can Do By My Master!`")
            return
    fake = Faker()
    print("FAKE DETAILS GENERATED\n")
    name = str(fake.name())
    fake.add_provider(internet)
    address = str(fake.address())
    ip = fake.ipv4_private()
    cc = fake.credit_card_full()
    email = fake.ascii_free_email()
    job = fake.job()
    android = fake.android_platform_token()
    pc = fake.chrome()
    await event.reply(
        f"<b><u> Fake Data Generated</b></u>\n<b>Name :- </b><code>{name}</code>\n\n<b>Address:- </b><code>{address}</code>\n\n<b>IP ADDRESS:- </b><code>{ip}</code>\n\n<b>credit card:- </b><code>{cc}</code>\n\n<b>Email Id:- </b><code>{email}</code>\n\n<b>Job:- </b><code>{job}</code>\n\n<b>android user agent:- </b><code>{android}</code>\n\n<b>Pc user agent:- </b><code>{pc}</code>",
        parse_mode="HTML",
    )

# start handler

@rizad.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    if event.is_group:
        await event.reply("**Random Data Bot Is Active**")
        return
    await event.reply(f"**Hey!! {event.sender.first_name}**\nI can generate random Data's of citizens.\n My Master Mind Is Here @riz4d",
                    buttons=[
                        [Button.url("Instagram", url="https://instagram.com/rizad__x96")],
                        [Button.inline("Help",data="help")]
                    ])

@rizad.on(events.callbackquery.CallbackQuery(data="help"))
async def ex(event):
    await event.edit("**Heyy Dude it's not aa complecated task just type `/fakedb`.**\n : **Queries @riz4d**")

print ("Hosted Successfully")
rizad.run_until_disconnected()

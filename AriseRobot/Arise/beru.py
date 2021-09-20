import os
import sys
import json
import asyncio
import requests
import subprocess
import time
from io import StringIO

import psutil
from pyrogram import filters
from pyrogram.errors import FloodWait

from AriseRobot import ARISE
from pyrogram import client, filters
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AriseRobot import (ME_ID, NIGGERS)

@ARISE.on_message(filters.command(["help"]))
async def help(_, message):
    await message.reply_text('''
        General:
        /arise To Check if the bot is Alive
        
        Owner:
        /py run py code
        /dematter turn off the bot
        /rerise Cancel Shutdown
        
        Group Management:
        /shutup you know how it works
        /speak you know how it works
        /del Delete a Message
        /info info of a user in a group
        Working on it
        ''')
    
@ARISE.on_message(filters.regex("arise"))
async def shadow_extraction(_, message):
    await message.reply_text("This Shadow is alive and surging with power... \n**COMMAND ME** ")
    
@ARISE.on_message(filters.user(sudoers + ME_ID) & ~filters.forwarded & ~filters.via_bot & filters.command("shutup"))
async def mute(_, message):    
    try:
        chat_id = message.chat.id
        from_user_id = message.from_user.id
        victim = message.reply_to_message.from_user.id
        if victim == ME_ID:
            await message.reply_text("I cant mute him... idk y... maybe its him")
        else:
            await message.chat.restrict_member(victim, permissions=ChatPermissions())
            await message.reply_text("The Shadow Monarch's authority commands you to stay quiet...")
    except Exception as e:
        await message.reply_text(str(e))
        
@ARISE.on_message(filters.user(sudoers + ME_ID)& ~filters.forwarded & ~filters.via_bot & filters.command("speak"))
async def unmute(_, message: Message):
    try:
        chat_id = message.chat.id
        from_user_id = message.from_user.id
        victim = message.reply_to_message.from_user.id
        await message.chat.unban_member(victim)
        await message.reply_text("Try saying something... Can u?")
    except Exception as e:
        await message.reply_text(str(e))
        
@ARISE.on_message(filters.command("info"))
async def info(_, message):
    try:
        victim = message.reply_to_message.from_user.id
        chat_id = message.chat.id
        info_user = await app.get_chat_member(chat_id, victim)
        await message.reply_text(info_user)
    except Exception as e:
        await message.reply_text(str(e))
        
@ARISE.on_message(filters.user(ME_ID + sudoers) & filters.command("del"))
async def delete(_, message: Message):
    await message.reply_to_message.delete()
    await message.delete()        
    
#here is our beloved eval    




#lol idk forgot will add later


#herre is your py runner

    
@ARISE.on_message(filters.user(ME_ID) & ~filters.forwarded & ~filters.via_bot & filters.command("py"))
async def executor(client, message):
    try:
        cmd = message.text.split(" ", maxsplit=1)[1]
    except IndexError:
        await message.delete()
        return
    reply_to_id = message.message_id
    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    redirected_error = sys.stderr = StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd, client, message)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    final_output = (
        "**QUERY**:\n```{}```\n\n**OUTPUT**:\n```{}```".format(
            cmd,
            evaluation.strip()
        )
    )
    if len(final_output) > 4096:
        filename = "output.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(evaluation.strip()))
        await message.reply_document(
            document=filename,
            caption=cmd,
            disable_notification=True,
            reply_to_message_id=reply_to_id,
        )
        os.remove(filename)
        await message.delete()
    else:
        await edit_or_reply(message, text=final_output)
        
#u see this shit.... its shutdown
        
@ARISE.on_message(filters.command(['free_shadows']))
async def shutdown(_, message):
    if message.from_user.id == ME_ID:
        await message.reply_text("Sending all Shadows to nothingness in 60s...")
        os.system("sudo shutdown")
    else:
        await message.reply_text("Authority Overridden Shadow affinity maximum")

# lol the strings make no sense
@ARISE.on_message(filters.command(['return_shadow']))
async def cancelshutdown(_, message):
    if message.from_user.id == ME_ID:
        await message.reply_text("Shadows returning to Shadow Monarch")
        os.system("sudo shutdown -c")
    else:
        await message.reply_text("You can't stop me now...")        

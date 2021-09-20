from AriseRobot import ARISE
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

IGRIS_START = """
I am Arise Robot [(.)](https://mfiles.alphacoders.com/840/840043.png) `"check ing markdown."` \n
**"blah blah robot. \n \nblah blah bot.”**
lol
"""
    
@ARISE.on_message(filters.command(["start"], prefixes = "/") & ~filters.edited)
async def info(client, message):
    buttons = [
                [InlineKeyboardButton("BOT Support", url="https://t.me/kazutosupport")],
                [InlineKeyboardButton("Add this NOOB bot to your Group", url = "t.me/AriseRobot?startgroup=true")]
              ]
    await ARISE.send_message(chat_id = message.chat.id, text = START_MSG, reply_markup = InlineKeyboardMarkup(buttons))
    
    
    
    
   # [@#$%](https://i.redd.it/8jyzn83m3k471.jpg)

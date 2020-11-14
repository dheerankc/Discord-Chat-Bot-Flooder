#use visual studio code and install discord.py. open Command Prompt and type pip install discord.py on windows

# You Must read This before you use this flooder at your own risk. 
# this flooder is made for fun so if you upload this on top.gg or other websites
# YOU WILL PAY FOR IT

#this bot is already on top.gg so copyrights will be harsfully taken

#use this bot code to prank your friends or GET REVENGE ON UR FRNDS SERVER IF U MAKE DIS

# very gud for famouse youtubers. pls youtubers give credit to me on discord if u pranked or did somthing

#dani's biggest fan of all times



#hippity hopitty my code is not ur property

#---------------------Dont change any code or else it will go boom---------------------------


import discord
from discord.ext import commands
import datetime

from urllib import parse, request
import re
# these are important since they allow the bot to run using these modules



#no prefixes there and no description since this is a all time flood bot
bot = commands.Bot(command_prefix='', description="")

@bot.listen()
async def on_message(message):
    if " " in message.content.lower():
        await message.channel.send(' HAHAH ')
        await bot.process_commands(message)
#this code is the code which will flood all the channels this bot is invited to

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="To Laugh", url="http://www.twitch.tv/dheeran2010"))
    print('Im Ready To Flood the servers!')
# This code is the satus code but its gonna stream when you run the whole code. DONT CHANGE ANYTING OR ELSE IT BOOM


bot.run('Your bot token')

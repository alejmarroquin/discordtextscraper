# -*- coding: utf-8 -*-
from tokensafe import token
import discord
import os
from discord.ext import commands
import nest_asyncio
import datetime
import pytz
import requests
nest_asyncio.apply()

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix = '!', intents= discord.Intents.all())


@client.command()
async def scrape_all_messages(ctx, user: discord.User):
    # Get the target channel
    target_channel = discord.utils.get(ctx.guild.text_channels, name='general')
    
    # Get all the messages from the target channel
    async for message in target_channel.history(limit=None):
        # Check if the message was sent by the target user
        if message.author == user:
         
   
            # Format the message
              tz = pytz.timezone('America/Los_Angeles')
              timestamp = message.created_at.astimezone(tz)
              formatted_message = f"{message.author.name}, {timestamp}, {message.content}"
        
          #Write the message to a file
              with open("test2.csv", "a",encoding="utf-8") as file:
          #ext_file.write(formatted_message + '\n')
                file.write(formatted_message + "\n")
                
    # Confirm that the messages have been saved
   #await ctx.send("Messages have been saved to messages.txt")'''

client.run(token)
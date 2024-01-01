"""Importing the system module"""
import os
from dotenv import load_dotenv # pylint: disable=E0401
import responses
import discord # pylint: disable=E0401




# Loading the variables from .env file
load_dotenv()
responses = [responses.GoodMorning()]
def run_discord_bot():
    """Describing how to run the discord bot"""
    token = os.getenv("token")
    intents = discord.Intents(messages = True, message_content = True,
                               dm_messages = True, reactions = True, emojis = True)
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running!")
    @client.event
    async def on_message(message):
        for response in responses:
            await response.respond(message=message)
    client.run(token)

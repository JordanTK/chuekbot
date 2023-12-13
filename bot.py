import discord,os,responses
from dotenv import load_dotenv

# Loading the variables from .env file
load_dotenv()
responses = [responses.GoodMorning()]
def run_discord_bot():
    TOKEN = os.getenv("token")
    intents = discord.Intents(messages = True, message_content = True, dm_messages = True, reactions = True, emojis = True)
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running!")
    
    @client.event
    async def on_message(message):
        for response in responses:
            response.process(message=message,client=client)
            await response.respond(message=message)

 
    
    client.run(TOKEN)
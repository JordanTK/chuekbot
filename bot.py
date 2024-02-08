import discord,os,responses
from dotenv import load_dotenv

# Standard way for loading variables from environment
load_dotenv()

# Chose to store response procedures in a list and call them sequentially
responses = [responses.GoodMorning()]

# Function describing the parameters needed to start session
# Firstly we get the token environment containing the bot unique token that connects to discord servers
# Secondly we specify the intents, instance of the Intents class- what is our bot purpose and what permissions(access to information) does it have
# Thirdly we start the session by creating an instance of the client class specfying the intents parameter as the intents variable defined above
def run_discord_bot():
    TOKEN = os.getenv("token")
    intents = discord.Intents(messages = True, message_content = True, dm_messages = True, reactions = True, emojis = True)
    client = discord.Client(intents=intents)

    # Discord package takes event-driven approach. Here when our session is initiated(ready) we are going to see message
    # saying the bot is running which is nice letting us know we have succeeded in starting the service
    @client.event
    async def on_ready():
        print(f"{client.user} is now running!")

    # Again following the event-driven approach when the bot detects message(direct or in a channel) the bot looks up in the list
    # of responses to a message and responds to the message as described in responses.py
    @client.event
    async def on_message(message):
        for response in responses:
                    await response.respond(message=message)
                    
    # Using the token to run the bot on discord servers                 
    client.run(TOKEN)
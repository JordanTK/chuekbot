import discord,re
with open(".//discord//disco_link.txt", "r") as f:
    t = f.readline()

def run_discord_bot():
    TOKEN = t
    intents = discord.Intents(messages = True, message_content = True, dm_messages = True, reactions = True, emojis = True)
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running!")
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        # Adding reactions
        if re.search("добро утро", str(message.content).lower()):
            await message.add_reaction("☕")

 
    
    client.run(TOKEN)
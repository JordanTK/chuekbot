import asyncio
class GoodMorning:
    def respond(self,message):
        if "добро утро" in str(message.content).lower():
             return message.add_reaction("☕")
        else:
            return asyncio.sleep(0)
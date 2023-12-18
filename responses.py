import asyncio
class GoodMorning:
    # Would give us better test design
    def good_morning(self, text):
        return "добро утро" in text.lower()
    def respond(self,message):
        if self.good_morning(str(message.content)):
             return message.add_reaction("☕")
        else:
            return asyncio.sleep(0)
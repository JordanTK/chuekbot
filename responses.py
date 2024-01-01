"""Module dealing with sleeping(doing nothing) that is preffered choice for discord bots"""
import asyncio
class GoodMorning:
    """Class representing a reaction to a 'good morning' message"""
    # Would give us better test design
    def good_morning(self, text):
        """Function for identifying 'good morning' message in a character string."""
        return "добро утро" in text.lower()
    def respond(self,message):
        """Function for reacting with a hot drink emoji to a good morning message"""
        if self.good_morning(str(message.content)):
            return message.add_reaction("☕")

        return asyncio.sleep(0)
        
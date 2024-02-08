# Need this to make the bot do nothing and wait for a certain period when it should not respond
import asyncio

# Separating distinct response behaviour in class of its own, in this case class GoodMorning is dealing with response to a
# message possibly containing good morning greeting
class GoodMorning:

    # Following test-driven development we do not neeed to test whether discord package adds reactions properly
    # we are going to trust its fuctionality and test whether the string good morning is present in a text string
    # then evaluate that with the actual message the bot has detected
    def good_morning(self, text):

        # check whether good morning in string
        return "добро утро" in text.lower()
    
    def respond(self,message):

        # check whether string good morning is contained within the specific message
        if self.good_morning(str(message.content)):
            return message.add_reaction("☕")
        
        #do nothing and wait for a certain period when bot should not respond
        return asyncio.sleep(0)
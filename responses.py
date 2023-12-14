class GoodMorning:
    def respond(self,message):
        if "добро утро" in str(message.content).lower():
            return message.add_reaction("☕")
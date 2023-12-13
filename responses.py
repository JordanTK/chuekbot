class GoodMorning:
    def process(self, message,client):
        if message.author == client.user:
            return
        
    def dobro(self, message):
        return "добро" in str(message.content).lower()
    
    def utro(self,message):
        return "утро" in str(message.content).lower()
    
    def respond(self,message):
        if self.dobro(message) and self.utro(message):
            return message.add_reaction("☕")
import random

class ai:
       
    def ai_wager(self, bank):
        if(bank > 50):
            return random.randint(1, 50)
        else:  
            return random.randint(1, bank)
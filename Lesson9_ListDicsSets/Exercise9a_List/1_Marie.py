class BiscuitBox: 

    def __init__(self, biscuits): 
        self.biscuits = biscuits

    def get_biscuit_type(self):
        word = ''
        for i in range(len(self.biscuits)-1):
            for j in range(i+1, len(self.biscuits)):
                if (self.biscuits[i].lower() == self.biscuits[j].lower()):
                    word = self.biscuits[i]
                    return word
        if (word == ''):
            return 'None'
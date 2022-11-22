class WordWizards:
    def __init__(self, player1, player2, prefix):
        self.player1 =player1
        self.player2 =player2
        self.prefix =prefix

    def player_points(self, player, opponent):
        score = 0
        listOfword = player.word.symmetric_difference(opponent.word)   
        for word in listOfword:
            if (self.prefix in word and word in player.word):
                score = score + len(word)
        return score

    def winner(self):
        p1 = self.player_points(self.player1,self.player2 ) 
        p2 = self.player_points(self.player2,self.player1 ) 
        if (p1 == p2):
            return 'draw'
        if (p1>p2):
            return self.player1.name
        return self.player2.name


class Player:
    def __init__(self, name):
       self.name = name
       self.word = set()

    def add_word(self, word):
        self.word.add(word)   
player1 = Player("John")
player2 = Player("Sam")
player1.add_word("misdemeanor")
player1.add_word("mischievous")
player1.add_word("miscarriage")
player1.add_word("misused")

player2.add_word("mislead")
player2.add_word("misplace")
player2.add_word("misdemeanor")

player2.add_word("mischievous")
print(player1.word)
print(player2.word)
word_wizards = WordWizards(player1, player2, "mis")
print(word_wizards.player_points(player1, player2))
print(word_wizards.player_points(player2, player1))
print(word_wizards.winner())
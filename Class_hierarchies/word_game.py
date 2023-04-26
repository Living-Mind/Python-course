# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):

        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) == len(player2_word):
            pass
        else:
            return 2


class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):

        p1_num_vowels = 0
        p2_num_vowels = 0

        for char in player1_word:
            if char.lower() in "aeiou":
                p1_num_vowels += 1
        

        for char in player2_word:
            if char.lower() in "aeiou":
                p2_num_vowels += 1

        
        if p1_num_vowels > p2_num_vowels:
            return 1
        elif p1_num_vowels == p2_num_vowels:
            pass
        else:
            return 2

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):

        choise = ["rock", "paper", "scissors"]

        #ties
        if player1_word == player2_word or player1_word not in choise and player2_word not in choise:
            pass

        elif player1_word not in choise and player2_word in choise:
            return 2
            
        elif player2_word not in choise and player1_word in choise:
            return 1

        elif player1_word == "rock" and player2_word == "paper" or player1_word == "paper" and player2_word == "scissors" or player1_word == "scissors" and player2_word == "rock":
            return 2

        elif player2_word == "rock" and player1_word == "paper" or player2_word == "paper" and player1_word == "scissors" or player2_word == "scissors" and player1_word == "rock":
            return 1

if __name__ == "__main__":

#game1
   # p = WordGame(3)
   # p.play()

#game2
   # p = LongestWord(3)
   # p.play()

#game3 
    p = MostVowels(2)
    p.play()

#game4
   # p = RockPaperScissors(4)
   # p.play()
import random

def roll():
    die_roll = random.choice([1,2,3,4,5,6])
    print(die_roll)
    return die_roll


class Game:
  def __init__(self):
    self.player = Player()
    self.comp_player = CompPlayer()
    self.play_game 
    
class Player:
  def __init__(self):
    self.round_points = 0 
    self.total_score = 0

  def player_roll(self):
    choice = input('Do you want to "R"oll or "S"tay?')
    if choice == "r": 
      print('Your roll is a', roll())
    elif choice == "h":
      print("It's the computer's turn!")
      return choice
    
  # def rolls(self):
  #   rolls= []
  #   rolls.extend(roll())
  #   Sum = sum(rolls) 
  #   print(Sum)
  #   return Sum 

class CompPlayer:
  def __init__(self):
    self.round_points = 0
    self.total_score = 0

  def conmputer_roll(self):
    while self.round_score < 20:
        roll()
    if self.total_score >= 100:
        print("Computer Wins!")
        return


  
player = Player()
player.player_roll()
# player.rolls()
import random

def roll():
    die_roll = random.choice([1,2,3,4,5,6])
    print(die_roll)
    return die_roll


class Game:
  def __init__(self):
    self.player = Player()
    self.comp_player = CompPlayer()
    self.score = {self.player: 0, self.comp_player: 0}
   
 
class Player:
  def __init__(self):
    self.points = 0 

  def player_roll(self):
    choice = input('Do you want to "R"oll or "S"tay?')
    if choice == "r": 
      print('Your roll is a', roll())
      return choice
    
  def rolls(self):
    rolls= []
    rolls.list.append(roll())
    Sum = sum(roll())
    print(Sum) 
    return Sum    

class CompPlayer:
  def __init__(self, score):
    self.score = 0

  
player = Player()
player.player_roll()
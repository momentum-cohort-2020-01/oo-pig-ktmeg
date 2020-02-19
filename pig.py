import random

def roll():
    die_roll = random.choice([1,2,3,4,5,6])
    print(die_roll)
    return die_roll


class Game:
  def __init__(self, score):
    self.score = score 
    self.player = Player()


    
 
class Player:
  def __init__(self):
    self.points = 0

  def player_roll(self):
    choice = input('Do you want to "R"oll or "S"tay?')
    print(choice)
    return choice


    
  
  # def player_score(self,score)

class CompPlayer:
  def __init__(self):
    self.points = 0

  pass
  
player = Player()
player.player_roll()
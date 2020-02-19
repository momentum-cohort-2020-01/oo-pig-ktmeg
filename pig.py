import random

def roll():
    score = random.choice([1,2,3,4,5,6])
    print(score)
    return score


class Game:
  def __init__(self, score):
    self.score = score 
    self.player = Player()

    
 
class Player:
  def __init__(self, name):
    self.name = name
    self.points = 0
    
    

class CompPlayer:
  def __init__(self):
    self.points = 0

  
roll()
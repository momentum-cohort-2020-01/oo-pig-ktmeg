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

  def roll_hold(self):
    choice = input('Do you want to "R"oll or "S"tay?')
    return choice 


  def player_roll(self):
      roll_score = roll() 
      self.player.round.points += roll_score

  def player_turn(self):
    input = self.roll_hold()
    if input == "R":
      self.player_roll()
    else:
      retun False 

    
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
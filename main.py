#import math
class Dealer:
  def __init__(self, name, hand):
    self.name = name
    self.hand = hand

class Player:
  def __init__(self, name, hand, credits):
    self.name = name
    self.hand = hand
    self.credits = credits

def play():
  #assign_player_count
  #assign_players
  #start_game
  return

def assign_player_count():
    player_count = -1
    while player_count < 2 or player_count > 7:
      player_count = input("How many people are playing? ") 
    if player_count 
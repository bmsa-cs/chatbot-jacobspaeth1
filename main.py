"""
Chatbot
Author: jacob spaeth
Period/Core: 6

"""

import os
import importlib.util

import random

def run_tests():
  """
  This function will check for the pytest module
  before calling it to run the included tests.py
  """
  if importlib.util.find_spec('pytest') is None: # Check if pytest is installed
    os.system('python3 -m pip install -q pytest')

  command = "python3 -m pytest --tb=line -v -s tests.py"
  print(command)
  os.system(command)

def main():
  """This function contains all code for the chatbot."""
  print("Hello!")


if __name__ == "__main__":
  main()
  t = input("Run pytest? (y/n)").lower()
  if t == 'y':
    run_tests()

quest1 = input("What is your favorite color out of red, blue, green, or orange?")
if quest1 == 'red':
  print("i like red as well")
if quest1 == 'blue':
  print("Blue is my favorite as well")
if quest1 == 'green':
  print("You can never go wrong with green")
if quest1 == 'orange':
  print("Orange is a awsome color")

quest2 = input("What is your favorite sport out of american football, soccer, basketball or baseball?")
if quest2 == 'american football':
  print("I love american football even though the steelers lost :(")
if quest2 == 'soccer':
  print("I also like soccer, you must be in good shape if you play it too!")
if quest2 == 'basketball':
  print("Basketball is so fun!")
if quest2 == 'baseball':
  print("baseball is my favorite too!")

quest3 = input("Who is the GOAT out of lebron, jordan, wilt, or kobe?")
if quest3 == 'lebron':
  print("I would have to agree with you!")
if quest3 == 'jordan':
  print("interesting, lets talk sports sometime!")
if quest3 == 'wilt':
  print("I would say that wilt is probably the most dominant player ever! ")
if quest3 == 'kobe':
  print("in my opinion he is a top 5 player of all time!")

quest4 = input("What is your favorite video game out of fortnite, warzone, 2k, and cold war?")
if quest4 == 'fortnite':
  print("you are very epic!")
if quest4 == 'warzone':
  print("Cool!")
if quest4 == '2k':
  print("I am not a huge fan of 2k, but still a cool game!")
if quest4 == 'cold war':
  print("Havent played this game yet but it looks fun!")

quest5 = input("Who do you think will win the superbowl this year?")
if quest5 == 'buffalo bills':
  print("that is a interesting choice!")
if quest5 == 'kansas city cheifs':
  print("I have to agree with you!")
if quest5 == 'green bay packers':
  print("i think that they have a great chance on winning!?")
if quest5 == 'tampa bay buccaneers':
  print("they do have a great team!")

quest6 = input("Do you like talking to me?")
if quest6 == 'yes':
  print("Im glad!")
if quest6 == 'no':
  print("Im sorry to hear that")


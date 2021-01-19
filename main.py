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

g = int(input("a number: "))
if (g == 9):
print("Freshman")
elif (g == 10):
print("Sophomore")
elif (g == 11):
print("Junior")
elif (g == 12):
print("Senior")
else:
print("You\’re not in high school!")

g = int(input("a number: "))
if (g == 9):
print("Freshman")
elif (g == 10):
print("Sophomore")
elif (g == 11):
print("Junior")
elif (g == 12):
print("Senior")
else:
print("You\’re not in high school!")

g = int(input("a number: "))
if (g == 9):
print("Freshman")
elif (g == 10):
print("Sophomore")
elif (g == 11):
print("Junior")
elif (g == 12):
print("Senior")
else:
print("You\’re not in high school!")

g = int(input("a number: "))
if (g == 9):
print("Freshman")
elif (g == 10):
print("Sophomore")
elif (g == 11):
print("Junior")
elif (g == 12):
print("Senior")
else:
print("You\’re not in high school!")

g = int(input("a number: "))
if (g == 9):
print("Freshman")
elif (g == 10):
print("Sophomore")
elif (g == 11):
print("Junior")
elif (g == 12):
print("Senior")
else:
print("You\’re not in high school!")

g = int(input("a number: "))
if (g == 9):
print("Freshman")
elif (g == 10):
print("Sophomore")
elif (g == 11):
print("Junior")
elif (g == 12):
print("Senior")
else:
print("You\’re not in high school!")

g = int(input("a number: "))
if (g == 9):
print("Freshman")
elif (g == 10):
print("Sophomore")
elif (g == 11):
print("Junior")
elif (g == 12):
print("Senior")
else:
print("You\’re not in high school!")

g = int(input("a number: "))
if (g == 9):
print("Freshman")
elif (g == 10):
print("Sophomore")
elif (g == 11):
print("Junior")
elif (g == 12):
print("Senior")
else:
print("You\’re not in high school!")

g = int(input("a number: "))
if (g == 9):
print("Freshman")
elif (g == 10):
print("Sophomore")
elif (g == 11):
print("Junior")
elif (g == 12):
print("Senior")
else:
print("You\’re not in high school!")

g = int(input("a number: "))
if (g == 9):
print("Freshman")
elif (g == 10):
print("Sophomore")
elif (g == 11):
print("Junior")
elif (g == 12):
print("Senior")
else:
print("You\’re not in high school!")
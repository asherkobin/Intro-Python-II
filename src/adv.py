from room import Room
from player import Player
import sys
from termcolor import colored, cprint

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Asher", room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def north():
  try:
    player.room = player.room.n_to
  except AttributeError:
    cprint("\n** Blocked **", "red")

def south():
  try:
    player.room = player.room.s_to
  except AttributeError:
    cprint("\n** Blocked **", "red")

def east():
  try:
    player.room = player.room.e_to
  except AttributeError:
    cprint("\n** Blocked **", "red")

def west():
  try:
    player.room = player.room.w_to
  except AttributeError:
    cprint("\n** Blocked **", "red")

def list_commands():
  cprint("\nn (North), s (South), e (East), w (West), q (Quit)", "white", attrs=["bold"])

options = {
  "n": north,
  "s": south,
  "e": east,
  "w": west,
  "?": list_commands,
}

while (True):
  cprint(f"\n{player.name} is in the {player.room.name}", "blue")
  print(player.room.description)

  action = input("\nAction: ")

  if (action == "q"):
    break

  try:
    options[action]()
  except KeyError:
    print("\nInvalid Action: Type ? to get list of actions")





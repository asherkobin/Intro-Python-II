from item import Item
from room import Room
from player import Player
from termcolor import colored, cprint

import textwrap

# ITEMS

item = {
  "rock":
    Item("rock", "mysterious rune carvings surround the rock")
}

# ROOMS

room = {
  "outside":
    Room(
      "Outside Cave Entrance",
      "North of you, the cave mount beckons",
      [item["rock"]]),

  "foyer":
    Room(
      "Foyer",
      "Dim light filters in from the south. Dusty passages run north and east.",
      []),

  "overlook":
    Room(
      "Grand Overlook",
      "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.",
      []),

  "narrow":
    Room(
      "Narrow Passage",
      "The narrow passage bends here from west to north. The smell of gold permeates the air.",
      []),
  
  "treasure":
    Room(
      "Treasure Chamber",
      "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.",
      [])
}

def print_room_description():
  cprint(f"\nYou are in the {player.room.name}", "green") 
  cprint(player.room.description, "white")

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

player = Player("Asher", room["outside"])

def north():
  try:
    player.room = player.room.n_to
    print_room_description()
  except AttributeError:
    cprint("\n** Blocked **", "red")

def south():
  try:
    player.room = player.room.s_to
    print_room_description()
  except AttributeError:
    cprint("\n** Blocked **", "red")

def east():
  try:
    player.room = player.room.e_to
    print_room_description()
  except AttributeError:
    cprint("\n** Blocked **", "red")

def west():
  try:
    player.room = player.room.w_to
    print_room_description()
  except AttributeError:
    cprint("\n** Blocked **", "red")

def list_commands():
  cprint("""
Movement Commands: n (north), s (south), e (east), w (west), q (quit)

Room Commands:
- look (describe your current location)
- search (search your current location)

Item Commands:
- pickup [item_name] (pickup an item that you have found)
- drop [item_name] (drop an item from your inventory)

Inventory Commands:
- i (displays your inventory)
- inspect [item_name] (inspect an item)
- use [item_name] (use an item in your)""")

def search():
  cprint("\nYou search the area and see...", "white")
  if len(player.room.items) == 0:
    cprint("Nothing", "red")
  else:
    for item in player.room.items:
      cprint("- " + item.name, "yellow")

def look():
  print_room_description()

def pickup(item):
  print("you picked up " + item)

# def move_to(dir, cur_loc):
#   attribute = dir + "_to"

#   if hasattr(cur_loc, attribute):
#     return getattr(cur_loc, attribute)
#   else:
#     print("Can't Go That Way!")
#     return cur_loc

options = {
  "n": north,
  "s": south,
  "e": east,
  "w": west,
  "?": list_commands,
  "search": search,
  "look": look,
  "pickup": pickup
}

cash_needed_to_win = 10000

cprint(f"\n Welcome {player.name}.  The story so far... ", "white", attrs=['reverse'])

intro = """You have accumulated a sports gambling debt of $10,000.
 Your bookie is looking for you to collect his money.
 You must find the money needed within 24 hours.
 You decide to go on a dangerous adventure to find a way to pay your debt."""

print()

for line in textwrap.wrap(intro, 80):
  cprint(line, "cyan")

cprint("\nType '?' to list player commands")

cprint(f"\nYou are in the {player.room.name}", "green") 
cprint(player.room.description, "white")

while (True):
  action = input("\nAction: ")

  decontructed_command = action.split(" ")

  if (len(decontructed_command) > 1):
    verb = decontructed_command[0]
    subject = decontructed_command[1]
  else:
    verb = decontructed_command[0]
    subject = None

  if (verb == "q"):
    break

  try:
    options[verb](subject)
  except KeyError:
    print("\nInvalid Action: Type ? to get list of actions.")





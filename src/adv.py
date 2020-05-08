from item import Item
from room import Room
from player import Player
from termcolor import colored, cprint
from actions import Actions
from rooms import rooms

import textwrap

# Link rooms together

rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']

player = Player("Asher", rooms["outside"])
actions = Actions(player)

# def move_to(dir, cur_loc):
#   attribute = dir + "_to"

#   if hasattr(cur_loc, attribute):
#     return getattr(cur_loc, attribute)
#   else:
#     print("Can't Go That Way!")
#     return cur_loc

options = {
  "n": actions.north,
  "s": actions.south,
  "e": actions.east,
  "w": actions.west,
  "?": actions.list_commands,
  "search": actions.search,
  "look": actions.look,
  "pickup": actions.pickup,
  "drop": actions.drop,
  "loot": actions.show_inventory
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
    if (subject is None):
      options[verb]()
    else:
      options[verb](subject)
  except KeyError:
    print("\nInvalid Action: Type ? to get list of actions.")





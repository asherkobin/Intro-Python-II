from item import Item
from room import Room
from player import Player
from termcolor import colored, cprint
from actions import Actions
from rooms import rooms
from inspect import signature
import roomsetup
import textwrap

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
  "loot": actions.show_inventory,
  "inspect": actions.inspect,
  "use": actions.use
}

cash_needed_to_win = 10000

cprint(f"\n Welcome {player.name}.  The story so far... ", "white", attrs=['reverse'])

intro = """You have accumulated a sports gambling debt of $10,000.
 Your bookie is looking for you to collect his money.
 You must find the money needed within 24 hours.
 You decide to explore an abandoned mine hoping to find anything of value to pay your debt."""

hint = "\n" + colored("HINT: ", "white") + "When you pickup an item, you can learn more about it\n      (and discover possible clues) by " + colored("inspect", "green", attrs=["bold", "underline"]) + "ing the item."

print()

for line in textwrap.wrap(intro, 80):
  cprint(line, "cyan")

cprint(hint)

cprint("\nType '?' to list player commands")

cprint(f"\nYou are in the {player.room.name}", "green") 
cprint(player.room.description, "white")

while (True):
  user_action = input("\nAction: ")

  decontructed_command = user_action.split(" ")

  if (len(decontructed_command) == 2):    # eg: pickup key
    action = decontructed_command[0]
    subject = decontructed_command[1]
    function = None
    target = None
  elif (len(decontructed_command) == 4):  # eg: use key on door
    action = decontructed_command[0]
    subject = decontructed_command[1]
    function = decontructed_command[2]
    target = decontructed_command[3]
  else:
    action = decontructed_command[0]      # eg: search
    subject = None

  if (action == "q"):
    break

  try:
    if (subject is None):
      try:
        fn_sig = signature(options[action])
        if len(fn_sig.parameters) > 0:
          cprint("\n" + action + " what?", "red")
        else:
          options[action]()
      except TypeError:
        cprint("\nCommand not recognized.  Type '?' for proper syntax.", "red")
    elif (function is None and target is None):
      try:
        options[action](subject)
      except TypeError:
        cprint(f"\n{action} {subject} on what?", "red")
    else:
      options[action](subject, function, target)
  except KeyError:
    print("\nInvalid Action: Type '?' to get list of actions.")





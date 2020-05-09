from item import Item
from room import Room
from player import Player
from termcolor import colored, cprint

#
# Items can be used on Targets
# Targets can be opened
# Targets cannot be pickedup
#

class Actions():
  def __init__(self, player):
    self.player = player

  def list_commands(self):
    cprint("""
  Movement Commands: n (north), s (south), e (east), w (west), q (quit)

  Room Commands:
  - look (describe your current location)
  - search (search your current location)

  Item Commands:
  - pickup [item_name] (pickup an item that you have found)
  - drop [item_name] (drop an item from your inventory)
  - open [item_name] (opens an object)

  Inventory Commands:
  - loot (displays your inventory)
  - inspect [item_name] (inspect an item)
  - use [item_name] on [target] (use an item on an object)""")

  def print_room_description(self):
    cprint(f"\nYou are in the {self.player.room.name}", "green") 
    cprint(self.player.room.description, "white")

  def north(self):
    try:
      self.player.room = self.player.room.n_to
      self.print_room_description()
    except AttributeError:
      cprint("\n** Blocked **", "red")

  def south(self):
    try:
      self.player.room = self.player.room.s_to
      self.print_room_description()
    except AttributeError:
      cprint("\n** Blocked **", "red")

  def east(self):
    try:
      self.player.room = self.player.room.e_to
      self.print_room_description()
    except AttributeError:
      cprint("\n** Blocked **", "red")

  def west(self):
    try:
      self.player.room = self.player.room.w_to
      self.print_room_description()
    except AttributeError:
      cprint("\n** Blocked **", "red")

  def search(self):
    cprint("\nYou search the area and see...\n", "white")
    if len(self.player.room.items) == 0:
      cprint("\nNothing", "red")
    else:
      for item in self.player.room.items:
        print("- " + colored(item.name, "yellow"))
      for target in self.player.room.targets:
        if (target.include_in_search == True):
          print("- " + colored(target.name, "cyan"))

  def open(self, target_name):
    found_target = None
    for target in self.player.room.targets:
      if target.name == target_name:
        found_target = target
        break
    if found_target == None:
      cprint("\nNo such target.")
    else:
      if (found_target.locked == False):
        found_target.open_action(self.player, found_target)
      else:
        cprint("\nThe " + found_target.name + " is locked.", "red")

  def look(self):
    self.print_room_description()

  def pickup(self, item_name):
    found_item = None
    found_target = None
    for item in self.player.room.items:
      if item.name == item_name:
        found_item = item
        break
    for target in self.player.room.targets:
      if target.name == item_name:
        found_target = item
        break
    if (found_target is not None):
      cprint("\nThe " + item_name + " is too heavy to pickup.")
    elif (found_item is None):
      cprint("\nThere is no " + item_name + " here.")
    elif found_item.can_be_pickedup == False:
      cprint("\nYou cannot pickup the " + colored(item_name, "yellow") + ".")
    else:
      cprint("\nYou picked up the " + colored(item_name, "yellow") + ".")
      self.player.room.items.remove(item)
      self.player.add_item(item)

  def drop(self, item_name):
    found_item = None
    for item in self.player.items:
      if item.name == item_name:
        found_item = item
        break
    if (found_item is None):
      cprint("\nYou do not possess a \033[93m" + item_name)
    else:
      cprint("\nYou dropped the \033[93m" + item_name)
      self.player.room.items.append(item)
      self.player.remove_item(item)

  def show_inventory(self):
    cprint("\nIn your loot bag you have:\n")
    if len(self.player.items) == 0:
      cprint("Nothing", "red")
    else:
      cprint(f"You have ${self.player.get_cash_amount()}")
      for item in self.player.items:
        cprint("- \033[93m" + item.name)

  def inspect(self, item_name):
    found_item = None
    for item in self.player.items:
      if item.name == item_name:
        found_item = item
        break
    if (found_item is None):
      cprint("\nYou do not possess a \033[93m" + item_name)
    else:
      cprint("\n" + found_item.description, "magenta")

#Bug names may be misspelled
  def use(self, item_name, function, target_name):
    found_item = None
    found_target = None
    for item in self.player.items:
      if item.name == item_name:
        found_item = item
        break
    if (found_item is None):
      cprint("\nYou do not possess a \033[93m" + item_name)
    else:
      for target in self.player.room.targets:
        if target.name == target_name:
          found_target = target
          break
      if (found_target is None):
        cprint("\nThis room does not have a " + colored(target_name, "cyan"))
      elif (found_target.item_used_for == found_item.used_for):
        found_target.success_action(self.player, found_target)
      elif (found_target.fail_action != None):
        found_target.fail_action(self.player, found_target)
      else:
        cprint("\nNo Effect", "magenta")

from item import Item
from room import Room
from player import Player
from termcolor import colored, cprint

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
        cprint("- \033[93m" + item.name)

  def look(self):
    self.print_room_description()

  def pickup(self, item_name):
    found_item = None
    for item in self.player.room.items:
      if item.name == item_name:
        found_item = item
        break
    if (found_item is None):
      cprint("\nThere is no " + item_name + " here.")
    else:
      cprint("\nYou picked up the \033[93m" + item_name)
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
        cprint("\nThis room does not have a \033[93m" + target_name)
      elif (found_target.item_used_for == found_item.used_for):
        cprint("\nWorked!", "green")
      else:
        cprint("\nNo Effect", "magenta")

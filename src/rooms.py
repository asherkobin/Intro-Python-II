from room import Room
from item import Item
from target import Target
from termcolor import colored, cprint

items = {
  "brick":
    Item("brick", "An ordinary red brick.  This may be useful to break things.", True, "brick_for_steel_gate"),
  "rusty-key":
    Item("rusty-key", "The key looks like it hasn't been used in decades.", True),
  "dirt":
    Item("dirt", "", False),
  "mystic_stone":
    Item("stone", "Mysterious rune carvings surround the stone.", True),
  "key_for_chest":
    Item("key", "An ordinary key for a padlock", True, "key_for_chest")
}

def steel_grate_use_success(player, target):
  if (target.opened == True):
    cprint("\nThe steel-grate has already been broken open.")
  else:
    target.opened = True
    target.locked = False
    cprint("\nThe brick destroys the rusty lock and the steel-grate is opened.", "magenta")
    rooms["outside"].description = "North of you, the mine entrance is opened."
    rooms["outside"].n_to = rooms["mine-entrance"]

def steel_grate_use_fail(player, target):
  cprint("\nThe steel-grate remains locked.", "magenta")

def steel_grate_open_action(player, target):
  if (target.opened == True):
    cprint("\nThe steel-grate is already opened.")

def chest_unlocked(player, target):
  if (target.locked == False):
    cprint("\nThe chest is already unlocked.")
  else:
    target.locked = False
    cprint("\nYou unlocked the chest, unfortunately the chest was trapped and poison gas caused 10 damage.")

def chest_opened(player, target):
  if (target.opened == True):
    cprint("\nThe chest is empty.")
  else:
    target.opened = True
    cprint("\nYou find 100 twenty-dollar bills wrapped in a currency strap! $2000 is added to your loot bag.")
    player.add_cash(2000)

targets = {
  "steel-grate":
    Target("steel-grate", "brick_for_steel_gate", steel_grate_use_success, steel_grate_use_fail, steel_grate_open_action),
  "chest":
    Target("chest", "key_for_chest", chest_unlocked, None, chest_opened, True)
}

rooms = {
  "outside":
    Room(
      "Outside Mine Entrance",
      "North of you, the mine entrance is blocked by a locked " + colored("steel-grate", "cyan") + colored(".", "white"),
      [items["rusty-key"], items["brick"], items["dirt"]],
      [targets["steel-grate"]]),

  "mine-entrance":
    Room(
      "Mine Entrance",
      "The entrance is full of cobwebs and fallen stone",
      [items["key_for_chest"], items["mystic_stone"]],
      [targets["chest"]]),

  "overlook":
    Room(
      "Grand Overlook",
      "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.",
      [],
      []),

  "narrow":
    Room(
      "Narrow Passage",
      "The narrow passage bends here from west to north. The smell of gold permeates the air.",
      [],
      []),
  
  "treasure":
    Room(
      "Treasure Chamber",
      "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.",
      [],
      []),
}

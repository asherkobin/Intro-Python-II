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
  "stone":
    Item("stone", "Mysterious rune carvings surround the stone.", True),
  "key_for_wooden_door":
    Item("key", "An ordinary key for a padlock", True, "key_for_wooden_door")
}

def steel_grate_opened():
  cprint("\nThe brick destroys the rusty lock and the grate is opened.", "magenta")
  rooms["outside"].description = "North of you, the mine entrance is opened."
  rooms["outside"].n_to = rooms["foyer"]

def wooden_door_unlocked():
  rooms['outside'].n_to = rooms['foyer']

targets = {
  "steel-grate":
    Target("steel-grate", "brick_for_steel_gate", steel_grate_opened),
  "wooden-door":
    Target("wooden-door", "key_for_wooden_door", wooden_door_unlocked)
}

rooms = {
  "outside":
    Room(
      "Outside Mine Entrance",
      "North of you, the mine entrance is blocked by a " + colored("steel-grate", "cyan") + colored(".", "white"),
      [items["rusty-key"], items["brick"], items["dirt"]],
      [targets["steel-grate"]]),

  "foyer":
    Room(
      "Foyer",
      "Dim light filters in from the south. Dusty passages run north and east.",
      [items["key_for_wooden_door"]],
      [targets["wooden-door"]]),

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

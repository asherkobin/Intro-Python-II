from room import Room
from item import Item

items = {
  "rock":
    Item("rock", "Mysterious rune carvings surround the rock"),
  "key":
    Item("key", "An ordinary key for a padlock")
}

rooms = {
  "outside":
    Room(
      "Outside Cave Entrance",
      "North of you, the cave mount beckons",
      [items["rock"], items["key"]]),

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

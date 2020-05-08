# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
  """ Player """
  def __init__(self, name, room):  # self not needed
    self.name = name
    self.room = room
    self.items = []
  
  def add_item(self, item):
    self.items.append(item)

  def remove_item(self, item):
    self.items.remove(item)
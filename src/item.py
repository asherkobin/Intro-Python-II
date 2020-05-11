class Item():
  def __init__(self, name, description, can_be_pickedup = True, used_for = None):
    self.name = name
    self.description = description
    self.can_be_pickedup = can_be_pickedup
    self.used_for = used_for

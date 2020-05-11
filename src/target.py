# refactor so player doesn't have to be passed into Target()

class Target():
  def __init__(self, name, item_used_for, success_action, fail_action = None, open_action = None, include_in_search = False):
    self.name = name
    self.item_used_for = item_used_for
    self.success_action = success_action
    self.fail_action = fail_action
    self.open_action = open_action
    self.include_in_search = include_in_search
    self.opened = False
    self.locked = True

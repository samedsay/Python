class Node:
  def __init__(self, value, link_node = None):
    self.value = value
    self.link_node = link_node
    
  # Getters
  def get_value(self):
    return self.value
    
  def get_link_node(self):
    return self.link_node

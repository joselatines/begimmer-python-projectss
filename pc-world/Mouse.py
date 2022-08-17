from Input_device import Input_device

class Mouse(Input_device):
  counter = 0 
  def __init__(self, brand, input_type):
    Mouse.counter += 1
    self._id = Mouse.counter
    super().__init__(brand, input_type)
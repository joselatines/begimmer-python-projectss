from Input_device import Input_device

class Keyboard(Input_device):
  counter = 0 
  def __init__(self, brand, input_type):
    Keyboard.counter += 1
    self._id = Keyboard.counter
    super().__init__(brand, input_type)
from Input_device import Input_device

class Monitor(Input_device):
  counter = 0 
  def __init__(self, brand, input_type, resolution):
    Monitor.counter += 1
    self._id = Monitor.counter
    super().__init__(brand, input_type, resolution)
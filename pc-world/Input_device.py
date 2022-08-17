class Input_device():
  def __init__(self, brand, type, resolution = False):
    self._brand = brand
    self._type = type
    self._resolution = resolution

  def __str__(self): 
    return f'Brand: {self._brand}, Type: {self._type} Resolution: {self._resolution}' if self._resolution else f'Brand: {self._brand}, Type: {self._type}'
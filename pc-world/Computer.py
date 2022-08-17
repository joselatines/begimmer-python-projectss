from typing import Counter

class Computer(): 
  counter = 0
  def __init__(self, name, monitor, keyboard, mouse):
    Computer.counter += 1
    self._id = Computer.counter
    self._name = name
    self._monitor = monitor
    self._keyboard = keyboard
    self._mouse = mouse

  def __str__(self):
    return f'😀 {self._id} - Pc: {self._name} \n Monitor: {self._monitor} \n Keyboard: {self._mouse} \n Mouse: {self._mouse}'
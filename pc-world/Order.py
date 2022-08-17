from random import randint

class Order:
  orders = []
  def __init__(self, order):
    self._order = order
    self._id = randint(1, 100)
    Order.orders.append(order)

  def __str__(self):
    return f'Order {self._id}: {self._order}'

  def showOrders(self):
    return Order.orders

  def show_orders_str(self):
    str = ''

    for x in Order.orders:
      str += f'Your orders {x}'
     
 
    return f'Your orders {str}'
  
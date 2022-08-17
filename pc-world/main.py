from Computer import Computer
from Keyboard import Keyboard
from Monitor import Monitor
from Mouse import Mouse
from Order import Order
key = Keyboard('kbrand', 'blutu')
mouse = Mouse('Mouawbrand', 'conector')
monitor = Monitor('MGamer', 'blutu', 5000)
monitor2 = Monitor('MsddsdsdsdGamer', 'blutu', 5000)

pc1 = Computer('Prueba', monitor, key, mouse)
pc2 = Computer('Prueba2', monitor2, key, mouse)
order = Order(pc1)
order2 = Order(pc2)

print(order.show_orders_str())
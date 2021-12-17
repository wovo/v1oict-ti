import machine
import time

print( "GPIO blink" )

pin = machine.Pin( 22, machine.Pin.OUT )
while True:
     pin.on()
     time.sleep( 2.0 )
     pin.off()
     time.sleep( 0.1 )

"""
>>> import machine
>>> import time
>>> pin = machine.Pin(0, machine.Pin.OUT)
>>> for i in range(10):
...     pin.on()
...     time.sleep(0.5)
...     pin.off()
...     time.sleep(0.5)
"""
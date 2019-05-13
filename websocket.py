import ctypes
import numpy as np
import asyncio
import websockets
import time

np.set_printoptions(suppress=True)

m = ctypes.cdll.LoadLibrary('./lsm9ds0.so')
gpio = ctypes.cdll.LoadLibrary('./gpio.so')
# m.py_readAccel.restype = c_float

m.py_readAccel.restype = np.ctypeslib.ndpointer(dtype=ctypes.c_float, shape=(6,))


async def light():
  print('light_on')
  
  gpio.open_pin()
  print('turn_on')
  gpio.turn_on()
  await asyncio.sleep(0.5)
  print('turn_off')
  gpio.turn_off()
  print('light_off')
  #gpio.close_pin()
  

async def hello(websocket, path):
  name = await websocket.recv()
  lock = asyncio.Lock()  
  while(True):
      output = m.py_readAccel().tolist()
      #print(output)
      #print(type(output))
      obj = []
      for i in output:
          obj.append(str(i))
      #print(obj)
      await websocket.send(obj[0])
      await websocket.send(obj[1])
      await websocket.send(obj[2])
      await websocket.send(obj[3])
      await websocket.send(obj[4])
      await websocket.send(obj[5])

      jump = await websocket.recv()
      if jump == '1' and lock.locked() == False:

          print("JUMP")
          await lock.acquire()
          await light()
          lock.release()
          
          

start_server = websockets.serve(hello, '192.168.7.2', 8675)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

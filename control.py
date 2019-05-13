import pyautogui
import websockets
import asyncio
import time

# pyautogui.press('space')

print("Hello")


async def handler():
    async with websockets.connect(
            'ws://192.168.7.2:8675') as websocket:
        print("Connected")
        await websocket.send("Works")

        while True:
            ax = await websocket.recv()
            ay = await websocket.recv()
            az = await websocket.recv()
            gx = await websocket.recv()
            gy = await websocket.recv()
            gz = await websocket.recv()
            print("ax:", ax, " ay:", ay, " az:", az)
            print("gx:", gx, " gy:", gy, " gz:", gz)

            thehold = 80
            if float(gx) > thehold or float(gy) > thehold or float(gz) > thehold:
                pyautogui.press('space')  # Dinasour Jump!
                await websocket.send("1")
            else:
                await websocket.send("0")


asyncio.get_event_loop().run_until_complete(handler())

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
            data = await websocket.recv()
            print(data)



asyncio.get_event_loop().run_until_complete(handler())

import asyncio
import websockets

async def listen():
    url = "ws://localhost:8001"
    print("WebSocket Client bağlanıyor:", url)

    async with websockets.connect(url) as ws:
        print("Bağlandı!")

        while True:
            msg = await ws.recv()
            print("Gelen:", msg)

asyncio.run(listen())

import asyncio
import websockets

async def listen():
    uri = "ws://localhost:8001"
    print("WebSocket Client bağlanıyor:", uri)

    async with websockets.connect(uri) as ws:
        print("Bağlandı!")

        while True:
            msg = await ws.recv()
            print("Gelen:", msg)

asyncio.run(listen())

import asyncio
import datetime
import websockets

connected = set()

async def chat(websocket, path):
    global connected
    connected.add(websocket)
    while True:
        recv_text = await websocket.recv()
        print("\n" + recv_text +'\n')
        send_text = datetime.datetime.utcnow().isoformat() + ': ' + recv_text
        print('\n' + send_text + "\n")
        await asyncio.wait([ws.send(send_text) for ws in connected])


start_server = websockets.serve(chat, '10.0.0.178', 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

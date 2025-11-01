import asyncio

_connections = set()

async def register(ws):
    _connections.add(ws)

async def unregister(ws):
    _connections.discard(ws)

async def broadcast(item):
    closed = []
    for ws in list(_connections):
        try:
            await ws.send_json(item)
        except Exception:
            closed.append(ws)
    for w in closed:
        _connections.discard(w)

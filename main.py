import asyncio
from monitor import monitor

# لو uvloop موجود، سيستخدمه، لو مش موجود يتخطاه
try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    print("uvloop غير موجود، سيتم استخدام default asyncio loop")

if __name__ == "__main__":
    asyncio.run(monitor())

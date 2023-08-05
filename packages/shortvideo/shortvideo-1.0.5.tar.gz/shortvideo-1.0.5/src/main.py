import asyncio
import sys
from src.client import Client

async def run():
    client = Client()
    await client.start()
    if client.do_action=='1':
        await client.query('/exit')
        
    print('已退出程序')

def main():
    if sys.version_info.minor>=10:
        asyncio.run(run())
    else:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(run())
    
    


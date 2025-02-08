import asyncio,os
#useful for async programming on io bound tasks(file,db,socket,http)

async def uploade_file():
    print("upload coroutine started")
    #perfom big task of IO
    await asyncio.sleep(3)
    print("upload coroutine ended")

async def download_file():
    print("download coroutine started")
    #perfom big task of IO
    await asyncio.sleep(3)
    print("download coroutine ended")

if __name__ == '__main__':
    print("Main coroutine started")
    loop=asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(uploade_file(),download_file()))
    loop.close()
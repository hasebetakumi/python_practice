# 270. ジェネレーターベースのコルチーン
# def gene_hello():
#     # この書き方だとyieldがなくなってもエラーではなくNoneを出力できる
#     r = yield 'hello'
#     yield r


# g = gene_hello()
# print(next(g))
# print(g.send('plus'))


# 271. yield from文
# def s_hello():
#     yield 'hello1'
#     yield 'hello2'
#     yield 'hello3'


# def gene_hello():
#     while True:
#         r = yield from s_hello()
#         yield r

# # 別の関数からのyieldを受け取るとNoneを表示した後
# # もう一度その関数を呼びなおす

# g = gene_hello()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# 272. コルーチンとネイティブコルーチン
# 以下はコルーチン（python 3.5以前）
# import asyncio

# loop = asyncio.get_event_loop()

# @asyncio.coroutine
# def worker():
#     print('start')
#     # 非同期用のsleep
#     # ここにHTTPリクエストとかを書く
#  　 # ２秒止めてその間にほかの処理を行っている
#     # →yieldを使っているため、処理待ちをさせることができる
#     yield from asyncio.sleep(2)
#     print('stop')


# if __name__ == '__main__':
#     # 配列内に記載できるのはデコレーターでasyncio.coroutineとなっているもののみ
#     loop.run_until_complete(asyncio.wait([worker(), worker()]))
#     loop.close()

# 以下がネイティブコルーチン（python 3.6以降）
# →デコレーター不要
# import asyncio

# loop = asyncio.get_event_loop()


# async def worker():
#     print('start')
#     # 非同期用のsleep
#     # ここにHTTPリクエストとかを書く
#     # ２秒止めてその間にほかの処理を行っている
#     await asyncio.sleep(2)
#     print('stop')


# if __name__ == '__main__':
#     # 配列内に記載できるのはデコレーターでasyncio.coroutineとなっているもののみ
#     loop.run_until_complete(asyncio.wait([worker(), worker()]))
#     loop.close()


# 273. asyncioを使用する場面をイメージする
# →非同期化したい関数の中身はなんでもいいわけではない
# →threadとprocessのときは普通の関数と同じ書き方だったが
# 非同期では専用の書き方をする必要がある
"""
import asyncio


# 以下は今までと同じ→非同期では走らない
import requests
async def hello(url):
    print(requests.get(url).content)

# 以下のように非同期用の書き方をする必要がある
import aiohttp
async def as_hello(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()
            print(response)
"""


# 274. asyncio.Lock
# import asyncio

# loop = asyncio.get_event_loop()

# async def worker1(lock):
#     print('worker1 start')
#     async with lock:
#         print('worker1 got lock')
#         await asyncio.sleep(3)
#     print('worker1 end')


# async def worker2(lock):
#     print('worker2 start')
#     async with lock:
#         print('worker1 got lock')
#         await asyncio.sleep(3)
#     print('worker2 end')


# lock = asyncio.Lock()
# loop.run_until_complete(asyncio.wait([
#     worker1(lock),
#     worker2(lock)
# ]))
# loop.close()


# 275. asyncio.Event
# import asyncio

# loop = asyncio.get_event_loop()


# async def worker1(event):
#     print('worker1 start')
#     # withではなくawaitで待つ！
#     # event_set待ち
#     await event.wait()
#     print('worker1 got event')
#     await asyncio.sleep(3)
#     print('worker1 end')


# async def worker2(event):
#     print('worker2 start')
#     await event.wait()
#     print('worker2 got event')
#     await asyncio.sleep(3)
#     print('worker2 end')


# async def worker3(event):
#     print('worker3 start')
#     await asyncio.sleep(3)
#     print('worker3 end')
#     event.set()


# event = asyncio.Event()
# loop.run_until_complete(asyncio.wait([
#     worker1(event),
#     worker2(event),
#     worker3(event)
# ]))
# loop.close()


# 276. asyncio.Condition
# import asyncio

# loop = asyncio.get_event_loop()


# async def worker1(condition):
#     # withで待つ！
#     async with condition:
#         await condition.wait()
#         print('worker1 start')
#         print('worker1 got condition')
#         await asyncio.sleep(3)
#         print('worker1 end')
#         condition.notify_all()


# async def worker2(condition):
#     async with condition:
#         await condition.wait()
#         print('worker2 start')
#         print('worker2 got condition')
#         await asyncio.sleep(3)
#         print('worker2 end')
#         condition.notify_all()


# async def worker3(condition):
#     async with condition:
#         print('worker3 start')
#         await asyncio.sleep(3)
#         print('worker3 end')
#         condition.notify_all()


# condition = asyncio.Condition()
# loop.run_until_complete(asyncio.wait([
#     worker1(condition),
#     worker2(condition),
#     worker3(condition)
# ]))

# loop.close()


# 278. asyncio.Semaphore
# import asyncio

# loop = asyncio.get_event_loop()


# async def worker1(semaphore):
#     # withで待つ！
#     async with semaphore:
#         print('worker1 start')
#         await asyncio.sleep(3)
#         print('worker1 end')


# async def worker2(semaphore):
#     async with semaphore:
#         print('worker2 start')
#         await asyncio.sleep(3)
#         print('worker2 end')


# # 何個同時に走らせるかを指定する
# semaphore = asyncio.Semaphore(1)
# loop.run_until_complete(asyncio.wait([
#     worker1(semaphore),
#     worker2(semaphore)
# ]))

# loop.close()


# 279. asyncio.Queue
# import asyncio

# loop = asyncio.get_event_loop()


# async def worker1(queue):
#     print('worker1 start')
#     await asyncio.sleep(3)
#     await queue.put(100)
#     print('worker1 end')


# async def worker2(queue):
#     print('worker2 start')
#     # 値が入ってくるのを待つため、lockとかは必要ない
#     x = await queue.get()
#     print(x)
#     print('worker2 end')


# # 何個同時に走らせるかを指定する
# queue = asyncio.Queue()
# loop.run_until_complete(asyncio.wait([
#     worker1(queue),
#     worker2(queue)
# ]))

# loop.close()


# 280. asyncio.Future
# import asyncio

# loop = asyncio.get_event_loop()


# async def f(future):
#     await asyncio.sleep(1)
#     future.set_result('Future is done')


# future = asyncio.Future()
# asyncio.ensure_future(f(future))

# loop.run_until_complete(future)
# print(future.result())
# loop.close()


# 281. asyncio.call_soonとasyncio.call_later
# import asyncio

# loop = asyncio.get_event_loop()


# def hello(name, loop):
#     print('hello {}'.format(name))
#     loop.stop()


# # ３秒後にhelloという関数をmike loopという引数を渡して起動する
# loop.call_later(3, hello, 'mike', loop)
# # すぐに実行したい
# # →mikeが呼ばれる前にloop.stopが起きるので、以下しか実行されない
# loop.call_soon(hello, 'nancy', loop)

# # loop.stopまで動き続ける
# loop.run_forever()
# loop.close()
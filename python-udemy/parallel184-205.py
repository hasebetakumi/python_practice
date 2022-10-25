# 185.スレッド
# 186. スレッドに渡す引数

# import logging
# import threading
# import time

# logging.basicConfig(
#     level=logging.DEBUG, format='%(threadName)s: %(message)s')


# def worker1():
#     logging.debug('start')
#     time.sleep(5)
#     logging.debug('end')


#     logging.debug('start')
#     logging.debug(x)
#     logging.debug(y)
#     time.sleep(5)
#     logging.debug('end')


# if __name__ == '__main__':
#     # 186. スレッドに渡す引数
#     t1 = threading.Thread(name='rename worker1', target=worker1)
#     # argsはタプルで渡す→（）内にカンマが必要
#     t2 = threading.Thread(target=worker2, args=(100, ), kwargs={'y': 200})

#     # t1とt2を同時に走らせる
#     # 関数を同時に走らせている
#     # 関数同士が依存してないなら、同時に走らせたほうが早い？
#     t1.start()
#     t2.start()
#     print('started')


# 187. デーモンスレッド
# import logging
# import threading
# import time

# logging.basicConfig(
#     level=logging.DEBUG, format='%(threadName)s: %(message)s')


# def worker1():
#     logging.debug('start')
#     time.sleep(5)
#     logging.debug('end')


# def worker2():
#     logging.debug('start')
#     time.sleep(2)
#     logging.debug('end')


# if __name__ == '__main__':
#     t1 = threading.Thread(target=worker1)
#     # 先に処理が終わったスレッドのタイミングで終了→遅いほうの関数は強制終了
#     t1.setDaemon(True)
#     t2 = threading.Thread(target=worker2)

#     t1.start()
#     t2.start()
#     print('started')

#     # t1の処理を必ず待たせるための記述（デーモンさせた時のみ記述）
#     # →startには勝手にjoinの機能も入っている
#     t1.join()

# 188. 生存中の Thread オブジェクト全てのリスト
# import logging
# import threading
# import time

# logging.basicConfig(
#     level=logging.DEBUG, format='%(threadName)s: %(message)s')


# def worker1():
#     logging.debug('start')
#     time.sleep(5)
#     logging.debug('end')


# def worker2():
#     logging.debug('start')
#     time.sleep(2)
#     logging.debug('end')


# if __name__ == '__main__':
#     # ５つスレッドを起動
#     for _ in range(5):
#         t = threading.Thread(target=worker1)
#         t.setDaemon(True)
#         t.start()

#     # 生存しているスレッドを取得し表示
#     for t in threading.enumerate():
#         if t is threading.currentThread():
#             print(t)
#             continue
#         t.join()


# 189. タイマー
# import logging
# import threading
# import time

# logging.basicConfig(
#     level=logging.DEBUG, format='%(threadName)s: %(message)s')


# def worker1():
#     logging.debug('start')
#     time.sleep(5)
#     logging.debug('end')


# def worker2():
#     logging.debug('start')
#     time.sleep(2)
#     logging.debug('end')


# if __name__ == '__main__':
#     # 3秒後に開始
#     t = threading.Timer(3, worker1)
#     t.start()


# 190. スレッドのLockとRLock
# →他の関数の処理を待たなければいけない場合、引数が正しく引っ張れないことがある
# import logging
# import threading
# import time

# logging.basicConfig(
#     level=logging.DEBUG, format='%(threadName)s: %(message)s')


# def worker1(d, lock):
#     logging.debug('start')
#     # どこかのスレッドでlockが発生したら、
#     # lockがreleaseされるまで、他の処理が止まる
#     lock.acquire()
#     i = d['x']
#     time.sleep(2)
#     logging.debug(d)
#     lock.release()
#     logging.debug('end')


# def worker2(d, lock):
#     logging.debug('start')
#     # lockはwithでも書ける→releaseいらない
#     with lock:
#         i = d['x']
#         logging.debug(d)
#     logging.debug('end')


# if __name__ == '__main__':
#     d = {'x': 0}
#     # ここのLockをRLockに書き換え→lockの中でlockができるようになる
#     lock = threading.Lock()
#     t1 = threading.Thread(target=worker1, args=(d, lock))
#     t2 = threading.Thread(target=worker2, args=(d, lock))
#     t1.start()
#     t2.start()


# 191. セマフォ→スレッド数をコントロール
# import logging
# import threading
# import time

# logging.basicConfig(
#     level=logging.DEBUG, format='%(threadName)s: %(message)s')


# def worker1(semaphore):
#     with semaphore:
#         logging.debug('start')
#         time.sleep(2)
#         logging.debug('end')


# def worker2(semaphore):
#     with semaphore:
#         logging.debug('start')
#         time.sleep(2)
#         logging.debug('end')


# def worker3(semaphore):
#     with semaphore:
#         logging.debug('start')
#         time.sleep(2)
#         logging.debug('end')


# if __name__ == '__main__':
#     # セマフォの引数でロックをかけるスレッドの数をコントロール
#     semaphore = threading.Semaphore(2)
#     t1 = threading.Thread(target=worker1, args=(semaphore, ))
#     t2 = threading.Thread(target=worker2, args=(semaphore, ))
#     t3 = threading.Thread(target=worker3, args=(semaphore, ))

#     t1.start()
#     t2.start()
#     t3.start()


# 192. キュー→スレッド間でのデータのやり取り
# import logging
# import queue
# import threading
# import time

# logging.basicConfig(
#     level=logging.DEBUG, format='%(threadName)s: %(message)s')


# def worker1(queue):
#     logging.debug('start')
#     queue.put(100) 
#     time.sleep(2)
#     queue.put(200)  # [100, 200]リストのイメージ
#     logging.debug('end')


# def worker2(queue):
#     logging.debug('start')
#     # 一つずつ取り出し→値が入ってなかったら入るまで待ってる
#     # →lockのような機能
#     logging.debug(queue.get())
#     logging.debug(queue.get()) 
#     logging.debug('end')


# if __name__ == '__main__':
#     queue = queue.Queue()
#     t1 = threading.Thread(target=worker1, args=(queue, ))
#     t2 = threading.Thread(target=worker2, args=(queue, ))

#     t1.start()
#     t2.start()


# 192.キューの応用→いろんなところで処理待ちを作る
# import logging
# import queue
# import threading

# logging.basicConfig(
#     level=logging.DEBUG, format='%(threadName)s: %(message)s')


# def worker1(queue):
#     logging.debug('start')
#     while True:
#         item = queue.get()
#         if item is None:
#             break
#         logging.debug(item)
#         # queueの終了報告→join完了
#         # 10回putされたのを検知しているため、
#         # 10回task_doneを呼び出すことでqueueのjoinとなる
#         queue.task_done()
#     logging.debug('longgggggggggggggggggg')
#     logging.debug('end')


# if __name__ == '__main__':
#     queue = queue.Queue()
#     for i in range(10):
#         queue.put(i)
#     t1 = threading.Thread(target=worker1, args=(queue, ))

#     t1.start()

#     logging.debug('tasks are not done')

#     # queueが終わるまでここで待つ
#     queue.join()

#     logging.debug('tasks are done')

#     # noneを入れてwhile文からのbreak許可
#     queue.put(None)

#     # worker1の終了
#     t1.join


# 192. キューの応用→分担作業
# import logging
# import queue
# import threading

# logging.basicConfig(
#     level=logging.DEBUG, format='%(threadName)s: %(message)s')


# def worker1(queue):
#     logging.debug('start')
#     while True:
#         item = queue.get()
#         if item is None:
#             break
#         logging.debug(item)
#         queue.task_done()
#     logging.debug('longgggggggggggggggggg')
#     logging.debug('end')


# if __name__ == '__main__':
#     queue = queue.Queue()
#     for i in range(10000):
#         queue.put(i)
    
#     ts = []

#     # ３つのスレッドで分担
#     for _ in range(3):
#         t1 = threading.Thread(target=worker1, args=(queue, ))
#         t1.start()
#         ts.append(t1)

#     logging.debug('tasks are not done')
#     # 10000回task_doneが呼ばれるのを待つ
#     queue.join()
#     logging.debug('tasks are done')

#     # スレッドの分だけnoneを入れてあげないとbreakできない
#     for _ in range(len(ts)):
#         queue.put(None)

#     # 各スレッドの終了を待つ
#     for t in ts:
#         t.join()


# 193. イベント

# import logging
# import threading
# import time

# logging.basicConfig(
#     level=logging.DEBUG, format='%(threadName)s: %(message)s')


# def worker1(event):
#     # event.set()待ち
#     event.wait()
#     logging.debug('start')
#     time.sleep(3)
#     logging.debug('end')


# def worker2(event):
#     # event.set()待ち
#     event.wait()
#     logging.debug('start')
#     time.sleep(3)
#     logging.debug('end')


# def worker3(event):
#     logging.debug('start')
#     time.sleep(3)
#     logging.debug('end')
#     event.set()


# if __name__ == '__main__':
#     event = threading.Event()
#     t1 = threading.Thread(target=worker1, args=(event, ))
#     t2 = threading.Thread(target=worker2, args=(event, ))
#     t3 = threading.Thread(target=worker3, args=(event, ))

#     t1.start()
#     t2.start()
#     t3.start()


# 194. コンディション→先にwith conditionに入ったら、終わるまで他のは待ってる
# イメージはlock+event
# import logging
# import threading
# import time

# logging.basicConfig(
#     level=logging.DEBUG, format='%(threadName)s: %(message)s')


# def worker1(condition):
#     # withの中でwaitする
#     with condition:
#         condition.wait()
#         logging.debug('start')
#         time.sleep(3)
#         logging.debug('end')


# def worker2(condition):
#     with condition:
#         condition.wait()
#         logging.debug('start')
#         time.sleep(3)
#         logging.debug('end')


# def worker3(condition):
#     with condition:
#         logging.debug('start')
#         time.sleep(3)
#         logging.debug('end')
#         condition.notifyAll()


# if __name__ == '__main__':
#     condition = threading.Condition()
#     t1 = threading.Thread(target=worker1, args=(condition, ))
#     t2 = threading.Thread(target=worker2, args=(condition, ))
#     t3 = threading.Thread(target=worker3, args=(condition, ))

#     t1.start()
#     t2.start()
#     t3.start()


# 195. バリア
# import logging
# import threading
# import time

# logging.basicConfig(
#     level=logging.DEBUG, format='%(threadName)s: %(message)s')


# def worker1(barrier):
#     # Barrierで指定した値の数だけbarrier.waitが呼ばれたら次に進む
#     # トラブルで何かが立ち上がらなかったときに、全ての処理を停止させられる
#     r = barrier.wait()
#     logging.debug('num={}'.format(r))
#     while True:
#         logging.debug('start')
#         time.sleep(3)
#         logging.debug('end')


# def worker2(barrier):
#     r = barrier.wait()
#     logging.debug('num={}'.format(r))
#     while True:
#         logging.debug('start')
#         time.sleep(3)
#         logging.debug('end')


# if __name__ == '__main__':
#     # スレッドが２個立ち上がるまで次に進まない
#     barrier = threading.Barrier(2)
#     t1 = threading.Thread(target=worker1, args=(barrier, ))
#     t2 = threading.Thread(target=worker2, args=(barrier, ))

#     t1.start()
#     t2.start()


# 196. マルチプロセス
"""
スレッドの
lock rlock semaphore queue event condition barrier
はまったく同じ
"""

# 197. ワーカープロセスのプールで非同期
# import logging
# import multiprocessing
# import time

# logging.basicConfig(
#     level=logging.DEBUG, format='%(processName)s: %(message)s')


# def worker1(i):
#     logging.debug('start')
#     time.sleep(3)
#     logging.debug('end')
#     return i


# if __name__ == '__main__':
#     # poolに入れた引数分しかプロセスを走らせられない
#     with multiprocessing.Pool(1) as p:
#         p1 = p.apply_async(worker1, (100, ))
#         p2 = p.apply_async(worker1, (100, ))
#         logging.debug('executed')

#         # 値をgetできるまで待つ
#         # タイムエラーも設定できる
#         logging.debug(p1.get(timeout=10))
#         logging.debug(p2.get())


# 198. ワーカープロセスのプールでブロック
# import logging
# import multiprocessing
# import time

# logging.basicConfig(
#     level=logging.DEBUG, format='%(processName)s: %(message)s')


# def worker1(i):
#     logging.debug('start')
#     time.sleep(3)
#     logging.debug('end')
#     return i


# if __name__ == '__main__':
#     with multiprocessing.Pool(3) as p:
#         # 下の一行がブロック→この１行の処理が終わるまで次に行かない
#         logging.debug(p.apply(worker1, (200, )))

#         p1 = p.apply_async(worker1, (100, ))
#         p2 = p.apply_async(worker1, (100, ))
#         logging.debug('executed')

#         logging.debug(p1.get(timeout=10))
#         logging.debug(p2.get())


# 199. ワーカープロセスのプールとマップ
# import logging
# import multiprocessing
# import time

# logging.basicConfig(
#     level=logging.DEBUG, format='%(processName)s: %(message)s')


# def worker1(i):
#     logging.debug('start')
#     time.sleep(3) 
#     logging.debug('end')
#     return i * 2


# if __name__ == '__main__':
#     with multiprocessing.Pool(3) as p:
#         # map→asyncの書き方を短縮できる→リストで渡すだけでその分起動できる
#         # →for文を回さなくてよい
#         # 返り値もリストで受け取る
#         # map_asyncとすると、返り値の代入を待たずに次の行へ
#         # →getで止めておいて表示させる
#         r = p.map(worker1, [100, 200])
#         logging.debug(r)
#         # p1 = p.apply_async(worker1, (100, ))
#         # p2 = p.apply_async(worker1, (100, ))
#         logging.debug('executed')

#         # imapにすると定義だけ行う
#         # →必要な時にループで呼び出す
#         r = p.imap(worker1, [100, 200])
#         logging.debug(r)
#         logging.debug('executed')
#         for i in r:
#             logging.debug(i)
    

# 201. パイプ
# import logging
# import multiprocessing
# import time

# logging.basicConfig(
#     level=logging.DEBUG, format='%(processName)s: %(message)s'
# )


# def f(conn):
#     # child_connに送る
#     # →child_conn.recv()で受け取る
#     conn.send(['test'])
#     # すでに送っているので、関数終了まで５秒かかるが、recvから先が走る
#     time.sleep(5)
#     conn.close()


# if __name__ == '__main__':
#     parent_conn, child_conn = multiprocessing.Pipe()
#     p = multiprocessing.Process(target=f, args=(parent_conn, ))
#     p.start()

#     # ここでjoinしてしまうと、既にsendされているのに関数終了を待ってしまう
#     # p.join()
#     logging.debug(child_conn.recv())


# 202. プロセス間での共有メモリ（value array）
# import logging
# import multiprocessing

# logging.basicConfig(
#     level=logging.DEBUG, format='%(processName)s: %(message)s'
# )


# def f(num, arr):
#     logging.debug(num)
#     num.value += 1.0
#     logging.debug(arr)
#     # 標準のリストではなく共有メモリ特有のリストになっている
#     # →arrをfor文で展開できないため、インデックスを指定して引っ張らないといけない
#     for i in range(len(arr)):
#         arr[i] *= 2


# if __name__ == '__main__':
#     num = multiprocessing.Value('f', 0.0)
#     arr = multiprocessing.Array('i', [1, 2, 3, 4, 5])

#     p1 = multiprocessing.Process(target=f, args=(num, arr))
#     p2 = multiprocessing.Process(target=f, args=(num, arr))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     logging.debug(num.value)
#     logging.debug(arr[:])


# 203. マネージャー→value arrayはpythonの記述とは少し異なる
# →managerならpythonに近い文法を使える
# 欠点はvalue arrayより遅い
# import logging
# import multiprocessing

# logging.basicConfig(
#     level=logging.DEBUG, format='%(processName)s: %(message)s'
# )


# def worker1(l, d, n):
#     l.reverse()
#     d['x'] += 1
#     n.y += 1


# if __name__ == '__main__':
#     with multiprocessing.Manager() as manager:
#         l = manager.list()
#         d = manager.dict()
#         n = manager.Namespace()

#         l.append(1)
#         l.append(2)
#         l.append(3)

#         d['x'] = 0

#         n.y = 0

#         p1 = multiprocessing.Process(target=worker1, args=(l, d, n))
#         p2 = multiprocessing.Process(target=worker1, args=(l, d, n))
        
#         p1.start()
#         p2.start()
        
#         p1.join()
#         p2.join()

#         logging.debug(l)
#         logging.debug(d)
#         logging.debug(n)


# 205. 高水準のインタフェース
# concurrent.futures→簡単な並列化であればこれを使ったほうが楽
import concurrent.futures
import logging

# まずはスレッド

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s'
)


def worker(x, y):
    logging.debug('start')
    r = x * y
    logging.debug(r)
    logging.debug('end')
    return r


def main():
    # スレッドを５つまで同時に走らせる
    # ここをProcessに書き換えるだけ！！
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as execuor:
        # 関数と引数を指定して走らせる
        f1 = execuor.submit(worker, 2, 5)
        f2 = execuor.submit(worker, 2, 5)
        logging.debug(f1.result())
        logging.debug(f2.result())

        # mapも使える
        args = [[2, 2], [2, 5], [100, 250]]
        r = execuor.map(worker, *args)
        logging.debug(r)
        logging.debug([i for i in r])


if __name__ == '__main__':
    main()
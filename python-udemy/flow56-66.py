# 56.クロージャー
# def outer(a, b):

#     def inner():
#         return a + b

#     return inner

# f = outer(1 ,2)
# r = f()
# print(r)


# def circle(pi):
#     """
#         円周率を先に複数決めて、半径で場合分けしたい
#     """
#     def area(radius):
#         return pi * radius * radius

#     return area

# cal = circle(3.14)
# cal2 = circle(3)

# print(cal(10))
# print(cal2(10))


# 57.デコレーター
# def print_info(func):
#     def wrapper(*args, **kwargs):
#        print('start')
#        result = func(*args, **kwargs)
#        print('end')
#        return result
#     return wrapper

# def add_num(a, b):
#     return a + b

# f = print_info(add_num)
# r = f(10, 20)
# print(r)

# # 上記の処理だと分かりにくいから以下のようにする
# def print_info(func):
#     def wrapper(*args, **kwargs):
#        print('start')
#        result = func(*args, **kwargs)
#        print('end')
#        return result
#     return wrapper

# # 受け取った関数の情報を公開するデコレーター→便利！！
# def print_more(func):
#     def wrapper(*args, **kwargs):
#        print('function: ', __name__)
#        print('args: ', args)
#        print('kwargs: ', kwargs)
#        result = func(*args, **kwargs)
#        print('result: ', result)
#        return result
#     return wrapper

# # 順序大事
# @print_info
# @print_more
# def add_num(a, b):
#     return a + b

# r = add_num(10, 20)
# print(r)

# # print_infoを一度定義してあるので、何回でも同じ処理を使うことができる
# # @print_info
# # def square(a,b):
# #     return a * b

# # print(square(10, 20))


# 58.ラムダ
# l = ['Mon', 'tue', 'Wed']

# def change_words(words, func):
#     for word in words:
#         print(func(word))

# # capital = lambda word: word.capitalize()
# # change_words(l, capital)

# """
# 引数とする関数が1行で終わる処理であれば
# ラムダを使ってそのまま送ってあげる

# →コード量の削減とファンクション数を抑えられる
# """
# change_words(l, lambda word: word.capitalize())


# 59.ジェネレーター
# l = ['morning', 'afternoon', 'night']

# for i in l:
#     print(i)

# print('#################################')

# def greet():
#     yield 'morning'
#     yield 'afternoon'
#     yield 'night'

# for g in greet():
#     print(g)

# print('#################################')


# g = greet()
# print(next(g)) # yield 'morning'だけ処理して抜ける
# print('aa')
# print(next(g))


# def counter(num=10):
#     for _ in range(num):
#         yield 'run'


# """
# いろんなジェネレーターから好きな順番で呼び出すことができる

# yieldの間に重い処理をはさむことで
# 重い処理を小分けにして実行することができる
# """
# c = counter()
# print(next(c))
# print(next(g))


# 60.リスト内包表記 for文を3個以上内包するのは見づらいのでやめる
# t = (1,2,3,4,5)

# r = []

# for i in t:
#     if i % 2 ==0:
#         r.append(i)

# print(r)

# # 上記のタプルからリストへの移動を一行で書くことができる
# # コード量減かつ使用メモリの削減
# rr = [i for i in t if i % 2 == 0]
# print(rr)

# # tから取ってきたiとt2から取ってきたjをかけてrrrに入れる
# t2 = (5,6,7,8,9)
# rrr = [i * j for i in t for j in t2]
# print(rrr)


# 61.辞書内包表記
# w = ['mon', 'tue', 'wed']
# f = ['coffee', 'milk', 'water']

# d = {}
# for x, y in zip(w, f):
#     d[x] = y

# print(d)

# # 上記の処理を短く
# dd = {x: y for x, y in zip(w, f)}
# print(dd)


# 62.集合内包表記
# s = set()

# for i in range(10):
#     s.add(i)

# print(s)

# ss = {i for i in range(10)}
# print(ss)


# 63.ジェネレーター内包表記
# def g():
#     for i in range(10):
#         yield i

# g = g()
# print(type(g))
# print(next(g))


# gg = (i for i in range(10) if i % 2 ==0)
# print(type(gg))
# print(next(gg))
# print(next(gg))
# print(next(gg))

# # タプルの時はtupleと明記する必要あり
# ggg = tuple(i for i in range(10) if i % 2 ==0)
# print(type(ggg))
# print(ggg)


# 64.名前空間とスコープ
# animal = 'cat'
# print(animal)

# def f():
#     print(animal)
#     # animal = 'dog' # print(animalが関数内のanimalを見に行ってしまうためエラー)

# def g():
#     # global animal
#     animal = 'dog'
#     print(animal)
#     print(locals())

# f()
# g()
# print(globals())


# 65.例外処理
# l = [1,2,3]
# i = 5

# try:
#     l[0]
# except IndexError as exc:
#     print("dont worry: {}".format(exc))
# except NameError as ex:
#     print(ex)
# except Exception as all: # →全てのエラーを拾ってプログラムを進める→よろしくない
#     print('その他のエラーです', all)
# else:
#     print('エラーが発生しなかったときに実行されます')
# finally:
#     print('これは必ず実行されます（エラーの有無を問わず）')

# print('エラーが起きてもプログラムを進めることができる')

# """
# https://docs.python.org/3/library/exceptions.html
# のException hierarchyに一覧がある
# """


# 66.独自例外の作成
from tabnanny import check
class UpperCaseError(Exception):
    """
    Exceptionクラスを継承した
    UpperCaseErrorという自作のエラー
    """
    pass 

def check():
    num = ['AA','bb','cc','dd']
    for n in num:
        if n.isupper():
            raise UpperCaseError(n)

try:
    check()
except UpperCaseError as a:
    print(a, 'は小文字ではありません')


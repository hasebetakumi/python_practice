# 67.コマンドライン引数
# """
# dir: 現在のファイル情報を表示
# ls
# """

# import sys
# print(sys.argv)

# """
# module67-.py aaa
# のようにパイソンファイルの実行の後ろの文字列を
# プログラム内で使用することができる
# """


# 68.import文とas
# # 下の書き方が望ましい→モジュールを定義して、その都度その中の関数を呼び出す
# # asもできれば使わないほうがいい→どっからきた関数なのかが分からなくなる
# from lesson_package import import68 as i
# r = i.say('hello')
# print(r)

# # 以下の書き方は望ましくない→どっからきた関数なのかが分からなくなる
# from lesson_package.import68 import say
# r = say('good')
# print(r)


# 69.絶対パスと相対パスのimport
# # 絶対パス
# from lesson_package.pass_practice_69 import import69

# r = import69.sing()
# print(r)

# # 相対パス→現在のディレクトリを示す、. 以外は使わないようにする
# """
# . :現在のディレクトリ
# .. :一個上のディレクトリ
# """


# 70.アスタリスクのインポートと__init__.pyと__all__の意味
# # from lesson_package.pass_practice_69 import import69
# # from lesson_package.pass_practice_69 import import70

# # 呼び出したいディレクトリの__init__.pyに__all__でファイルを指定する
# # 使用は避けるべき→どのファイルを呼び出したのかが分からない
# from lesson_package.pass_practice_69 import *

# print(import70.cry())
# print(import70.sing())


# 71.importErrorの使いどころ
# """ 例 パッケージをダウンロードして使う場合
# tryに古いバージョンを指定
# exceptに新しいバージョンを指定して
# バージョンが変わっても動くようにしておく
# """
# try:
#     from lesson_package import import70
# except ImportError:
#     from lesson_package.pass_practice_69 import import70

# print(import70.cry())


# 72.setup.pyでパッケージ化して配布する
# pycharmだと作成ツールがあるためノーコードで作成可能
# 以下はvscodeのやり方
# https://qiita.com/SolKul/items/9208163c79dc4002733c


# 73.組み込み関数　sort
# # これがもともと入っている関数
# # https://docs.python.org/ja/3/library/functions.html

# l = {
#     'A': 100,
#     'B': 76,
#     'C': 98
# }

# print(sorted(l))
# # lのgetをした100で並べ替え
# print(sorted(l, key=l.get))

# # 降順にする
# print(sorted(l, key=l.get, reverse=True))


# 74.標準ライブラリ
# # https://docs.python.org/ja/3/library/index.html

# s = "aweliuahliajjolijriguaikejapo"

# d = {}
# for c in s:
#     if c not in d:
#         d[c] = 0
#     d[c] += 1
# print(d)

# d = {}
# for c in s:
#     d.setdefault(c, 0)
#     d[c] += 1
# print(d)


# from collections import defaultdict
# d = defaultdict(int)
# for c in s:
#     d[c] += 1
# print(d)

# print(d['f'])


# 75.サードパーティーのライブラリ
# # https://pypi.org/
# # pycharmだと簡単
# # コンソールからだとpip install termcolor

# from termcolor import colored

# print(colored('test', 'red'))


# 76.importする際の記述の仕方
# """
# カンマで複数読み込めるが望ましくない
# アルファベット順で読み込む
# サードパーティーを入れるときは1行空ける
# 自分たちで作ったものはさらに1行空ける
# 最後はローカルファイル
# """
# # 標準ライブラリ
# import collections
# import os
# import sys

# # サードパーティー
# import termcolor

# # 自作ライブラリ
# import lesson_package

# # ローカルファイル
# # import aaa

# # ライブラリがどこにあるか
# print(collections.__file__)
# print(lesson_package.__file__)

# # pythonがどこから読み取るか
# print(sys.path)


# 77.__name__ __main__
# # importされていない、最初に読み込まれるファイル→__main__
# print(__name__)

# # importされる側で、importされたときには実行したくない処理
# # 生で関数を配置しておくと、importされたときに実行されてしまう。
# if __name__ == "__main__":
#     print('今はメインです')




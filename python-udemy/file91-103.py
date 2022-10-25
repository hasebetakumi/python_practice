# 91.ファイルの作成
# # openメソッドは対象ファイルがない場合は新規登録
# """
# w  書き換え（open時に内部消去）
# w+ 書き換え読み込み（open時に内部消去）
# a  追記
# r  読み込み
# 
# """
# f = open('test.txt', 'a')
# f.write('Test')

# # これでも書き込めるbut基本はwriteを用いる
# print('print', file=f)
# # このようにオプションが付けられて便利
# print('my', 'name', 'is', 'mike', sep='#', end='!', file=f)

# f.close()

# # fileがopenされていないと書き込めないため、以下を実行しても何も起こらない
# # print('print', file=f)


# 92.withステートメントでファイルをopenする
# # →こっちを使うのが適切→勝手にcloseしてくれるから
# with open('test.txt', 'w') as f:
#     f.write('92\n')


# 93.ファイルの読み込み
# s = """\
# AAA
# BBB
# CCC
# """

# with open('test.txt', 'w') as f:
#     f.write(s)

# with open('test.txt', 'r') as f:
#     # # readは全て読み取り、readlineは一行ずつ読み取り
#     # print(f.read())
#     while True:
#         line = f.readline()
#         print(line)
#         if not line:
#             break

# # ２文字ずつ読み取り→chunkごとに読み取り
# with open('test.txt', 'r') as f:
#     while True:
#         chunk = 2
#         line = f.read(chunk)
#         print(line)
#         if not line:
#             break


# 94.seekを使って移動する
# s = """\
# AAA
# BBB
# CCC
# """

# with open('test.txt', 'r') as f:
#     # tellでファイル内のどこにカーソルがあるか調べる
#     print(f.tell())
#     print(f.read(1))
#     f.seek(5)
#     print(f.read(1))
#     f.seek(8)
#     print(f.read(1))
#     f.seek(15)
#     print(f.read(1))


# 95.読み込み書き込みモード（w+）
# s = """\
# AAA
# BBB
# CCC
# DDD
# """

# # w w+は書き換えのため、ファイルを開いた瞬間にファイル内が消去される
# with open('test.txt', 'w+') as f:
#     f.write(s)
#     # ページの先頭に戻った後に読み込む
#     f.seek(0)
#     print(f.read())

# # r+はまず読み込みのため、存在しないファイルは指定できない
# with open('test.txt', 'r+') as f:
#     print(f.read())
#     f.seek(20)
#     f.write('abc')


# 96.テンプレート
# import string

# # 以下の内容を別ファイルに置いて、withで呼び込むことも可能
# # with内の変数はwith外でも使用可能
# s = """\

# hi $name

# $contents

# have a good day
# """

# # templateにすると読み込み専用
# # →sを直接書き換えてしまうことがない
# t = string.Template(s)
# content = t.substitute(name='mike', contents='how are you?')
# print(content)


# 97.csvファイルへの書き込みと読み込み
# import csv

# with open('test.csv', 'w', newline='') as csv_file:
#     fieldnames = {'Name', 'Count'}
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'Name': "A", 'Count': 1})
#     writer.writerow({'Name': "B", 'Count': 2})
#     writer.writerow({'Name': "C", 'Count': 3})

# with open('test.csv', 'r', newline='') as csv_file:
#     reader = csv.DictReader(csv_file)
#     for row in reader:
#         print(row)


# 98.ファイル操作
# import os

# # 存在しているか
# print(os.path.exists('test.txt'))

# # ファイルかどうか
# print(os.path.isfile('test.txt'))

# # ディレクトリかどうか
# print(os.path.isdir('test.txt'))

# # 名前変更
# if os.path.isfile('test.txt'):
#     os.rename('test.txt', 'renamed.txt')

# # シムリンク（renamedにリンクさせてる→symlinkを変更するとrenamedも変更される）
# # os.symlink('renamed.txt', 'symlink.txt')

# # ディレクトリを作る→すでに同じ名前がある場合は作成されない
# if not os.path.exists('test_dir'):
#     os.mkdir('test_dir')
#     print('ディレクトリ作成')

# # ディレクトリを削除する※中身が空のときのみ削除できる
# os.rmdir('test_dir')

# # 空のファイル作成
# import pathlib
# pathlib.Path('empty.txt').touch()
# print('空ファイル作成')

# # ファイル削除
# os.remove('empty.txt')

# # 階層の奥にも作成できる
# os.mkdir('test_dir')
# os.mkdir('test_dir/test_dir2')

# # 指定したディレクトリの中に何のディレクトリがあるか
# print(os.listdir('test_dir'))

# # 指定したディレクトリの中に何のファイルがあるか
# import glob
# print(glob.glob('test_dir/test_dir2/*'))

# # ファイルのコピー
# import shutil
# shutil.copy('test_dir/test_dir2/empty.txt',
#             'test_dir/test_dir2/empty.txt2')

# # 中身が入ってるディレクトリを削除する
# # 重要ファイルを削除してしまう恐れあり！！！
# shutil.rmtree('test_dir')

# # 現在のパスを取得
# print(os.getcwd())


# 99.tarfileの圧縮展開→linux macでの圧縮ファイル
# import tarfile

# # 圧縮（test_tar99というディレクトリをtest.tar.gzという名前で圧縮）
# # with tarfile.open('test.tar.gz', 'w:gz') as tr:
# #     tr.add('test_tar99')

# # 全て展開（test.tar.gzという圧縮ファイルをtest_tarというディレクトリ内で展開）
# with tarfile.open('test.tar.gz', 'r:gz') as tr:
#     # tr.extractall(path='test_tar')

#     # 展開せずに中身を確認する方法
#     with tr.extractfile('test_tar99/test_tar.txt') as f:
#         print(f.read())


# 100.zipfileの圧縮展開
# import glob
# import zipfile

# # 圧縮
# # with zipfile.ZipFile('test.zip', 'w') as z:
# #     # ファイル名まで指定しないといけない
# #     # z.write('test_tar99/test_tar.txt')
# #     # for文と**で全てを入れてあげる処理
# #     for f in glob.glob('test_tar99/**', recursive=True):
# #         print(f)
# #         z.write(f)

# # 展開
# with zipfile.ZipFile('test.zip', 'r') as z:
#     z.extractall('zzz')


# 101.tempfile→一時ファイル→使い終わった後自動消去
# import tempfile

# with tempfile.TemporaryFile(mode='w+') as t:
#     t.write('hello')
#     t.seek(0)
#     print(t.read())

# # temporaryファイルを保存したい
# with tempfile.NamedTemporaryFile(delete=False) as t:
#     # テンポラリーファイルのパス
#     # C:\Users\t-hasebe\AppData\Local\Temp\ に作られる
#     print(t.name)
#     with open(t.name, 'w+') as f:
#         f.write('test\n')
#         f.seek(0)
#         print(f.read())

# # ディレクトリもできる→圧縮前提のバッファーとして利用


# 102.subprocessでコマンドを実行する→エラーばかりなので対策必要
# import subprocess

# # subprocess.run(['ls'])

# # shell=True→どんなコマンドでも実行できる→セキュリティ面から非推奨
# # subprocess.run('ls', shell=True)

# # 一応パイプを使った処理も可能


# 103.datetime
# import datetime

# now = datetime.datetime.now()
# print(now)
# print(now.isoformat())
# print(now.strftime('%d/%m/%y'))

# today = datetime.date.today()
# print(today)

# t = datetime.time(hour=1, minute=10,second=5, microsecond=100)
# print(t)
# print(t.isoformat())

# print(now)
# d = datetime.timedelta(weeks=1)
# print(now + d)
# print(now - d)

# import time
# print('aaa')
# time.sleep(2)
# print('aaa')

# # エポックタイム→1970年1月1日午前0時0分0秒からの秒数
# print(time.time())


# 135. SQLite
# import sqlite3

# conn = sqlite3.connect('test_aqlite.db')

# # cursにカーソルを入れる→cursにいろんな作業をさせる
# curs = conn.cursor()

# # curs.execute(
# #    'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING )')

# # # commitをすると反映される
# # conn.commit()

# # # データ入れる
# # curs.execute(
# #     'INSERT INTO persons(name) values("mike")'
# # )
# # # またコミットする
# # conn.commit()

# # curs.execute('SELECT * FROM persons')
# # print(curs.fetchall())

# # curs.execute('UPDATE persons set name = "michel" WHERE name = "mike"')
# # conn.commit()

# curs.execute('DELETE FROM persons WHERE name = "michel"')
# conn.commit()

# # カーソルもクローズする
# curs.close()
# conn.close()


# 138
from curses import echo
from inspect import stack
import mysql.connector

# データベース作成
# conn = mysql.connector.connect(host='127.0.0.1', user='root')

# cursor = conn.cursor()

# cursor.execute(
#     'CREATE DATABASE test_mysql_database'
# )

# cursor.close()
# conn.close()

# テーブル作成
# conn = mysql.connector.connect(host='127.0.0.1', user='root', database='test_mysql_database')
# cursor = conn.cursor()
# cursor.execute(
#     'CREATE TABLE persons('
#     'id int NOT NULL AUTO_INCREMENT,'
#     'name varchar(14) NOT NULL,'
#     'PRIMARY KEY(id))'
# )
# conn.commit()
# cursor.close()
# conn.close()

# データ保存
# conn = mysql.connector.connect(host='127.0.0.1', user='root', database='test_mysql_database')
# cursor = conn.cursor()
# cursor.execute(
#     'INSERT INTO persons(name) values("Mike")'
# )
# conn.commit()

# cursor.execute('SELECT * FROM persons')
# for row in cursor:
#     print(row)

# cursor.close()
# conn.close()


# 138.sqlAlchemy→オブジェクト指向の中でデータベースを操作する（オブジェクトを作ってからaddしたりする）
# # DBの変更時にコードを変えなくて済む！！！
# import pymysql
# import sqlalchemy
# import sqlalchemy.ext.declarative
# import sqlalchemy.orm

# # 今回はメモリ上のデータベースを用いる→echoをオンにすると実行したsql文が全て表示される
# # engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)
# # :memory:のところを変えてあげれば、その名前のファイルができる
# # engine = sqlalchemy.create_engine('sqlite:///sqlite139.db', echo=True)
# # 新規に作ったmysqlのデータベースを指定するとmysqlにもそのままのコードでアクセスできる（どうやってrootでログインする？）
# engine = sqlalchemy.create_engine('mysql+pymysql:///root:test_mysql_database2')

# Base = sqlalchemy.ext.declarative.declarative_base()

# class Person(Base):
#     __tablename__ = 'persons'
#     id = sqlalchemy.Column(
#         sqlalchemy.Integer, primary_key=True, autoincrement=True
#     )
#     name = sqlalchemy.Column(
#         sqlalchemy.String(14)
#     )

# # Baseを継承したクラスのメタデータをエンジンを使ってcreate_allしてください
# Base.metadata.create_all(engine)

# # 以下はメモリ上のデータベースを見にいくための記述
# Session = sqlalchemy.orm.sessionmaker(bind=engine)
# session = Session()

# # create
# person = Person(name='mike')
# session.add(person)
# p1 = Person(name='nancy')
# session.add(p1)
# session.commit()

# # update
# p4 = session.query(Person).filter_by(name='mike').first()
# p4.name = 'michel'
# session.add(p4)
# session.commit()

# # delete
# p5 = session.query(Person).filter_by(name='nancy').first()
# session.delete(p5)
# session.commit()

# # 以下はメモリ上のデータベースを見にいくための記述
# persons = session.query(Person).all()
# for person in persons:
#     print(person.id, person.name)


# 140.DBMデータベース→pythonの標準ライブラリ
# # integerは入れられない！！　文字列のみ！！
# import dbm

# # cacheというdbがなかったら'c'reate
# # with dbm.open('cache', 'c') as db:
# #     db['key1'] = 'value1'

# # 取り出し
# with dbm.open('cache', 'r') as db:
#     print(db.get('key1'))


# 141.memcached→キャッシュ保存によりデータベースとのやりとりを減らす

# 142.pickle→pythonのデータをそのまま保存
# import pickle

# class T(object):
#     def __init__(self, name):
#         self.name = name

# data = {
#     'a': [1,2,3],
#     'b': ('test', 'test'),
#     'c': {'key': 'value'},
#     'd': T('test')
# }

# with open('data.pickle', 'wb') as f:
#     pickle.dump(data, f)

# with open('data.pickle', 'rb') as f:
#     data_loaded = pickle.load(f)
#     print(data_loaded)
#     print(data_loaded['d'].name)


# 145. mongodb→jsonでぶちこむ→nonSQL
# import datetime
# from pymongo import MongoClient

# client = MongoClient('mongodb://localhost:27017/')
# db = client['test_database']

# stack1 = {
#     'name': 'c1',
#     'pip': ['python', 'java'],
#     'info': {'os': 'mac'},
#     'data': datetime.datetime.utcnow()
# }

# stack2 = {
#     'name': 'c2',
#     'pip': ['python', 'java'],
#     'info': {'os': 'windows'},
#     'data': datetime.datetime.utcnow()
# }

# # データ保存
# db_stacks = db.stacks
# stack_id = db_stacks.insert_one(stack1).inserted_id

# print(stack_id, type(stack_id))

# print(db_stacks.find_one({'_id': stack_id}))

# # データ検索→idをobjectID型に変えないと入れられない
# from bson.objectid import ObjectId
# str_stack_id = '635501167d14ffaffa0dcc9d'
# print(db_stacks.find_one({'_id': ObjectId(str_stack_id)}))

# print(db_stacks.find_one({'name': 'c1'}))

# # update
# db_stacks.find_one_and_update(
#     {'name': 'c1'}, {'$set': {'name': 'YYY'}}
# )

# print(db_stacks.find_one({'name': 'YYY'}))
# print('#############')


# # delete
# db_stacks.delete_many({'name': 'YYY'})

# print(db_stacks.find_one({'name': 'YYY'}))


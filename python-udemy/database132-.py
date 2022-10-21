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

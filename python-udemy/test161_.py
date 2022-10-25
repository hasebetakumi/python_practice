# 161. doctest→関数のドキュメントに書く→関数の使い方も提示できる
# class Cal(object):
#     def add_double(self, x, y):
#         """ Add and Double
        
#         >>> c = Cal()
#         >>> c.add_double(1, 1)
#         4

#         エラー内容でもひっかけられる
#         >>> c.add_double('1', '1')
#         Traceback (most recent call last):
#         ...
#         ValueError
#         """

#         if type(x) is not int or type(y) is not int:
#             raise ValueError
#         result = x + y
#         result *= 2
#         return result


# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()


# 162. Unittest
# import unittest


# class Cal(object):
#     def add_double(self, x, y):
#         if type(x) is not int or type(y) is not int:
#             raise ValueError
#         result = x + y
#         result *= 2
#         return result


# # unittestを継承して、以下の中にテストを書いていく→基本は別ファイルで作成する
# class CalTest(unittest.TestCase):
#     def test_add_double(self):
#         cal = Cal()
#         self.assertEqual(
#             cal.add_double(1, 1), 4
#         )


# if __name__ == "__main__":
#     unittest.main()


# 163. Unittestで例外テスト
# import unittest


# class Cal(object):
#     def add_double(self, x, y):
#         if type(x) is not int or type(y) is not int:
#             raise ValueError
#         result = x + y
#         result *= 2
#         return result


# class CalTest(unittest.TestCase):
#     def test_add_double(self):
#         cal = Cal()
#         self.assertEqual(
#             cal.add_double(1, 1), 4
#         )

#     # 以下が例外テスト
#     def test_add_double_raise(self):
#         cal = Cal()
#         # この関数を起動したらこのエラーが起きます
#         with self.assertRaises(ValueError):
#             cal.add_double('1', '1')


# if __name__ == "__main__":
#     unittest.main()


# 164. Unittestのsetupとteardown→テストの前後に処理をしたい
# import unittest


# class Cal(object):
#     def add_double(self, x, y):
#         if type(x) is not int or type(y) is not int:
#             raise ValueError
#         result = x + y
#         result *= 2
#         return result


# class CalTest(unittest.TestCase):
#     def setUp(self):
#         print('事前処理')
#         self.cal = Cal()

#     def tearDown(self):
#         print('終了')

#     def test_add_double(self):
#         self.assertEqual(
#             self.cal.add_double(1, 1), 4
#         )

#     # 以下が例外テスト
#     def test_add_double_raise(self):
#         # この関数を起動したらこのエラーが起きます
#         with self.assertRaises(ValueError):
#             self.cal.add_double('1', '1')


# if __name__ == "__main__":
#     unittest.main()


# 165. Unittestのスキップ
# import unittest


# class Cal(object):
#     def add_double(self, x, y):
#         if type(x) is not int or type(y) is not int:
#             raise ValueError
#         result = x + y
#         result *= 2
#         return result


# class CalTest(unittest.TestCase):
#     def setUp(self):
#         print('事前処理')
#         self.cal = Cal()

#     def tearDown(self):
#         print('終了')

#     release_name = 'lesson'
#     # デコレーターに書くだけ！
#     # @unittest.skip('スキップ！')
#     # 条件付きスキップ

#     @unittest.skipIf(release_name == 'lesson', 'リリースネームがレッスンだったのでスキップ')
#     def test_add_double(self):
#         self.assertEqual(
#             self.cal.add_double(1, 1), 4
#         )

#     # 以下が例外テスト
#     def test_add_double_raise(self):
#         # この関数を起動したらこのエラーが起きます
#         with self.assertRaises(ValueError):
#             self.cal.add_double('1', '1')


# if __name__ == "__main__":
#     unittest.main()


# 166. pytest
# class Cal(object):
#     def add_double(self, x, y):
#         if type(x) is not int or type(y) is not int:
#             raise ValueError
#         result = x + y
#         result *= 2
#         return result


# # test_でこれがテストだと判断してくれる
# # unittestのようにクラスを作って継承させる必要がない。
# # 文法を覚えなくても、パイソンの演算子でテストをかける
# def test_add_double():
#     cal = Cal()
#     assert cal.add_double(1, 1) == 4


# # クラスにしたい場合はクラスの頭文字をTestにして関数を入れるだけ→継承はいらない
# class TestCal(object):
#     def test_add_double(self):
#         cal = Cal()
#         assert cal.add_double(1, 1) == 4


# 167. pytestで例外テスト
# 168. pytestのsetupとteardown
# 169. pytestのスキップ
# import pytest


# class Cal(object):
#     def add_double(self, x, y):
#         if type(x) is not int or type(y) is not int:
#             raise ValueError
#         result = x + y
#         result *= 2
#         return result


# class TestCal(object):
#     @classmethod
#     def setup_class(cls):
#         print('開始')
#         cls.cal = Cal()

#     def setup_method(self, method):
#         print('method={}'.format(method.__name__))

#     def teardown_method(self, method):
#         print('method={}'.format(method.__name__))
#         # del self.cal

#     release = True

#     @pytest.mark.skipif(release == True, reason='スキップ！')
#     def test_add_double(self):
#         assert self.cal.add_double(1, 1) == 4

#     # 以下が例外テスト
#     def test_add_double_raise(self):
#         with pytest.raises(ValueError):
#             self.cal.add_double('1', '1')


# 170. pytestのconftest→オプションをつけたテストを実施
# 動いていない→もう一度確認
# →172で同じことができる


# 171. pytestのfixture
# import os


# class Cal(object):
#     def add_double(self, x, y):
#         if type(x) is not int or type(y) is not int:
#             raise ValueError
#         result = x + y
#         result *= 2
#         return result

#     def save(self, dir_path, file_name):
#         if not os.path.exists(dir_path):
#             os.mkdir(dir_path)
#         file_path = os.path.join(dir_path, file_name)
#         with open(file_path, 'w') as f:
#             f.write('test')

        
# class TestCal(object):
#     @classmethod
#     def setup_class(cls):
#         print('開始')
#         cls.cal = Cal()
#         cls.test_file_name = 'test.txt'

#     def test_add_double(self):
#         assert self.cal.add_double(1, 1) == 4

#     def test_save(self, tmpdir):
#         self.cal.save(tmpdir, self.test_file_name)
#         test_file_path = os.path.join(
#             tmpdir, self.test_file_name
#         )
#         assert os.path.exists(test_file_path) is True

    
# 172. pytestの独自のfixture
# import os


# class Cal(object):
#     def add_double(self, x, y):
#         if type(x) is not int or type(y) is not int:
#             raise ValueError
#         result = x + y
#         result *= 2
#         return result

#     def save(self, dir_path, file_name):
#         if not os.path.exists(dir_path):
#             os.mkdir(dir_path)
#         file_path = os.path.join(dir_path, file_name)
#         with open(file_path, 'w') as f:
#             f.write('test')

        
# class TestCal(object):
#     @classmethod
#     def setup_class(cls):
#         print('開始')
#         cls.cal = Cal()
#         cls.test_file_name = 'test.txt'

#     def test_add_double(self, csv_file):
#         # ※importしてないのに呼び出せる
#         # →conftestに書いておけば、どこのテストからでも簡単に呼べる
#         print(csv_file)
#         assert self.cal.add_double(1, 1) == 4


# # 173. pytest-cov　どこまでテストをすればいいのか
# # テストのカバー率を表示してくれる
# # 関数のリザルトに対してテストが設定されているのかを調べる
# # テストを作成していてもif文の中がテストに入っていないとかもわかる

# """
# ファイルの有無に関してテストする場合は
# shutil.rmtree()等のコマンドで
# テスト終了時にテストで作成したファイルを削除する必要がある
# その場合はteardown_classに書いておくとよい
# """


# 178. mock
# 179. mock.assert
# 180. mock.patch
# 181. mock.side_effect
# 182. mock spec

# salary178 test_salary178へ

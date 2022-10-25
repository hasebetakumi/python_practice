# 78.クラスの定義
# # python3からここのobjectの記載は不要になったが、暗黙の了解
# class Person(object):
#     def say_something(self):
#         print('hello')

# person = Person()
# person.say_something()


# 79.クラスの初期化とクラス変数
# class Person(object):
#     # 作成しただけで呼ばれる関数
#     # selfがないと、自分自身に値を保持できない
#     def __init__(self, name):
#         self.name = name
#         print(self.name)

#     def say_something(self):
#         print('I am {} hello'.format(self.name))
#         # 自分自身のメソッドにアクセスするときもselfが必要
#         self.run(5)

#     def run(self, num):
#         print('run' * num)

# person = Person('mike')
# person.say_something()


# 80.コンストラクタとデストラクタ
# class Person(object):
#     # 作成しただけで呼ばれる関数
#     # selfがないと、自分自身に値を保持できない
#     # initの部分をコンストラクタと呼ぶ
#     def __init__(self, name):
#         self.name = name
#         print(self.name)

#     def say_something(self):
#         print('I am {} hello'.format(self.name))
#         # 自分自身のメソッドにアクセスするときもselfが必要
#         self.run(5)

#     def run(self, num):
#         print('run' * num)

#     # このオブジェクトが使われなくなる時に出力→ファイル内のプログラムを読み終わってから実行
#     # もしくはdelでオブジェクトを消去したとき
#     # これがデストラクタ
#     def __del__(self):
#         print('bye')

# person = Person('mike')
# person.say_something()

# del person

# print('########################')


# 81.クラスの継承
# class Car(object):
#     def run(self):
#         print('run')

# class Toyota(Car):
#     pass

# class Tesla(Car):
#     def auto_run(self):
#         print('auto run')

# car = Car()
# car.run()

# toyota = Toyota()
# toyota.run()

# tesla = Tesla()
# tesla.run()
# tesla.auto_run()


# 82.メソッドのオーバーライドとsuperによる親のメソッドの呼び出し
# class Car(object):
#     def __init__(self, model=None):
#         self.model = model

#     def run(self):
#         print('run')

# class Toyota(Car):
#     def run(self):
#         print('toyota: ', self.model)

# class Tesla(Car):
#     def __init__(self, model=None):
#         # superを使うと親クラスのメソッドを呼び出せる
#         super().__init__(model)
#         print('aa')

#     def run(self):
#         print('tesla: ', self.model)

#     def auto_run(self):
#         print('auto run')

# car = Car()
# car.run()

# toyota = Toyota('raize')
# print(toyota.model)
# toyota.run()

# tesla = Tesla('model S')
# print(tesla.model)
# tesla.run()
# tesla.auto_run()


# 83.プロパティーを使った属性の設定

# class Car(object):
#     def __init__(self, model=None):
#         self.model = model

#     def run(self):
#         print('run')

# class Toyota(Car):
#     def run(self):
#         print('toyota: ', self.model)

# class Tesla(Car):
#     def __init__(self, model=None, enable_auto_run=False, pwd='123'):
#         # superを使うと親クラスのメソッドを呼び出せる
#         super().__init__(model)
#         # アンダースコアをつける→外部から参照してほしくないという意思表示
#         # アンダースコア２個にするとクラス内からは参照可能
#         self._enable_auto_run = enable_auto_run
#         self.pwd = pwd

#     # propertyを設定すると読み取り専用になる
#     @property
#     def enable_auto_run(self):
#         return self._enable_auto_run

#     # 条件が合致したときのみ書き込み可能（今回はパスワード、パスが違ったらValueError）
#     # enable_auto_runに対するセッターとして記述
#     @enable_auto_run.setter
#     def enable_auto_run(self, is_enable):
#         if self.pwd == '456':
#             self._enable_auto_run = is_enable
#         else:
#             raise ValueError

#     def run(self):
#         print('tesla: ', self.model)

#     def auto_run(self):
#         print('auto run')

# tesla = Tesla('model S', pwd='456')
# # propertyに設定した関数は（）をつけないで呼び出す
# tesla.enable_auto_run = True
# print(tesla._enable_auto_run)

# 84.クラスを構造体として扱う時の注意点
# class Car(object):
#     def __init__(self, model=None):
#         self.model = model

#     def run(self):
#         print('run')

# class Toyota(Car):
#     def run(self):
#         print('toyota: ', self.model)

# toyota_car = Toyota()
# # 以下を実行するとインスタンスの中身を書き換えられる
# # →基本は使用しない
# # →→
# toyota_car.name = '86'
# toyota_car.price = 3000000
# print(toyota_car.name)
      

# 85.ダックタイピング
# class Person(object):
#     def __init__(self, age=1):
#         self.age = age

#     def drive(self):
#         if self.age >= 18:
#             print('OK')
#         else:
#             raise Exception('No Drive')

# class Baby(Person):
#     def __init__(self, age=1):
#         if age < 18:
#             super().__init__(age)
#         else:
#             raise ValueError

# class Adult(Person):
#     def __init__(self, age=18):
#         if age >= 18:
#             super().__init__(age)
#         else:
#             raise ValueError

# baby = Baby()
# adult = Adult()

# class Car(object):
#     def __init__(self, model=None):
#         self.model = model

#     def run(self):
#         print('run')
    
#     def ride(self, person):
#         person.drive()

# car = Car()
# # car.ride(baby)
# car.ride(adult)


# 86.抽象クラス（子クラスの中に絶対定義してほしい関数がある場合）
# # 使わないほうが見やすいかも→無理に使う必要はない
# import abc

# # 下の設定でこのクラスが抽象クラスであることを宣言
# class Person(metaclass=abc.ABCMeta):
#     def __init__(self, age=1):
#         self.age = age

#     # 子クラスで定義してほしい関数を宣言
#     @abc.abstractmethod
#     def drive(self):
#         pass

# class Baby(Person):
#     def __init__(self, age=1):
#         if age < 18:
#             super().__init__(age)
#         else:
#             raise ValueError

#     def drive(self):
#         print('NG')

# class Adult(Person):
#     def __init__(self, age=18):
#         if age >= 18:
#             super().__init__(age)
#         else:
#             raise ValueError

#     def drive(self):
#         print('OK')

# baby = Baby()
# adult = Adult()

# class Car(object):
#     def __init__(self, model=None):
#         self.model = model

#     def run(self):
#         print('run')

# adult.drive()


# 87.多重継承
# # できれば使用しないほうがいい
# class Person(object):
#     def talk(self):
#         print('talk')
    
#     def run(self):
#         print('person run')

# class Car(object):
#     def run(self):
#         print('run')

# # 左の引数から先に継承→同じ名前の関数を定義していた場合は
# # 左のクラスに定義しているものが読み込まれる
# class PersonCarRobot(Person, Car):
#     def fly(self):
#         print('fly')

# robot = PersonCarRobot()
# robot.fly()
# robot.run()
# robot.talk()


# 88.クラス変数
# class Person(object):

#     # これがクラス変数
#     kind = 'human'

#     def __init__(self, name):
#         self.name = name

#     def who_are_you(self):
#         print(self.name, self.kind)

# a = Person('A')
# a.who_are_you()

# # クラス変数でリストを渡すと、別のインスタンスで変更を加えると全てに反映される。
# # このケースはクラス変数を用いないほうがいい
# # インスタンスごとに使用するリストを変えたいなら
# # __init__内で指定する
# class T(object):
#     words = []

#     def add(self, word):
#         self.words.append(word)

# c = T()
# c.add(1)
# c.add(2)
# c.add(3)
# print(c.words)

# d = T()
# d.add(123)
# # クラスの中で共有されているため、別のインスタンスでappendしても入ってる
# print(d.words)


# 89.クラスメソッドとスタティックメソッド
# class Person(object):

#     kind = 'human'

#     def __init__(self):
#         self.x = 100

#     # クラスのメソッドとして定義→インスタンスを生成しなくても使える
#     @classmethod
#     def what_is_your_kind(cls):
#         return cls.kind

#     @staticmethod
#     def about():
#         print('about human')

# # ()をつけるとオブジェクトを生成し、aには新しいオブジェクトが入っている
# a = Person()
# print(a.x)
# print(a.what_is_your_kind())

# # ()がないとclassそのものを代入することができる
# # オブジェクトは生成されていないが、クラス変数のkingにはアクセスできる
# b = Person
# print(b.kind)
# print(b.what_is_your_kind())

# # スタティックメソッドの呼び出し
# Person.about()

# print(b.x)


# 90.特殊メソッド（アンダーバー二つではさまれているもの）
# class Word(object):

#     def __init__(self, text):
#         self.text = text
#         print('作成')

#     # str型が渡されたら起動する
#     def __str__(self):
#         return 'word!!!!!!!!!!!'

#     # ＋を使ってクラスが呼び出されると自動起動
#     def __add__(self, word):
#         return self.text.lower() + word.text.lower()

#     # ==を使ってクラスが呼び出されると自動起動
#     def __eq__(self, word):
#         return self.text.lower() == word.text.lower()

# w = Word('test')
# print(w)

# w2 = Word('#################')

# # __add__
# print(w + w2)

# # __eq__
# print(w == w2)

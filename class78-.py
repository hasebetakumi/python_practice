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

class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

class Toyota(Car):
    def run(self):
        print('toyota: ', self.model)

class Tesla(Car):
    def __init__(self, model=None, enable_auto_run=False, pwd='123'):
        # superを使うと親クラスのメソッドを呼び出せる
        super().__init__(model)
        # アンダースコアをつけると外部から見えなくなる
        self._enable_auto_run = enable_auto_run
        self.pwd = pwd

    # propertyを設定すると読み取り専用になる
    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    # 条件が合致したときのみ書き込み可能（今回はパスワード、パスが違ったらValueError）
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.pwd == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    def run(self):
        print('tesla: ', self.model)

    def auto_run(self):
        print('auto run')

tesla = Tesla('model S', pwd='456')
tesla.enable_auto_run = True
print(tesla._enable_auto_run)
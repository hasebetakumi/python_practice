# 118. configparser
# """
# [DEFAULT]
# debug = False

# [web_server]
# host = 127.0.0.1
# port = 80

# [db_server]
# host = 127.0.0.1
# port = 3306
# """

# import configparser

# # configファイル生成
# # config = configparser.ConfigParser()
# # config['DEFAULT'] = {
# #     'debug': True
# # }

# # config['web_server'] = {
# #     'host': '127.0.0.1',
# #     'port': 80
# # }

# # config['db_server'] = {
# #     'host': '127.0.0.1',
# #     'port': 3306
# # }

# # with open('config.ini', 'w') as config_file:
# #     config.write(config_file)

# # config読み取り
# config = configparser.ConfigParser()
# config.read('config.ini')
# print(config['web_server']['host'])


# 119. yaml
# """
# web_server:
#   host: 127.0.0.1
#   port: 80

# db_server:
#   host: 127.0.0.1
#   port: 3306
# """
# import yaml

# # # yamlファイル生成
# # with open('config.yaml', 'w') as yaml_file:
# #     # dump→辞書をjsonに整形
# #     yaml.dump({
# #         'web_server': {
# #             'host': '127.0.0.1',
# #             'port': 80
# #         },
# #         'db_server': {
# #             'host': '127.0.0.1',
# #             'port': 3306
# #         }
# #     }, yaml_file)

# # yamlファイル読み取り
# with open('config.yaml', 'r') as yaml_file:
#     # 動画内のコードと違う。最新版だとLoaderを指定してあげないといけない
#     data = yaml.load(yaml_file, Loader=yaml.Loader)
#     print(data, type(data))


# 120. ロギング
# """
# ログのレベルは以下の通り
# critical
# error
# warning
# info
# debug
# デフォルトがレベル3なのでwarningまでしか表示されない
# """
# import logging

# # ログをコンソール上に表示
# # logging.basicConfig(level=logging.INFO)

# # logging.critical('critical')
# # logging.error('error')
# # logging.warning('warning')
# # logging.info('info')
# # logging.debug('debug')

# # ログをファイルに保存
# logging.basicConfig(filename= 'test120.log', level=logging.DEBUG)

# logging.critical('critical')
# logging.error('error')
# logging.warning('warning')
# logging.info('info')
# logging.debug('debug')


# 121. ロギング　フォーマッタ
# import logging

# formatter = '%(levelname)s:%(message)s:%(asctime)s'
# logging.basicConfig(level=logging.INFO, format=formatter)

# logging.warning('warning %s %s', 'test', 'test2')


# 122. ロギング　ロガー
# import logging

# """
# logging.basicConfig(level=logging.INFO)
# これをメインに置いておいて

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# これは各ファイルに置いておく（各ファイルごとにレベルを設定できる）

# あとはログを取りたいところに
# logger.debug('debug')
# これを置いて呼び出す
# """
# logging.basicConfig(level=logging.INFO)

# logging.info('info')

# # __name__＝自身のファイル名
# # これでどこのファイルでのログなのかがわかる
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# logger.debug('debug')


# 123. ロギング　ハンドラー→filehandlerでファイルに保存
# import logging

# logging.basicConfig(level=logging.INFO)

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

# hand = logging.FileHandler('test123.log')
# logger.addHandler(hand)

# logger.debug('from main')
# logger.warning('from main')


# 124. ロギング　フィルタ
# import logging

# logging.basicConfig(level=logging.INFO)

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

# # 誰かが間違えてログに重要な情報を載せてしまった
# logger.warning('from main')


# class NoPassFilter(logging.Filter):
#     def filter(self, record):
#         log_massage = record.getMessage()
#         # passwordが入っていなければtrueでログを表示
#         return 'password' not in log_massage


# # このクラスからのオブジェクトを渡してあげる
# logger.addFilter(NoPassFilter())
# logger.warning('from main password = "test"')
# logger.warning('from main aaa = "test"')


# 125. ロギング　コンフィグ
"""
loggingの設定ファイルを別で用意して読み取る
ドキュメント参考
"""


# 126. ロギングの書き方
# import logging

# logging.basicConfig()

# logger = logging.getLogger(__name__)

# logger.error('api call is failed')

# # 辞書で書いてあげると別のログ解析ソフトに入れるとき便利
# logger.error({
#     'action': 'create',
#     'status': 'fail',
#     'message': 'api failed'
# })

# """
# 重要な処理の前後（前はrun、後はsuccessと書くことが多い）
# raiseの直前にも

# """


# 127. Email送信

# 151. XML
# import xml.etree.ElementTree as ET

# # XMLファイル作成
# root = ET.Element('root')

# tree = ET.ElementTree(element=root)

# employee = ET.SubElement(root, 'employee')

# employ = ET.SubElement(employee, 'employ')
# employ_id = ET.SubElement(employ, 'id')
# employ_id.text = 11
# employ_id = ET.SubElement(employ, 'name')
# employ_id.text = 'mike'

# employ = ET.SubElement(employee, 'employ')
# employ_id = ET.SubElement(employ, 'id')
# employ_id.text = 22
# employ_id = ET.SubElement(employ, 'name')
# employ_id.text = 'namcy'

# # 以下にエラー、恐らくバージョン変更
# # tree.write('test151.xml', encoding='utf-8', xml_declaration=True)


# 152. Json
# import json

# j = {
#     "employee":
#         [
#             {"id": 111, "name": "mike"},
#             {"id": 111, "name": "nancy"}
#         ]
# }

# print(j)
# print('#####################')
# print(json.dumps(j))
# print('#####################')

# # ファイルに書き込む
# with open('test152.json', 'w') as f:
#     # 書き込むときはsを取って、dump
#     json.dump(j, f)

# # ファイルを読み込む
# with open('test152.json', 'r') as f:
#     print(json.load(f))

# # jsonを戻す→sをつけて、loads
# print('#####################')
# a = json.dumps(j)
# print(json.loads(a))


# 153. urllib.request
# import urllib.request
# import json

# # GETメソッド
# # urlにキーを渡したい
# # payload = {'key': 'value'}

# # url = 'http://httpbin.org/get' + '?' + urllib.parse.urlencode(payload)
# # print(url)

# # with urllib.request.urlopen(url) as f:
# #     print(f.read().decode('utf-8'))


# # POSTメソッド→putとdeleteはメソッドを書き換えるだけ
# payload = {'key': 'value'}
# payload = json.dumps(payload).encode('utf-8')
# req = urllib.request.Request(
#     'http://httpbin.org/post',
#     data=payload,
#     method='POST'
#     )
# with urllib.request.urlopen(req) as f:
#     print(json.loads(f.read().decode('utf-8')))


# 154. requests
# import requests

# payload = {'key': 'value'}

# r = requests.get('http://httpbin.org/get', params=payload, timeout=1)

# print(r.text)
# print(r.status_code)
# print(r.json())


# r = requests.post('http://httpbin.org/post', data=payload)

# # put deleteは入れ替えるだけ


# 155.socket通信

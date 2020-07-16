print('hello')


import requests
import json


resp = requests.post(url='http://172.30.37.123:8005/sysLogin/login',
                     data={'userAccount': 'yangxun', 'password': 'YWRtaW4'},
                     headers={'Content-Type': 'application/x-www-form-urlencoded'})
print(resp.text)
# result_json = json.loads(resp.text)
# token = result_json['data']['token']
#
# resp02 = requests.get(url='http://172.30.37.123:8005/sysMenuInfo/userMenuTree',
#                       params={'userAccount': 'yangxun'},
#                       cookies=token)
# print(resp02.text)


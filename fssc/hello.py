print('hello')


import requests
import json


resp = requests.post(url='http://172.30.37.123:8005/sysLogin/login',
                     data={'userAccount': 'yangxun', 'password': 'YWRtaW4'},
                     headers={'Content-Type': 'application/x-www-form-urlencoded'})
print(resp.text)
result_json = json.loads(resp.text)    # resp.text.json()  #字典格式字符串转为字典对象
token = result_json['data']['token']

resp02 = requests.get(url='http://172.30.37.123:8005/sysMenuInfo/userMenuTree',
                      params={'userAccount': 'yangxun'},
                      headers={'token': token})
print(resp02.text)

resp03 = requests.post(url='http://172.30.37.123:8005/reimbursement/pageList',
                       json={"reimbursementNo":"","formType":"","reimbursementDepartment":"","reimbursementer":"","applyer":"","costCenter":"","formStatus":"","startTime":"","endTime":"","stepName":"","time":[],"pageNum":1,"pageSize":10,"handleStatus":"0","queryType":"01"},
                       headers={'Content-Type': 'application/json', 'token': token})
import pprint
pprint.pprint(resp03.json())


# -*- coding: UTF-8 -*-
'''
=================================================
@Project -> File   ：fssc -> control
@IDE    ：PyCharm
@Author ：Mr. Jiang
@Date   ：2020/7/17 13:57
@Desc   ：
==================================================
'''
from fssc.common import common
import requests
from fssc.configure import configure
import pprint
import json
'''    
    @Author:Mr. Jiang    
    @Date:2020/7/17 15:23
    @Desc:请求接口
'''
def httpRequest():
    # 调用获取token函数
    token = common.getToken()
    workBook, rowObjectList = common.getReadExcel() # 获取行数据集合
    copyWorkBook, copySheet = common.getCopysheet(workBook)
    row = 0
    # 循环调用请求执行用例
    for rowObject in rowObjectList:
        row += 1
        action = rowObject[2] # 获取请求action
        method = rowObject[3] # 获取请求method
        headersFormat = rowObject[4] # 获取请求头格式
        params = json.loads(rowObject[5]) # 将字符串转为字典格式
        expect = rowObject[6] # 获取预期
        # try:
        if method == 'POST':
            if headersFormat == 'application/x-www-form-urlencoded': # form表单格式
                resp = requests.post(url=f'{configure.path}{action}',
                              data=params,
                              headers={'Content-Type': headersFormat, 'token': token})
                # 调用三合一函数
                assert_rTime_backWrite(expect, resp, row, copySheet)
            elif headersFormat == 'application/json': # json格式
                resp = requests.post(url=f'{configure.path}{action}',
                              json=params,
                              headers={'Content-Type': headersFormat, 'token': token})
                # 调用三合一函数
                assert_rTime_backWrite(expect, resp, row, copySheet)
        elif method == 'GET':
            resp = requests.get(url=f'{configure.path}{action}',
                         params=params,
                         headers={'token': token})
            # 调用三合一函数
            assert_rTime_backWrite(expect, resp, row, copySheet)
        # except:
        #     print('系统异常')
    # 调用生成测试结果函数
    common.getResultExcel(copyWorkBook=copyWorkBook)

'''
    @Author:Mr. Jiang    
    @Date:2020/7/20 17:37
    @Desc:断言+耗时+测试结果回写 三合一函数
'''
def assert_rTime_backWrite(expect,resp,row,copySheet):
    # 调用断言函数
    result = common.getAssert(expect=expect, actual=resp.json()['message'])
    # 获取请求响应耗时
    rTime = resp.elapsed.total_seconds()
    # 回写测试结果
    common.getWriteExcel(copySheet=copySheet, row=row, actual=resp.json()['message'], result=result, rTime=rTime)

# 调用执行用例入口函数
httpRequest()
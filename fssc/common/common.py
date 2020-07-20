# -*- coding: UTF-8 -*-
'''
=================================================
@Project -> File   ：fssc -> common
@IDE    ：PyCharm
@Author ：Mr. Jiang
@Date   ：2020/7/17 13:56
@Desc   ：
==================================================
'''
from fssc.configure import configure
import requests
import xlrd, xlwt
from xlutils.copy import copy
import time
import os
import pprint
'''    
    @Author:Mr. Jiang    
    @Date:2020/7/17 14:10
    @Desc:获取token
'''
def getToken():
    resp = requests.post(url=f'{configure.path}/sysLogin/login',
                          data={'userAccount': 'yangxun', 'password': 'YWRtaW4='},
                          headers={'Content-Type': 'application/x-www-form-urlencoded'})
    return resp.json()['data']['token']

'''
    @Author:Mr. Jiang    
    @Date:2020/7/17 14:29
    @Desc:读excel并返回:workBook, rowObjectList(行数据集合)
'''
def getReadExcel():
    workBook = xlrd.open_workbook(f'{configure.excelPath}.xlsx') # 获取excel对象
    workSheet = workBook.sheet_by_index(0) # 获取第一个sheet对象
    # 循环获取excel中数据值
    nrows = workSheet.nrows # 获取行数
    ncols = workSheet.ncols # 获取列数
    rowObjectList = []
    for row in range(1, nrows):
        rowObjectList.append(workSheet.row_values(row)) # 获取每行数据并放入List
    return workBook, rowObjectList

'''
    @Author:Mr. Jiang    
    @Date:2020/7/20 10:13
    @Desc:copy生成新excel回写测试结果函数
'''
def getCopysheet(workBook):
    # 复制表
    copyWorkBook = copy(workBook)
    # 获取sheet对象
    copySheet = copyWorkBook.get_sheet(0)
    return copyWorkBook, copySheet

'''
    @Author:Mr. Jiang    
    @Date:2020/7/20 13:35
    @Desc:生成测试结果表
'''
# def getResultExcel(copyWorkBook):
#     # 创建copy表时判断表时候存在
#     if os.path.exists('../data/api测试用例-result.xlsx') == True:
#         os.remove('../data/api测试用例-result.xlsx')
#         copyWorkBook.save('../data/api测试用例-result.xlsx')
#     else:
#         copyWorkBook.save('../data/api测试用例-result.xlsx')

def getResultExcel(copyWorkBook):
    timeTuple = time.localtime()
    loaclTime = time.strftime("%Y%m%d", timeTuple)
    copyWorkBook.save(f'{configure.excelPath}-result-{loaclTime}.xlsx')

'''
    @Author:Mr. Jiang    
    @Date:2020/7/20 13:17
    @Desc:重复写excel
'''
def getWriteExcel(copySheet, row, actual, result, rTime):
    copySheet.write(row, 7, actual)
    copySheet.write(row, 8, result)
    copySheet.write(row, 9, rTime)

'''    
    @Author:Mr. Jiang    
    @Date:2020/7/17 16:19
    @Desc:断言函数
'''
def getAssert(expect, actual):
    if expect in actual:
        return 'PASS'
    else:
        return 'FAIL'
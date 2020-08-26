# -*- coding: UTF-8 -*-
'''
=================================================
@Project -> File   ：fssc -> mockApi
@IDE    ：PyCharm
@Author ：Mr. Jiang
@Date   ：2020/8/14 14:11
@Desc   ：
==================================================
'''

from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import shutil
from mockApi.control import mockControl

# 实例化一个web服务对象
app = Flask(__name__)

#列表查询API
@app.route('/pageList',methods=['POST'])
def pageList():
    '''
    {"reimbursementNo":"","formType":"","reimbursementDepartment":"","reimbursementer":"","applyer":"","costCenter":"","formStatus":"","startTime":"","endTime":"","stepName":"","time":[],"pageNum":1,"pageSize":10,"handleStatus":"0","queryType":"01"}
    @return:{
            "code":"200",
            "data":{},
            "msg":"success"
    }
    '''
    try:
        params = request.get_json()
        get_pageNum = params["pageNum"]
        get_pageSize = params["pageSize"]
        get_handleStatus = params["handleStatus"]
        get_queryType = params["queryType"]
        if not all([get_pageNum, get_pageSize, get_handleStatus, get_queryType]):
            return jsonify({"msg": "未传参数"})
        get_reimbursementNo = params["reimbursementNo"] # 获取业务单号
        data={
            "code":"1000_0001_0000",
            "data":{
                "endRow":1,
                "hasNextPage":"false",
                "hasPreviousPage":"false",
                "isFirstPage":"true",
                "isLastPage":"true",
                "list":[
                    {
                        "accountChange":"0",
                        "actuallyAmount":"null",
                        "applyTime":1575388800000,
                        "applyer":"马上消费2",
                        "applyerNo":"msxf2",
                        "attCount":"1",
                        "cashFlowCode":"A99",
                        "checkAmount":"1.00",
                        "costCenter":"1829182901",
                        "costCenterCn":"总经理办公室",
                        "costPeriod":"2019-12-01 00:00:00.0",
                        "createTime":1575452376000,
                        "createUser":"OA",
                        "deductAmount":"0.00",
                        "formStatus":"00",
                        "formType":"5fc7a98653274e039a76b1f1ef4a3006",
                        "formTypeCn":"财务共享通用流程",
                        "handler":"yangxun",
                        "hangUpStatus":"02",
                        "id":87,
                        "oaId":"16ed045c812a7d0bf0059c34644a835b",
                        "org":"1829",
                        "orgCn":"重庆商社新世纪百货连锁经营有限公司凯瑞商都",
                        "reimbursementAmount":"1.00",
                        "reimbursementContent":"附件类型是Word",
                        "reimbursementDepartment":"马上消费",
                        "reimbursementDepartmentCn":"null",
                        "reimbursementNo":get_reimbursementNo,
                        "reimbursementer":"马上消费2",
                        "taxAmount":"0.00",
                        "updateTime":1581385320000,
                        "updateUser":"OA",
                        "voucherNo":"null",
                        "voucherState":0
                    }
                ],
                "navigateFirstPage":1,
                "navigateLastPage":1,
                "navigatePages":8,
                "navigatepageNums":[1],
                "nextPage":0,
                "pageNum":1,
                "pageSize":10,
                "pages":1,
                "prePage":0,
                "size":4,
                "startRow":1,
                "total":1
            },
            "message":"成功"
        }
        return jsonify(data)
    except Exception as e:
        print(e)
        return jsonify({"msg": "系统异常"})

#上传文件API
@app.route("/upload", methods=["POST"])
def upload():
    '''
    @param "file" : 文件
    @return:{
            "code":"200",
            "data":{},
            "msg":"success"
    }
    '''
    return mockControl.upload_file()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='9090', debug=True)
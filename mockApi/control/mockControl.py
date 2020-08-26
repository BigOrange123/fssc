# -*- coding: UTF-8 -*-
'''
=================================================
@Project -> File   ：fssc -> mockControl
@IDE    ：PyCharm
@Author ：Mr. Jiang
@Date   ：2020/8/14 14:15
@Desc   ：
==================================================
'''
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import shutil

# 上传文件函数
def upload_file():
    '''
    @param "file" : 文件
    @return:{
            "code":"200",
            "data":{},
            "msg":"success"
    }
    '''
    try:
        if os.path.exists("../uploadFile"):
            # os.rmdir("../uploadFile") # rmdir只能删除空文件夹
            shutil.rmtree("../uploadFile") # 清空文件夹并删除
            os.mkdir("../uploadFile")
        f = request.files['file']
        f.save("../uploadFile/" + secure_filename(f.filename))
        resp = {
                "code":"200",
                "data":{},
                "msg":"success"
        }
        return jsonify(resp)
    except Exception as e:
        print(e)
        return jsonify({"msg": "系统异常"})
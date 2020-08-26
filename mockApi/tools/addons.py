# -*- coding: UTF-8 -*-
'''
=================================================
@Project -> File   ：fssc -> addons
@IDE    ：PyCharm
@Author ：Mr. Jiang
@Date   ：2020/8/20 10:26
@Desc   ：
==================================================
'''

from mitmproxy import http,ctx
import json
class Modify():
    def response(self, flow):
        # 拦截请求地址
        if flow.request.url.endswith("http://172.30.37.123:8005/reimbursement/pageList"):
            # 获取拦截请求的响应报文并转成字典格式
            resp = json.loads(flow.response.get_text())
            # 修改响应报文
            resp["data"] = 10086
            # 把响应报文转成json格式并赋值给响应报文
            flow.response.set_text(json.dumps(resp))
            ctx.log.info("data = 10086") # 日志记录
        elif flow.request.url.endswith("http://172.30.37.123:8005/sysOperateRecord/workAssignmentPage"):
            resp = json.loads(flow.response.get_text())
            resp["data"] = 10000
            flow.response.set_text(json.dumps(resp))
            ctx.log.info("data = 10000")
addons = [
    Modify()
]
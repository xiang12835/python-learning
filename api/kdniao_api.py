# encoding=utf-8

__author__ = 'flyingfishyx <yuxiang0128@gmail.com>'

import json
import requests
import hashlib
import base64
import sys


reload(sys)
sys.setdefaultencoding('utf-8')


class Express(object):

    # http://www.kdniao.com/;start on 2017-12-19;free in 1 year
    APP_ID = "1313736"
    APP_KEY = "d843bb7c-a10f-4be4-878c-a7e16bf5a577"
    URL = "http://api.kdniao.cc/Ebusiness/EbusinessOrderHandle.aspx"

    @classmethod
    def encrypt(cls, origin_data, appkey):
        """数据内容签名：把(请求内容(未编码)+AppKey)进行MD5加密，然后Base64编码"""
        m = hashlib.md5()
        m.update((origin_data+appkey).encode("utf8"))
        encodestr = m.hexdigest()
        base64_text = base64.b64encode(encodestr.encode(encoding='utf-8'))
        return base64_text

    @classmethod
    def send_post(cls, url, datas):
        """发送post请求"""
        header = {
            "Accept": "application/x-www-form-urlencoded;charset=utf-8",
            "Accept-Encoding": "utf-8"
        }
        req = requests.post(url=url, data=datas, headers=header)
        data = json.loads(req.content)
        return data

    @classmethod
    def get_company(cls, logistic_code, appid, appkey, url):
        """获取对应快递单号的快递公司代码和名称"""
        data1 = {'LogisticCode': logistic_code}
        d1 = json.dumps(data1, sort_keys=True)
        requestdata = cls.encrypt(d1, appkey)
        post_data = {
            'RequestData': d1,
            'EBusinessID': appid,
            'RequestType': '2002',
            'DataType': '2',
            'DataSign': requestdata.decode()}
        json_data = cls.send_post(url, post_data)
        return json_data

    @classmethod
    def get_traces(cls, logistic_code, shipper_code, appid, appkey, url):
        """查询接口支持按照运单号查询(单个查询)"""
        data1 = {'LogisticCode': logistic_code, 'ShipperCode': shipper_code}
        d1 = json.dumps(data1, sort_keys=True)
        requestdata = cls.encrypt(d1, appkey)
        post_data = {'RequestData': d1, 'EBusinessID': appid, 'RequestType': '1002', 'DataType': '2',
                     'DataSign': requestdata.decode()}
        json_data = cls.send_post(url, post_data)
        return json_data

    @classmethod
    def recognise(cls, expresscode):
        """输出数据"""
        data = cls.get_company(expresscode, cls.APP_ID, cls.APP_KEY, cls.URL)
        if not data.get('Shippers', ""):
            print "未查到该快递信息,请检查快递单号是否有误！"
        else:
            print "已查到该", str(data['Shippers'][0]['ShipperName'])+"("+str(data['Shippers'][0]['ShipperCode'])+")", expresscode
            trace_data = cls.get_traces(expresscode, data['Shippers'][0]['ShipperCode'], cls.APP_ID, cls.APP_KEY, cls.URL)
            if trace_data['Success'] == "false" or not trace_data.get('Traces', ""):
                print "未查询到该快递物流轨迹！"
            else:
                str_state = "问题件"
                if trace_data['State'] == '2':
                    str_state = "在途中"
                if trace_data['State'] == '3':
                    str_state = "已签收"
                print "目前状态： "+str_state
                trace_data = trace_data['Traces']
                item_no = 1
                for item in trace_data:
                    print str(item_no)+":", item['AcceptTime'], item['AcceptStation']
                    item_no += 1
                print "\n"
        return

    @classmethod
    def get_express_info(cls, expresscode):
        """输出数据"""
        data = cls.get_company(expresscode, cls.APP_ID, cls.APP_KEY, cls.URL)
        result = {}
        if not data.get('Shippers', ""):
            result["msg"] = "未查到该快递信息,请检查快递单号是否有误！"
            result["success"] = False
            return result
        else:
            result["msg"] = "已查到该快递"
            result["success"] = True
            result["expressInfo"] = {
                "shipperName": str(data['Shippers'][0]['ShipperName']),
                "shipperCode": str(data['Shippers'][0]['ShipperCode']),
                "expressCode": expresscode,
            }
            trace_data = cls.get_traces(expresscode, data['Shippers'][0]['ShipperCode'], cls.APP_ID, cls.APP_KEY, cls.URL)

            # print trace_data['Success']

            if trace_data['Success']:

                # 物流状态:0-无轨迹, 1-已揽收, 2-在途中 201-到达派件城市, 3-签收, 4-问题件
                if trace_data['State'] == '0':
                    trace_data['StateStr'] = "无轨迹"
                    trace_data["msg"] = "该快递无轨迹信息！"
                elif trace_data['State'] == '1':
                    trace_data['StateStr'] = "已揽收"
                    trace_data["msg"] = "该快递已揽收！"
                elif trace_data['State'] == '2':
                    trace_data['StateStr'] = "在途中"
                    trace_data["msg"] = "该快递在途中！"
                elif trace_data['State'] == '3':
                    trace_data['StateStr'] = "已签收"
                    trace_data["msg"] = "该快递已签收！"
                elif trace_data['State'] == '4':
                    trace_data['StateStr'] = "问题件"
                    trace_data["msg"] = "该快递是问题件！"
            else:
                trace_data["msg"] = "未查询到该快递物流轨迹！"
                trace_data['State'] = '9'
                trace_data['StateStr'] = "无物流"

            result["traceInfo"] = trace_data
        return result


if __name__ == "__main__":
    while True:
        code = input("请输入快递单号：")  # 3909430112808
        # recognise(code)
        res = Express.get_express_info(str(code).strip())
        print json.dumps(res, ensure_ascii=False, sort_keys=True, indent=4)

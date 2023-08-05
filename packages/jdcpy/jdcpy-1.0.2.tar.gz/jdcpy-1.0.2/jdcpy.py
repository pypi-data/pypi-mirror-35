import json
from datetime import date, datetime

import requests
from pandas.io.json import json_normalize

headers = {}
# host = '192.168.80.154:8082'
host = '192.168.1.16:8080'
url = 'http://' + host


class jdcpy:
    def __init__(self):
        self.sess = requests.session()

    def login(self, username, password):
        # r = self.sess.post(url + '/data/login', data={'username': username, 'password': password})
        juser = json.dumps({'phone': username, 'password': password})
        self.sess.headers['Content-Type'] = 'application/json'
        r = self.sess.post(url + '/userLogin', data=juser)
        jresponse = json.loads(r.content)
        if jresponse['errcode'] != 0:
            return jresponse['errmsg']
        self.token = jresponse['data']['token']
        self.sess.headers['Authorization'] = self.token
        return 0

    def info(self, idList, basicInfo, classifycation, performance):
        """
        基金的基本信息
        :param idList:基金的标识列表,格式如list(string,string...)
        :param basicInfo:基金的基本信息列表,格式如list(string,string...)
        :param classifycation:投资分布信息列表,格式如list(string,string...)
        :param performance:业绩表现列表,格式如list(string,string...)
        :return: pandas.DataFrame
        """
        idList = list(idList)
        basicInfo = list(basicInfo)
        classifycation = list(classifycation)
        performance = list(performance)
        idList.sort()
        basicInfo.sort()
        classifycation.sort()
        performance.sort()
        idList = tuple(idList)
        basicInfo = tuple(basicInfo)
        classifycation = tuple(classifycation)
        performance = tuple(performance)
        jdata = json.dumps({'idList': idList, 'basicInfo': basicInfo, 'classifycation': classifycation, 'performance': performance})
        r = self.sess.post(url + '/data/fund_global/info', data=jdata)
        jresponse = json.loads(r.content, encoding='utf8')
        if jresponse['errcode'] != 0:
            return jresponse['errmsg']
        d = jresponse['data']['data']
        t = json_normalize(d)
        return t

    def nav(self, idList, startDate, endDate, nav):
        """
        返回基金的历史表现
        :param idList:基金的标识列表,格式如list(string,string...)
        :param startDate:起始日期,可以为timestamp格式,或者date,或者datetime,也可以为string如1999-08-10或1990/08/10格式
        :param endDate:结束日期
        :param nav:所要查询的信息列表,格式如list(string,string...)
        :return: pandas.DataFrame
        """
        idList = list(idList)
        nav = list(nav)
        idList.sort()
        nav.sort()
        idList = tuple(idList)
        nav = tuple(nav)
        if type(startDate) == str:
            try:
                startDate = int(datetime.strptime(startDate, '%Y-%m-%d').timestamp() * 1000)
                endDate = int(datetime.strptime(endDate, '%Y-%m-%d').timestamp() * 1000)
            except:
                try:
                    startDate = int(datetime.strptime(startDate, '%Y/%m/%d').timestamp() * 1000)
                    endDate = int(datetime.strptime(endDate, '%Y/%m/%d').timestamp() * 1000)
                except:
                    pass
        if type(startDate) == float:
            startDate = int(startDate * 1000)
            endDate = int(endDate * 1000)
        elif type(startDate) == date:
            startDate = int(datetime.fromordinal(startDate.toordinal()).timestamp() * 1000)
            endDate = int(datetime.fromordinal(endDate.toordinal()).timestamp() * 1000)
        elif type(startDate) == datetime:
            startDate = int(1000 * startDate.timestamp())
            endDate = int(1000 * endDate.timestamp())
        jdata = json.dumps({'idList': idList, 'startDate': startDate, 'endDate': endDate, 'nav': nav})
        r = self.sess.post(url + '/data/fund_global/nav', data=jdata)
        jresponse = json.loads(r.content, encoding='utf8')
        if jresponse['errcode'] != 0:
            return jresponse['errmsg']
        d = jresponse['data']['data']
        t = json_normalize(d)
        return t

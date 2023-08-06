# -*- coding: utf-8 -*-
import json
from VarOperHelper.datamodel import *
from urllib import request, parse
from urllib.parse import urlencode
import requests


class VarOper:
    serverAddress = ''
    serverPort = 0

    # region 构造函数
    def __init__(self, address, port):
        self.serverAddress = address
        self.serverPort = port

    # endregion

    # region 公共方法

    # 查询指定变量实时值
    def getVarValue(self, varnames, pageindex=0, pagesize=1000):
        try:
            lst = []
            if (str(self.serverAddress).strip() == '' or str(self.serverPort).strip == ''
                    or str(self.serverPort).isdigit() is False or len(varnames) == 0):
                return lst

            if str(pagesize).isdigit() is False:
                pagesize = 1000

            if str(pageindex).isdigit() is False:
                pageindex = 0

            lst = self.__getVarValueData(set(varnames), pageindex, pagesize)
            return lst
        except Exception as e:
            raise Exception('getvarvalue获取数据出错 ', e)

    # 用于查询系统内符合条件的变量摘要信息（比如变量的名称、描述、类型等）
    def getVarSummary(self, varclass='', rwmode='', vartype='', name='', desc='', pageindex=0, pagesize=1000):
        try:
            lst = []
            data = {}
            if str(varclass).strip() != '':
                data['Class'] = varclass

            if str(rwmode).strip() != '':
                data['RW'] = rwmode

            if str(vartype).strip() != '':
                data['Type'] = vartype

            if str(name).strip() != '':
                data['Name'] = name

            if str(desc).strip() != '':
                data['Desc'] = desc

            if str(pagesize).isdigit() is False:
                pagesize = 1000
            data['PageSize'] = pagesize

            if str(pageindex).isdigit() is False:
                pageindex = 0
            data['PageIndex'] = pageindex

            url = 'http://{0}:{1}/api/var/GetVarSummary'.format(self.serverAddress, self.serverPort)
            req_data = urlencode(data)  # 将字典类型的请求数据转变为url编码
            res = request.urlopen(url + '?' + req_data)  # 通过urlopen方法访问拼接好的url
            ret = res.read().decode()  # read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str

            dic = json.loads(ret)
            # 字典构成的序列
            data = dic['Data']
            if data is not None and 'List' in data.keys():
                vars = data['List']
                for item in vars:
                    lst.append(self.__convertToVarSummary(item))
            return lst
        except Exception as ex:
            raise Exception('获取数据出错' + ex)

    # 用于查询指定变量详细信息（比如变量摘要信息、变量值信息等等）
    def getVarDetail(self, varnames, pageindex=0, pagesize=1000):
        try:
            lst = []
            if (str(self.serverAddress).strip() == '' or str(self.serverPort).strip == ''
                    or str(self.serverPort).isdigit() is False or len(varnames) == 0):
                return lst

            if str(pagesize).isdigit() is False:
                pagesize = 1000

            if str(pageindex).isdigit() is False:
                pageindex = 0

            # 用集合进行去重操作
            s = set(varnames)
            url = 'http://{0}:{1}/api/var/GetVarDetail'.format(self.serverAddress, self.serverPort)
            data = {'names': [p for p in s], 'PageIndex': pageindex, 'PageSize': pagesize}
            req_data = urlencode(data)  # 将字典类型的请求数据转变为url编码
            res = request.urlopen(url + '?' + req_data)  # 通过urlopen方法访问拼接好的url
            ret = res.read().decode()  # read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str

            dic = json.loads(ret)
            # 字典构成的序列
            data = dic['Data']
            if data is not None and 'List' in data.keys():
                # 字典集合
                vars = data['List']
                for item in vars:
                    name = item['Name']
                    isok = item['IsOk']
                    vardetailItem = VarDetail(name, isok)
                    vardetailItem.BasicInfo = self.__convertToVarSummary(item['BasicInfo'])
                    vardetailItem.ValueInfo = self.__converToVarValue(item['ValueInfo'])
                    lst.append(vardetailItem)
            return lst
        except Exception as ex:
            raise Exception('getvrdetail获取数据出错 ' + ex)

    # 用于获取指定变量缓存数据（历史数据）
    def getValueBuffer(self, varname, index=0, size=100):
        try:
            lst = []
            if str(varname).strip() == '' or str(self.serverAddress).strip() == '' or str(self.serverPort).strip == '':
                return lst

            if str(index).isdigit() is False:
                index = 0

            if str(size).isdigit() is False:
                size = 100

            url = 'http://{0}:{1}/api/var/GetVarBuffer'.format(self.serverAddress, self.serverPort)
            data = {'name': varname, 'index': index, 'size': size}
            req_data = urlencode(data)
            res = request.urlopen(url + '?' + req_data)
            ret = res.read().decode()

            dic = json.loads(ret)
            data = dic['Data']
            if data is not None and 'List' in data.keys():
                vars = data['List']
                for item in vars:
                    lst.append(self.__converToVarValue(item))
            return lst
        except Exception as ex:
            raise Exception('getValueBuffer获取数据出错 ' + ex)

    # 用于获取指定变量各种类型统计数据
    def getValueStatistics(self, varname, statistype: StatisticsType, index=0, size=100):
        try:
            if str(varname).strip() == '' or type(statistype) != StatisticsType or str(
                    self.serverAddress).strip() == '' or str(self.serverPort).strip == '':
                raise Exception("参数错误")

            if str(index).isdigit() is False:
                index = 0

            if str(size).isdigit() is False:
                size = 100

            url = 'http://{0}:{1}/api/var/GetVarStatistics'.format(self.serverAddress, self.serverPort)
            data = {'name': varname, 'type': statistype.name, 'index': index, 'size': size}
            req_data = urlencode(data)
            res = request.urlopen(url + '?' + req_data)
            ret = res.read().decode()

            dic = json.loads(ret)
            data = dic['Data']
            if data is not None:
                isok = data['IsOk']
                result = data['Result']
                varvalueret = VarStatisticsResult(isok, result)

            return varvalueret
        except Exception as e:
            raise Exception("getValueStatistics数据出错 ", e)

    # 用于设定指定变量的实时值
    def setVarValue(self, varvalues):
        try:
            if str(self.serverAddress).strip() == '' or str(self.serverPort).strip == '' or len(varvalues) == 0:
                raise Exception("参数错误")
            lst = []
            # for x in varvalues:
            #     lst.append({'Name':x.Name,'Value':x.Value})
            # dic={}
            # dic['List',lst]
            url = 'http://{0}:{1}/api/var/SetVarValue'.format(self.serverAddress, self.serverPort)
            values = {'List': varvalues}

            # 将字典格式化成能用的形式
            encodjsoin = json.dumps(values)
            info = requests.post(url, data=encodjsoin, headers={'Content-Type': 'application/json'}).text
            dic = json.loads(info)
            data = dic['Data']
            if data is not None:
                for item in data:
                    lst.append(SetVarValue(item['Name'], item['IsOk']))
            return lst
        except Exception as ex:
            raise Exception('setVarValue设置变量值出错 ', ex)

    # endregion

    # region 私有方法

    def __getVarValueData(self, varnames, pageindex=0, pagesize=1000):
        lst = []
        url = 'http://{0}:{1}/api/var/GetVarValue'.format(self.serverAddress, self.serverPort)
        data = {'names': [p for p in varnames], 'PageIndex': pageindex, 'PageSize': pagesize}
        req_data = urlencode(data)  # 将字典类型的请求数据转变为url编码
        res = request.urlopen(url + '?' + req_data)  # 通过urlopen方法访问拼接好的url
        ret = res.read().decode()  # read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str

        dic = json.loads(ret)
        # 字典构成的序列
        data = dic['Data']
        if data is not None and 'List' in data.keys():
            vars = data['List']
            for item in vars:
                lst.append(self.__converToVarValue(item))

        # 当前页数
        pageIndex = data['PageIndex']
        # 数据总页数
        totalcount = data['TotalCount']
        # if totalcount > 1 and pageIndex < totalcount:
        #     pageIndex += 1
        #     self.__getvarvaluedata(varnames, lst, pageIndex, pagesize)
        return lst

    # 将字典数据转化为VarValue对象
    def __converToVarValue(selft, dic):
        return VarValue(dic['Name'], dic['IsOk'], dic['RawValue'], dic['Value'], dic['Date'])

    # 将字典数据转化为VarSummary对象
    def __convertToVarSummary(self, dic):
        return VarSummary(dic['Name'], dic['Desc'], dic['Type'], dic['RW'], dic['Unit'], dic['Quality'],
                          dic['TagName'])

    # endregion

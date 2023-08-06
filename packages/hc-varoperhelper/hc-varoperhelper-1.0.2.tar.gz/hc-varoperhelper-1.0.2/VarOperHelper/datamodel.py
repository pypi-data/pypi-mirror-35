# -*- coding: utf-8 -*-
from enum import Enum


class VarValue:
    Name = ''
    IsOk = False
    RawValue = 0
    Value = 0
    Date = ''

    def __init__(self, name, isok, rawvalue, value, date):
        self.Name = name
        self.IsOk = isok
        self.RawValue = rawvalue
        self.Value = value
        self.Date = date


class VarSummary:
    Name = ''
    Desc = ''
    Type = ''
    RW = ''
    Unit = ''
    Quality = ''
    TagName = ''

    def __init__(self, name, desc, type, rw, unit, quality, tagname):
        self.Name = name
        self.Desc = desc
        self.Type = type
        self.RW = rw
        self.Unit = unit
        self.Quality = quality
        self.TagName = tagname


class VarDetail:
    Name = ''
    IsOk = False
    BasicInfo = None
    ValueInfo = None

    def __init__(self, name, isok):
        self.Name = name
        self.IsOk = isok


class VarStatisticsResult:
    Result = 0
    IsOk = False

    def __init__(self, isok, result):
        self.Result = result
        self.IsOk = isok


class SetVarValue:
    Name = ''
    IsOk = ''

    def __init__(self, name, isok):
        self.Name = name
        self.IsOk = isok


# 接口getVarStatistics参数值 枚举类型
class StatisticsType(Enum):
    # 原始值方差
    RawValueVariance = 1
    # 处理值方差
    VarlueVariance = 2
    # 原始值平均
    RawValueAvg = 3
    # 处理值平均
    ValueAvg = 4

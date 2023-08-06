'''
Author: Hexu
Date: 2022-03-30 11:47:31
LastEditors: Hexu
LastEditTime: 2023-01-04 15:07:32
FilePath: /iw-algo-fx/intelliw/utils/exception.py
Description: 错误类定义
'''
####### error class #######


class PipelineException(Exception):
    pass


class DatasetException(Exception):
    pass


class InferException(Exception):
    pass


class FeatureProcessException(Exception):
    pass


class DataSourceDownloadException(Exception):
    pass


class LinkServerException(Exception):
    pass


class HttpServerException(Exception):
    pass

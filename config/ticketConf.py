# -*- coding: utf8 -*-
__author__ = 'MR.wen'

import os
import yaml
import codecs


def _get_yaml(ticket_config):
    """
    解析yaml
    :return: s  字典
    """
    path = os.path.join(os.path.dirname(__file__) + '/'+ticket_config)
    f = codecs.open(path,encoding='utf-8')
    s = yaml.load(f)
    f.close()
    return s

# def get_set_info():
#     return _get_yaml()["set"]
#
#
# def get_ticke_peoples():
#     return _get_yaml()["ticke_peoples"]
#
#
# def get_damatu():
#     return _get_yaml()["damatu"]
#
#
# print _get_yaml()["set"]["12306count"]
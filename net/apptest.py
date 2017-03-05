# coding:utf8

from firefly.server.globalobject import netserviceHandle
from firefly.server.globalobject import GlobalObject


@netserviceHandle
def net_handle_100(_conn, data):
    print data
    return data


@netserviceHandle
def net_handle_200(_conn, data):
    """
    所有 200 的消息进来后由我处理
    :param _conn:
    :param data:
    :return:
    """
    print 'net redirect gate!!!'
    return GlobalObject().remote['gate'].callRemote('gate_handle_200', data) # 在此将消息转发给我的父亲 gate

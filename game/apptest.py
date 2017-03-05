#coding:utf8

from firefly.server.globalobject import netserviceHandle,rootserviceHandle, remoteserviceHandle, GlobalObject

@remoteserviceHandle("gate")
def game_handle_200(data):
    """
    通过remoteserviceHandle("父节点name")
    在此方法内处理 ID 200的 消息
    :param data:
    :return:
    """
    print 'game process gate!!!'
    print data
    return data






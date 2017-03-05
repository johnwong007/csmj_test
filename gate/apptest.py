# coding:utf8

from firefly.server.globalobject import netserviceHandle, GlobalObject, remoteserviceHandle, rootserviceHandle


@rootserviceHandle
def gate_handle_200(data):
    """
    我的孩子可以调用我暴露的此接口, 将详细传递给我
    :param data:
    :return:
    """

    print 'gate redirect game!!!'
    print data
    return GlobalObject().root.callChild("game", "game_handle_200", data) #  在此 我将消息传递给我的孩子 game

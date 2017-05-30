# coding:utf8

from firefly.server.globalobject import netserviceHandle, rootserviceHandle, remoteserviceHandle, GlobalObject, \
    webserviceHandle
from twisted.web import resource
from servermanager import NEXT_CARD, WuXingHongHui
from twisted.internet import reactor
import json

w = WuXingHongHui()


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


@webserviceHandle(url="get_gold_pool")
class GameFireFly(resource.Resource):
    def render(self, request):
        code = request.code

        print code

        method = request.method

        print method

        print request.path

        value = request.args

        print "value=", value
        print "value type=", type(value)

        NEXT_CARD.append(int(value.get("next_card")[0]))
        print "next_card = ", NEXT_CARD
        return "OK"


@webserviceHandle(url="control")
class GameStartHandle(resource.Resource):
    def render(self, request):
        code = request.code
        print code
        method = request.method

        print method
        print request.path
        value = request.args

        print "value=", value
        print "value type=", type(value)
        if int(value.get("status", 999)[0]) == 1:
            if not w.is_start:
                reactor.callLater(2, self.start_game, w)
                return "game will start after 2 second"
            else:
                return "game is starting don't start again!!"
        elif int(value.get("status", 999)[0]) == 0:
            reactor.callLater(2, self.stop_game, w)
            return "game will stop after 2 second"
        else:
            return "params error"

    def start_game(self, w):
        w.is_start = True
        reactor.callWhenRunning(w.test_print, say="game start!!!")

    def stop_game(self, w):
        w.is_start = False

# coding=utf-8
from twisted.internet import reactor
from game.util.RandomUtil import get_next_card
import random

GOLD_POOL = 0  # 奖池金额
NEXT_CARD = []  # 测试用设定下局开出的点数
ONE_ROUND_TIME = 3  # 一局间隔时间
IS_START = False


class WuXingHongHui(object):
    def __init__(self, gold_pool=0, next_card=[], one_round_time=3, is_start=False):
        self.gold_pool = gold_pool
        self.next_card = next_card
        self.one_round_time = one_round_time
        self.is_start = is_start
        pass

    def test_print(self, say):
        print say
        self.get_lottery_result()

    def get_lottery_result(self):
        r = get_next_card(self.gold_pool)
        if self.next_card:
            r = self.next_card.pop()
        print r
        if self.is_start:
            reactor.callLater(self.one_round_time, self.get_lottery_result)


if __name__ == "__main__":
    w = WuXingHongHui()
    reactor.callWhenRunning(w.test_print, say="game start!!!")

    reactor.run()

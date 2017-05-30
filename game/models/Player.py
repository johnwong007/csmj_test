# coding=utf-8

class Player(object):

    def __init__(self,name, gander, age, tel, diamond=0, gold=0):
        self.name = name
        self.gander = gander
        self.age = age
        self.tel = tel
        self.diamond = diamond
        self.gold = gold
        self.user_id = None
        self.vip_level = 0
        self.avatar = None

    def update_player_info(self,user):
        self.name = user.name


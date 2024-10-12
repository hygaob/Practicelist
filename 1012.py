#設計一遊戲 玩家有防禦及攻擊  
#防禦有格檔(固定受到0.5傷害)，閃避(隨機閃避成功)
#攻擊有普通攻擊(固定傷害200)及特殊攻擊(隨機傷害50-500)
#有玩家及電腦雙方

import random

class player:
    HP=1000
    def __init__(self,姓名):
        self.姓名=姓名
    def 防禦(self,指令):
        if 指令=="格檔":
            print(f"{self.姓名}舉起武器格檔!")
            return 0.5
        elif 指令=="閃避":
            print(f"{self.姓名}進行閃避")
            是否命中=random.choice([0,1])
class 戰士(player):
    def 攻擊(self,指令):
        if 指令==1:
            print(f"{self.姓名}使出了突刺攻擊!!")
            return 200
        elif 指令==2:
            print(f"{self.姓名}奮力使出迴旋揮砍!!")
            return random.choice([300,100])


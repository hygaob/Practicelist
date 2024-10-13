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
        if 指令==1:
            print(f"{self.姓名}舉起武器格檔!")
            return 0.5
        elif 指令==2:
            print(f"{self.姓名}進行閃避")
            return random.choice([0.3,1])
class 戰士(player):
    def 攻擊(self,指令):
        if 指令==1:
            print(f"{self.姓名}使出了突刺攻擊!!")
            return 200
        elif 指令==2:
            print(f"{self.姓名}奮力使出迴旋揮砍!!")
            return random.choice([300,100])
class 魔物(player):
    def 攻擊(self,指令):
        if 指令==1:
            print(f"{self.姓名}使出了利爪攻擊!!")
            return 200
        elif 指令==2:
            print(f"{self.姓名}張出血口噴出毒液!!")
            return random.choice([300,100])

玩家姓名=input("請輸入你的姓名:")
玩家=戰士(玩家姓名)
敵方=魔物("哥布林")
隨機=random.choice([1,2])
while True:
    攻擊指令=int(input("請輸入您的攻擊指令(1)普功(2)特殊攻擊:"))
    玩家攻擊力=玩家.攻擊(攻擊指令)
    損血=int(敵方.防禦(隨機) * 玩家攻擊力)
    敵方.HP-=損血
    if 敵方.HP<=0:
        print(f"{敵方.姓名}倒下，{玩家.姓名}勝利!!")
        break
    else:
        print(f"{敵方.姓名}受到了{損血}傷害! 生命值剩下{敵方.HP}")
        print("")

    防禦指令=int(input("請輸入您的防禦指令(1)格擋(2)閃避:"))
    敵方攻擊力=敵方.攻擊(隨機)
    損血=int(玩家.防禦(防禦指令) * 敵方攻擊力)
    玩家.HP-=損血
    if 玩家.HP<=0:
        print(f"{玩家.姓名}倒下，{敵方.姓名}勝利!!")
        break
    else:
        print(f"{玩家.姓名}受到了{損血}傷害! 生命值剩下{玩家.HP}")
        print("")

    

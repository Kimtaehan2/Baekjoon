import sys
input = sys.stdin.readline

# 장신구 효과 발동되는 상황
# HR = 전투 승리 시
# RE = 주인공 사망 시
# CO = 모든 전투
# EX = 경험치 계산 시
# DX = 가시 밟았을 때
# HU = 보스 몬스터와 싸울 때
# CU = 쓰레기

class Player:
    def __init__(self,x,y) -> None:
        self.check_game = True # 게임 종료 여부

        self.index = [x,y] # 주인공 위치
        self.Weapon = 0 # 무기 공격력
        self.Armor = 0 # 방어구 방어력
        self.accessory = set() # 장신구
        self.N_DEF = 2 # 기본 방어력
        self.N_ATT = 2 # 기본 공격력

        self.REM_HP = 20 # 최대 체력
        self.CUR_HP = 20 # 현재 체력
        self.Turns = 0 # 턴 수

        self.LV = 1 # 레벨
        self.CUR_EXP = 0 # 현재 경험치
        self.MAX_EXP = 5 # 필요한 총 경험치

    def level_up_effect(self) -> None: # 레벨 업 효과
        self.N_DEF += 2 # 공격력 2 상승
        self.N_ATT += 2 # 방어력 2 상승
        self.REM_HP += 5 # 최대체력 5 상승
        self.CUR_HP = self.REM_HP # 체력 모두 회복
        self.MAX_EXP = 5 * self.LV

    def level_up_check(self,exp_get) -> None: # 레벨업 경험치 계산
        #------------------------장신구------------------------
        # EX : 얻는 경험치가 1.2배가 된다. 소수점 아래는 버린다.
        if 'EX' in self.accessory:
            self.CUR_EXP += int(exp_get*1.2)
        #------------------------------------------------------
        else: self.CUR_EXP += exp_get
        if self.CUR_EXP>=self.MAX_EXP:
          self.CUR_EXP = 0
          self.LV += 1
          self.level_up_effect()

    def move_on(self,cmd): # 이동
        if cmd == 'L': # 왼쪽
            if self.index[0]-1 >= 0:
                self.event(Map[self.index[1]][self.index[0]-1],(self.index[0]-1,self.index[1]))
            else:
                self.event(Map[self.index[1]][self.index[0]],(self.index[0],self.index[1]))
        if cmd == 'R': # 오른쪽
            if self.index[0]+1 < M:
                self.event(Map[self.index[1]][self.index[0]+1],(self.index[0]+1,self.index[1]))
            else:
                self.event(Map[self.index[1]][self.index[0]],(self.index[0],self.index[1]))
        if cmd == 'U': # 위
            if self.index[1]-1 >= 0:
                self.event(Map[self.index[1]-1][self.index[0]],(self.index[0],self.index[1]-1))
            else:
                self.event(Map[self.index[1]][self.index[0]],(self.index[0],self.index[1]))
        if cmd == 'D': # 아래
            if self.index[1]+1 < N:
                self.event(Map[self.index[1]+1][self.index[0]],(self.index[0],self.index[1]+1))
            else:
                self.event(Map[self.index[1]][self.index[0]],(self.index[0],self.index[1]))

    def game_over(self,cause): # 현재 상태를 기준으로 게임을 종료
        
        for y in range(N):
            for x in range(M):
                if Map[y][x] == '.':
                    continue
                elif Map[y][x] == '^':
                    continue
                elif Map[y][x] == '#':
                    continue
                elif type(Map[y][x]) == list:
                    Map[y][x] = 'B'
                else:
                    if type(Map[y][x]) == tuple:
                        Map[y][x] = 'M'
                    else:
                        Map[y][x] = '&'
        if cause == 'WIN':
            Map[self.index[1]][self.index[0]] = '@'
        elif cause == 'Press any key to continue.':
            Map[self.index[1]][self.index[0]] = '@'

        for i in Map:
            print(*i,sep='')
        if self.CUR_HP < 0:
            self.CUR_HP = 0
        print('Passed Turns :',self.Turns)
        print('LV :',self.LV)
        print('HP :',str(self.CUR_HP)+'/'+str(self.REM_HP))
        print('ATT :',str(self.N_ATT)+'+'+str(self.Weapon))
        print('DEF :',str(self.N_DEF)+'+'+str(self.Armor))
        print('EXP :',str(self.CUR_EXP)+'/'+str(self.MAX_EXP))

        # 원인 : 몬스터 이름, SPIKE TRAP, WIN, Press any key to continue.
        if cause == 'WIN':
            Map[self.index[1]][self.index[0]] = '@'
            print('YOU WIN!')
        elif cause == 'Press any key to continue.':
            Map[self.index[1]][self.index[0]] = '@'
            print('Press any key to continue.')
        else:
            print('YOU HAVE BEEN KILLED BY',str(cause)+'..')
        self.check_game = False



    def battle(self,monster,idx):
        if type(monster) == tuple: # 보스와의 전투
            monster = monster[1]
            #---------------------------------------------------장신구---------------------------------------------------
            # HU : 보스 몬스터와 전투에 돌입하는 순간 체력을 최대치까지 회복하고, 보스 몬스터의 첫 공격에 0의 데미지를 입는다.
            HU_cnt = 0
            if 'HU' in self.accessory:
                HU_cnt = 1 # 첫 공격 0 데미지 카운트
                self.CUR_HP = self.REM_HP # 체력 모두 회복
            #------------------------------------------------------------------------------------------------------------
            check = 0
            #-------------------------------------장신구-------------------------------------
            # CO : 모든 전투에서, 첫 번째 공격에서 주인공의 공격력(무기 합산)이 두 배로 적용된다.
            # DX : Courage 장신구와 함께 착용할 경우, Courage의 공격력 효과가 두 배로 적용되는 대신 세 배로 적용된다.
            if 'CO' in self.accessory:
                check = 1
                if 'DX' in self.accessory:
                    check = 2
            #-------------------------------------------------------------------------------
            while 1:
                
                if check == 1:
                    monster_harm = max(1,(self.N_ATT + self.Weapon)*2 - monster.DEF)
                    check = 0
                elif check == 2:
                    monster_harm = max(1,(self.N_ATT + self.Weapon)*3 - monster.DEF)
                    check = 0
                else:
                    monster_harm = max(1,self.N_ATT + self.Weapon - monster.DEF)

                monster.CUR_HP -= monster_harm

                if monster.CUR_HP <= 0: # 승리
                    #-------------------------------------장신구-------------------------------------
                    # HR : 전투에서 승리할 때마다 체력을 3 회복한다. 체력은 최대 체력 수치까지만 회복된다.
                    if 'HR' in self.accessory:
                        self.CUR_HP += 3
                        if self.CUR_HP > self.REM_HP:
                            self.CUR_HP = self.REM_HP
                    #-------------------------------------------------------------------------------
                    self.level_up_check(monster.E)
                    # 이동
                    self.index[0] = idx[0]
                    self.index[1] = idx[1]
                    # 몬스터 삭제
                    Map[idx[1]][idx[0]] = '.'
                    #------------------------------------게임종료------------------------------------
                    self.game_over('WIN')
                    #-------------------------------------------------------------------------------
                    break

                if HU_cnt == 1: # 공격 무효화 on
                    player_harm = 0
                    HU_cnt = 0
                else: # 공격 무효화 off
                    player_harm = max(1,monster.ATK - self.N_DEF - self.Armor)
                self.CUR_HP -= player_harm

                if self.CUR_HP <= 0: # 패배
                    #-------------------------------------------------장신구-------------------------------------------------
                    # RE : 주인공이 사망했을 때 소멸하며, 주인공을 최대 체력으로 부활시켜 준 뒤, 주인공을 첫 시작 위치로 돌려보낸다.
                    if 'RE' in self.accessory:
                        self.accessory.discard('RE')
                        self.CUR_HP = self.REM_HP
                        # 이동
                        self.index[0] = start[0]
                        self.index[1] = start[1]
                    #--------------------------------------------------------------------------------------------------------
                    else: self.game_over(monster.name)
                    break

        else: # 다른 몬스터와의 전투
            check = 0
            #-------------------------------------장신구-------------------------------------
            # CO : 모든 전투에서, 첫 번째 공격에서 주인공의 공격력(무기 합산)이 두 배로 적용된다.
            # DX : Courage 장신구와 함께 착용할 경우, Courage의 공격력 효과가 두 배로 적용되는 대신 세 배로 적용된다.
            if 'CO' in self.accessory:
                check = 1
                if 'DX' in self.accessory:
                    check = 2
            #-------------------------------------------------------------------------------
            while 1:
                if check == 1:
                    monster_harm = max(1,(self.N_ATT + self.Weapon)*2 - monster.DEF)
                    check = 0
                elif check == 2:
                    monster_harm = max(1,(self.N_ATT + self.Weapon)*3 - monster.DEF)
                    check = 0
                else:
                    monster_harm = max(1,self.N_ATT + self.Weapon - monster.DEF)
                monster.CUR_HP -= monster_harm
                if monster.CUR_HP <= 0: # 승리
                    #-------------------------------------장신구-------------------------------------
                    # HR : 전투에서 승리할 때마다 체력을 3 회복한다. 체력은 최대 체력 수치까지만 회복된다.
                    if 'HR' in self.accessory:
                        self.CUR_HP += 3
                        if self.CUR_HP > self.REM_HP:
                            self.CUR_HP = self.REM_HP
                    #-------------------------------------------------------------------------------
                    self.level_up_check(monster.E)
                    # 이동
                    self.index[0] = idx[0]
                    self.index[1] = idx[1]
                    # 몬스터 삭제
                    Map[idx[1]][idx[0]] = '.'
                    break

                player_harm = max(1,monster.ATK - self.N_DEF - self.Armor)
                self.CUR_HP -= player_harm

                if self.CUR_HP <= 0: # 패배
                    #-------------------------------------------------장신구-------------------------------------------------
                    # RE : 주인공이 사망했을 때 소멸하며, 주인공을 최대 체력으로 부활시켜 준 뒤, 주인공을 첫 시작 위치로 돌려보낸다.
                    # 전투 중이던 몬스터가 있다면 해당 몬스터의 체력도 최대치로 회복된다.
                    if 'RE' in self.accessory:
                        self.accessory.discard('RE')
                        self.CUR_HP = self.REM_HP
                        # 몬스터 체력 모두 회복
                        monster.CUR_HP = monster.MAX_HP
                        # 이동
                        self.index[0] = start[0]
                        self.index[1] = start[1]
                    #--------------------------------------------------------------------------------------------------------
                    else: self.game_over(monster.name)
                    break


    def event(self,other,idx): # 각 턴마다의 이벤트
        self.Turns += 1
        if other == '.': # 빈 칸
            # 이동
            self.index[0] = idx[0]
            self.index[1] = idx[1]

        elif other == '^': # 가시
            #----------------장신구-----------------
            # DX : 가시 함정에 입는 데미지가 1로 고정
            if 'DX' in self.accessory:
                self.CUR_HP -= 1
            else: self.CUR_HP -= 5
            #---------------------------------------
            if self.CUR_HP <= 0:
                #-------------------------------------------------장신구-------------------------------------------------
                # RE : 주인공이 사망했을 때 소멸하며, 주인공을 최대 체력으로 부활시켜 준 뒤, 주인공을 첫 시작 위치로 돌려보낸다.
                if 'RE' in self.accessory:
                    self.accessory.discard('RE')
                    self.CUR_HP = self.REM_HP
                    # 이동
                    self.index[0] = start[0]
                    self.index[1] = start[1]
                #--------------------------------------------------------------------------------------------------------
                else: self.game_over('SPIKE TRAP')
            # 이동
            else:
                self.index[0] = idx[0]
                self.index[1] = idx[1]

        elif other == '#': # 벽
            self.Turns -= 1
            self.event(Map[self.index[1]][self.index[0]],(self.index[0],self.index[1]))
            
        elif type(other) == list: # 아이템 상자
            if other[0] == 'W': # 무기
                self.Weapon = int(other[1])
            if other[0] == 'A': # 방어구
                self.Armor = int(other[1])
            if other[0] == 'O': # 장신구
                if len(self.accessory)<4:
                    self.accessory.add(other[1])
            # 이동
            self.index[0] = idx[0]
            self.index[1] = idx[1]
            # 빈칸으로 만들기
            Map[idx[1]][idx[0]] = '.'

        else: # 몬스터
            if type(other) == tuple: # 보스
                self.battle(other,idx)
            else:
                self.battle(other,idx)
            
        

class Monster: 
    def __init__(self,name,ATK,DEF,HP,E) -> None:
        self.name = name
        self.ATK = ATK
        self.DEF = DEF
        self.MAX_HP = HP
        self.CUR_HP = HP
        self.E = E


#---------------------------------입력----------------------------------
N,M = map(int,input().split())
Map = [list(input().rstrip()) for i in range(N)]

MOVE = list(input().rstrip())
monster_cnt = 0
item_cnt = 0
for y in range(N):
    for x in range(M):
        if Map[y][x] == '@':
            Map[y][x] = '.'
            start = [x,y]
            Hero = Player(x,y)
        elif Map[y][x] == '&':
            monster_cnt += 1
        elif Map[y][x] == 'B':
            item_cnt += 1
        elif Map[y][x] == 'M':
            Boss_idx = [x,y]

for _ in range(monster_cnt+1):
    cmd = list(input().split())
    if (int(cmd[1])-1 == Boss_idx[0]) and (int(cmd[0])-1 == Boss_idx[1]):
        Map[int(cmd[0])-1][int(cmd[1])-1] = ('Boss',Monster(cmd[2],int(cmd[3]),int(cmd[4]),int(cmd[5]),int(cmd[6])))
    else: Map[int(cmd[0])-1][int(cmd[1])-1] = Monster(cmd[2],int(cmd[3]),int(cmd[4]),int(cmd[5]),int(cmd[6]))

for _ in range(item_cnt):
    cmd = list(input().split())
    Map[int(cmd[0])-1][int(cmd[1])-1] = [cmd[2],cmd[3]]
#---------------------------------입력----------------------------------


for i in MOVE:
    if Hero.check_game:
        Hero.move_on(i)
    else: break

if Hero.check_game:
    Hero.game_over('Press any key to continue.')

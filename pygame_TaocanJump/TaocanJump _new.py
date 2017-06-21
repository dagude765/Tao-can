# -*- coding: utf-8 -*-
# 每次仅存在一个friends
import sys, time, random, math, pygame,locale
from pygame.locals import *
from MyDatabase import *

def delete_game():
    for e in group_flower:
        group_flower.remove(e)
    for e in group_river:
        group_river.remove(e)
    #group.remove(player)
    group.remove(tree)
    group_friends.remove(friends)
    group_love.remove(love)
    game_over = False
    #game_restart = False
    score = 0
    turnover_time = 10 #数据全还原
    
#重置tree函数
def reset_tree():
    #y = random.randint(270,350)
    y = 290
    tree.position = 800,y
    bullent_sound.play_sound()
    
#重置friends函数
def reset_friends(tree_x, group_river):
    temp_x = random.randint(0,840)+800
    canput_tag = 1
    dist1 = temp_x-tree_x
    if dist1 % 840 > 240 and dist1 % 840 < 600:
        for e in group_river:
            if e.X >= 560 and e.X <= 1880: #由于river也是随机生成有约束，只需考虑有可能有影响的部分
                dist2 = abs(temp_x-e.X)
                if dist2 % 840 <= 240 or dist2 % 840 >= 600:
                    canput_tag = 0
                    break
        if canput_tag:
            friends.X = temp_x

#定义一个滚动地图类
class MyMap(pygame.sprite.Sprite):
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.bg = pygame.image.load("background.png").convert_alpha()
    def map_rolling(self):
        if self.x < -300:
            self.x = 300
        else:
            self.x -=5
    def map_update(self):
        screen.blit(self.bg, (self.x,self.y))
    def set_pos(x,y):
        self.x =x
        self.y =y
#定义一个按钮类
class Button(object):
    def __init__(self, upimage, downimage,position):
        self.imageUp = pygame.image.load(upimage).convert_alpha()
        self.imageDown = pygame.image.load(downimage).convert_alpha()
        self.position = position
        self.push = False
        
    def isOver(self):
        point_x,point_y = pygame.mouse.get_pos()
        x, y = self. position
        w, h = self.imageUp.get_size()

        in_x = x - w/2 < point_x < x + w/2
        in_y = y - h/2 < point_y < y + h/2
        return in_x and in_y

    def render(self):
        w, h = self.imageUp.get_size()
        x, y = self.position
        
        if self.isOver():
            screen.blit(self.imageDown, (x-w/2,y-h/2))
        else:
            screen.blit(self.imageUp, (x-w/2, y-h/2))
    def is_start(self):
        if self.isOver():
            b1,b2,b3 = pygame.mouse.get_pressed()
            if b1 == 1:
                self.push = True
                bg_sound.play_pause()
                btn_sound.play_sound()
                bg_sound.play_sound()

def replay_music():
    bg_sound.play_pause()
    bg_sound.play_sound()

#定义一个数据IO的方法
def data_read():
    fd_1 = open("data.txt","r")
    best_score = fd_1.read()
    fd_1.close()
    return best_score

#定义开始界面
def showWelcome(gameStart):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              pygame.quit()
              exit()
        if event.type == pygame.MOUSEBUTTONUP:
            if gameStart.isOver():
                return False
    screen.blit(interface, (0,0))
    gameStart.render()
    return True
   
#定义一个控制声音的类和初始音频的方法
def audio_init():
    global btn_au,bg_au,bullent_au,bossstart_au,getscore_au,tree_au,friends_au
    pygame.mixer.init()
    btn_au = pygame.mixer.Sound("button.wav")
    bg_au = pygame.mixer.Sound("background.ogg")
    bullent_au = pygame.mixer.Sound("bullet.wav")
    #bossstart_au = pygame.mixer.Sound("bossstart.wav")
    #getscore_au = pygame.mixer.Sound("91.wav")
    #tree_au = pygame.mixer.Sound("tree.wav")
    #friends_au = pygame.mixer.Sound("friends.wav")
class Music():
    def __init__(self,sound):
        self.channel = None
        self.sound = sound     
    def play_sound(self):
        self.channel = pygame.mixer.find_channel(True)
        self.channel.set_volume(0.5)
        self.channel.play(self.sound)
    def play_pause(self):
        self.channel.set_volume(0.0)
        self.channel.play(self.sound)
      
#主程序部分
pygame.init()
audio_init()
screen = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption("韬璨快跳！")
font = pygame.font.Font(None, 22)
font1 = pygame.font.Font(None, 40)
font2 = pygame.font.SysFont('kaiti', 20)
framerate = pygame.time.Clock()
upImageFilename = 'game_start_up.png'
downImageFilename = 'game_start_down.png'
#创建按钮对象
startbutton = Button(upImageFilename,downImageFilename, (400,500))
restartbutton = Button('game_restart_up.png','game_restart_down.png', (400,400))
quitbutton = Button('game_quit_up.png','game_quit_down.png', (400,500))
interface = pygame.image.load("myinterface.png")

#创建地图对象
bg1 = MyMap(0,0)
bg2 = MyMap(300,0)

ground_y = 370#地面高度
#创建一个精灵组
group = pygame.sprite.Group()
group_flower = pygame.sprite.Group()
group_river = pygame.sprite.Group()
group_friends = pygame.sprite.Group()
group_love = pygame.sprite.Group()
group_lagrange = pygame.sprite.Group()
group_knowledge = pygame.sprite.Group()
group_teacher = pygame.sprite.Group()

#创建玩家精灵
player = MySprite()
player.load("sprite.png", 100, 100, 4)#选取第一个图
player.position = 300, (ground_y-100)
group.add(player)

#创建friends精灵
friends = MySprite()
friends.load("chang2.png", 55, 75, 1)
friends.position = -50, ground_y-75
group_friends.add(friends)

#创建love精灵
love = MySprite()
love.load("love.png",53,120,4)
love.position = -50, ground_y
group_love.add(love)

#创建lagrange精灵
lagrange = MySprite()
lagrange.load("crown.png",80,58,1)
lagrange.position = -50, random.randint(65,200)
group_lagrange.add(lagrange)

#创建子弹精灵
tree = MySprite()
#tree.load("chang.png", 40, 16, 1)
tree.load("tree.png", 75, 80, 1)
tree.position = 800, (ground_y-80)
group.add(tree)

#创建知识精灵
knowledge = MySprite()
knowledge.load("fruit.bmp", 75, 20, 1)
knowledge.position = -50, (ground_y-80)
group_knowledge.add(knowledge)

#创建老师精灵
teacher = MySprite()
teacher.load("teacher.png", 131, 150, 1)
teacher.position = 800-teacher.frame_width, (ground_y-teacher.frame_height)
group_teacher.add(teacher)

#定义一些变量
tree_vel = 7.0 #奇数可以保证显示爱心的成功
flower_vel = 5.0
game_over = False
you_win = False
player_jumping = False
jump_vel = 0.0
player_start_y = player.Y
player_hit = False
#monster_hit = False
jumpover_flag = False
love_flag = False
k_next = True
m_first = True
best_score = 0
global bg_sound,btn_sound,bullent_sound,bossstart_sound,getscore_sound,tree_sound,friends_sound
bg_sound=Music(bg_au)
btn_sound=Music(btn_au)
bullent_sound =Music(bullent_au)
#bossstart_sound = Music(bossstart_au)
#getscore_sound = Music(getscore_au)
#tree_sound = Music(tree_au)
#friends_sound = Music(friends_au)
game_round = {1:'ROUND ONE',2:'ROUND TWO',3:'ROUND THREE',4:'ROUND FOUR',5:'ROUND FIVE'}
game_pause = True
exjump_vel = {pygame.K_SPACE: 0.0} 
index =0
current_time = 0
start_time = 0
music_time = 0
turnover_time = 10 #可失误次数
score =0 #得分
replay_flag = True
game_restart = False #是否是重新开始
invincible_frame = 800 #800帧的无敌时间
get_knowledge_frame = 180 #180帧的消化时间
game_boss = False
boss_start = False
boss_life = 5
boss_beat = [False]*10
boss_round = 0
bossmusic_switch = True
lower_time = [1.2,1,0.8,0.6,0.4]
upper_time = [3.5,3,2.5,2,1.5]

river_x = 0#初始河流位置delta
i = 0
#循环
bg_sound.play_sound()
best_score = data_read()

#开始界面
while showWelcome(startbutton):
    pygame.display.update()

#event = pygame.event.wait()    
while True:
    framerate.tick(60)
    ticks = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: #按下space就给个初速度
            if event.key in exjump_vel:
                exjump_vel[event.key] = -0.2
        elif event.type == pygame.KEYUP: #松开space把速度设为0
            if event.key in exjump_vel:
                exjump_vel[event.key] = 0.0
                
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()
    
    if game_boss and not boss_start:
        current_time =time.clock()-start_time
        if bossmusic_switch:
            #bossstart_sound.play_sound()
            bossmusic_switch = False
            #print("hahaha")
        if current_time > 5:
            boss_life = 5
            boss_round += 1
            boss_start = True
            k_next = True
            start_time = time.clock()
            if boss_round <= 5:
                upperbound = upper_time[boss_round-1]
                lowerbound = lower_time[boss_round-1]
            else:
                upperbound = upper_time[4]
                lowerbound = lower_time[4]

        #检测玩家是否处于跳跃状态
        if player_jumping:
            if jump_vel <0:#上升阶段，初速度12，递减0.6
                jump_vel += 0.6 + exjump_vel[pygame.K_SPACE]
            elif jump_vel >= 0:#下降阶段，初速度0，递增0.8
                jump_vel += 0.8
            player.Y += jump_vel
            if player.Y > player_start_y:
                player_jumping = False
                player.Y = player_start_y
                jump_vel = 0.0

        #绘制背景
        bg1.map_update()
        bg2.map_update()
        bg1.map_rolling()
        bg2.map_rolling()
        
        #更新精灵组
        if not game_over:
            group.update(ticks, 60)#每个sprite都有update方法
            group_lagrange.update(ticks,60)
        #循环播放背景音乐
        music_time = time.clock()
        if music_time > 150 and replay_flag:
            replay_music()
            replay_flag =False
        #绘制精灵组
        group.draw(screen)#图片来自于self.image 位置来自于self.rect.topleft,表示图片左上角的位置
        group_lagrange.draw(screen)
        print_text(font, 330, 560, "press SPACE to jump up!")
        print_text(font, 100, 20, "You have get Score:",(219,224,22))
        print_text(font, 500, 20, "Your rest turnover time:",(219,224,22))
        print_text(font1, 280, 10, str(score),(255,0,0))
        print_text(font1, 700, 10, str(turnover_time),(255,0,0))
        print_text(font1, 200, 100, "WARNING!! BOSS APPEARS", (255,0,0))
        if player.invincible:
            print_text(font2, player.X-10, lagrange.Y-40, "我是拉格朗日，",(241,158,194))
            print_text(font2, player.X-10, lagrange.Y-20, "数学都是浮云！",(241,158,194))        
        
    elif game_boss and boss_start:
        if keys[K_SPACE]:
            if not player_jumping:
                player_jumping = True
                #jump_vel = -12.0 #初速度, 调低一点
                jump_vel = -12.0     
        
        current_time =time.clock()-start_time   
        if k_next:
            river_random = random.uniform(lowerbound, upperbound)
            k_next = False
            print(river_random)
        if current_time > river_random:#1/100的可能性
            element = MySprite()
            element.load("paper.png", 80, 60, 1)
            element.position = 800-teacher.frame_width, (ground_y-80)
            group_river.add(element)
            start_time = time.clock()
            k_next = True
        
        if knowledge.X < -200 and not player.knowledge_learned:
            knowledge.position = 800, random.randint(65,200)
        #lagrange到地图左端比较远了，请更新
        if (-lagrange.X) // tree_vel >= 2000:
            lagrange.position = 800+random.randint(0,800), random.randint(65,200)
        if player.invincible: #每帧的无敌时间减少
            invincible_frame -= 1
        if invincible_frame == 0: #无敌时间到
            player.invincible = False
            lagrange.X = -50
            invincible_frame = 800
            
        if player.get_knowledge:
            get_knowledge_frame -= 1
        if get_knowledge_frame == 0: 
            player.knowledge_learned = True
            #player.get_knowledge = False
            #get_knowledge_frame = 200
        
        #玩家是否吃上无敌
        if pygame.sprite.collide_rect(lagrange, player) and not player.invincible:
            #lagrange.X = -50
            lagrange.position = player.X+10, player.Y-50#player戴上日帽子
            #group_lagrange.add(lagrange) #如果把lagrange吃了就去掉
            player.invincible = True
        
        if pygame.sprite.collide_rect(knowledge, player) and not player.knowledge_learned:
            player.get_knowledge = True
            #player.knowledge_learned = True
            knowledge.position = -100, random.randint(65,200)
        
        #print(group_river)
        #遍历river，使river移动, 并与river碰撞
        for e in group_river:
            if e.X < -80 or e.X > 800-teacher.frame_width:
                group_river.remove(e)
            elif not e.perfect:
                e.X -= tree_vel
            else: #得到了满分向boss移动
                e.Y = 250
                e.X += tree_vel
            if pygame.sprite.collide_rect(e, player) and not e.crash and not e.perfect and not player.invincible and not player.knowledge_learned:
                e.crash = True
                #tree_sound.play_sound()
                e.image = pygame.image.load("0.png").convert_alpha()
                turnover_time -= 1
            elif pygame.sprite.collide_rect(e, player) and not e.perfect and (player.invincible or player.knowledge_learned):
                e.perfect = True
                #getscore_sound.play_sound()
                e.image = pygame.image.load("91.png").convert_alpha()
                player.knowledge_learned = False
                player.get_knowledge = False
                get_knowledge_frame = 180
        
        for e in group_river:
            if e.X > 800-teacher.frame_width and e.perfect:
                #score += 3
                boss_life -= 1 #击中boss加分，boss掉血
                e.perfect = False

        #使knowledge移动
        if not player.get_knowledge:
            knowledge.X -= flower_vel                
        
        #使lagrange移动
        if not player.invincible:
            lagrange.X -= flower_vel
        else:
            lagrange.Y = player.Y-50
        
        #检测玩家是否处于跳跃状态
        if player_jumping:
            if jump_vel <0:#上升阶段，初速度12，递减0.6
                jump_vel += 0.6 + exjump_vel[pygame.K_SPACE]
            elif jump_vel >= 0:#下降阶段，初速度0，递增0.8
                jump_vel += 0.8
            player.Y += jump_vel
            if player.Y > player_start_y:
                player_jumping = False
                player.Y = player_start_y
                jump_vel = 0.0

        #绘制背景
        bg1.map_update()
        bg2.map_update()
        bg1.map_rolling()
        bg2.map_rolling()

        #用完失误次数了
        if turnover_time <= 0:
            game_over = True
            game_boss = False
            
        #更新精灵组
        if not game_over:
            group.update(ticks, 60)#每个sprite都有update方法
            group_knowledge.update(ticks,60)
            group_river.update(ticks,60)
            group_lagrange.update(ticks,60)
            group_teacher.update(ticks,60)
        #循环播放背景音乐
        music_time = time.clock()
        if music_time > 150 and replay_flag:
            replay_music()
            replay_flag =False
        #绘制精灵组
        group.draw(screen)#图片来自于self.image 位置来自于self.rect.topleft,表示图片左上角的位置
        group_knowledge.draw(screen)
        group_river.draw(screen)
        group_lagrange.draw(screen)
        group_teacher.draw(screen)
        print_text(font, 330, 560, "press SPACE to jump up!")
        print_text(font, 100, 20, "You have get Score:",(219,224,22))
        print_text(font, 500, 20, "Your rest turnover time:",(219,224,22))
        print_text(font1, 280, 10, str(score),(255,0,0))
        print_text(font1, 700, 10, str(turnover_time),(255,0,0))
        print_text(font1, 700, 100, str(boss_life),(255,0,0))
        if player.invincible:
            print_text(font2, player.X-10, lagrange.Y-40, "我是拉格朗日，",(241,158,194))
            print_text(font2, player.X-10, lagrange.Y-20, "数学都是浮云！",(241,158,194))    
        if player.get_knowledge:
            if get_knowledge_frame > 0:
                cnt_down = get_knowledge_frame // 60 + 1
                print_text(font2, 200, 100, str(cnt_down),(255,0,0))
            else:
                print_text(font2, 200, 100, "就绪！",(255,0,0))
        else:
            print_text(font2, 200, 100, "没有！",(255,0,0))
            
        if boss_life == 0: #boss环节结束
            game_boss = False
            boss_start = False
            boss_beat[boss_round-1] = True
            delete_game()
            river_x = 0
            tree.position = 800, (ground_y-80)
            tree.crash = False
            group.add(tree)
            friends.position = -50, ground_y-75
            group_friends.add(friends)
            love.position = -50, ground_y
            group_love.add(love)
            score += 50
            print("you win")
        
    elif not game_over:
        #keys = pygame.key.get_pressed()
        if keys[K_SPACE]:
            if not player_jumping:
                player_jumping = True
                #jump_vel = -12.0 #初速度, 调低一点
                jump_vel = -12.0      
        #随机生成奖励
        flower_random = random.randint(1,250)
        if flower_random < 2:#1/150的可能性
            element = MySprite()
            element.load("flower.png", 50, 48, 1)
            #tmp_x +=random.randint(50,120)
            element.X = 800
            element.Y = random.randint(65,200)#跳跃极限高度是270-186=84，砖块最高下层是65+20=85，刚好吃到
            group_flower.add(element)

        #随机生成河流
        river_random = random.randint(1,100)
        if river_random < 2:#1/100的可能性
            element = MySprite()
            element.load("river.png", 150, 93, 1)#大小得调一下
            element.X = 800 + river_x 
            tmp = abs(element.X-tree.X)
            tmp2 = abs(element.X-friends.X)
            if (tmp % 840 > 300 and tmp % 840 < 540 and friends.X <= 0) or (tmp % 840 > 300 and tmp % 840 < 540 and friends.X > 0 and tmp2 % 840 > 240 and tmp2 % 840 < 600):#不能离tree太近，否则不加
                element.Y = ground_y-3 #地面是370
                river_x += 300
                group_river.add(element)
           
        #更新子弹
        if not game_over:
            tree.X -= tree_vel
        if tree.X < -40: 
            tree.crash = False
            jumpover_flag = False
            reset_tree()
        #friends到地图左端比较远了，判断是否更新
        if (-friends.X) // tree_vel >= 800:
            reset_friends(tree.X, group_river)
        #lagrange到地图左端比较远了，请更新
        if (-lagrange.X) // tree_vel >= 2000:
            lagrange.position = 800+random.randint(0,800), random.randint(65,200)
        if player.invincible: #每帧的无敌时间减少
            invincible_frame -= 1
        if invincible_frame == 0: #无敌时间到
            player.invincible = False
            lagrange.X = -50
            invincible_frame = 800
        
        #玩家是否吃上无敌
        if pygame.sprite.collide_rect(lagrange, player) and not player.invincible:
            #lagrange.X = -50
            lagrange.position = player.X+10, player.Y-50#player戴上日帽子
            #group_lagrange.add(lagrange) #如果把lagrange吃了就去掉
            player.invincible = True
            
        #碰撞检测，子弹是否击中玩家
        if pygame.sprite.collide_rect(tree, player) and not tree.crash and not player.invincible: #撞上树，且不是已撞过得状态，且不是无敌
            turnover_time -= 1
            tree.crash = True
            #tree_sound.play_sound()
            #game_over = False
            #game_over = True
        if player.X > tree.X+tree.frame_width and not jumpover_flag and not tree.crash:
            jumpover_flag = True
            score += 1 #跳过一个tree+1分
        #遍历果实，使果实移动
        for e in group_flower:
            e.X -= flower_vel
        collide_list = pygame.sprite.spritecollide(player,group_flower,True)
        score +=len(collide_list)
        
        #遍历river，使river移动
        for e in group_river:
            e.X -= tree_vel
            if pygame.sprite.collide_rect(e, player) and not e.crash and not player.invincible:
                e.crash = True
                turnover_time -= 1
                #game_over = True
                #game_over = False
                
        #使love移动
        love.X -= tree_vel
        
        #使lagrange移动
        if not player.invincible:
            lagrange.X -= flower_vel
        else:
            lagrange.Y = player.Y-50
                
        #使friends移动
        friends.X -= tree_vel
        if abs(friends.X+friends.frame_width//2-player.X-player.frame_width) < tree_vel / 2 and not player_jumping: #这个距离判断和player width=100有关
            score += 2
            love.frame = 0
            love.position = friends.X+5, friends.Y-130
        elif abs(friends.X+friends.frame_width//2-player.X-player.frame_width) < tree_vel / 2 and player_jumping:
            #friends_sound.play_sound()
            score -= 5
            
        #检测玩家是否处于跳跃状态
        if player_jumping:
            if jump_vel <0:#上升阶段，初速度12，递减0.6
                jump_vel += 0.6 + exjump_vel[pygame.K_SPACE]
            elif jump_vel >= 0:#下降阶段，初速度0，递增0.8
                jump_vel += 0.8
            player.Y += jump_vel
            if player.Y > player_start_y:
                player_jumping = False
                player.Y = player_start_y
                jump_vel = 0.0


        #绘制背景
        bg1.map_update()
        bg2.map_update()
        bg1.map_rolling()
        bg2.map_rolling()
        
        #用完失误次数了
        if turnover_time <= 0:
            game_over = True
            
        #更新精灵组
        if not game_over:
            group.update(ticks, 60)#每个sprite都有update方法
            group_flower.update(ticks,60)
            group_river.update(ticks,60)
            group_friends.update(ticks,60)
            group_love.update(ticks,120)#要播放变慢得往大了调
            group_lagrange.update(ticks,60)
        #循环播放背景音乐
        music_time = time.clock()
        if music_time   > 150 and replay_flag:
            replay_music()
            replay_flag = False
        #绘制精灵组
        group.draw(screen)#图片来自于self.image 位置来自于self.rect.topleft,表示图片左上角的位置
        group_flower.draw(screen)
        group_river.draw(screen)
        group_friends.draw(screen)
        group_love.draw(screen)
        group_lagrange.draw(screen)
        print_text(font, 330, 560, "press SPACE to jump up!")
        print_text(font, 100, 20, "You have get Score:",(219,224,22))
        print_text(font, 500, 20, "Your rest turnover time:",(219,224,22))
        print_text(font1, 280, 10, str(score),(255,0,0))
        print_text(font1, 700, 10, str(turnover_time),(255,0,0))
        if player.invincible:
            print_text(font2, player.X-10, lagrange.Y-40, "我是拉格朗日，",(241,158,194))
            print_text(font2, player.X-10, lagrange.Y-20, "数学都是浮云！",(241,158,194))
        
        if score >= (5*boss_round+65)*boss_round+10 and not boss_beat[boss_round]: #打boss了！！
            game_boss = True
            delete_game()
            river_x = 0
            start_time = time.clock()
            bossmusic_switch = True
            
    else: 
        if score >int (best_score):
            best_score = score
        fd_2 = open("data.txt","w+")
        fd_2.write(str(best_score))
        fd_2.close()
        
        screen.fill((200, 200, 200))                
        print_text(font1, 300, 100,"GAME OVER!",(240,20,20))
        print_text(font1, 320, 200, "Best Score:",(120,224,22))
        print_text(font1, 370, 240, str(best_score),(255,0,0))
        print_text(font1, 270, 280, "This Game Score:",(120,224,22))
        print_text(font1, 370, 330, str(score),(255,0,0))
        restartbutton.render()
        quitbutton.render()
        pygame.display.update()
        event = pygame.event.wait() #必须做一个操作来重新开始
        #print('haha')
        #print(event)
        if event.type == pygame.MOUSEBUTTONUP:   
            if restartbutton.isOver():
                delete_game()
                game_over = False
                #game_restart = False
                score = 0
                river_x = 0
                turnover_time = 10 #数据全还原
                #print(group)
                start_time = time.clock()
                current_time =time.clock()-start_time
                while current_time<3:
                    screen.fill((200, 200, 200))
                    print_text(font1, 250, 250, "New game, ready?!",(240,20,20))
                    pygame.display.update()
                    current_time =time.clock()-start_time
                #player.position = 300, (ground_y-100)
                #group.add(player)
                tree.position = 800, (ground_y-80)
                tree.crash = False
                group.add(tree)
                friends.position = -50, ground_y-75
                group_friends.add(friends)
                love.position = -50, ground_y
                group_love.add(love)
            if quitbutton.isOver():
                pygame.quit()
                sys.exit()
    pygame.display.update()

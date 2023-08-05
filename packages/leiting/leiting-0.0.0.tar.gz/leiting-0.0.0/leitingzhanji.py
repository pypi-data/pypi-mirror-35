import pygame,math,sys,os,time
import random as r

class HighScore:
    #最高分储存
    hestory=0
    def __init__(self,path="hestory.txt"):
        self.path=path
        #首次配置文件
        #文件存在读取文件位置
        if os.path.exists(self.path):
            with open(self.path,"r")as f_r:
                HighScore.hestory=f_r.read()
        else:
            with open(self.path,"w")as f_w:
                f_w.write("0")
    #写入数据
    def write_high_score(self,history):
        if history>int(HighScore.hestory):
            with open(self.path,"w")as f_w:
                f_w.write(str(history))
    #读取数据
    def read_high_score(self):
        with open(self.path,"r")as f_r:
            HighScore.hestory=f_r.read()
#启动界面类
begin_image=[   pygame .image.load(r"image\screen.jpg"),
                pygame .image.load(r"image\loading.png"),
                pygame .image.load(r"image\title.png"),
                pygame .image.load(r"image\Begin.png"),
                pygame .image.load(r"image\1.png"),
                pygame .image.load(r"image\2.png"),
                pygame .image.load(r"image\3.png"),
                pygame .image.load(r"image\4.png"),
                pygame .image.load(r"image\5.png"),
                pygame .image.load(r"image\6.png"),
                pygame .image.load(r"image\7.png"),
                pygame .image.load(r"image\8.png"),
                pygame.image.load("image\warBg.jpg"),
                pygame.image.load("image\warBg1.jpg"),
                pygame.image.load("image/logo.png")



            ]
#暂停按钮图片
pause_play_button=[pygame.image.load("image\pause_.png"),
                 pygame.image.load("image\start.png")]

#血量图片
hp_img=pygame.image.load("image\hp.png")

class BeginWindow:
    #开始界面
    is_inside=False

    def __init__(self,begin_image,screen):
        self.bg=begin_image[0]
        self.bg1=begin_image[14]
        self.looding=begin_image[1]
        self.name=begin_image[2]
        self.kaishi=begin_image[3]
        self.roll=begin_image[4:12]
        self.lei_ting=begin_image[12]
        self.screen=screen
        self.index=0

        #动图变量
        self.add_index=0
        self.img_index=0

    #图片渲染
    def display(self):
        #主背景图片
        self.screen.blit(self.bg,(0,0))
        self.screen.blit(self.bg1,(0,0))
        #浮动文字
        self.index+=r.uniform(0,0.07)
        name_pos_x=(self.screen.get_width()-self.name.get_width())/2
        name_pos_y=120+25*math.sin(self.index)
        self.screen.blit(self.name,(name_pos_x,name_pos_y))
        #副背景图片
        self.looding=pygame.transform.scale(self.looding,(510,510))
        self.screen.blit(self.looding,(0,330))
        #self.screen.blit(self.lei_ting,(0,0))

        #开始游戏按钮
        button_rect=self.screen.blit(self.kaishi,(200,563))
        BeginWindow.is_inside=button_rect.collidepoint(pygame.mouse.get_pos())

        #动图
        self.add_index+=1
        if self.add_index%10==0:
            self.img_index+=1
            if self.img_index==7:
                self.img_index=0
        self.screen.blit(self.roll[self.img_index],((510-self.roll[self.img_index].get_width())/2,630))

pygame.mixer.init()
pygame.mixer.music.load("image\qjzx.mp3")


class Bgm:
    #音乐
    #循环播放
    @staticmethod
    def circulate_play():
        pygame.mixer.music.play(-1)

    #暂停播放
    @staticmethod
    def pause():
        if music_is_play==False or is_pause:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

#音效
sound_list=[pygame.mixer.Sound(r"image\button.ogg"),
pygame.mixer.Sound(r"image\bullet.wav"),
pygame.mixer.Sound(r"image\baozha.wav")
           ]


class Sound:
    #音乐播放
    @staticmethod
    def play(sound):
        sound.play()


#物品类
article_imgs=[pygame.image.load(r"image\article1.png"),
             pygame.image.load(r"image\article2.png")]
article_list=[]

class Article(pygame.sprite.Sprite):
    #随机物品类
    def __init__(self,image,screen,pos,speed,sign):
        self.sign=sign
        self.image=image
        self.image = article_imgs[self.sign]
        self.rect=self.image.get_rect()
        self.screen=screen
        self.rect.topleft=pos
        self.speed=speed

        article_list.append(self)


    def move(self):
        self.rect=self.rect.move(0,self.speed)

        #越界自动销毁
        if self.rect.y>=800:
            article_list.remove(self)
        self.screen.blit(self.image,self.rect)


class ArticleManager:
    #随机物品管理类
    @staticmethod
    def creat_article():
        ran_num_2=r.randint(1,100)
    #升级子弹
        if ran_num_2<=50:
            ran_width=r.randint(0 , screen.get_width() - article_imgs[0].get_width())
            Article(article_imgs[0],screen,(ran_width,-article_imgs[0].get_width()),5,0)
    #全屏秒杀
        else:
            ran_width = r.randint(0,screen.get_width() - article_imgs[1].get_width())
            Article(article_imgs[0],screen,(ran_width,-article_imgs[1].get_height()),5,1)
    @staticmethod
    def article_move():
        for i in article_list:
            if isinstance(i,Article):
                i.move()


#敌机类

  #小敌机
enemy0_imgs=[pygame.image.load("image\\enemy1.png"),
pygame.image.load("image\\enemy1_down1.png"),
pygame.image.load("image\\enemy1_down2.png"),
pygame.image.load("image\\enemy1_down3.png"),
pygame.image.load("image\\enemy1_down4.png"),
pygame.image.load("image\\enemy1_down5.png"),
pygame.image.load("image\\enemy1_down6.png"),
pygame.image.load("image\\enemy1_down7.png"),
pygame.image.load("image\\enemy1_down8.png")
            ]
  #中敌机
enemy1_imgs=[pygame.image.load("image\\enemy2.png"),
pygame.image.load("image\\enemy2_down1.png"),
pygame.image.load("image\\enemy2_down2.png"),
pygame.image.load("image\\enemy2_down3.png"),
pygame.image.load("image\\enemy1_down4.png"),
pygame.image.load("image\\enemy2_down5.png"),
pygame.image.load("image\\enemy2_down6.png")
            ]
  #大敌机
enemy2_imgs=[pygame.image.load("image\\enemy3.png"),
pygame.image.load("image\\enemy3_down1.png"),
pygame.image.load("image\\enemy3_down2.png"),
pygame.image.load("image\\enemy3_down3.png"),
pygame.image.load("image\\enemy3_down4.png"),
pygame.image.load("image\\enemy3_down5.png"),
pygame.image.load("image\\enemy3_down6.png"),
pygame.image.load("image\\enemy3_down7.png"),
pygame.image.load("image\\enemy3_down8.png")

            ]
#boss
baozha_imgs=[
pygame.image.load("image\\enemy3_down1.png"),
pygame.image.load("image\\enemy3_down2.png"),
pygame.image.load("image\\enemy3_down3.png"),
pygame.image.load("image\\enemy3_down4.png"),
pygame.image.load("image\\enemy3_down5.png"),
pygame.image.load("image\\enemy3_down6.png"),
pygame.image.load("image\\enemy3_down7.png"),
pygame.image.load("image\\enemy3_down8.png"),
pygame.image.load("image\\boss.png"),
            ]
boss=pygame.transform.scale(baozha_imgs[8], (200, 100))
baozha_img0 = pygame.transform.scale(baozha_imgs[0], (200, 100))
baozha_img1 = pygame.transform.scale(baozha_imgs[1], (200, 100))
baozha_img2 = pygame.transform.scale(baozha_imgs[2], (200, 100))
baozha_img3 = pygame.transform.scale(baozha_imgs[3], (200, 100))
baozha_img4 = pygame.transform.scale(baozha_imgs[4], (200, 100))
baozha_img5 = pygame.transform.scale(baozha_imgs[5], (200, 100))
baozha_img6 = pygame.transform.scale(baozha_imgs[6], (200, 100))
baozha_img7 = pygame.transform.scale(baozha_imgs[7], (200, 100))
enemy3_imgs=[
            boss,
            baozha_img0,
            baozha_img1,
            baozha_img2,
            baozha_img3,
            baozha_img4,
            baozha_img5,
            baozha_img6,
            baozha_img7
]
enemy4_imgs=[
            pygame.image.load("image\\boss1.png"),
            baozha_img0,
            baozha_img1,
            baozha_img2,
            baozha_img3,
            baozha_img4,
            baozha_img5,
            baozha_img6,
            baozha_img7
]

enemy_list=[]
enemy_boss_list=[]
enemy_boss_list1=[]

class Enemy(pygame.sprite.Sprite):
    #敌机类
    def __init__(self,images,screen,pos,hp,speed,speed_x,sign):
        self.images=images
        self.image=images[0]
        self.rect=self.image.get_rect()
        self.screen=screen
        self.rect.topleft=pos
        self.hp=hp
        self.speed=speed
        self.speed_x=speed_x
        self.sign=sign
        self.index=0
        self.img_index=0

        #添加到敌机列表中
        if self.sign==4:
            enemy_boss_list.append(self)
        elif self.sign==5:
            enemy_boss_list1.append(self)
        else:
            enemy_list.append(self)
        if len(enemy_boss_list)>1:
            enemy_boss_list.pop(1)
        if len(enemy_boss_list1)>1:
            enemy_boss_list1.pop(1)



    def move(self):
        self.rect = self.rect.move(self.speed_x, self.speed)
        if self.rect.x >= self.screen.get_width() - self.image.get_width():
            self.speed_x = -self.speed_x
        if self.rect.x <= 0:
            self.speed_x = -self.speed_x

        #越界自动销毁
        if self.rect.y>=750:
            enemy_list.remove(self)

        #判断敌机死亡
        if self.hp<=0:
            self.dead()

        else:
            self.screen.blit(self.image,self.rect)

    def move1(self):
        self.rect = self.rect.move(self.speed, 0)
        if self.rect.x >= self.screen.get_width() - self.image.get_width():
            self.speed = -self.speed
        if self.rect.x <= 0:
            self.speed = -self.speed

        # 判断敌机死亡
        if self.hp <= 0:
            self.dead()
            enemy_bullet_list.clear()

        else:
            self.screen.blit(self.image, self.rect)

        if is_pause == False:
            self.index += 1
            if self.index % 150 == 0:
                if is_auto_shoot_c:
                    EnemyBullet(enemy_bullet_img[1],
                                ((self.rect.centerx - bullet_img[0].get_width() / 2), self.rect.top),
                                screen, 2,1,0)
                    EnemyBullet(enemy_bullet_img[1],
                                ((self.rect.centerx - bullet_img[0].get_width() / 2), self.rect.top),
                                screen, 2, -1, 0)

            # 敌方飞机边移动边发射子弹
            for i in enemy_bullet_list:
                if isinstance(i, EnemyBullet) and i in enemy_bullet_list:
                    i.move()


        else:
            for i in enemy_bullet_list:
                i.display()
    def move2(self):
        self.rect = self.rect.move(self.speed, 0)
        if self.rect.x >= self.screen.get_width() - self.image.get_width():
            self.speed = -self.speed
        if self.rect.x <= 0:
            self.speed = -self.speed

        # 判断敌机死亡
        if self.hp <= 0:
            self.dead()
            enemy_bullet_list1.clear()

        else:
            self.screen.blit(self.image, self.rect)

        if is_pause == False:
            self.index += 1
            if self.index % 200 == 0:
                if is_auto_shoot_c:
                    EnemyBullet(enemy_bullet_img[0],
                                ((self.rect.centerx - bullet_img[0].get_width() / 2), self.rect.top),
                                screen, 0,1,1)
                    EnemyBullet(enemy_bullet_img[0],
                                ((self.rect.centerx - bullet_img[0].get_width() / 2), self.rect.top),
                                screen, 1,0,1)
                    EnemyBullet(enemy_bullet_img[0],
                                ((self.rect.centerx - bullet_img[0].get_width() / 2), self.rect.top),
                                screen, 0,-1,1)
                    EnemyBullet(enemy_bullet_img[0],
                                ((self.rect.centerx - bullet_img[0].get_width() / 2), self.rect.top),
                                screen, -1,0,1)
                    EnemyBullet(enemy_bullet_img[0],
                                ((self.rect.centerx - bullet_img[0].get_width() / 2), self.rect.top),
                                screen, 3,2,0)
                    EnemyBullet(enemy_bullet_img[0],
                                ((self.rect.centerx - bullet_img[0].get_width() / 2), self.rect.top),
                                screen, 3, -2,0)
                    EnemyBullet(enemy_bullet_img[0],
                                ((self.rect.centerx - bullet_img[0].get_width() / 2), self.rect.top),
                                screen, -1, 1,1)
                    EnemyBullet(enemy_bullet_img[0],
                                ((self.rect.centerx - bullet_img[0].get_width() / 2), self.rect.top),
                                screen, -1, -1,1)



            # 敌方飞机边移动边发射子弹
            for i in enemy_bullet_list1:
                if isinstance(i, EnemyBullet) and i in enemy_bullet_list1:
                    i.move1()
            for i in enemy_bullet_list:
                if isinstance(i, EnemyBullet) and i in enemy_bullet_list:
                    i.move()

        else:
            for i in enemy_bullet_list1:
                i.display()
            for i in enemy_bullet_list:
                i.display()





    def dead(self):
        #敌机死亡分为碰撞死亡和越界死亡
        #读取死亡动画和敌机死亡后加分
        self.index+=1
        if self.index%10:
            if self.sign==1:
                self.img_index+=1
                if self.img_index==8:
                    if self in enemy_list:
                        Hero.score+=1
                        enemy_list.remove(self)
            elif self.sign==2:
                self.img_index+=1
                if self.img_index==6:
                    self.img_index=0
                    if self in enemy_list:
                        Hero.score +=2
                        enemy_list.remove(self)
            elif self.sign == 3:
                self.img_index+=1
                if self.img_index==8:
                    self.img_index=0
                    if self in enemy_list:
                        Hero.score +=5
                        enemy_list.remove(self)
            elif self.sign == 4:
                self.img_index+=1
                if self.img_index==8:
                    self.img_index=0
                    if self in enemy_boss_list:
                        Hero.score +=40
                        enemy_boss_list.remove(self)
            else:
                self.img_index += 1
                if self.img_index == 8:
                    self.img_index = 0
                    if self in enemy_boss_list:
                        Hero.score += 500
                        enemy_boss_list.remove(self)

        self.screen.blit(self.images[self.img_index],self.rect)




#敌机，管理类
class EnemyMamger:

    @staticmethod
    def create_enemy():
        ran_num_1=r.randint(1,1000)
        #设定不同种类敌机的生产几率
        if ran_num_1<=650:
            ran_width=r.randint(0,screen.get_width()-enemy0_imgs[0].get_width())
            Enemy(enemy0_imgs,screen,(ran_width,-enemy0_imgs[0].get_height()),1,4,-3,1)
        elif ran_num_1<=850:
            ran_width=r.randint(0,screen.get_width()-enemy1_imgs[0].get_width())
            Enemy(enemy1_imgs,screen,(ran_width,-enemy1_imgs[0].get_height()),3,3,2,2)
        else:
            ran_width=r.randint(0,screen.get_width()-enemy2_imgs[0].get_width())
            Enemy(enemy2_imgs,screen,(ran_width,-enemy2_imgs[0].get_height()),6,2,1,3)


    @staticmethod
    def create_enemy1():
        ran_num_1 = r.randint(1, 1000)
        # 设定不同种类敌机的生产几率
        if ran_num_1 <= 600:
            ran_width = r.randint(0, screen.get_width() - enemy0_imgs[0].get_width())
            Enemy(enemy0_imgs, screen, (ran_width, -enemy0_imgs[0].get_height()), 2, 4, -3, 1)
        elif ran_num_1 <= 800:
            ran_width = r.randint(0, screen.get_width() - enemy1_imgs[0].get_width())
            Enemy(enemy1_imgs, screen, (ran_width, -enemy1_imgs[0].get_height()), 5, 3, 2, 2)
        elif ran_num_1 <= 900:
            ran_width = r.randint(0, screen.get_width() - enemy2_imgs[0].get_width())
            Enemy(enemy2_imgs, screen, (ran_width, -enemy2_imgs[0].get_height()), 8, 2, 1, 3)
        else:

            x = r.uniform(0, screen.get_width() - enemy3_imgs[0].get_width())
            y = r.uniform(0, 100)
            Enemy(enemy3_imgs, screen, (x, y), 150, 2, 0, 4)

    @staticmethod
    def create_enemy2():
        x = r.uniform(0, screen.get_width() - enemy4_imgs[0].get_width())
        y = r.uniform(0, 100)
        Enemy(enemy4_imgs, screen, (x, y), 1000, 2, 0, 5)
    @staticmethod
    def enemy_move():
        for i in enemy_list:
            if isinstance(i,Enemy):
                i.move()

    @staticmethod
    def enemy_boss_move():
        for i in enemy_boss_list:
            if isinstance(i, Enemy):
                i.move1()
    @staticmethod
    def enemy_boss_move1():
        for i in enemy_boss_list1:
            if isinstance(i, Enemy):
                i.move2()

#英雄子弹类
bullet_img=[pygame.image.load("image\\bullet.png"),
            pygame.image.load("image\\bullet_2.png"),
            pygame.image.load(r"image\baozhadonghua.png"),
            pygame.image.load("image\\daodan1.png"),
            pygame.image.load("image\\b.png"),


            ]
bullet_list=[]
bullet_l_list=[]
bullet_r_list=[]
class Bullet(pygame.sprite.Sprite):
    def __init__(self,image,pos,screen,speed,sign,attack_num=1,):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x,self.rect.y=pos
        self.screen=screen
        self.speed=speed
        self.attack_num=attack_num
        self.sign=sign
        #对象产生加入列表
        if self.sign==1 or self.sign==4:
            bullet_list.append(self)
        if self.sign == 2:
            bullet_l_list.append(self)
        if self.sign == 3:
            bullet_r_list.append(self)


        Sound.play(sound_list[1])


    #子弹移动
    def move(self):
        self.rect=self.rect.move(0,-self.speed)
        self.screen.blit(self.image,self.rect)
        if self.rect.y<-70:
            bullet_list.remove(self)
        self.collide_enemy()
        self.collide_boss_enemy()
        self.collide_boss_enemy1()
    #左移
    def move_l(self):
        self.rect=self.rect.move(-5,-self.speed)
        self.screen.blit(self.image,self.rect)
        if self.rect.y<-70:
            bullet_l_list.remove(self)
        self.collide_enemy()
        self.collide_boss_enemy()
        self.collide_boss_enemy1()
    #右移
    def move_r(self):
        self.rect=self.rect.move(5,-self.speed)
        self.screen.blit(self.image,self.rect)
        if self.rect.y<-70:
            bullet_r_list.remove(self)
        self.collide_enemy()
        self.collide_boss_enemy()
        self.collide_boss_enemy1()


    def display(self):
        self.screen.blit(self.image,self.rect)

    #子弹碰撞
    def collide_enemy(self,enemy=enemy_list):
        obj = pygame.sprite.spritecollideany(self,enemy,collided=pygame.sprite.collide_mask)
        if isinstance(obj,Enemy):
            obj.hp-=1
            if isinstance(self,Bullet)and self in bullet_list:
                bullet_list.remove(self)
            if isinstance(self,Bullet)and self in bullet_l_list:
                bullet_l_list.remove(self)
            if isinstance(self, Bullet) and self in bullet_r_list:
                bullet_r_list.remove(self)
    def collide_boss_enemy(self,enemy=enemy_boss_list):
        obj = pygame.sprite.spritecollideany(self,enemy,collided=pygame.sprite.collide_mask)
        if isinstance(obj,Enemy):
            obj.hp-=1
            if isinstance(self,Bullet)and self in bullet_list:
                bullet_list.remove(self)
            if isinstance(self,Bullet)and self in bullet_l_list:
                bullet_l_list.remove(self)
            if isinstance(self, Bullet) and self in bullet_r_list:
                bullet_r_list.remove(self)
    def collide_boss_enemy1(self,enemy=enemy_boss_list1):
        obj = pygame.sprite.spritecollideany(self,enemy,collided=pygame.sprite.collide_mask)
        if isinstance(obj,Enemy):
            obj.hp-=1
            if isinstance(self,Bullet)and self in bullet_list:
                bullet_list.remove(self)
            if isinstance(self,Bullet)and self in bullet_l_list:
                bullet_l_list.remove(self)
            if isinstance(self, Bullet) and self in bullet_r_list:
                bullet_r_list.remove(self)


s=[pygame.image.load("image\\bullet1.png"),

   ]
enemy_bullet=pygame.transform.scale(s[0], (50, 48))
enemy_bullet_img=[enemy_bullet,
                  pygame.image.load("image\\daodan3.png")]

enemy_bullet_list=[]
enemy_bullet_list1=[]

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self,image,pos,screen,speed,speed_x,sign,attack_num=1):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x,self.rect.y=pos
        self.screen=screen
        self.speed=speed
        self.speed_x=speed_x
        self.sign=sign
        self.attack_num=attack_num
        #对象产生加入列表
        if self.sign==0:
            enemy_bullet_list.append(self)
        else:
            enemy_bullet_list1.append(self)
        self.index=0




    def move(self):
        self.rect = self.rect.move(self.speed_x, self.speed)
        if self.rect.x >= self.screen.get_width() - self.image.get_width():
            self.speed_x = -self.speed_x
        if self.rect.x <= 0:
            self.speed_x = -self.speed_x


        self.screen.blit(self.image,self.rect)
        if self.rect.y>780:
            enemy_bullet_list.remove(self)
    def move1(self):
        self.rect = self.rect.move(self.speed_x, self.speed)
        self.screen.blit(self.image,self.rect)
        if self.rect.y>780 or self.rect.x>520 or self.rect.y<0 or self.rect.x<0 :
            enemy_bullet_list1.remove(self)



    def display(self):
        self.screen.blit(self.image,self.rect)




#角色
hero_list_a=[pygame.image.load("image\Role1.png"),
pygame.image.load("image\Role1.1.png"),
pygame.image.load(r"image\roleDeath1.png"),
pygame.image.load(r"image\roleDeath2.png"),
pygame.image.load(r"image\roleDeath3.png"),
pygame.image.load(r"image\roleDeath4.png"),
pygame.image.load(r"image\roleDeath5.png"),
pygame.image.load(r"image\roleDeath6.png"),
pygame.image.load(r"image\roleDeath6.png"),
pygame.image.load("image\hudun.png"),
pygame.image.load(r"image\baozhadonghua.png"),

]
s1=[pygame.image.load("image\\hero_1.png")]
hero_1=pygame.transform.scale(s1[0], (150, 90))
hero_list_b=[hero_1,
hero_1,
pygame.image.load(r"image\roleDeath1.png"),
pygame.image.load(r"image\roleDeath2.png"),
pygame.image.load(r"image\roleDeath3.png"),
pygame.image.load(r"image\roleDeath4.png"),
pygame.image.load(r"image\roleDeath5.png"),
pygame.image.load(r"image\roleDeath6.png"),
pygame.image.load(r"image\roleDeath6.png"),
pygame.image.load("image\hudun.png"),
pygame.image.load(r"image\baozhadonghua.png"),

]
hero_list_d=[pygame.image.load("image\hero_2.png"),
pygame.image.load("image\hero_2.png"),
pygame.image.load(r"image\roleDeath1.png"),
pygame.image.load(r"image\roleDeath2.png"),
pygame.image.load(r"image\roleDeath3.png"),
pygame.image.load(r"image\roleDeath4.png"),
pygame.image.load(r"image\roleDeath5.png"),
pygame.image.load(r"image\roleDeath6.png"),
pygame.image.load(r"image\roleDeath6.png"),
pygame.image.load("image\hudun.png"),
pygame.image.load(r"image\baozhadonghua.png"),

]
hero_list=[]

class Hero(pygame.sprite.Sprite):
    #英雄
    up =False
    down =False
    left= False
    right =False

    #屏幕，游戏背景图，角色初始坐标，血量，速度，分数
    score =0
    def __init__(self,screen,hero_list,pos,hp,speed):
        self.screen=screen
        self.imgs=hero_list
        self.image=self.imgs[0]
        self.rect=self.imgs[0].get_rect()
        self.rect.x,self.rect.y=pos
        self.hp=hp
        self.speed=speed
        self.mask=pygame.mask.from_surface(self.image)
        hero_list.append(self)

        #图片运动索引
        self.index=0
        #图片切换索引
        self.img_index=0
        #无敌时间索引
        self.hp_index=0
        #死亡动画切换索引
        self.death_index=2
        #全屏爆炸个数
        self.clear_index=1
        #清屏特效索引
        self.boom_index=0
        self.boom1_index=9


        self.state=True#True活着False死亡

    def move(self):
        if Hero.up:
            self.rect=self.rect.move(0,-self.speed)
        if Hero.down:
            self.rect=self.rect.move(0,self.speed)

        if Hero.left:
            self.rect=self.rect.move(-self.speed,0)
        if Hero.right:
            self.rect=self.rect.move(self.speed,0)
        #约束位置
        if self.rect.x<0:
            self.rect.x=0
        if self.rect.x>self.screen.get_width()-self.image.get_width():
            self.rect.x = self.screen.get_width() - self.image.get_width()
        if self.rect.y<0:
            self.rect.y=0
        if self.rect.y>self.screen.get_height()-self.image.get_height():
            self.rect.y = self.screen.get_height() - self.image.get_height()

        #图片渲染
        if is_pause == False:
            # global is_auto_shoot_b
            # global is_auto_shoot_a
            self.index+=1
            if self.index%10==0:
                if is_auto_shoot_a :
                    Bullet(bullet_img[0],((hero_a.rect.centerx - bullet_img[0].get_width()/2),hero_a.rect.top),screen,30,1)
                    if is_up_bullet:
                        #三排子弹
                        add_bullet_1=int(hero_a.image.get_width()/4+hero_a.rect.x-bullet_img[0].get_width()/2)
                        add_bullet_2=int(hero_a.image.get_width()/4*3+hero_a.rect.x-bullet_img[0].get_width()/2)
                        Bullet(bullet_img[0],(add_bullet_1,hero_a.rect.top),screen,35,1)
                        Bullet(bullet_img[0],(add_bullet_2,hero_a.rect.top),screen,35,1)

                if is_auto_shoot_b :
                    Bullet(bullet_img[1],
                           ((hero_b.rect.centerx - bullet_img[1].get_width() / 2), hero_b.rect.top), screen, 30,
                           1)
                    if is_up_bullet:
                        # 三排子弹
                        add_bullet_1 = int(
                            hero_b.image.get_width() / 4 + hero_b.rect.x - bullet_img[1].get_width() / 2)
                        add_bullet_2 = int(
                            hero_b.image.get_width() / 4 * 3 + hero_b.rect.x - bullet_img[1].get_width() / 2)
                        Bullet(bullet_img[1], (add_bullet_1, hero_b.rect.top), screen, 35, 2)
                        Bullet(bullet_img[1], (add_bullet_2, hero_b.rect.top), screen, 35, 3)
                if is_auto_shoot_d :
                    Bullet(bullet_img[3],
                           ((hero_d.rect.centerx - bullet_img[3].get_width() / 2), hero_d.rect.top), screen, 30,
                           1)
                    if is_up_bullet:
                        # 三排子弹

                        add_bullet_1 = int(
                            hero_d.image.get_width() / 4 + hero_d.rect.x - bullet_img[3].get_width() / 2)
                        add_bullet_2 = int(
                            hero_d.image.get_width() / 4 * 3 + hero_d.rect.x - bullet_img[3].get_width() / 2)
                        Bullet(bullet_img[3], (add_bullet_1, hero_d.rect.top), screen, 35, 2)
                        Bullet(bullet_img[3], (add_bullet_2, hero_d.rect.top), screen, 35, 3)


                self.img_index+=1
                if self.img_index==2:
                    self.img_index=0
            #英雄飞机边移动边发射子弹
            for i in bullet_list:
                if isinstance(i,Bullet) and i in bullet_list:
                    i.move()
            for i in bullet_l_list:
                if isinstance(i,Bullet) and i in bullet_l_list:
                    i.move_l()
            for i in bullet_r_list:
                if isinstance(i,Bullet) and i in bullet_r_list:
                    i.move_r()

        else:
            for i in bullet_list:
                i.display()
            for i in bullet_l_list:
                i.display()
            for i in bullet_r_list:
                i.display()

        self.screen.blit(self.imgs[self.img_index],self.rect)

        #角色移动碰撞检测
        self.collide_enemy()

        #角色死亡
        if self.hp<=0:
            global is_play


            is_play=0

            high.write_high_score(self.score)

        if self.state==False:
            self.dead()






    def dead(self):
        self.index +=1
        if self.index%3==0:
            self.death_index +=1
            if self.death_index==8:
                self.death_index=0
                self.state=True

                self.rect.topleft = (200,600)
        self.screen.blit(self.imgs[self.death_index],self.rect)

    #角色碰撞
    def collide_enemy(self,enemys=enemy_list,articles=article_list,bullet=enemy_bullet_list,bullet1=enemy_bullet_list1):
        global is_hit
        global is_up_bullet
        global is_clear

        if is_hit:
            #无敌光盾生成
            hu_dun_x=self.rect.x - (self.imgs[9].get_width() - self.image.get_width())/2
            hu_dun_y=self.rect.y - (self.imgs[9].get_height() - self.image.get_height())/2

            temp = self.screen.blit(self.imgs[9],(hu_dun_x,hu_dun_y))
            en_index = temp.collidelist(enemys)
            if en_index != -1:
                enemys[en_index].hp = 0
            self.hp_index+=1
            if self.hp_index%100==0:
                is_hit = False
        #碰撞敌机
        else:
            obj_1=pygame.sprite.spritecollideany(self,enemys,collided=pygame.sprite.collide_mask)
            if obj_1 in enemy_list:
                obj_1.hp =0
                self.hp -=1
                self.state=False
                is_up_bullet=False
                is_hit =True

        #碰撞buffer
        obj_2 = pygame.sprite.spritecollideany(self,articles,collided=pygame.sprite.collide_mask)
        if obj_2 in articles:
            if obj_2.sign == 0:
                is_up_bullet = True
            if obj_2.sign == 1:
                self.clear_index+=1
                if self.clear_index ==3:
                    self.clear_index=3
            article_list.remove(obj_2)
        #碰撞子弹
        obj_3 = pygame.sprite.spritecollideany(self, bullet, collided=pygame.sprite.collide_mask)
        if isinstance(obj_3,EnemyBullet)and obj_3 in enemy_bullet_list:
            self.hp -= 1
            self.state = False
            is_hit = True
            is_up_bullet = False
            enemy_bullet_list.remove(obj_3)

        obj_4 = pygame.sprite.spritecollideany(self, bullet1, collided=pygame.sprite.collide_mask)
        if isinstance(obj_4, EnemyBullet) and obj_4 in enemy_bullet_list1:
            self.hp -= 1
            self.state = False
            is_hit = True
            is_up_bullet = False
            enemy_bullet_list1.remove(obj_4)

     #清屏
    def clear(self):
        if self.clear_index>0:
            self.clear_index-=1

            enemy_bullet_list.clear()

            for i in enemy_list :
                i.hp=0
            for i in  enemy_boss_list:
                i.hp-=100
            for i in  enemy_boss_list1:
                i.hp-=200



class AtkImg:
    #战斗界面类
    is_inside=False
    def __init__(self,war_bg,screen,speed,pos=(0,0)):
        self.screen=screen
        self.war_bg_1=war_bg
        self.war_bg_1_rect=self.war_bg_1.get_rect()
        self.war_bg_1_rect.x,self.war_bg_1_rect.y=pos
        self.war_bg_2=self.war_bg_1.copy()
        self.war_bg_2_rect=self.war_bg_2.get_rect()
        self.war_bg_2_rect.x,self.war_bg_2_rect.y=(0,-self.war_bg_2_rect.h)
        self.speed = speed

        #动画播放帧数
        self.index=0
    #背景
    def display(self):
        self.war_bg_1_rect=self.war_bg_1_rect.move(0,self.speed)
        self.war_bg_2_rect=self.war_bg_2_rect.move(0,self.speed)

        if self.war_bg_1_rect.y>=750:
            self.war_bg_1_rect.y=self.war_bg_2_rect.y-780

        if self.war_bg_2_rect.y >= 750:
            self.war_bg_2_rect.y = self.war_bg_1_rect.y - 780

        #背景渲染
        self.screen.blit(self.war_bg_1,self.war_bg_1_rect)
        self.screen.blit(self.war_bg_2,self.war_bg_2_rect)


        #暂停和播放按钮渲染
        if is_pause == False:
            AtkImg.is_inside = self.screen.blit(pause_play_button[0],(440,30)).collidepoint(pygame.mouse.get_pos())
        else:
            AtkImg.is_inside = self.screen.blit(pause_play_button[1],(440,30)).collidepoint(pygame.mouse.get_pos())

        #全屏爆炸图片显示
        self.screen.blit(article_imgs[1],(10,670))


#########################


#初始化
pygame.init()
#初始化显示
pygame.display.init()
#设置窗口
screen = pygame.display.set_mode((510,750))
#游戏是否开始
is_play=0
#游戏是否暂停
is_pause= False
#音乐播放
Bgm.circulate_play()
music_is_play = True
#是否自动射击
is_auto_shoot_a=True
is_auto_shoot_b=False
is_auto_shoot_c=True
is_auto_shoot_d=False


#复活是否无敌
is_hit=False
#子弹升级道具
is_up_bullet=False
#全屏爆炸道具

#产生敌机计时器
pygame.time.set_timer(pygame.USEREVENT,600)
#产生BUFFER
pygame.time.set_timer(pygame.USEREVENT+1,10000)
pygame.time.set_timer(pygame.USEREVENT+2,600)
#时间声明
clock=pygame.time.Clock()

#字体对象
font1=pygame.font.Font("image\Cobac.ttf",40)
font2=pygame.font.Font("image\Cobac.ttf",30)
#启动窗口
begin_window = BeginWindow(begin_image,screen)
#zhong_window = ZhongWindow(begin_image,screen)
#建立角色
hero_a=Hero(screen,hero_list_a,(200,600),8,8)
hero_b=Hero(screen,hero_list_b,(200,600),8,8)
hero_d=Hero(screen,hero_list_d,(200,600),8,8)
#战斗背景
warBgs=[
        pygame.image.load("image\warBg1.jpg"),
        pygame.image.load("image\warBg4.jpg"),
        pygame.image.load("image\warBg3.jpg")
]
warBg1 = pygame.transform.scale(warBgs[0], (520, 780))
warBg2 = pygame.transform.scale(warBgs[1], (520, 780))
# warBg3 = pygame.transform.scale(warBgs[2], (520, 780))

game_img=AtkImg(begin_image[12],screen,1)
game_img1=AtkImg(warBg1,screen,1)
game_img2=AtkImg(warBg2,screen,1)
# game_img2=AtkImg(warBg2,screen,1)
# game_img3=AtkImg(warBg3,screen,1)
# #历史最高分
high = HighScore()


def Event():
    #事件监测
    global is_auto_shoot_b
    global is_auto_shoot_a
    global is_auto_shoot_d
    global is_play
    global is_pause
    global music_is_play
    global is_up_bullet
    global is_hit
    global index
    global zhong_window

    for i in pygame.event.get():
        #窗口退出
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #控制敌机产生事件
        if i.type == pygame.USEREVENT and is_pause == False and is_play ==1:
            EnemyMamger.create_enemy()
        if i.type == pygame.USEREVENT and is_pause == False and is_play ==2:
            EnemyMamger.create_enemy1()
        if i.type == pygame.USEREVENT and is_pause == False and is_play ==3:
            EnemyMamger.create_enemy2()
        #物品产生
        if i.type == pygame.USEREVENT+1 and is_pause == False:
            ArticleManager.creat_article()
        #鼠标
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1 and BeginWindow.is_inside and is_play == 0:
                Sound.play(sound_list[0])
                hero_a.hp =8
                is_auto_shoot_b = False
                is_auto_shoot_a= True
                is_auto_shoot_d= False
                is_hit=False
                enemy_bullet_list1.clear()
                hero_a.clear_index=1
                enemy_list.clear()
                bullet_list.clear()
                bullet_l_list.clear()
                bullet_r_list.clear()
                enemy_boss_list.clear()
                enemy_boss_list1.clear()

                article_list.clear()
                Hero.score=0
                is_up_bullet =False
                high.read_high_score()

                is_play = 1
                hero_a.rect.topleft= (200,600)
            if i.button == 1 and AtkImg.is_inside and is_play == 1:
                is_pause = not is_pause
                if is_pause:
                    hero_a.speed = 0

                    game_img.speed = 0

                    Bgm.pause()
                    Sound.play(sound_list[0])
                    for j in enemy_list:
                        j.speed_x = 0
                        j.speed = 0
                    for j in enemy_boss_list:
                        j.speed = 0
                    for j in article_list:
                        j.speed = 0
                else:
                    hero_a.speed = 8

                    game_img.speed = 1

                    Bgm.pause()
                    Sound.play(sound_list[0])
                    for j in enemy_list:
                        if j.sign == 1:
                            j.speed_x = 3
                            j.speed = 4
                        elif j.sign == 2:
                            j.speed_x = 2
                            j.speed = 3
                        else:
                            j.speed_x = 1
                            j.speed = 2
                    for j in enemy_boss_list:
                        j.speed = 2
                    for j in article_list:
                        j.speed = 5
            if i.button == 1 and AtkImg.is_inside and is_play == 2:
                is_pause = not is_pause
                if is_pause:

                    hero_b.speed = 0

                    game_img1.speed = 0

                    Bgm.pause()
                    Sound.play(sound_list[0])
                    for j in enemy_list:
                        j.speed_x = 0
                        j.speed = 0
                    for j in enemy_boss_list:
                        j.speed = 0
                    for j in article_list:
                        j.speed = 0
                else:

                    hero_b.speed = 8

                    game_img1.speed = 1
                    Bgm.pause()
                    Sound.play(sound_list[0])
                    for j in enemy_list:
                        if j.sign == 1:
                            j.speed_x = 3
                            j.speed = 4
                        elif j.sign == 2:
                            j.speed_x = 2
                            j.speed = 3
                        else:
                            j.speed_x = 1
                            j.speed = 2
                    for j in enemy_boss_list:
                        j.speed = 2
                    for j in article_list:
                        j.speed = 5
            if i.button == 1 and AtkImg.is_inside and is_play == 3:
                is_pause = not is_pause
                if is_pause:

                    hero_d.speed = 0

                    game_img2.speed = 0

                    Bgm.pause()
                    Sound.play(sound_list[0])
                    for j in enemy_list:
                        j.speed_x = 0
                        j.speed = 0
                    for j in enemy_boss_list1:
                        j.speed = 0
                    for j in article_list:
                        j.speed = 0
                else:

                    hero_d.speed = 8

                    game_img2.speed = 1
                    Bgm.pause()
                    Sound.play(sound_list[0])
                    for j in enemy_list:
                        if j.sign == 1:
                            j.speed_x = 3
                            j.speed = 4
                        elif j.sign == 2:
                            j.speed_x = 2
                            j.speed = 3
                        else:
                            j.speed_x = 1
                            j.speed = 2
                    for j in enemy_boss_list1:
                        j.speed = 2
                    for j in article_list:
                        j.speed = 5
            if i.button == 3 and is_play ==1:
                is_auto_shoot_a = not is_auto_shoot_a
            if i.button == 3 and is_play == 2:
                is_auto_shoot_b = not is_auto_shoot_b
            if i.button == 3 and is_play == 3:
                is_auto_shoot_d = not is_auto_shoot_d
            # if Hero.score >= 50 and is_play == 1 and i.button == 3:
            #     # 初始化
            #     pygame.init()
            #     # 初始化显示
            #     pygame.display.init()
            #     zhong_window = ZhongWindow(begin_image, screen)
            #     pygame.display.update()
            #     # index+=1
            #     # if pygame.time.delay(10000):
            #     #     print(index)
            #     #     break
            #
            #     if i.button == 1 and ZhongWindow.is_inside and is_play == 1:
            #          is_play = 2


        #键盘

        if i.type == pygame.KEYDOWN:

            if i.key == pygame.K_ESCAPE:
                high.write_high_score(Hero.score)
                Hero.score = 0
                is_up_bullet =False
                is_play =0
            if i.key == pygame.K_F1:
                music_is_play= not music_is_play
            if i.key == pygame.K_UP or i.key== pygame.K_w:
                Hero.up=True
            if i.key == pygame.K_DOWN or i.key== pygame.K_s:
                Hero.down=True
            if i.key == pygame.K_LEFT or i.key== pygame.K_a:
                Hero.left=True
            if i.key == pygame.K_RIGHT or i.key== pygame.K_d:
                Hero.right=True
            if i.key == pygame.K_o and hero_a.clear_index>0 and is_pause==False :
                Sound.play(sound_list[2])
                hero_a.clear()

                Bullet(bullet_img[2],(0,0),screen,40,4)
            if i.key == pygame.K_o and hero_b.clear_index>0 and is_pause==False :
                Sound.play(sound_list[2])

                hero_b.clear()
                Bullet(bullet_img[2],(0,0),screen,40,4)
            if i.key == pygame.K_o and hero_d.clear_index>0 and is_pause==False :
                Sound.play(sound_list[2])

                hero_d.clear()
                Bullet(bullet_img[2],(0,0),screen,40,4)


            # if Hero.score >= 50 and is_play == 1:
            #     zhong_window = ZhongWindow(begin_image, screen)
            #     pygame.display.update()
            #         # index+=1
            #         # if pygame.time.delay(10000):
            #         #     print(index)
            #         #     break
            #
            #
            #     if i.button == 1 and ZhongWindow.is_inside and is_play == 1:
            #         is_play =2

            if i.key == pygame.K_e:
                global index
                index=0
                index +=1
                for x in s:
                    if index%50==0:
                        screen.blit(x,(0,0))
                        pygame.display.update()
                if Hero.score >= 50:
                    is_play =2
            if is_play == 2 and is_auto_shoot_a :
                is_auto_shoot_b = True
                is_auto_shoot_a = False
                hero_b.clear_index = 1
                hero_b.hp = 8
                Sound.play(sound_list[0])

                enemy_list.clear()
                bullet_list.clear()
                bullet_l_list.clear()
                bullet_r_list.clear()
                enemy_boss_list.clear()
                article_list.clear()
                Hero.score = Hero.score
                is_up_bullet = False
                high.read_high_score()

                hero_b.rect.topleft = (200, 600)
            if i.key == pygame.K_e:
                if Hero.score >= 150:
                    is_play =3
            if is_play == 3 and is_auto_shoot_b :
                is_auto_shoot_b = False
                is_auto_shoot_a = False
                is_auto_shoot_d = True
                hero_d.clear_index = 1
                hero_d.hp = 8
                Sound.play(sound_list[0])

                enemy_list.clear()
                bullet_list.clear()
                bullet_l_list.clear()
                bullet_r_list.clear()
                enemy_boss_list.clear()
                article_list.clear()
                Hero.score = Hero.score
                is_up_bullet = False
                high.read_high_score()

                hero_d.rect.topleft = (200, 600)





            #空格发射子弹
            if i.key == pygame.K_SPACE and is_play ==1 and is_pause == False :
                Bullet(bullet_img[0],((hero_a.rect.centerx-bullet_img[0].get_width()/2),hero_a.rect.top),screen,40,1)
                if is_up_bullet:
                    # 三排子弹
                    add_bullet_1 = int(hero_a.image.get_width() / 4 + hero_a.rect.x - bullet_img[0].get_width() / 2)
                    add_bullet_2 = int(hero_a.image.get_width() / 4 * 3 + hero_a.rect.x - bullet_img[0].get_width() / 2)
                    Bullet(bullet_img[0], (add_bullet_1, hero_a.rect.top), screen, 35, 2)
                    Bullet(bullet_img[0], (add_bullet_2, hero_a.rect.top), screen, 35, 3)
            if i.key == pygame.K_SPACE and is_play==2 and is_pause == False :
                Bullet(bullet_img[1],((hero_b.rect.centerx-bullet_img[1].get_width()/2),hero_b.rect.top),screen,40,1)
                if is_up_bullet:
                    # 三排子弹
                    add_bullet_1 = int(hero_b.image.get_width() / 4 + hero_b.rect.x - bullet_img[1].get_width() / 2)
                    add_bullet_2 = int(hero_b.image.get_width() / 4 * 3 + hero_b.rect.x - bullet_img[1].get_width() / 2)
                    Bullet(bullet_img[1], (add_bullet_1, hero_b.rect.top), screen, 35, 2)
                    Bullet(bullet_img[1], (add_bullet_2, hero_b.rect.top), screen, 35, 3)
            if i.key == pygame.K_SPACE and is_play==3 and is_pause == False :
                Bullet(bullet_img[3],((hero_d.rect.centerx-bullet_img[3].get_width()/2),hero_d.rect.top),screen,40,1)
                if is_up_bullet:
                    # 三排子弹
                    add_bullet_1 = int(hero_d.image.get_width() / 4 + hero_d.rect.x - bullet_img[3].get_width() / 2)
                    add_bullet_2 = int(hero_d.image.get_width() / 4 * 3 + hero_d.rect.x - bullet_img[3].get_width() / 2)
                    Bullet(bullet_img[3], (add_bullet_1, hero_d.rect.top), screen, 35, 2)
                    Bullet(bullet_img[3], (add_bullet_2, hero_d.rect.top), screen, 35, 3)
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_UP or i.key== pygame.K_w:
                Hero.up=False
            if i.key == pygame.K_DOWN or i.key== pygame.K_s:
                Hero.down=False
            if i.key == pygame.K_LEFT or i.key== pygame.K_a:
                Hero.left=False
            if i.key == pygame.K_RIGHT or i.key== pygame.K_d:
                Hero.right=False
icon_img = pygame.image.load("image/logo.png")


def main():
    #主函数
    #设置标题
    pygame.display.set_caption("                                             $$$!雷霆战机!$$$             ")
    while True:

        Event()
        Bgm.pause()
        if is_play==1:
            game_img.display()
            ArticleManager.article_move()
            EnemyMamger.enemy_move()
            EnemyMamger.enemy_boss_move()
            EnemyMamger.enemy_boss_move1()

            hero_a.move()
            #角色血量显示
            for i in range(0,hero_a.hp):
                screen.blit(hp_img,(25*i+120,10))
            #显示字体，血量
            hp = font1.render("    HP   :",True,(255,75,28))
            screen.blit(hp,(0,0))
            # Boss血量
            for i in enemy_boss_list:
                boss = font1.render("BOSSHP :%s"%(i.hp), True, (255, 75, 28))
                screen.blit(boss, (0, 110))
            #当前分数
            score_font=font1.render("Score:%s"%(hero_a.score),True,(76,214,255))
            screen.blit(score_font,(0,35))
            #历史分数
            score_font1 = font2.render("HighScore:%s" % (high.hestory), True, (255, 255, 255))
            screen.blit(score_font1, (0, 75))
            #全屏爆炸的数量显示
            clear_font = font2.render("X   %s" % (hero_a.clear_index), True, (255, 128, 16))
            screen.blit(clear_font, (80, 680))
        elif is_play == 2:
            game_img1.display()
            ArticleManager.article_move()
            EnemyMamger.enemy_move()
            EnemyMamger.enemy_boss_move()
            EnemyMamger.enemy_boss_move1()


            hero_b.move()
            # 角色血量显示
            for i in range(0, hero_b.hp):
                screen.blit(hp_img, (25 * i + 120, 10))
            # 显示字体，血量
            HP = font1.render("    HP   :", True, (255, 75, 28))
            screen.blit(HP, (0, 0))
            #Boss血量
            for i in enemy_boss_list:
                boss = font1.render("BOSSHP :%s"%(i.hp), True, (255, 75, 28))
                screen.blit(boss, (0, 110))
            # 当前分数
            score_font = font1.render("Score:%s" % (hero_b.score), True, (76, 214, 255))
            screen.blit(score_font, (0, 35))
            # 历史分数
            score_font1 = font2.render("HighScore:%s" % (high.hestory), True, (255, 255, 255))
            screen.blit(score_font1, (0, 75))
            # 全屏爆炸的数量显示
            clear_font = font2.render("X   %s" % (hero_b.clear_index), True, (255, 128, 16))
            screen.blit(clear_font, (80, 680))
        elif is_play == 3:
            game_img2.display()
            ArticleManager.article_move()
            EnemyMamger.enemy_move()
            EnemyMamger.enemy_boss_move()
            EnemyMamger.enemy_boss_move1()


            hero_d.move()
            # 角色血量显示
            for i in range(0, hero_d.hp):
                screen.blit(hp_img, (25 * i + 120, 10))
            # 显示字体，血量
            HP = font1.render("    HP   :", True, (255, 75, 28))
            screen.blit(HP, (0, 0))
            #Boss血量
            for i in enemy_boss_list1:
                boss = font1.render("BOSSHP :%s"%(i.hp), True, (255, 75, 28))
                screen.blit(boss, (0, 110))
            # 当前分数
            score_font = font1.render("Score:%s" % (hero_d.score), True, (76, 214, 255))
            screen.blit(score_font, (0, 35))
            # 历史分数
            score_font1 = font2.render("HighScore:%s" % (high.hestory), True, (255, 255, 255))
            screen.blit(score_font1, (0, 75))
            # 全屏爆炸的数量显示
            clear_font = font2.render("X   %s" % (hero_d.clear_index), True, (255, 128, 16))
            screen.blit(clear_font, (80, 680))



        else:
            begin_window.display()
        #画面更新
        pygame.display.update()

        #帧率
        clock.tick(60)


if __name__=="__main__":
    #开始函数
    main()
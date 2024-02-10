import pygame
import math
import random
from sys import exit
#import RPi.GPIO as GPIO 

pygame.init()
ActualScreen = pygame.display.set_mode((320,300),pygame.RESIZABLE)
screen = ActualScreen.copy()
pygame.display.set_caption('QuiVeut2GrammesDansLeSang')
clock = pygame.time.Clock()

Blood0=pygame.image.load('Sprite/Blood/SPLURG/000.png').convert_alpha()
Blood1=pygame.image.load('Sprite/Blood/SPLURG/001.png').convert_alpha()
Blood2=pygame.image.load('Sprite/Blood/SPLURG/002.png').convert_alpha()
Blood3=pygame.image.load('Sprite/Blood/SPLURG/003.png').convert_alpha()
Blood4=pygame.image.load('Sprite/Blood/SPLURG/004.png').convert_alpha()
Blood5=pygame.image.load('Sprite/Blood/SPLURG/005.png').convert_alpha()
Blood6=pygame.image.load('Sprite/Blood/SPLURG/006.png').convert_alpha()
Blood7=pygame.image.load('Sprite/Blood/SPLURG/007.png').convert_alpha()
Blood8=pygame.image.load('Sprite/Blood/SPLURG/008.png').convert_alpha()
Blood9=pygame.image.load('Sprite/Blood/SPLURG/009.png').convert_alpha()
Blood10=pygame.image.load('Sprite/Blood/SPLURG/010.png').convert_alpha()
BloodFrames=[Blood0,Blood1,Blood2,Blood3,Blood4,Blood5,Blood6,Blood7,Blood8,Blood9,Blood10]
animation_index=10

Flush0=pygame.image.load('Sprite/Blood/Sflush/000.png').convert_alpha()
Flush1=pygame.image.load('Sprite/Blood/Sflush/001.png').convert_alpha()
Flush2=pygame.image.load('Sprite/Blood/Sflush/002.png').convert_alpha()
Flush3=pygame.image.load('Sprite/Blood/Sflush/003.png').convert_alpha()
Flush4=pygame.image.load('Sprite/Blood/Sflush/004.png').convert_alpha()
Flush5=pygame.image.load('Sprite/Blood/Sflush/005.png').convert_alpha()
Flush6=pygame.image.load('Sprite/Blood/Sflush/006.png').convert_alpha()
Flush7=pygame.image.load('Sprite/Blood/Sflush/007.png').convert_alpha()
Flush8=pygame.image.load('Sprite/Blood/Sflush/008.png').convert_alpha()
Flush9=pygame.image.load('Sprite/Blood/Sflush/009.png').convert_alpha()
Flush10=pygame.image.load('Sprite/Blood/Sflush/010.png').convert_alpha()
Flush11=pygame.image.load('Sprite/Blood/Sflush/011.png').convert_alpha()
Flush12=pygame.image.load('Sprite/Blood/Sflush/012.png').convert_alpha()
Flush13=pygame.image.load('Sprite/Blood/Sflush/013.png').convert_alpha()
Flush14=pygame.image.load('Sprite/Blood/Sflush/014.png').convert_alpha()
Flush15=pygame.image.load('Sprite/Blood/Sflush/015.png').convert_alpha()
FlushFrames=[Flush0,Flush1,Flush2,Flush3,Flush4,Flush5,Flush6,Flush7,Flush8,Flush9,Flush10,Flush11,Flush12,Flush13,Flush14,Flush15]
animation_index2=15


TFont = pygame.font.Font('Font/8-bit Arcade In.ttf',17)
TFont3 = pygame.font.Font('Font/8-bit Arcade In.ttf',36)
TFont2 = pygame.font.Font('Font/Kenney Mini Square.ttf',16)

Title = pygame.image.load('Sprite/UI/Title.png').convert_alpha()
EndTitle = pygame.image.load('Sprite/UI/END.png').convert_alpha()

BackGround= pygame.image.load('Sprite/Tiles/TILES.png').convert()

WarnG= pygame.image.load('Sprite/Warning/Green/000.png').convert_alpha()
WarnR= pygame.image.load('Sprite/Warning/Red/000.png').convert_alpha()
WarnY= pygame.image.load('Sprite/Warning/Yellow/000.png').convert_alpha()

WarnR.set_alpha(0)

Dummy0 = pygame.image.load('Sprite/Dummy/000.png').convert_alpha()
Dummy1 = pygame.image.load('Sprite/Dummy/001.png').convert_alpha()

Ramp = pygame.image.load('Sprite/Ramp/004.png').convert_alpha()

Obstacle0 = pygame.image.load('Sprite/Obstacle/000.png').convert_alpha()
Obstacle1 = pygame.image.load('Sprite/Obstacle/001.png').convert_alpha()
Obstacle2 = pygame.image.load('Sprite/Obstacle/002.png').convert_alpha()

Car0 = pygame.image.load('Sprite/Car/000.png').convert_alpha()
Car1 = pygame.image.load('Sprite/Car/001.png').convert_alpha()
Car2 = pygame.image.load('Sprite/Car/002.png').convert_alpha()
Car3 = pygame.image.load('Sprite/Car/003.png').convert_alpha()
Car4 = pygame.image.load('Sprite/Car/004.png').convert_alpha()
Car5 = pygame.image.load('Sprite/Car/005.png').convert_alpha()
Car6 = pygame.image.load('Sprite/Car/006.png').convert_alpha()
Car7 = pygame.image.load('Sprite/Car/007.png').convert_alpha()
Car8 = pygame.image.load('Sprite/Car/008.png').convert_alpha()
Car9 = pygame.image.load('Sprite/Car/009.png').convert_alpha()

TimeLeft=30
KillCounter=0
Text1 = TFont2.render('  Ecrase les globulards ',False,'Black').convert_alpha()
Text2 = TFont2.render('   Evite les obstacles',False,'Black').convert_alpha()

Obstacle0 = pygame.transform.scale(Obstacle0, (13,12))
Obstacle1 = pygame.transform.scale(Obstacle1, (32,32))
Obstacle2 = pygame.transform.scale(Obstacle2, (16,30))
Dummy0 = pygame.transform.scale(Dummy0, (24,24))
Dummy1 = pygame.transform.scale(Dummy1, (24,24))

Has_Touched = False
Background_y = 0
Speed= 0
Accel=0.02
Player_Angle=90
Player_y = 280
Player_x = 144
Player_x_spd = 0
Left=False
Right=False
DamagedTime=0
StartTimer=0
JumpStart=-2
KillStart=1000
Scale=1
AlphaT=255
AlphaE=0
JumpHeight=0
End=False
Start=False
ScreenShake=0
JumpCons=1
ObstacleList=[]
Counter=0
ObstacleRecList=[]
DummyTouched=False
DummyPos=[160,-150,0]
BloodPos=[150,150,0]
ScoreTab=[]
#TailleEcran=[640,480]
TailleEcran=[1280,1048]
ActualScreen = pygame.display.set_mode(TailleEcran,pygame.FULLSCREEN)

def pipe_pick(DummyX):
    PipeId=math.ceil((DummyX-24)/43)
    if PipeId < 1:
        PipeId=1
    if PipeId > 6:
        PipeId=6
    return PipeId

def collisions(player,obstacles):
    global Del
    if obstacles:
        for obstacle_rect in obstacles:
            if obstacle_rect!=[] and player.colliderect(obstacle_rect): 
                Del=obstacle_rect
                return True
    return False

def init():
    global Background_y,KillStart,DummyTouched,DummyPos,BloodPos,Counter,ObstacleRecList,ObstacleList,JumpCons,JumpHeight,Speed,Accel,AlphaT,AlphaE,Start,Has_Touched,Player_Angle,Player_y,Player_x,Player_x_spd,Left,Right,DamagedTime,JumpStart,Scale,End,TimeLeft,KillCounter
    Background_y = 0            
    Speed= 0
    Accel=0.02
    KillStart=1000
    JumpHeight=0
    Player_Angle=90
    Player_y = 280
    Player_x = 145
    Player_x_spd = 0
    Left=False
    Right=False
    DamagedTime=0
    JumpStart=-2
    Scale=1
    End=False
    TimeLeft=30
    KillCounter=0
    AlphaT=255
    AlphaE=0
    Start=False
    Has_Touched = False
    JumpCons=1
    ObstacleList=[]
    ObstacleRecList=[]
    Counter=0
    DummyTouched=False
    DummyPos=[160,-150,0]
    BloodPos=[150,150,0]

def moyenne(list):
    Somme=0
    Counter=0
    for nombre in list:
        Somme+=nombre
        Counter+=1
    if Counter==0:
        Counter=1
    return (Somme/Counter)

def lerp(a, b, t):
    return (1 - t) * a + t * b

def CarJump():
    global JumpStart, JumpHeight, Speed, JumpCons
    if pygame.time. get_ticks()/1000 < JumpStart + 2: 
        JumpHeight=20*(pygame.time. get_ticks()/1000-JumpStart)**2-40*(pygame.time. get_ticks()/1000-JumpStart)
        JumpCons=1/5
    if JumpStart + 2.1 > pygame.time. get_ticks()/1000 > JumpStart + 2:
        JumpHeight=0
        bam(3,Speed)
        JumpCons=1
        
def bam(Shaker, NewSpeed):
    global ScreenShake, Speed
    ScreenShake = Shaker
    Speed = NewSpeed

def rot_center(image, angle):
    loc = image.get_rect().center
    rot_sprite = pygame.transform.rotate(image, angle)
    rot_sprite.get_rect().center = loc
    return rot_sprite
"""    
def right_button(channel): 
    global Right
    if GPIO.input(3):
        print("PLUS APPUIE DROIT")
        Right=False
    else:
        print("APPUIE DROIT")
        Right=True

def left_button(channel):
    global Left
    if GPIO.input(5):
        print("PLUS APPUIE GAUCHE")
        Left=False
    else:
        print("APPUIE GAUCHE")
        Left=True
    
        
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(3,GPIO.BOTH,callback=right_button)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(5,GPIO.BOTH,callback=left_button) 
"""
while True:
    dt=clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #GPIO.cleanup() # Clean up
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Left=True
            if event.key == pygame.K_RIGHT:
                Right=True


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                Left=False
            if event.key == pygame.K_RIGHT:
                Right=False
        
    if Left or Right:
        if Left and Right:
            Player_Angle=lerp(Player_Angle,90,0.1*JumpCons)
            Player_x_spd=lerp(Player_x_spd,0,0.1*JumpCons)
            if not Start:
                Start=True
                StartTimer=pygame.time. get_ticks()/1000
                ScreenShake=15
                for _ in range(8):
                    ObstacleList.append([str(random.randint(1,3)),random.randint(1,16)*16+24,random.randint(2,58)*32+500,Counter])
                    Counter +=1
                    ObstacleRecList.append([])
            if End:
                ScoreTab.append(KillCounter)
                print(moyenne(ScoreTab))
                print(ScoreTab)
                init()
                WarnR.set_alpha(0)

        else:
            if Left and not End and Start:
                Player_Angle=lerp(Player_Angle,120,0.1*JumpCons*Speed/6)
                Player_x_spd=lerp(Player_x_spd,-4,0.1*JumpCons*Speed/6)
            if Right and not End and Start:
                Player_Angle=lerp(Player_Angle,60,0.1*JumpCons*Speed/6)
                Player_x_spd=lerp(Player_x_spd,4,0.1*JumpCons*Speed/6)
    else:
        if not End:
            Player_Angle=lerp(Player_Angle,90,0.1*JumpCons)
            Player_x_spd=lerp(Player_x_spd,0,0.2*JumpCons)




    #ScreenShake
    render_offset = [0,0]
    if ScreenShake > 0:
        ScreenShake -=1
        render_offset[0] = random.randint(0,8) - 4
        render_offset[1] = random.randint(0,8) - 4

    screen.blit(BackGround,(render_offset[0],-2700+Background_y+render_offset[1]))


    #GameOnlyAction
    
    if TimeLeft > 0:
        if Start:
            Player_x+=Player_x_spd*dt/17
            if Player_x < 16:
                Player_x = 18
                Player_x_spd=6*JumpCons
                Player_Angle=40
                Speed=Speed/4
                Left=False
                ScreenShake=5
                
            if Player_x > 274:
                Player_x = 272
                Player_x_spd=-6*JumpCons
                Player_Angle=140
                Speed=Speed/4
                Right=False
                ScreenShake=5
            
            Speed+=Accel*dt/17
            if Speed > 6:
                Speed=6
            Background_y += Speed*dt/17
            
            #Compteur de tour
            if Background_y > 2700:
                Background_y = Background_y%2700
                for _ in range(6):
                    ObstacleList.append([str(random.randint(1,3)),random.randint(1,16)*16+24,random.randint(2,58)*32+500,Counter])
                    Counter +=1
                    ObstacleRecList.append([])
                
            TimeLeft = int(30 + StartTimer - pygame.time. get_ticks()/1000)
        Chrono = TFont.render('    temps               Globulards',False,'Black')
        Chrono2 = TFont.render('   restant                aplatis    ',False,'Black')
        ChronoTime = TFont3.render(str(TimeLeft),False,(150,0,0))
        ChronoKill = TFont3.render(str(KillCounter),False,(150,0,0))

    else:
        End=True
        AlphaE+=2
        WarnR.set_alpha(0)

    #Collisionq

    for obstacle in ObstacleList:
        if obstacle[0]=='1':
            screen.blit(Obstacle0,Obstacle0.get_rect(center=(obstacle[1],-obstacle[2]+Background_y%2700)))
            ObstacleRecList[obstacle[3]]=Obstacle0.get_rect(center=(obstacle[1],-obstacle[2]+Background_y%2700))
        if obstacle[0]=='2':
            screen.blit(Obstacle1,Obstacle1.get_rect(center=(obstacle[1],-obstacle[2]+Background_y%2700)))
            ObstacleRecList[obstacle[3]]=Obstacle1.get_rect(center=(obstacle[1],-obstacle[2]+Background_y%2700))
        if obstacle[0]=='3':
            screen.blit(Obstacle2,Obstacle2.get_rect(center=(obstacle[1],-obstacle[2]+Background_y%2700)))
            ObstacleRecList[obstacle[3]]=Obstacle2.get_rect(center=(obstacle[1],-obstacle[2]+Background_y%2700))

    screen.blit(Chrono2,Chrono2.get_rect(midbottom=(150,319)))
    screen.blit(Chrono,Chrono.get_rect(midbottom=(150,312)))
    screen.blit(ChronoTime,ChronoTime.get_rect(midbottom=(135,319)))
    screen.blit(ChronoKill,ChronoKill.get_rect(midbottom=(280,319)))

    if collisions(Car0.get_rect(bottomleft=(Player_x, Player_y+Speed)), ObstacleRecList) and not Has_Touched and JumpHeight==0:
        Has_Touched=True
        bam(20, Speed/10)
        Player_x_spd=Player_x_spd/3
    if not collisions(Car0.get_rect(bottomleft=(Player_x, Player_y+Speed)), ObstacleRecList):
        Has_Touched=False

    if int(pygame.time. get_ticks()/250)%2==0:
        Dummy = Dummy0
    if int(pygame.time. get_ticks()/250)%2==1:
        Dummy = Dummy1

    screen.blit(rot_center(Dummy,DummyPos[2]),Dummy.get_rect(center=(DummyPos[0],(-DummyPos[1]+Background_y)%2700)))
    
    if Car0.get_rect(bottomleft=(Player_x, Player_y+Speed)).colliderect(Dummy.get_rect(center=(DummyPos[0],(-DummyPos[1]+Background_y)%2700))) and not DummyTouched and JumpHeight==0:
        DummyTouched=True
        print(pipe_pick(DummyPos[0]))
        WarnR.set_alpha(0)
        KillCounter+=1
        animation_index=0
        animation_index2=0
        BloodPos[0]=DummyPos[0]
        BloodPos[1]=DummyPos[1]
        KillStart = pygame.time. get_ticks()/1000
        bam(12, Speed*6)

    if DummyTouched:
        DummyPos[1]+=12*dt/17
        DummyPos[2]+=4*dt/17
    if pygame.time. get_ticks()/1000 -KillStart > 4.4:
        DummyTouched=False
        KillStart=10000
        WarnR.set_alpha(255)
        DummyPos[2]=0
        DummyPos[0]=random.randint(1,16)*16+24
    else:
        if int(pygame.time. get_ticks()/150)%2==0:
            WarnR = pygame.transform.scale(WarnR, (16,16))
        if int(pygame.time. get_ticks()/150)%2==1:
            WarnR = pygame.transform.scale(WarnR, (8,8))
    screen.blit(WarnR,WarnR.get_rect(center=(DummyPos[0],20)))

    animation_index2 += 0.3*dt/17 
    if animation_index2 >= len(FlushFrames): animation_index2 = 15
    FlushImage = FlushFrames[int(animation_index2)]
    FlushImage = pygame.transform.scale(FlushImage, (128,128))
    FlushImage = rot_center(FlushImage,DummyPos[2])
    screen.blit(FlushImage,FlushImage.get_rect(center=(DummyPos[0],(-DummyPos[1]+Background_y)%2700)))


    #Title and End Vanish
    if Start:
        AlphaT-=3
    if AlphaT >=0:    
        Text1.set_alpha(AlphaT*2)
        Text2.set_alpha(AlphaT*2)
        Title.set_alpha(AlphaT*2)
        Instruct = TFont2.render(" Pour commencer pose ton gobelet",False,'Black')
        Instruct2 = TFont2.render(" et appuie sur les 2 boutons",False,'Black')
        Instruct.set_alpha(AlphaT)
        Instruct2.set_alpha(AlphaT)
        MoyenneScore = TFont2.render("Score moyen:"+str(int(moyenne(ScoreTab)*10)/10),False,(0,0,0))
        MoyenneScore.set_alpha(AlphaT)
        screen.blit(MoyenneScore,MoyenneScore.get_rect(center=(160,235)))
        screen.blit(Text1,Text1.get_rect(center=(160,100)))
        screen.blit(Text2,Text2.get_rect(center=(160,115)))
        screen.blit(Title,Title.get_rect(center=(160+5*math.sin(2*pygame.time. get_ticks()/1000),50+2.5*math.sin(6*pygame.time. get_ticks()/1000))))
        screen.blit(Instruct,Instruct.get_rect(center=(160,190+2*math.sin(6*pygame.time. get_ticks()/1000))))
        screen.blit(Instruct2,Instruct2.get_rect(center=(160,204+2*math.sin(6*pygame.time. get_ticks()/1000))))
    EndTitle = pygame.transform.scale(EndTitle, (242,154))
    EndTitle.set_alpha(AlphaE)
    screen.blit(EndTitle,EndTitle.get_rect(center=(160,120)))


    #Car Draw    
    screen.blit(rot_center(Car0, Player_Angle),rot_center(Car0, Player_Angle).get_rect(center=Car0.get_rect(topleft=(Player_x, Player_y-Speed*1.5)).center).topleft)
    screen.blit(rot_center(Car1, Player_Angle),rot_center(Car0, Player_Angle).get_rect(center=Car1.get_rect(topleft=(Player_x, Player_y-1.25-Speed*1.5+JumpHeight)).center).topleft)
    screen.blit(rot_center(Car2, Player_Angle),rot_center(Car0, Player_Angle).get_rect(center=Car2.get_rect(topleft=(Player_x, Player_y-2.5-Speed*1.5+JumpHeight)).center).topleft)
    screen.blit(rot_center(Car3, Player_Angle),rot_center(Car0, Player_Angle).get_rect(center=Car3.get_rect(topleft=(Player_x, Player_y-3.75-Speed*1.5+JumpHeight)).center).topleft)
    screen.blit(rot_center(Car4, Player_Angle),rot_center(Car0, Player_Angle).get_rect(center=Car4.get_rect(topleft=(Player_x, Player_y-5-Speed*1.5+JumpHeight)).center).topleft)
    screen.blit(rot_center(Car5, Player_Angle),rot_center(Car0, Player_Angle).get_rect(center=Car5.get_rect(topleft=(Player_x, Player_y-6.25-Speed*1.5+JumpHeight)).center).topleft)
    screen.blit(rot_center(Car6, Player_Angle),rot_center(Car0, Player_Angle).get_rect(center=Car6.get_rect(topleft=(Player_x, Player_y-7.5-Speed*1.5+JumpHeight)).center).topleft)
    screen.blit(rot_center(Car7, Player_Angle),rot_center(Car0, Player_Angle).get_rect(center=Car7.get_rect(topleft=(Player_x, Player_y-8.75-Speed*1.5+JumpHeight)).center).topleft)
    screen.blit(rot_center(Car8, Player_Angle),rot_center(Car0, Player_Angle).get_rect(center=Car8.get_rect(topleft=(Player_x, Player_y-10-Speed*1.5+JumpHeight)).center).topleft)
    screen.blit(rot_center(Car9, Player_Angle),rot_center(Car0, Player_Angle).get_rect(center=Car9.get_rect(topleft=(Player_x, Player_y-11.25-Speed*1.5+JumpHeight)).center).topleft)
    animation_index += 0.4*dt/17 
    if animation_index >= len(BloodFrames): animation_index = 10
    BloodImage = BloodFrames[int(animation_index)]
    BloodImage = pygame.transform.scale(BloodImage, (196,196))
    screen.blit(BloodImage,BloodImage.get_rect(midbottom=(BloodPos[0],(-BloodPos[1]+Background_y)%2700)))
    ActualScreen.fill((0,0,0))
    ActualScreen.blit(pygame.transform.scale(screen, (ActualScreen.get_rect().height,ActualScreen.get_rect().height)), (ActualScreen.get_rect().width/8, 0))
    pygame.display.update()

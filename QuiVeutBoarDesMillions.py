import pygame
import math
import random
from sys import exit
#import RPi.GPIO as GPIO 
import subprocess
import serial
import time

pygame.init()
ActualScreen = pygame.display.set_mode((320,320),pygame.RESIZABLE)
screen = ActualScreen.copy()
pygame.display.set_caption('QuiVeutBoarDesMillions')
clock = pygame.time.Clock()
#ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0.05)

TFont = pygame.font.Font('Font/8-bit Arcade In.ttf',17)
TFont3 = pygame.font.Font('Font/8-bit Arcade In.ttf',36)
TFont2 = pygame.font.Font('Font/Kenney Mini Square.ttf',16)

Title = pygame.image.load('Sprite\QuiVeutBoarDesMillionsLogo.png').convert_alpha()
EndTitle = pygame.image.load('Sprite\QuiVeutBoarDesMillionsLogo.png').convert_alpha()
BackGround= pygame.image.load('Sprite/QuiBoarDesMillions.png').convert()

TimeLeft=30
Score=0
Text1 = TFont2.render('Répond au plus de question possible',False,(240,100,0)).convert_alpha()

pygame.mouse.set_visible(False)

waitStart = True
Left=False
Right=False
StartTimer=0
AlphaT=255
AlphaE=0
End=False
Start=False
ScreenShake=0
ScoreTab=[]
TailleEcran=[640,480]
SpeedJustMaxed=True
TwoSecHasPassed=False
Select=0
#ActualScreen = pygame.display.set_mode(TailleEcran,pygame.FULLSCREEN)
#subprocess.Popen(["curl", "--silent", "-o /dev/null", "http://barbot.local/win&PL=1"], start_new_session=True)
Title=pygame.transform.scale(Title, (0,0))

def pipe_pick(QuestionNumber):
    PipeId = QuestionNumber
    if PipeId < 0:
        PipeId=0
    if PipeId > 5:
        PipeId=5
    return PipeId

def init():
    global AlphaT,AlphaE,Start,Left,Right,End,TimeLeft,Score,Select
    Left=False
    Right=False
    End=False
    TimeLeft=30
    Score=0
    AlphaT=255
    AlphaE=0
    Start=False
    Select=0
    #subprocess.Popen(["curl", "--silent", "-o /dev/null", "http://barbot.local/win&PL=1"], start_new_session=True)


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
        Right=False
    else:
        Right=True

def left_button(channel):
    global Left
    if GPIO.input(5):
        Left=False
    else:
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
        #ScreenShake
    render_offset = [0,0]
    if ScreenShake > 0:
        ScreenShake -=1
        render_offset[0] = random.randint(0,8) - 4
        render_offset[1] = random.randint(0,8) - 4

    screen.blit(BackGround,BackGround.get_rect(center=(160+render_offset[0],160+render_offset[1])))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #ser.close()
            #GPIO.cleanup()
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                #ser.close()
                #GPIO.cleanup()
                pygame.quit()
                exit()
            
            if event.key == pygame.K_LEFT:
                Left=True
            if event.key == pygame.K_RIGHT:
                Right=True
            
            if event.key == pygame.K_a and not Start:
                #ser.write(b"/START")
                time.sleep(2)
                #ser.write(b"/ARM")
                time.sleep(60)
                #ser.write(b"/STOP")
                time.sleep(5)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                Left=False
            if event.key == pygame.K_RIGHT:
                Right=False

    if End:
        waitStop = True
        while waitStop:
            #ser.write(b"/STOP")
            time.sleep(1)
            #line = ser.readline()
            if int(pygame.time.get_ticks()/250)%2==0 and AlphaE>254:
                EndTitle.set_alpha(125)
                    
            if int(pygame.time.get_ticks()/250)%2==1 and AlphaE>254:
                EndTitle.set_alpha(255)
            """
            if b"/STOP" in line:
                ser.close()
                waitStop = False  
                time.sleep(2)
                ScoreTab.append(Score)
                init()
                WarnR.set_alpha(0)
                #ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0.05)
            """        
    if not Start:
        line = 0
        #line = ser.readline()
    if Left or Right:
        if Left and Right:
            #print("LES DEUX")
            if not Start:
                Start=True
                StartTimer=pygame.time. get_ticks()/1000
                ScreenShake=15
            """
            if not Start and (b"/START" in line):
                subprocess.Popen(["curl", "--silent", "-o /dev/null", "http://barbot.local/win&PL=3"], start_new_session=True)
                Start=True
                #ser.write(b"/START")
                StartTimer=pygame.time. get_ticks()/1000
                ScreenShake=15
                #initialisation des questions
            """
        else:
            if Left and not End and Start:
                Select=(Select-1)%4
                Left=False
                print(Select)
            if Right and not End and Start:
                Select=(Select+1)%4
                Right=False
                print(Select)
    #else:
        #if not End:
            #print("RIEN")

    #GameOnlyAction
    
    if TimeLeft > 0:
        if Start:           
            #Compteur de quesion
            TimeLeft = int(60 + StartTimer - pygame.time. get_ticks()/1000)
            screen.blit(ChronoTime,ChronoTime.get_rect(midbottom=(160,272)))
        ChronoTime = TFont3.render(str(TimeLeft),False,(240,100,0))
        ChronoKill = TFont3.render(str(Score),False,(240,100,0))

    else:
        End=True
        AlphaE=255
        #subprocess.Popen(["curl", "--silent", "-o /dev/null", "http://barbot.local/win&PL=2"], start_new_session=True)


    #Questions/réponse

    #screen.blit(Chrono2,Chrono2.get_rect(midbottom=(150,295)))
    #screen.blit(Chrono,Chrono.get_rect(midbottom=(150,287)))

    #screen.blit(ChronoKill,ChronoKill.get_rect(midbottom=(280,295)))


    #Title and End Vanish
    if Start:
        AlphaT-=3
    if AlphaT >=0:    
        Text1.set_alpha(AlphaT*2)
        Title.set_alpha(AlphaT*2)
        Instruct = TFont2.render(" Pose ton gobelet",False,(240,100,0))
        Instruct2 = TFont2.render(" et maintiens les 2 boutons",False,(240,100,0))
        Instruct.set_alpha(AlphaT)
        Instruct2.set_alpha(AlphaT)
        MoyenneScore = TFont2.render("Score moyen:"+str(int(moyenne(ScoreTab)*10)/10),False,(240,100,0))
        MoyenneScore.set_alpha(AlphaT)
        screen.blit(MoyenneScore,MoyenneScore.get_rect(center=(160,263)))
        screen.blit(Text1,Text1.get_rect(center=(160,120)))
        screen.blit(Title,Title.get_rect(center=(160+5*math.sin(2*pygame.time. get_ticks()/1000),20+2.5*math.sin(6*pygame.time. get_ticks()/1000))))
        screen.blit(Instruct,Instruct.get_rect(center=(160,169+2*math.sin(6*pygame.time. get_ticks()/1000))))
        screen.blit(Instruct2,Instruct2.get_rect(center=(160,185+2*math.sin(6*pygame.time. get_ticks()/1000))))
    EndTitle.set_alpha(AlphaE)
    """
    if int(pygame.time.get_ticks()/250)%2==0 and AlphaE>254:
        EndTitle.set_alpha(125)
            
    if int(pygame.time.get_ticks()/250)%2==1 and AlphaE>254:
        EndTitle.set_alpha(255)
    """
    screen.blit(EndTitle,EndTitle.get_rect(center=(160,120)))
    #pygame.draw.rect(screen,(0,0,0),pygame.Rect(Player_x+8, Player_y-Speed-10,16,32))
    ActualScreen.fill((0,0,0))
    ActualScreen.blit(pygame.transform.scale(screen, (ActualScreen.get_rect().width,ActualScreen.get_rect().height)), (8, 0))
    pygame.display.update()
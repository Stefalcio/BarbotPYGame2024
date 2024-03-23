import pygame
import math
import random
from sys import exit
import RPi.GPIO as GPIO
import subprocess
import serial
import time

pygame.init()
ActualScreen = pygame.display.set_mode((320,320),pygame.RESIZABLE)
screen = ActualScreen.copy()
pygame.display.set_caption('QuiVeutBoarDesMillions')
clock = pygame.time.Clock()
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0.05)

TFont = pygame.font.Font('Font/8-bit Arcade In.ttf',17)
TFont3 = pygame.font.Font('Font/8-bit Arcade In.ttf',38)
TFont2 = pygame.font.Font('Font/Kenney Mini Square.ttf',16)
TFont4 = pygame.font.Font('Font/Kenney Mini Square.ttf',8)
TFont5 = pygame.font.Font('Font/Kenney Mini Square.ttf',14)

EndTitle = pygame.image.load('Sprite/QuiVeutBoarDesMillionsLogo.png').convert_alpha()
Selector = pygame.image.load('Sprite/Selector.png').convert_alpha()
BackGround= pygame.image.load('Sprite/QuiBoarDesMillions.png').convert()

TimeLeft=30
Score=0
Text1 = TFont5.render('Réponds aux 6 questions pour ta boisson',False,(240,100,0)).convert_alpha()

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
ReponseX=-800
MReponseX=-800
trigger = False
ActualScreen = pygame.display.set_mode(TailleEcran,pygame.FULLSCREEN)
Question =["Quel est l'ancien nom de l'association Unifly ?", "Quel est le numéro de l'édition 2024 de la Journée de l’Aéronautique ?", "Combien d'aéronefs sont présents en statique cette année ?", "A quelle école était rattaché le club Esifly ?", "Combien de pistes possèdent l'aéroport de Valence Chabeuil ?", "À qui appartient le hangar où se déroule l'événement ?", "Comment s'appelle l'organisme français qui rassemble tous les ULM ?", "Comment sont remorqués les planeurs ?", "Comment s'appelle la partie goudronnée qui rejoint la piste ?", "Comment d'associations rassemble le pôle aviation de loisir à Valence ?", "Comment s'appelle la base militaire sur l'aéroport de Valence ?", "Quel est le nom de l'actuel président d'Unifly ?", "Quel est le nom de l'hélicoptère présent à cette édition ?", "Quel est le nom du premier avion électrique certifié ?", "Quel est le nom du champion du monde de voltige aérienne 2022 ?", "Quelle force armée contrôle le GAMSTAT ?", "Quelle est l'année de création de l'association Unifly ?", "Qui est le créateur de l'association Unifly ?", "Combien de mètres mesure la piste principale de l'aéroport ?", "Quelle est l'altitude de la piste ?", "Quelle est la hauteur de la tour de contrôle de Valence ?", "Pour quelle raison a été construit l'aéroport de Valence Chabeuil ?", "De quelle année date la première ligne régulière à Valence Chabeuil ?", "En 2019, combien d'atterrissages et décollages ont été effectué ?"]

Reponse = [["Etufly", "LikeFly", "Esifly", "IutFly"], ["1ere", "2eme", "3eme", "4eme"], ["3", "4", "5", "6"], ["Grenoble INP Phelma", "Grenoble INP Esisar", "IUT Valence", "UGA Sciences"], ["1", "2", "3", "4"], ["Valence Planeur", "Valence ULM", "Valence Voleur", "Valeur Rêveur"], ["FFVOL", "FFPLUM", "FFAIL", "FFBEC"], ["Par un ULM", "Par une voiture", "Par oiseaux", "Par Zeus"], ["Plane Way", "Landing Way", "Approach Way", "Taxi Way"],  ["1", "2", "3", "4"], ["GAMSTAT", "GAMVAL", "GAMGNAM", "GAMVERT"], ["Jérémy Boissel", "Jérémy Boeing", "Jérémy Breguet", "Jérémy Buffett"], ["AS532", "EC665", "H225M", "NH90"], ["VoltAero Cassio", "Velis Electro", "eFlyer", "Sun Flyer"], ["Florent O'Connor", "Florent O'Brien", "Florent Oddon", "Florent Olsen"], ["Armée de l'air", "Armée de terre", "Marine", "Gendarmerie"], ["2017", "2018", "2019", "2020"], ["Guilhem Roland", "Guilhem Robinson", "Guilhem Reynolds", "Guilhem Ryan"], ["1500m", "1800m", "2100m", "2400m"], ["450 pieds", "475 pieds", "500 pieds", "525 pieds"], ["22 mètres", "27 mètres", "32 mètres", "37 mètres"], ["WW1", "WW2", "JO 1968", "Coupé aéro 1910"], ["1959", "1964", "1969", "1974"], ["20000", "24000", "28000", "32000"]]

BonneReponse = [2, 3, 2, 1, 2, 0, 1, 0, 3, 2, 0, 0, 3, 1, 2, 1, 3, 0, 2, 3, 1, 1, 2, 3]

#Reponse=[["1939", "1989", "1992", "2035"], ["32ème", "33ème", "34ème", "35ème"], ["Le GC", "La Cave", "Le Cercle", "Le Carré"], ["Fil Rouge", "Morpion", "Relai 1,2,3,4", "Va Chercher"], ["Valence", "La CAVE", "Le GC", "L'AVE"], ["10", "11", "12", "13"], ["Cercle de l'AVE", "Contre l'AVE", "Caca Aka Vaka Eka", "La pièce en sous-sol là"], ["Les Alcooliques", "Les Mineurs", "Les Vieux", "Les Volcans"], ["Un week-end bien arrosé", "Une fête sans s'arrêter", "Un apéro un peu trop grand", "Une compétition toujours gagnée"], ["Alcooliques", "Champions", "Génies", "Infatiguables"], ["10", "11", "12", "50"], ["Francaise", "Italienne", "Norvégienne", "Japonaise"], ["Corée du Sud", "Japon", "Italie", "Finlande"], ["Vin Rouge", "Vin Blanc", "Vin Rosé", "Bière Blonde"], ["La Cave", "L’ISAR", "Le CEDE", "FC Châteauroux"], ["1", "3", "34", "51"], ["Au bar", "En trappage", "A l’Esisar", "A l’EHPAD"], ["128 L/adulte", "142 L/adulte", "168 L/adulte", "188 L/adulte"], ["0", "26", "54", "82"], ["0, c’est de l'eau", "8", "69", "1000° dans la soirée"], ["108 ans", "112 ans", "115 ans", "117 ans"], ["15 %", "17 %", "20 %", "22 %"], ["78 ans", "80 ans", "82 ans", "85 ans"], ["5 milliard", "10 milliard", "15 milliard", "30 milliard"], ["32 ans", "38 ans", "42 ans", "48 ans"], ["L’Alcool", "Poulpy", "La Victoire", "Les Inf’"], ["Du piment d'espelette", "Des champignons", "Des prostituées", "Du cacaaaa"], ["Le goulot d'étranglement", "Le passage étroit", "La trachée gazeuse", "Le sphincter"], ["1948", "1956", "1962", "1970"], ["500 euros", "1000 euros", "2000 euros", "4000 euros"], ["20,5", "23", "27,5", "32"], ["65 ans", "70 ans", "75 ans", "80 ans"], ["Esisar - VALENCE INP", "ESISAR - Grenoble INP", "Grenoble INP - Esisar", "Valence INP - Esisar"], ["T'es enceinte de 3 mois", "T'es enceinte de 6 mois", "On décale ton bassin", "Tu jouis 3 fois"], ["98", "128", "168", "200"], ["5", "6", "7", "8"], ["Kette", "Alonzo", "Lorenzo", "Ninho"], ["715MHz", "815MHz", "915MHz", "1015MHz"], ["500 mega ohms", "1200 mega ohms", "2000 mega ohms", "3750 mega ohms"], ["2556", "5789", "7324", "9293"], ["1000 degrée", "1300 degrée", "1600 degrée", "1900 degrée"], ["CAMILLE VERNET", "IUT", "DROIT-ECO", "ESISAR"]]
#BonneReponse=[1,  2 ,  2 ,  1 ,  3 ,  3 ,  1 ,  3 ,  2 ,  0 ,  2 ,  3 ,  1 ,  0 ,  2 ,  1 ,  3 ,  0 ,  3 ,  1 ,  3 ,  2 ,  3 ,  2 ,  0 ,  1 ,  1 ,  0 ,  1 ,  3 ,  0 ,  0 ,  2 ,  0 ,  1 ,  2 ,  1 ,  2 ,  2 ,  3 ,  0 ,  3 ]
#Question = ["Quelle est l'année de la 1re édition du Challenge de l'Étudiant ?", "Quel est le numéro de l'édition 2024 du Challenge de l'Étudiant ?", "Quel BDE a le plus de victoires au Challenge de l'Étudiant ?", "Quel est le nouveau jeu du Challenge de l'Étudiant 2024 ?", "Qui organise le Challenge ?", "Combien d'équipes sont présentes au Challenge de l'Étudiant 2024 ?", "La CAVE, c'est ?", "Si on te demande, c'est quoi le thème de l'Esisar ?", "Dans les chants Esisariens, comment est décrit le challenge ?", "Dans ses chants, comment sont décrits les étudiants de l'Esisar ?", "Combien d'étoiles à le BDE de l'Esisar ?", "Quelle est la nationalité de la doyenne du monde ?", "Quel est le pays avec la plus grande proportion de vieux ?", "Quel alcool est le plus consommé des + de 65 ans en France ?", "Qui a gagné le 1er challenge de l'Étudiant ?", "Quel est le record de victoires successives au Challenge de l'Étudiant ?", "Où peux-tu trouver la Cave à Valence ?", "En 1960, en moyenne combien un Français buvait-il de litres de vin par an ?", "Combien y-t-il eu de comas éthyliques lors du salon de l'agriculture 2023 ?", "À combien de degrés d'alcool est la clairette de Die, cuvée Obsidienne ?", "Quel âge avait la doyenne française ?", "Quel est le pourcentage de la population française ayant plus de 65 ans ?", "Quel est l'âge moyen à l'entrée en EHPAD ?", "Quel est le déficit des retraites en France ?", "À partir de quel âge un homme commence à avoir des cheveux blancs ?", "Dans les chants Esisariens, pour qui les étudiants ont le coeur qui bat ?", "Dans les chants Esisariens, avec quoi assaisonner un sanglier ?", "Quel est le nom donné à la partie la plus étroite du conduit d'un volcan ?", "Jusqu'à quelle année on servait du vin à la cantine ?", "Combien coûte un dentier haut de gamme ?", "En moyenne, combien de dents a une personne de 80 ans ?","Quel est l'âge moyen des personnes atteintes d'incontinence fécale ?", "Quelle est la bonne charte graphique ?", "Dans le rap de l'Esisar, on vous baise tellement fort que ?", "Combien de coupes à ramener l'Esisar depuis la création du Challenge ?", "Combien de couches y a-t-il dans le modèle OSI ?", "Dans les chants Esisariens, que répondre à la question : Qui est là ?", "Quelle fréquence utilisent les antennes RFID ?", "Quelle est la résistance moyenne du corps humain en mega ohms ?", "À ce jour, combien y a-t-il de RFC ?", "Quelle est la température dans la chambre magmatique d'un volcan ?", "De quelle école était l'étudiant ayant créé la Cave ?"]
NumeroQuestion=0
QuestionOffset=random.randint(0,14)
QuestionAsked=[]
subprocess.Popen(["curl", "--silent", "-o /dev/null", "http://wled.local/win&PL=1"], start_new_session=True)

def pipe_pick(NumeroQuestion):
    PipeId = math.floor(NumeroQuestion)
    if PipeId < 0:
        PipeId=0
    if PipeId > 5:
        PipeId=5
    return PipeId

def display_text(surface, text, pos, font, color, size):
    collection = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    x,y = pos
    for lines in collection:
        for words in lines:
            word_surface = font.render(words, False, color)
            word_width , word_height = word_surface.get_size()
            if x + word_width >= size:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x,y))
            x += word_width + space
        x = pos[0]
        y += word_height

def init():
    global AlphaT,AlphaE,Start,Left,Right,End,TimeLeft,Score,Select,ReponseX,MReponseX,NumeroQuestion, QuestionAsked, QuestionOffset
    Left=False
    Right=False
    End=False
    TimeLeft=30
    Score=0
    AlphaT=255
    AlphaE=0
    Start=False
    Select=0
    ReponseX=-800
    MReponseX=-800
    NumeroQuestion=0
    QuestionAsked=[]
    QuestionOffset=random.randint(0,14)
    subprocess.Popen(["curl", "--silent", "-o /dev/null", "http://wled.local/win&PL=1"], start_new_session=True)


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

def rot_center(image, angle):
    loc = image.get_rect().center
    rot_sprite = pygame.transform.rotate(image, angle)
    rot_sprite.get_rect().center = loc
    return rot_sprite

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
            ser.close()
            GPIO.cleanup()
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                ser.close()
                GPIO.cleanup()
                pygame.quit()
                exit()
            
            if event.key == pygame.K_LEFT:
                Left=True
            if event.key == pygame.K_RIGHT:
                Right=True
            
            if event.key == pygame.K_a and not Start:
                ser.write(b"/START")
                time.sleep(2)
                ser.write(b"/ARM")
                time.sleep(60)
                ser.write(b"/STOP")
                time.sleep(5)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                Left=False
            if event.key == pygame.K_RIGHT:
                Right=False

    if End:
        waitStop = True
        while waitStop:
            ser.write(b"/STOP")
            time.sleep(1)
            line = ser.readline()
            if int(pygame.time.get_ticks()/250)%2==0 and AlphaE>254:
                EndTitle.set_alpha(125)
                    
            if int(pygame.time.get_ticks()/250)%2==1 and AlphaE>254:
                EndTitle.set_alpha(255)
            """
            waitStop = False
            time.sleep(2)
            ScoreTab.append(Score)
            init()
            """
            if b"/STOP" in line:
                ser.close()
                waitStop = False  
                time.sleep(1)
                ScoreTab.append(Score)
                init()
                ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0.05)        
    if not Start:
        line = 0
        line = ser.readline()
    if Left or Right:
        if Left and Right:
            #print("LES DEUX")
            """
            if not Start:
                Start=True
                StartTimer=pygame.time. get_ticks()/1000
                ScreenShake=14
                subprocess.Popen(["curl", "--silent", "-o /dev/null", "http://wled.local/win&PL=3"], start_new_session=True)
            """ 
            if not Start and (b"/START" in line):
                subprocess.Popen(["curl", "--silent", "-o /dev/null", "http://wled.local/win&PL=3"], start_new_session=True)
                Start=True
                ser.write(b"/START")
                StartTimer=pygame.time. get_ticks()/1000
                ScreenShake=14
                #initialisation des questions

        else:
            if Left and not End and Start:
                Select=(Select-1)%4
                Left=False
                Right=False
            if Right and not End and Start:
                Select=(Select+1)%4
                Right=False
                Left=False
    #else:
        #if not End:
            #print("RIEN")

    #GameOnlyAction
    
    if TimeLeft > 0:
        if Start:           
            #Compteur de quesion
            TimeLeft = int(96 + StartTimer - pygame.time. get_ticks()/1000)
            screen.blit(ChronoTime,ChronoTime.get_rect(midbottom=(160,272)))
            screen.blit(BonneReponseText,BonneReponseText.get_rect(center=(ReponseX+480,115)))
            screen.blit(MauvaiseReponseText,MauvaiseReponseText.get_rect(center=(MReponseX+480,115)))
            screen.blit(Selector,Selector.get_rect(center=(92+Select%2*135,240+int(Select/2)*48)))
            ReponseX=-0.25*dt+ReponseX
            MReponseX=-0.25*dt+MReponseX
        if TimeLeft > 5:
            ChronoTime = TFont3.render(str(max(TimeLeft-(5-NumeroQuestion)*15-5,0)),False,(240,100,0))
            if Start:
                display_text(screen, str(Question[(NumeroQuestion+QuestionOffset)%8+8*math.floor(NumeroQuestion/2)]), (50,150), TFont5, (240,240,240), 280)
                display_text(screen, str(Reponse[(NumeroQuestion+QuestionOffset)%8+8*math.floor(NumeroQuestion/2)][0]), (100-32,240-10), TFont4, (240,240,240), 140)
                display_text(screen, str(Reponse[(NumeroQuestion+QuestionOffset)%8+8*math.floor(NumeroQuestion/2)][1]), (240-37,240-10), TFont4, (240,240,240), 280)
                display_text(screen, str(Reponse[(NumeroQuestion+QuestionOffset)%8+8*math.floor(NumeroQuestion/2)][2]), (100-32,288-10), TFont4, (240,240,240), 140)
                display_text(screen, str(Reponse[(NumeroQuestion+QuestionOffset)%8+8*math.floor(NumeroQuestion/2)][3]), (240-37,288-10), TFont4, (240,240,240), 280)
            QuestionText = TFont5.render(str(Question[(NumeroQuestion+QuestionOffset)%8+8*math.floor(NumeroQuestion/2)]),False,(240,240,240))
            ReponseA = TFont4.render(str(Reponse[(NumeroQuestion+QuestionOffset)%8+8*math.floor(NumeroQuestion/2)][0]),False,(240,240,240))
            ReponseB = TFont4.render(str(Reponse[(NumeroQuestion+QuestionOffset)%8+8*math.floor(NumeroQuestion/2)][1]),False,(240,240,240))
            ReponseC = TFont4.render(str(Reponse[(NumeroQuestion+QuestionOffset)%8+8*math.floor(NumeroQuestion/2)][2]),False,(240,240,240))
            ReponseD = TFont4.render(str(Reponse[(NumeroQuestion+QuestionOffset)%8+8*math.floor(NumeroQuestion/2)][3]),False,(240,240,240))
        BonneReponseText = TFont3.render("Bonne réponse",False,(0,170,0))
        MauvaiseReponseText = TFont3.render("Mauvaise réponse",False,(170,0,0))
        if Start:
            if TimeLeft < 80 and NumeroQuestion == 0:
                if Select == BonneReponse[(NumeroQuestion+QuestionOffset)%8]:
                    Score+=1
                    ScreenShake=8
                    ReponseX=0
                    subprocess.Popen(["curl", "--silent", "-o /dev/null", "http://wled.local/win&PL=4"], start_new_session=True)
                    ser.write(str.encode("/EV="+str(pipe_pick(NumeroQuestion))))
                else:
                    ScreenShake=40
                    MReponseX=0
                    subprocess.Popen(["curl", "--silent", "-o /dev/null", "http://wled.local/win&PL=5"], start_new_session=True)
                
                QuestionAsked.append((NumeroQuestion+QuestionOffset)%8)

                NumeroQuestion = 1

                trigger = True
                QuestionOffset = random.randint(8,45)

                if ((NumeroQuestion+QuestionOffset)%8) in QuestionAsked:
                    QuestionOffset += 1

            if TimeLeft < 65 and NumeroQuestion == 1:
                if Select == BonneReponse[(NumeroQuestion+QuestionOffset)%8]:
                    Score+=1
                    ScreenShake=8
                    ReponseX=0
                    subprocess.Popen(["curl", "--silent", "-o /dev/null", "http://wled.local/win&PL=4"], start_new_session=True)
                    ser.write(str.encode("/EV="+str(pipe_pick(NumeroQuestion))))
        
                else:
                    ScreenShake=40
                    MReponseX=0
                    subprocess.Popen(["curl", "--silent", "-o /dev/null", "http://wled.local/win&PL=5"], start_new_session=True)
                    
                QuestionAsked.append((NumeroQuestion+QuestionOffset)%8+8)

                NumeroQuestion = 2
                trigger = True
                QuestionOffset = random.randint(8,45)

                if ((NumeroQuestion+QuestionOffset)%8+8) in QuestionAsked:
                    QuestionOffset += 1

            if TimeLeft < 50 and NumeroQuestion == 2:
                if Select == BonneReponse[(NumeroQuestion+QuestionOffset)%8+8]:
                    Score+=1
                    ScreenShake=8
                    ReponseX=0
                    subprocess.Popen(["curl", "--silent", "-o /dev/null", "http://wled.local/win&PL=4"], start_new_session=True)
                    ser.write(str.encode("/EV="+str(pipe_pick(NumeroQuestion))))
                else:
                    ScreenShake=40
                    MReponseX=0
                    subprocess.Popen(["curl", "--silent", "-o /dev/null", "http://wled.local/win&PL=5"], start_new_session=True)
                    
                QuestionAsked.append((NumeroQuestion+QuestionOffset)%8+8)

                NumeroQuestion = 3
                trigger = True
                QuestionOffset = random.randint(0,45)

                if ((NumeroQuestion+QuestionOffset)%8+8) in QuestionAsked:
                    QuestionOffset += 1

            if TimeLeft < 35 and NumeroQuestion == 3:
                if Select == BonneReponse[(NumeroQuestion+QuestionOffset)%8+8]:
                    Score+=1
                    ScreenShake=8
                    ReponseX=0
                    subprocess.Popen(["curl", "--silent", "-o /dev/null", "http://wled.local/win&PL=4"], start_new_session=True)
                    ser.write(str.encode("/EV="+str(pipe_pick(NumeroQuestion))))
                else:
                    ScreenShake=40
                    MReponseX=0
                    subprocess.Popen(["curl", "--silent", "-o /dev/null", "http://wled.local/win&PL=5"], start_new_session=True)
                    
                QuestionAsked.append((NumeroQuestion+QuestionOffset)%8+8)

                NumeroQuestion = 4
                trigger = True
                QuestionOffset = random.randint(8,45)

                if ((NumeroQuestion+QuestionOffset)%8+2*8) in QuestionAsked:
                    QuestionOffset += 1
                
            if TimeLeft < 20 and NumeroQuestion == 4:
                if Select  == BonneReponse[(NumeroQuestion+QuestionOffset)%8+2*8]:
                    Score+=1
                    ScreenShake=8
                    ReponseX=0
                    subprocess.Popen(["curl", "--silent", "-o /dev/null", "http://wled.local/win&PL=4"], start_new_session=True)
                    ser.write(str.encode("/EV="+str(pipe_pick(NumeroQuestion))))
                else:
                    ScreenShake=40
                    MReponseX=0
                    subprocess.Popen(["curl", "--silent", "-o /dev/null", "http://wled.local/win&PL=5"], start_new_session=True)
                    
                QuestionAsked.append((NumeroQuestion+QuestionOffset)%8+2*8)

                NumeroQuestion = 5
                trigger = True
                QuestionOffset = random.randint(8,45)

                if ((NumeroQuestion+QuestionOffset)%8+2*8) in QuestionAsked:
                    QuestionOffset += 1
                
            if TimeLeft < 6 and NumeroQuestion == 5:
                 
                if Select == BonneReponse[(NumeroQuestion+QuestionOffset)%8+2*8]:
                    Score+=1
                    ScreenShake=8
                    ReponseX=0
                    subprocess.Popen(["curl", "--silent", "-o /dev/null", "http://wled.local/win&PL=4"], start_new_session=True)
                    ser.write(str.encode("/EV="+str(pipe_pick(NumeroQuestion))))
                else:
                    ScreenShake=40
                    MReponseX=0
                    subprocess.Popen(["curl", "--silent", "-o /dev/null", "http://wled.local/win&PL=5"], start_new_session=True)

                NumeroQuestion = 6
                trigger = True
                ChronoTime = TFont3.render(("0"),False,(240,100,0))
                QuestionText = TFont5.render((""),False,(240,240,240))
                ReponseA = TFont4.render((""),False,(240,240,240))
                ReponseB = TFont4.render((""),False,(240,240,240))
                ReponseC = TFont4.render((""),False,(240,240,240))
                ReponseD = TFont4.render((""),False,(240,240,240))

            if TimeLeft < 4:
                ChronoKill = TFont2.render("Score = "+str(Score),False,(240,100,0))
                screen.blit(ChronoKill,ChronoKill.get_rect(center=(160,120)))
                if TimeLeft > 3:
                    trigger = True

            if trigger and ((77 < TimeLeft <= 78) or 62 < TimeLeft <= 63 or 47 < TimeLeft <= 48 or 32 < TimeLeft <= 33 or 17 < TimeLeft <= 18 or  2 < TimeLeft <= 3):
                subprocess.Popen(["curl", "--silent", "-o /dev/null", "http://wled.local/win&PL=3"], start_new_session=True)
                trigger = False


    else:
        End=True
        AlphaE=255    
        screen.blit(ChronoKill,ChronoKill.get_rect(center=(160,120)))
        subprocess.Popen(["curl", "--silent", "-o /dev/null", "http://wled.local/win&PL=2"], start_new_session=True)


    #Title and End Vanish
    if Start:
        AlphaT-=20
    if AlphaT >=0:    
        Text1.set_alpha(AlphaT*2)
        Instruct = TFont2.render(" Pose ton gobelet",False,(240,100,0))
        Instruct2 = TFont2.render(" et maintiens les 2 boutons",False,(240,100,0))
        Instruct.set_alpha(AlphaT)
        Instruct2.set_alpha(AlphaT)
        MoyenneScore = TFont2.render("Score moyen:"+str(int(moyenne(ScoreTab)*10)/10),False,(240,100,0))
        MoyenneScore.set_alpha(AlphaT*2)
        screen.blit(MoyenneScore,MoyenneScore.get_rect(center=(160,130)))
        screen.blit(Text1,Text1.get_rect(center=(160,110)))
        screen.blit(Instruct,Instruct.get_rect(center=(160,169+2*math.sin(6*pygame.time. get_ticks()/1000))))
        screen.blit(Instruct2,Instruct2.get_rect(center=(160,185+2*math.sin(6*pygame.time. get_ticks()/1000))))
    EndTitle.set_alpha(AlphaE)

    ActualScreen.fill((0,0,0))
    ActualScreen.blit(pygame.transform.scale(screen, (ActualScreen.get_rect().width,ActualScreen.get_rect().height)), (8, 0))
    pygame.display.update()
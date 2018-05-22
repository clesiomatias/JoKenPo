# -*- coding: utf-8 -*-
from turtle import *
import time
import turtle 
import math
import random
import pygame
pygame.init()
#---------------------ATIVIDADES DE TELA INICIAL-------------------------------#
#criando a tela
tela = turtle.Screen()
tela.setup(800,800)
tela.bgcolor('black')
tela.title('Jo - Ken - Po')

#dividindo a tela no meio
caneta = turtle.Turtle()
caneta.color('white')
caneta.speed(0)
caneta.width(5)
caneta.setpos(-300,0)
caneta.fd(600)
caneta.penup()
caneta.ht()

#Criando o texto central
text = turtle.Turtle()
text.color('yellow')
text.write('ESCOLHA, PEDRA, PAPEL OU TESOURA',False,align='center',font=('Arial',22,'bold'))
text.penup()
text.setpos(0,0)
text.speed(0)
text.ht()


#----------------------FIM DAS ATIVIDADES DE TELA------------------------------#

#-----------------------CRIAÇÃO DAS IMAGENS DO JOGADOR-------------------------#

#definindo as imagens e posicionando os em campo
    #registrando as imagens
turtle.register_shape('pedra.gif')
turtle.register_shape('papel.gif')
turtle.register_shape('tesoura.gif')
    #criando as imagens
        #pedra
pedra = turtle.Turtle()
pedra.speed(0)
pedra.shape('pedra.gif')
pedra.penup()
pedra.setpos(-250,-200)

        #papel
papel = turtle.Turtle()
papel.speed(0)
papel.shape('papel.gif')
papel.penup()
papel.setpos(0,-200)

        #tesoura
tesoura = turtle.Turtle()
tesoura.speed(0)
tesoura.shape('tesoura.gif')
tesoura.penup()
tesoura.setpos(250,-200)

#-------------------FIM DAS IMAGENS DO JOGADOR--------------------------------#

#-------------------------CRIAÇÃO DOS SONS DO JOGO----------------------------#
escolhe=pygame.mixer.Sound('escolha.wav')
sor=pygame.mixer.Sound('sorteio.wav')
res=pygame.mixer.Sound('reset.wav')
vit=pygame.mixer.Sound('vitoria.wav')
der=pygame.mixer.Sound('derrota.wav')
#-------------------FIM DOS SONS DO JOGO--------------------------------------#

#----------------CRIAÇÃO DE IMAGENS DA MÁQUINA--------------------------------#
    #criando as imagens
        #pedra
mpedra = turtle.Turtle()
mpedra.speed(0)
mpedra.shape('pedra.gif')
mpedra.penup()
mpedra.setpos(-250,200)

        #papel
mpapel = turtle.Turtle()
mpapel.speed(0)
mpapel.shape('papel.gif')
mpapel.penup()
mpapel.setpos(0,200)

        #tesoura
mtesoura = turtle.Turtle()
mtesoura.speed(0)
mtesoura.shape('tesoura.gif')
mpedra.penup()
mtesoura.setpos(250,200)

#---------------------FIM DAS IMAGENS DA MAQUINA------------------------------#

#------------------CRIAÇÃO DOS COMANDOS E CONTROLES DE JOGO ------------------#
#variavel que controla se pode continuar o jogo
ingame = True
#variavel que controla sua escolha
''' 0 = inicio do jogo sem escolha
    1 = pedra escolhida
    2 = papel escolhido
    3 = tesoura escolhido    '''
escolha = 0

#criando o evento de click
    #clicando na pedra
def cpedra(x,y):
    global escolha
    escolhe.play()
    pedra.setpos(0,-100)
    papel.ht()
    tesoura.ht()
    escolha = 1
    #sorteando o jogo da maquina
    time.sleep(1)
    sortear()
    #definindo quem venceu
    venceu(sorteio,escolha)
    
    
    
    #clicando no papel
def cpapel(x,y):
    global escolha
    escolhe.play()
    papel.setpos(0,-100)
    pedra.ht()
    tesoura.ht()
    escolha = 2
    #sorteando o jogo da maquina
    time.sleep(1)
    sortear()
    #definindo quem venceu
    venceu(sorteio,escolha)
    
   
    
    #clicando na tesoura
def ctesoura(x,y):
    global escolha
    escolhe.play()
    tesoura.setpos(0,-100)
    papel.ht()
    pedra.ht()
    escolha = 3
    #sorteando o jogo da maquina
    time.sleep(1)
    sortear()
    #definindo quem venceu
    venceu(sorteio,escolha)
    
   
    

#criando processo de sorteio da opção da máquina
    #variavel de controle do sorteio
sorteio = 0
    #função que sorteia a opção
def sortear():
    global sorteio
    sorteio = random.randint(1,3)#sorteando
        #destacando figura sorteada, tal qual escolha do jogador
    if sorteio == 1:
        sor.play()
        mpedra.setpos(0,120)
        mpapel.ht()
        mtesoura.ht()
    elif sorteio ==2:
        sor.play()
        mpapel.setpos(0,120)
        mpedra.ht()
        mtesoura.ht()
    elif sorteio == 3:
        sor.play()
        mtesoura.setpos(0,120)
        mpapel.ht()
        mpedra.ht()

#resetando o jogo e reposicionando as imagens
def reset_game():
    global escolha,sorteio
    res.play()

    #resetando variavel de controle de escolha
    escolha =0
    sorteio =0
    text.clear()
    text.write('ESCOLHA, PEDRA, PAPEL OU TESOURA',False,align='center',font=('Arial',22,'bold'))
    pedra.st()
    papel.st()
    tesoura.st()
    mpedra.st()
    mpapel.st()
    mtesoura.st()
    pedra.setpos(-250,-200)
    papel.setpos(0,-200)
    tesoura.setpos(250,-200)
    mpedra.setpos(-250,200)
    mpapel.setpos(0,200)
    mtesoura.setpos(250,200)
    ingame = True
    
#definindo conexões de entrada de teclado
turtle.listen()
turtle.onkey(bye,'Escape')


#definindo ganhador
def venceu(sorteio,escolha):
    #empates
    if sorteio == 1 and escolha == 1:
            text.clear()
            text.write('EMPATE, TENTE NOVAMENTE',False,align='center',font=('Arial',22,'bold'))
            texto='JOGAR NOVAMENTE?[S/N] \nPRESSIONE ESC PRA SAIR'
            #caixa de texto para escolha de jogar novamente
            t=turtle.textinput(texto, texto)
            while t!='s' or t!='n':
                if t == 's':
                    reset_game()
                elif t=='n':
                    bye()
                    done()
                else:
                    t=turtle.textinput(texto, 'OPÇÃO INVÁLIDA!\nJOGAR NOVAMENTE?[S/N] \nPRESSIONE ESC PRA SAIR')
                    pass
            
    if sorteio == 2 and escolha == 2:
            text.clear()
            text.write('EMPATE, TENTE NOVAMENTE',False,align='center',font=('Arial',22,'bold'))
            texto='JOGAR NOVAMENTE?[S/N] \nPRESSIONE ESC PRA SAIR'
            #caixa de texto para escolha de jogar novamente
            while t!='s' or t!='n':
                if t == 's':
                    reset_game()
                elif t=='n':
                    bye()
                    done()
                else:
                    t=turtle.textinput(texto, 'OPÇÃO INVÁLIDA!\nJOGAR NOVAMENTE?[S/N] \nPRESSIONE ESC PRA SAIR')
                    pass

    if sorteio == 3 and escolha == 3:
            text.clear()
            text.write('EMPATE, TENTE NOVAMENTE',False,align='center',font=('Arial',22,'bold'))
            texto='JOGAR NOVAMENTE?[S/N] \nPRESSIONE ESC PRA SAIR'
            #caixa de texto para escolha de jogar novamente
            t=turtle.textinput(texto, texto)
            while t!='s' or t!='n':
                if t == 's':
                    reset_game()
                elif t=='n':
                    bye()
                    done()
                else:
                    t=turtle.textinput(texto, 'OPÇÃO INVÁLIDA!\nJOGAR NOVAMENTE?[S/N] \nPRESSIONE ESC PRA SAIR')
                    pass
        #vitórias do jogador
    if sorteio == 1 and escolha == 2:
            text.clear()
            text.write('PARABÉNS! VOCÊ VENCEU!',False,align='center',font=('Arial',22,'bold'))
            texto='JOGAR NOVAMENTE?[S/N] \nPRESSIONE ESC PRA SAIR'
            #caixa de texto para escolha de jogar novamente
            t=turtle.textinput(texto, texto)
            while t!='s' or t!='n':
                if t == 's':
                    reset_game()
                elif t=='n':
                    bye()
                    done()
                else:
                    t=turtle.textinput(texto, 'OPÇÃO INVÁLIDA!\nJOGAR NOVAMENTE?[S/N] \nPRESSIONE ESC PRA SAIR')
                    pass

    if sorteio == 2 and escolha == 3:
            text.clear()
            text.write('PARABÉNS! VOCÊ VENCEU!',False,align='center',font=('Arial',22,'bold'))
            texto='JOGAR NOVAMENTE?[S/N] \nPRESSIONE ESC PRA SAIR'
            #caixa de texto para escolha de jogar novamente
            t=turtle.textinput(texto, texto)
            while t!='s' or t!='n':
                if t == 's':
                    reset_game()
                elif t=='n':
                    bye()
                    done()
                else:
                    t=turtle.textinput(texto, 'OPÇÃO INVÁLIDA!\nJOGAR NOVAMENTE?[S/N] \nPRESSIONE ESC PRA SAIR')
                    pass

    if sorteio == 3 and escolha == 1:
              text.clear()
              text.write('PARABÉNS! VOCÊ VENCEU!',False,align='center',font=('Arial',22,'bold'))
              texto='JOGAR NOVAMENTE?[S/N] \nPRESSIONE ESC PRA SAIR'
              #caixa de texto para escolha de jogar novamente
              t=turtle.textinput(texto, texto)
              while t!='s' or t!='n':
                if t == 's':
                    reset_game()
                elif t=='n':
                    bye()
                    done()
                else:
                    t=turtle.textinput(texto, 'OPÇÃO INVÁLIDA!\nJOGAR NOVAMENTE?[S/N] \nPRESSIONE ESC PRA SAIR')
                    pass

        #vitórias da máquina
    if sorteio == 1 and escolha == 3:
            text.clear()
            text.write('QUE PENA, VOCÊ PERDEU!',False,align='center',font=('Arial',22,'bold'))
            texto='JOGAR NOVAMENTE?[S/N] \nPRESSIONE ESC PRA SAIR'
            #caixa de texto para escolha de jogar novamente
            t=turtle.textinput(texto, texto)
            while t!='s' or t!='n':
                if t == 's':
                    reset_game()
                elif t=='n':
                    bye()
                    done()
                else:
                    t=turtle.textinput(texto, 'OPÇÃO INVÁLIDA!\nJOGAR NOVAMENTE?[S/N] \nPRESSIONE ESC PRA SAIR')
                    pass

    if sorteio == 2 and escolha == 1:
            text.clear()
            text.write('QUE PENA, VOCÊ PERDEU!!',False,align='center',font=('Arial',22,'bold'))
            texto='JOGAR NOVAMENTE?[S/N] \nPRESSIONE ESC PRA SAIR'
            #caixa de texto para escolha de jogar novamente
            t=turtle.textinput(texto, texto)
            while t!='s' or t!='n':
                if t == 's':
                    reset_game()
                elif t=='n':
                    bye()
                    done()
                else:
                    t=turtle.textinput(texto, 'OPÇÃO INVÁLIDA!\nJOGAR NOVAMENTE?[S/N] \nPRESSIONE ESC PRA SAIR')
                    pass

    if sorteio == 3 and escolha == 2:
            text.clear()
            text.write('QUE PENA, VOCÊ PERDEU!!',False,align='center',font=('Arial',22,'bold'))
            texto='JOGAR NOVAMENTE?[S/N] \nPRESSIONE ESC PRA SAIR'
            #caixa de texto para escolha de jogar novamente
            t=turtle.textinput(texto, texto)
            while t!='s' or t!='n':
                if t == 's':
                    reset_game()
                elif t=='n':
                    bye()
                    done()
                else:
                    t=turtle.textinput(texto, 'OPÇÃO INVÁLIDA!\nJOGAR NOVAMENTE?[S/N] \nPRESSIONE ESC PRA SAIR')
                    pass
#--------------------FIM DOS COMANDOS E CONTROLES DO JOGO----------------------#

#---------------------------LOOP DO JOGO (MAINLOOP)----------------------------#
while True:
    if ingame:
        #colocando os eventos e click pra funcionar
        if pedra.onclick(cpedra):
            #definindo quem venceu
            venceu(sorteio,escolha)
            
        
        if papel.onclick(cpapel):
            #definindo quem venceu
            venceu(sorteio,escolha)
        
        if tesoura.onclick(ctesoura):
            #definindo quem venceu
            venceu(sorteio,escolha)
        
    
    
    
       



import random


d6 = [1,2,3,4,5,6] 
d10 =[1,2,3,4,5,6,7,8,9,10]
 #FUNÇÃO DECLARADA
def reroll_dice(): 
 #INPUT PARA VERIFICAR SE QUER GIRAR O DADO
  girar_dado = input("Você deseja rolar um D6 ? :(sim) ou (não) ") # 1
 #TRANSFORMANDO A STRING EM MINUSCULA PARA CASO A PESSOA ESCREVA (SIM,Sim)
  girar_dado.lower 
 
  x = "sim" in girar_dado
  #ALEATORIZANDO A LISTA D6
  if x == True:
    dado_girado = random.choice(d6)
        
    print(dado_girado)
  else:
    print('gira logo esse dado rapaz')
  #CHAMAR NOVAMENTE APÓS O AVISO
    reroll_dice()
  #VERIFICAÇÃO PARA ACERTO
  if dado_girado == 1:
    print ("você errou") 
  elif dado_girado == 2:
    print ("você acertou de raspão")
  else: 
    print ("você acertou em cheio")

  #CONSTATAÇÃO DE ACERTO E INPUT PARA LISTA [D10]
  if dado_girado ==1:
     print("que cara azarado meu deus") 
  elif dado_girado == 2:
     print ("de raspão não da dano ne pai")
  else :
     girar_d10 = input("quer girar um d10 de dano ? (yeap) ou (not) : ")
     girar_d10.lower
     y = "yeap" in girar_d10
     #ALEATORIZAR D10 CASO YEAP SEJA CONSTATADO
     if y == True:
       d10_girado = random.choice(d10)
       print (F"você tirou {d10_girado} nos dados") 
     else:
      print ("então não vai ter dano ne")
      
      print(F"o monstro recebeu {d10_girado} de dano")


  if d10_girado >=8 and dado_girado >=3:
    print("você matou o monstro")
    
      
  reroll_dice()
  #CHAMANDO PARA SE MANTER INFINITO
reroll_dice()
reroll_dice()
from tkinter import *
from datetime import date
import datetime


print()
print(datetime.datetime.now())


print()
print('Olá')
texto ='Bem vindo vamos responder algumas perguntas ;-) '
texto=texto.upper()
print()
print(texto)
print()
print ('Como você chama  ? ')
print()
nome= str(input(''))
nome=nome.upper() 
print(f'olá tudo bem    { nome }   ? ')
print() 

continuar=True

while continuar:
    print()
    print()
    resposta = input('Como você está se sentido hoje ? "bem ou mal". ')
    print()
    print()
    if resposta.lower()=='mal':
        print()
        print('Sinto muito em ouvie isso. ')
        
    elif resposta.lower()=='bem':
        print()
        print('Que otimo, fico feliz')
        
    else:
        print('Desculpe, não entendi aresposta. Por favor,responda apenas "bem ou mal". ')
        continue
    
    resposta_continuar= input('Deseja continuar (sim/não):')
    
    if resposta_continuar.lower()=='não':
        continuar=False
ano_nascimento= int(input('  Digite seu ano de nascimento '  ))    
idade = 2023 - ano_nascimento 
print() 
print(f'Sua idade é de { idade } anos.')
print()       

if idade < 30:
    print()
    print('Nossa como você está jovem.   :-) ')
    print()
elif idade > 30:
    print()
    print('Ops... Ta ficando velho. :->')
    print()
    
imc = input ('Voce gostaria de saber se sua massa corporal IMC está bem  sim ou não ?   ' )
imc=imc.upper()
print('')
print('OK vamos comerçar')
print('')
altura = float(input('qual é a sua Altura em cm :  '))
peso = float(input('Qual é seu peso em Kg:' ))

IMC = peso / (altura/100)** 2
print('')
print('')
if IMC < 18.5:
 print('Seu IMC é-- MUITO MAGRO')
elif IMC  >= 18.5 and IMC < 24.9:
  print('Seu IMC é --NORMAL--')
elif IMC  >= 25.0 and IMC < 29.9:
  print('Seu IMC é --SOBREPESO--') 
elif IMC  >= 30.0 and IMC < 39.9:
  print('Seu IMC é --OBESIDADE--')
  print() 
else:
  print('--OBESIDADE GRAVE--')
  print('')  
  print('')  
    
cidade=input('Vamos agora saber em que cidade você nasceu  ?  '  )
cidade=cidade.upper()
print() 
print( 'O (a) ' + nome  +  ' tem '  +  str(idade)  + ' anos '  ' e '  ' mora em '  +  cidade  +  '.')
print()
print(' Até logo !!!')  











 
    
           


   

    
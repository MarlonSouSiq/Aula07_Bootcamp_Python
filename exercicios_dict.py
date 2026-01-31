import os
from datetime import datetime
import random
import time

os.system("cls")

# pessoas={'nome':'Gustavo','Sexo': 'M','idade': 22}
# print(pessoas['idade'])   # mostra o valor 
# print(*pessoas.keys())  # sem o dict....
# print(pessoas.values())
# print(pessoas.items())
# pessoas['nome']='Marcelo'
# print(pessoas.items())
# pessoas['peso']= '200kg'

# print(pessoas.items())

# #for k,v pessoas.items():
'''
Docstring for exercicios_dict : lista com dicionario
'''
# 
# estado=dict()
# brasil=list()
# for c in range(0,3):
#     estado['uf'] = input(f'Entre com un estado: ')
#     estado['sigla']=input(f'Entre com a sigla: ')
#     brasil.append(estado.copy())
   
# # print(brasil)
# # for e in brasil:
# #     print(e)

# for e in brasil:
#     for k,v in e.items():
#         print(f'O campo {k} tem valor {v}')

'''
Pergunta nome
pergunta nota
situação > 7 Aprovado

'''
# dict={}

# dict['key']=input("Entre com o seu nome: ")
# dict['values']=float(input("Entre com a sua nota: "))
# if dict['values'] > 7:
#     print(" Aprovado")
# else:
#     print('Reprovado')

'''
gera valores aleatorios de 1 a 6 , 
atribui cada resultado a um jogador
colocar na oredm de vencedores.

'''

# import random
# dict={}
# for x in range(1,6):
#     dado=random.randint(1,6)
#     print(f'Jogador: {x} -- Resultado:  {dado}')
#     dict["Jogador " + str(x)]=dado

# print(dict)
# tupla=dict.items()
# ordenada=sorted(tupla, key=lambda item:item[1],reverse=True)
# print(ordenada)

# cont=1
# for k,v  in ordenada:
#     print(f' O {cont} lugar foi {k} com valor: {v}')
#     cont+=1



'''
Leia nome, ano de nascimento, carteira de trabalho, contratação, 
quando vai aposentar: 35 anos
cadastrar em um dicionario
se não tiver carteira de trabalho, não calcular aposentadoria
'''
# dict={}

# nome=input("Digite o seu nome: ")
# ano_nasc=int(input("Digite o seu ano de nascimento: "))
# carteira=input("Digite o némero da carteira:")
# if carteira=="" or 0:
#     carteira= 0
# ano_contrato=int(input("Digite o ano da contratação"))
# tempo=35-(datetime.now().year - ano_contrato)
# tempo_para_aposentar=0
# if 0 < tempo < 35:
#     tempo_para_aposentar==tempo
# elif tempo < 0:
#     tempo_para_aposentar==0


# dict['nome']=nome
# dict['Nascimento']=ano_nasc
# dict['Carteira']= carteira
# dict['Contrato']=ano_contrato
# dict['Tempo_para_aposentar']=tempo_para_aposentar

# print("-="*60)
# print("   Resumo  do Funcionario")
# print(dict)

# for v,k in dict.items():
#     print(v)










'''
Pergunta nome do jogador
quantas partidas jogou
quantos gols em cad partida
resultado: quantos gols no total

'''

'''
Digita o nome
Digita o sexo M/F
Digita Idade

quer continuar S/N

RESUMO:
O grupo tem x pessoas
A media da idade é
As mulheres cadastradas são:
Os Homens cdatrados são:
As pessoas que estão com idade acima d a media

'''
grupo={}
lista_grupo=[]

while True:
    while True:
        nome=input('Digite o nome: ')
        if nome=="":
            print("Não digitou seu nome")
            time.sleep(2)
        else:
            break
    while True:
        sexo=input('Digite o sexo [M/F]: ')
        sexook=sexo.upper()
        if (sexook=="") or ((sexook!="M") and (sexook!="F")):
            print("Não digitou seu sexo")
            time.sleep(2)
        else:
            break

    while True:
        idade=input('Digite a idade: ')
        if not idade.isdigit():
            print("Não digitou idade")
            time.sleep(2)
        else:
            idade=int(idade)
            break

    grupo['nome']=nome
    grupo['sexo']=sexo
    grupo['idade']=idade

   # brasil.append(estado.copy())
    lista_grupo.append(grupo.copy())  ######## IMPORTANTE .COPY, SE NÃO COPIA SEMPR MESMA DICT  

    print(lista_grupo)

    continuar=input("Quer Continuar cadastro? Digite S para continuar: ")
    if continuar ==  "S" or continuar=="s":
        os.system("cls")
    else:
        break    
        
total_idade=0
for dict in lista_grupo:
    total_idade += dict['idade']
media=total_idade/len(lista_grupo)

lista_f=[]
for pessoa in lista_grupo:
    if pessoa['sexo']=='F':
        lista_f.append(pessoa['nome'])

lista_m=[]
for pessoa in lista_grupo:
    if pessoa['sexo']=='M':
        lista_m.append(pessoa['nome'])
   
#print(f' O total de mulheres cadastradas é: {len(lista_f)} sendo elas : {lista_f}')
print(f'O total de mulheres cadastradas : {len(lista_f)} sendo elas: {", ".join(lista_f)}')  # .join... para não aparecer oc []
print(f'O total de homens cadastrados : {len(lista_m)} sendo elas: {", ".join(lista_m)}')  # .join... para não aparecer oc []



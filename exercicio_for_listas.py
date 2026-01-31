'''
Valoes unicos em uma lista
'''

import os

os.system("cls")

# texto=" A televisao azul estava passando filme azul e vermelho"
# lista=texto.split()
# print(lista)

# total={}

# for item in lista:
#     if item in total:
#         total[item]+= 1
#     else:
#         total[item]=1

# print(total)


'''
Em uma lista, pode-se ter a posição  e o valor.
'''
# valores=[5,9,4]
# for c,v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}')


#Pega 5 valores numericos, e define o maior e menor com as suas posições.

# lista=[]
# for x in range(5):
#     lista.append(int(input(f"Entre com o número {x} :")))
# maior=max(lista)
# menor=min(lista)

# pos_maior=[]
# pos_menor=[]
# for pos,item  in enumerate(lista):
#     if item == maior:
#         pos_maior.append(pos)

#     elif item==menor:
#         pos_menor.append(pos)

# print(f'O maior valor da lista é {maior} na posição {pos_maior} '
#       f'e o menor valor na lista é {menor} na posição {pos_menor}')
# print(lista)

#######################################################################
    #   pede para digitar um valor
    # pergunta se quer digitar outro sim ou não4
    # não pode repetir
    # se sim acrescenta
    # não , finaliza e mostra os valores em ordem crescente


# lista=[]
# while True:
#     try:
#         valor=input("Digite um valor: ")
#         if "." in valor or "," in valor:  # no python não pode tester . e , ao  mesmo tempo
#             valorok=float(valor.replace(",","."))
#         else:
#             valorok=int(valor)
#         if isinstance(valorok,(float,int)) and valorok not in lista:
#             lista.append(valorok)
#         else:
#             print("Valor repetido. Não será incluido")
#     except:  
#         print("Valor digitado não é um número")
    
#     continuar = input("Quer continuar? Digite  S para continuar ")
#     if (continuar.upper() != "S"):
#         break

# lista.sort()

# print(*lista)

##################################################################################
'''
pedir p digitar 5 numeros
posicionar o numero na lista sem usar sort
'''

def pos_lista(listax:list,valor:int):
    listax.append(valor)
    tamanho_lista=len(listax)
    lista_crescente=[]
    for cont in range(tamanho_lista):
        lista_crescente.append(min(listax))
        listax.remove(min(listax))
    posicao_valor= lista_crescente.index(valor)
    return posicao_valor,lista_crescente


lista=[]   
for x in range(5):
    
    valor= int(input(f'Entre com o número {x+1}: '))
    if x== 0:
        print(f"Valor {valor} foi inserido na lista vazia")
        lista.append(valor)
    else:
        posicao,lista_res = pos_lista(lista,valor)
        lista=lista_res
        print(f' O valor {valor} foi inserido na posição {posicao}')
        print(lista)
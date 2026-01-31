import os

# utilzando o type hint
"""
Uma função para somar  --doc string
"""

# def soma(valor_1: float, valor_2: float) -> float:
#     valor_3 = valor_1 + valor_2
#     return valor_3

#Calcular Média de Valores em uma Lista
# def medialista(lista: list[float]) -> float:
#     media=sum(lista)/len(lista)
#     return(media)

# med= medialista([2,5,6,8,9])
# print(med)


######## Filtrar Dados Acima de um Limite

# def filtravaloresacima(Lista: list[float], limite: int)  -> list:
#     resposta=[]
#     for item in Lista:
#         if item > limite:
#             resposta.append(item)
#     return resposta

# listavalores=[2,10,0.2,5]
# print(filtravaloresacima(listavalores,2))


#### Contar valores em uma lista  - versão com for

# os.system("cls")

# def contavalores(lista: list) -> dict:
#     resposta={}
        
#     for item in lista:
#         if item in resposta:
 #            resposta[item] += 1
#         else:
#             resposta[item]=1

#     return resposta
 
# lista=[1,2,3,2,4,3,2,2,2]
# contagem = contavalores(lista)
# print(contagem)

########## contar valores com counter
# from collections import Counter
# lista = [1, 2, 3, 2, 4, 3, 2, 2, 2]
# contagem = Counter(lista)
# print(contagem)

############# valores unicos em uma lista.

os.system("cls")

def valor_unico(lista: list) -> list:
    resposta={}
    for item in lista:
        if item in resposta:
            resposta[item] += 1
        else:    
            resposta[item]=1
    unicos=[]      
    for chave,valor in resposta.items():
        if valor == 1:
            unicos.append(chave)
    return unicos


lista=[1, 2, 3, 2, 4, 3, 2, 2, 2]
print(valor_unico(lista))

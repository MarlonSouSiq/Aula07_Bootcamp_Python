# #Calcular Média de Valores em uma Lista
# total: int =0
# lista=[2,4,6,8]
# for x in lista:
#     total += x
# media=total/len(lista)
# print(media)

# #Filtrar Dados Acima de um Limite

# lista=[2,6,25,10,44,20]
# resultado=[]
# limite=10
# for item in lista:
#     if item > limite:
#         resultado.append(item)
# print(resultado)

#Contar Valores Únicos em uma Lista

lista=[2,6,25,10,44,10,6,20]
dict={}

for item in lista:
    if item in dict:
        dict[item] += 1

    else:
        dict[item]=1
print(dict)

lista_dos_unitarios=[]
for k,v  in dict.items():
    if v==1:
        lista_dos_unitarios.append(k)

print(lista_dos_unitarios)
import csv
import os

path_arquivo="vendas.csv"
os.system("cls")

def ler_csv(nome_do_arquivo_csv: str) -> list[dict]:
    """
    Docstring for Ler_csv
    Função que le um rquivo CSV e retorna uma lista de dicionarios
    """
    lista=[]
    with open(nome_do_arquivo_csv, mode="r", encoding='utf-8') as arquivo:
        leitor= csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista

def filtrar_produtos_nao_entregues(lista:list[dict]) -> list[dict]:
    lista_produtos_filtrados=[]
    for produto in lista:
        if produto.get("entregue") == "True":
            lista_produtos_filtrados.append(produto)
    return lista_produtos_filtrados



def somar_valores_dos_produtos_filtrados(lista_com_valores_filtrados: list[dict])  -> int:
    valor_total=0
    for produto in lista_com_valores_filtrados:
        valor_total += int(produto["price"])
    return valor_total



"""
Python scripts supporting monitory of students.

Ⓒ 2022 - VNET :: Vida Nova Escola de Tecnologia
"""

"""
Este site possui um compilado de todas as palavras do português brasileiro (ou, pelo menos, é o que eles dizem). Minha sugestão é baixar o arquivo 

br-utf8.txt, mas podem optar pelo que remove todos os caracteres especiais das palavras


https://www.ime.usp.br/~pf/dicios/


Faça o download e salve seu conteúdo num arquivo chamado “palavras.txt”.

Faça uma função para cada item abaixo:
    Conte quantas palavras há no arquivo
    Conte quantas vezes cada letra do alfabeto aparece no arquivo
    Conte quantas palavras começam com cada letra do alfabeto
    Identifique as palavras começam com as mesmas 3 letras do seu nome e salve-as num arquivo separado
    Identifique as palavras que possuem todas as letras do seu nome e salve-as num arquivo separado
    Identifique todas as palavras que são palíndromos e salve-as num arquivo separado
"""

lista_palavras = []
with open("br-utf8.txt", "r", encoding="utf-8") as arquivo_portugues:
    for linha in arquivo_portugues:
        lista_palavras.append(linha.upper())


"""
Conte quantas palavras há no arquivo
"""
def conta_palavras(lista_palavras):     # assinatura da funcao que recebe um parametro do tipo lista
    return len(lista_palavras)

contagem_palavras = conta_palavras(lista_palavras)      # chamada da funcao
print(f"O Total de palavras eh: {contagem_palavras}")


"""
Conte quantas vezes cada letra do alfabeto aparece no arquivo
"""
def conta_letras(lista_palavras):
    dicionario_acumula = {}
    # dicionario_acumula {
    #   'A':1213,
    #   'B':3245435,
    #   ...
    # }
    for palavra in lista_palavras:
        # palavra = 'ABELARDO'
        lista_letras = list(palavra)
        # lista_letras = ['A','B','E','L','A','R','D','O']
        for letra in lista_letras:
            # letra = 'A'
            if letra not in dicionario_acumula:
                dicionario_acumula[letra] = 1
                # dicionario_acumula {
                #   'A':1
                # }
            else:
                dicionario_acumula[letra] += 1
                # dicionario_acumula {
                #   'A':2
                # }
    return dicionario_acumula

contagem_letras = conta_letras(lista_palavras)      # chamada da funcao
print("O acumulado de aparicoes por letra eh:")
print(contagem_letras)


"""
Conte quantas palavras começam com cada letra do alfabeto
"""
def conta_inicio_palavra(lista_palavras):
    dicionario_acumula = {}
    for palavra in lista_palavras:
        if palavra[0] not in dicionario_acumula:
            dicionario_acumula[palavra[0]] = 1
        else:
            dicionario_acumula[palavra[0]] += 1
    return dicionario_acumula

contagem_inicia_palavra = conta_inicio_palavra(lista_palavras)      # chamada da funcao
print("O acumulado de palavras iniciadas por cada letra eh:")
print(contagem_inicia_palavra)


"""
Identifique as palavras começam com as mesmas 3 letras do seu nome e salve-as num arquivo separado
"""
# dica! 
# >>> texto="ABCDEFG"
# >>> texto
# 'ABCDEFG'
# >>> texto[:3]
# 'ABC'
def conta_palavra_tres_letras(lista_palavras, inicias_nome):
    with open("arquivos_iniciam_tres_letras.txt", "a", encoding="utf-8") as arquivo_escrita:
        for palavra in lista_palavras:
            if palavra[:3] == inicias_nome:
                arquivo_escrita.write(palavra)

conta_palavra_tres_letras(lista_palavras, inicias_nome="DOU")        # DOUGLAS


"""
Identifique as palavras que possuem todas as letras do seu nome e salve-as num arquivo separado
"""
# TODO


"""
Identifique todas as palavras que são palíndromos e salve-as num arquivo separado
"""
# TODO

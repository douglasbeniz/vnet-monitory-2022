"""
Python scripts supporting monitory of students.

Ⓒ 2022 - VNET :: Vida Nova Escola de Tecnologia
"""

# ------------------------------------------------------------------------------
# Listas
# ------------------------------------------------------------------------------
minha_lista_vazia = []                      # lista nao inicializada
minha_lista = ["Banana","Abacaxi","Pera"]   # lista inicializada com alguns itens

print(" LISTA ".center(80, '='))
print(f"minha_lista_vazia antes: {minha_lista_vazia}")
print(f"type(minha_lista_vazia): {type(minha_lista_vazia)}")

for item in minha_lista:
    print(f"Item da lista: {item}")
    minha_lista_vazia.append(item)

print(f"minha_lista_vazia depois: {minha_lista_vazia}")

# ------------------------------------------------------------------------------
# Dicionarios
# ------------------------------------------------------------------------------
meu_dict_vazio = {}                     # dicionario de dados nao inicializado
meu_dict = {'chave-1':10,'chave-2':20}  # cada item em um dicionario eh definido 'CHAVE':VALOR (ou 'KEY':VALUE, ingles)

print(" DICIONARIO ".center(80, '='))
print(f"meu_dict_vazio antes: {meu_dict_vazio}")
print(f"type(meu_dict_vazio): {type(meu_dict_vazio)}")

for chave_item, valor_item in meu_dict.items():     # nao eh possivel iterar sobre itens como na lista!
    print(f"Chave: {chave_item}, valor: {valor_item}")
    meu_dict_vazio[chave_item] = valor_item         # associacao de valores a cada chave diferente da lista tambem!

print(f"meu_dict_vazio depois: {meu_dict_vazio}")

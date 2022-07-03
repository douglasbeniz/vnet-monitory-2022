"""
Python scripts supporting monitory of students.

Ⓒ 2022 - VNET :: Vida Nova Escola de Tecnologia
"""

valorEntrada = input("Digite valores separados por virgula ',': ")
print(valorEntrada)

# Separando itens da entrada por ',' em uma lista
minhaLista = valorEntrada.split(',')
# equivalente a utilizar dessa forma com atribuicao explicita do parametro "sep" ("separator", separador):
#   minhaLista = valoreEntrada.split(sep=',')

print(minhaLista)

for item in minhaLista:
    print(f"Um item da lista eh: {item}")

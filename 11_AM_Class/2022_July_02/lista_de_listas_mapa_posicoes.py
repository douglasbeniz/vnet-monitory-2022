"""
Python scripts supporting monitory of students.

Ⓒ 2022 - VNET :: Vida Nova Escola de Tecnologia
"""

# ------------------------------------------------------------------------------
# Espaco de declaracoes de variaveis de uso comun
# ------------------------------------------------------------------------------
global cabecalhoMapa
cabecalhoMapa='abcdefghijklmnopqrstuvwxyz'.upper()      # 26 itens

# ------------------------------------------------------------------------------
# Espaco de declaracoes de funcoes de uso comun
# ------------------------------------------------------------------------------
def mostraMapaSalao(colunas, mapaSalao):
    global cabecalhoMapa

    # ------------------------------------------------------------------------------
    # Exibindo como esta o salao, mapa
    # ------------------------------------------------------------------------------
    print("\nmapa atual do salao".title())

    # cabecalho (header)
    print('  ',end='')    # espaco que sera usado para indices das fileiras
    for coluna in range(colunas):
        print(f' {cabecalhoMapa[coluna]} ',end='')
    print() # proxima linha
    indice = 1

    # ocupacao do mapa ('_' significa "livre")
    for fila in mapaSalao:
        print(f'{indice}:',end='')
        for posicaoItem in fila:        # iterando itens de uma coluna (dentro da fila)
            print(f' {posicaoItem} ',end='')
        indice += 1
        print() # proxima linha


# ------------------------------------------------------------------------------
# Inicio do programa e solicitacao de entradas do usuario
# ------------------------------------------------------------------------------
print("\nespaco de convencoes vida nova escola de technologia\n".title())

print("vamos preparar o salao?\n".title())

fileiras = int(input("por favor, informe quantas fileiras de cadeiras existem:".title()))
colunas = int(input("agora informe quantas colunas de cadeiras existem:".title()))

# ------------------------------------------------------------------------------
# Declaracao da lista de listas (matriz) que sera usapara para criar o mapa
#   do salao
# ------------------------------------------------------------------------------
mapaSalao = [['_']*colunas for _ in range(fileiras)]    # sera nossa lista de listas (ou matriz), organizada em: 1.a dimensao = filas; 2.a dimensao = colunas

# perceba que essa linha acima eh equivalente a inicializar a matriz (lista de listas) desta forma:
# e.g.:
# ------------------------------------------------------------------------------
#  mapaSalao = []
#  for fila in range(fileiras):
#    listaAuxiliar=[]
#    for coluna in range(colunas):
#      listaAuxiliar.append('_')
#    mapaSalao.append(listaAuxiliar)
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Exibe mapa do salao atual
# ------------------------------------------------------------------------------
mostraMapaSalao(colunas, mapaSalao)

# ------------------------------------------------------------------------------
# Pergunta ao usuario qual posicao deseja marcar como ocupada
# ------------------------------------------------------------------------------
while True:
    print('\ndeseja marcar uma posicao como ocupada?\n'.title())
    # Fileira
    filaOcupada = input("qual a fileira (numeros), ou <0> (ZERO) para encerrar: ".title())
    if filaOcupada == str(0):
        break
    else:
        filaOcupada = int(filaOcupada)
        if filaOcupada > fileiras:
            print (f"Fileira {filaOcupada} inexistente. Escolha outra, por favor")
            continue    # repetir o loop (while)
    # Coluna
    colunaOcupada = input("qual a coluna (letras), ou <0> (ZERO) para encerrar: ".title())
    if colunaOcupada == str(0):
        break
    else:
        colunaOcupadaIdx = cabecalhoMapa.find(colunaOcupada.upper())
        if colunaOcupadaIdx == -1 or colunaOcupadaIdx +1 > colunas:
            print (f"Coluna {colunaOcupada.upper()} inexistente. Escolha outra, por favor")
            continue    # repetir o loop (while)

    # Marca ludar caso disponivel
    if mapaSalao[filaOcupada -1][colunaOcupadaIdx] == "_":    # posicao livre
        mapaSalao[filaOcupada -1][colunaOcupadaIdx] = 'X'
        if not any("_" in sublist for sublist in mapaSalao):     # nao ha assentos livres
            # consulte a documentacao da funcao 'any()'
            #   https://docs.python.org/pt-br/3/library/functions.html#any
            # consulte "list comprehension" (compreensao de listas) na documentacao, uso do <chave_busca> in <sub-lista> for <sub-lista> in <list>
            #   https://docs.python.org/pt-br/3/tutorial/datastructures.html#nested-list-comprehensions
            mostraMapaSalao(colunas, mapaSalao)
            print (f"Salao lotado!")
            break   # interrompe a repeticao (while)
    else:   # assento ocupado ou fora da lista
        print (f"Posicao '{filaOcupada}-{colunaOcupada.upper()}' ja reservada. Escolha outra, por favor!")
        continue    # repetir o loop (while)

    mostraMapaSalao(colunas, mapaSalao)

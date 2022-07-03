"""
Python scripts supporting monitory of students.

Ⓒ 2022 - VNET :: Vida Nova Escola de Tecnologia
"""

# Dados persistentes; i.e. salvo no HD (hard disk); memoria principal;
#  arquivo texto (.txt)) no mesmo diretório do script Python (.py), o programa
# Modos de abertura:
#  > w = write (escrever)
#  > r = read (leitura)
#  > a = append (concatenar)
try:
    arquivo = open("meu_arquivo.txt","r")
    # arquivo eh variavel to tipo TextIOWrapper +/- "involucro de Entrada/Saida de
    #  texto"
    #IO = Input/Output

    for linha in arquivo:
        if 'a' in linha:    # apenas para mostrar que podem processar as linhas como "lista de caracteres"
            print(f'a está na linha:{linha}',end='')
        else:
            print(linha,end='')

    arquivo.close()
except FileNotFoundError:
    print("Arquivo nao encontrado!")
    exit()


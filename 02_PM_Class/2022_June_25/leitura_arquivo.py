"""
Python scripts supporting monitory of students.

Ⓒ 2022 - VNET :: Vida Nova Escola de Tecnologia
"""

# Dados persistentes; i.e. salvo no HD (hard disk); memoria secundaria;
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


# Equivalente a utilizar o 'with .. as ..:'
#   porem com with nao eh preciso se preocupar em fechar o arquivo
#
# with <objeto> as <variavel>
with open("meu_arquivo.txt","r") as meuArquivo:
    for line in meuArquivo:
        print(line)

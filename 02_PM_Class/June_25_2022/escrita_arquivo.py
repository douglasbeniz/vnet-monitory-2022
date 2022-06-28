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
arquivo = open("meu_arquivo.txt","a")
# arquivo eh variavel to tipo TextIOWrapper +/- "involucro de Entrada/Saida de
#  texto"
#IO = Input/Output


# Muito CUIDADO com repeticoes infinitas (infinite looping)! Aqui para uso
#   didatico;
# Caso nao haja comando de pausa (e.g.: timer.sleep(SECONDS))
#   nem condicao de saida, para interromper o loop (e.g.: usando break)
#   o computador pode ate travar;
while True:
    palavra = input("Digite uma palavra para adicionar ao arquivo\nEnter para finalizar:")

    if not palavra:
        break

    arquivo.write(palavra)
    arquivo.write('\n')

    arquivo.flush()

arquivo.close()


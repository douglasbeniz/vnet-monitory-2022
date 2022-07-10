"""
Python scripts supporting monitory of students.

Ⓒ 2022 - VNET :: Vida Nova Escola de Tecnologia
"""

# Tratamento de excecao
#  try:
#       pass    # seu codigo/sua logica
#  except:
#       pass    # o que fazer caso uma excecao aconteca (que interromperia o seu programa)

while True:         # repetir "enquanto for verdadeiro" (sempre, caso não haha condicao de saida, "break", por isso cuidado!)
    try:
        entrada = int(input("Digite um valor: "))      # espera um "int" (numero/inteiro); condicao de pausa na execucao aguardando entrada do usuario
        if (entrada < 0):       # apenas para demonstrar como seria "levantar", ou gerar/forcar, uma excecao, neste caso nao tratada
            raise Exception("Valores negativos nao permitidos!")
        else:
            break   # interrompe a repeticao (while)
    except ValueError:      # tratamento de uma excecao especifica, evitando interrupcao abrupta da execucao, quando o usuario nao digitou um numero e que a classe "int()" nao aceita
        print("Valor invalido, por favor tente novamente...")

print(f"Voce digigou: {entrada}")  # apenas exibindo o que recebei do usuario no "input"


if entrada > 100:
    raise Exception("Valor nao permitido, maior do que 100!")

print("Fim do programa")
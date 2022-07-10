"""
Python scripts supporting monitory of students.

Ⓒ 2022 - VNET :: Vida Nova Escola de Tecnologia
"""

# ------------------------------------------------------------------------------
# Esta eh uma versao modificada a partir da proposta da nossa colega Fabiana
#   trabalhada durante a monitoria.
# 
# Momento no qual algumas ideas e propostas de melhorias foram feitas e
#   discutidas em grupo.
#
# Versoes originais para solucionar o exercicio proposto sao estimuladas, mas
#   partes do que se fez aqui podem ser uteis a quem esta com dificuldades.
#
# Assistam ao video da discussao e procure o monitor para tirar duvidas se 
#   necessario!
#
# Boas praticas!
# ------------------------------------------------------------------------------

def recebeEntradaInteiro(orientacaoUsuario):
    while True:
        entrada = input(f"{orientacaoUsuario}")
        if (not entrada.isdecimal()):       # objetos/instancias da classe "str" possuem metodos para verificar o tipo de informacao contida
            # e.g. (exemplo):
            #   <str>.isdecimal()   # is = "eh" decimal (numero inteiro de base 10)
            #   <str>.isalnum()     # is alpha-numeric (letras e numeros)
            #   <str>.isalpha()     # is alphabetic (letras do alfabeto)
            # consulte a pagina oficial do Python para mais informacoes:
            #   https://docs.python.org/pt-br/3/library/stdtypes.html
            print("Por favor informe apenas numeros!")
        else:
            break
    return entrada  # funcao retorna a entrada digitada pelo usuario, guarantindo ser um numero inteiro

def mostraOcupacaoCinema(vetor):
    print("Ocupacao atual do cinema")
    numero_assento = 1
    for situacao in vetor:
        print(f"Assento {numero_assento}: {situacao} ")
        numero_assento = numero_assento +1

print("\n CINEMA VIDA NOVA \n")

lugares = recebeEntradaInteiro("Digite o numero total de assentos disponiveis: ")
lugares = int(lugares)

vetorLugares = ["-"]*lugares

mostraOcupacaoCinema(vetorLugares)

while True:
    assento = recebeEntradaInteiro("Informe o assento desejado, ou '0' (ZERO) para sair: ")
    if assento == str(0):
        break
    else:
        assento = int(assento)

    if assento > len(vetorLugares):  # assento fora da lista
        print (f"Assento {assento} inexistente. Escolha outro lugar")   # exibe posicao do assento ajustada para mundo "normal", {assento+1} (lista inicia em 1 para o usuario)
        continue    # repetir o loop (while)
    elif vetorLugares[assento -1] == "-":    # assento livre
        # Note o ajuste, [assento -1] entre a posicao informada pelo usuario (comecando em 1) e os indices de lista no Python (comecando em 0)
        vetorLugares[assento -1] = 'Reservado'
        if "-" not in vetorLugares:     # nao ha assentos livres
            mostraOcupacaoCinema(vetorLugares)
            print ("Cinema lotado!")
            break   # interrompe a repeticao (while)
    else:   # assento ocupado ou fora da lista
        print (f"Assento {assento} reservado. Escolha outro lugar")
        continue    # repetir o loop (while)

    mostraOcupacaoCinema(vetorLugares)

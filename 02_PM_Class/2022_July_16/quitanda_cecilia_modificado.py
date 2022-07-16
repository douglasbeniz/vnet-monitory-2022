"""
Python scripts supporting monitory of students.

Ⓒ 2022 - VNET :: Vida Nova Escola de Tecnologia
"""

"""
Obrigado à Cecilia Rosa por compartilhar seu código durante a monitoria

Esta versao é uma sugestao de melhorias... existem outras possíveis!

Não copie por copiar... saiba o que está fazendo, pergunto do contrário,
e principalmente, consulte a Cecilia antes de utilizar partes do código dela!
"""

global lista_valor_total
lista_valor_total = []      # valor total da compra do usuario

global lista_fruta
lista_fruta = []            # todas as frutas desta compra

#Lista das frutas disponiveis na quitanda e indice
global quitanda_fruta
quitanda_fruta = {
    "1": "Laranja",
    "2": "Melancia",
    "3": "Banana",
    "4": "Morango",
}      

#Valor das frutas de acordo com o indice das frutas
global quitanda_valor
quitanda_valor = {
    "1" : 2,
    "2" : 10,
    "3" : 5,
    "4" : 3,
}

#Quantidade das frutas de acordo com o indice das frutas
global quitanda_qnt
quitanda_qnt = {
    "1" : 15,
    "2" : 5,
    "3" : 5,
    "4" : 25,
}

def quitanda():
    global lista_valor_total
    global lista_fruta
    global quitanda_fruta
    global quitanda_valor
    global quitanda_qnt

    #imprimindo layout de menu das frutas, quantidade e valor unitário
    print("| Codigo | Fruta      | Qnt Disp | Valor Unit |" )
    for fruta_lista in quitanda_fruta.keys():
        print(f"|{fruta_lista:^8}|{quitanda_fruta[fruta_lista]:<12}|{quitanda_qnt[fruta_lista]:^10}| R${quitanda_valor[fruta_lista]:>5},00 |")

    #criando a lista de compras do cliente
    #identificando fruta e quantidade solicitadas pelo cliente  
    fruta = input("\nQual fruta deseja comprar ? ").title()
    lista_fruta.append(fruta)
    quantidade = int(input(f"\nQuantas {quitanda_fruta[fruta]}s deseja comprar?"))

    #verificando se a fruta esta no estoque disponivel
    if quitanda_qnt[fruta] >= quantidade:
        #definindo a varial de valor unitario de acordo com valor do estoque
        valor_unit = quitanda_valor[fruta]
        #calculando o total por fruta
        valor_total_fruta = (valor_unit*quantidade)
        #guardando o valor total por fruta (para calculo do valor total)
        lista_valor_total.append(valor_total_fruta)
        #imprimindo para o cliente a fruta, valor unitario e valor total por fruta
        print("\nQnt {} - {} - R$  {},00 = Total R$ {},00 ".format(quantidade,quitanda_fruta[fruta],valor_unit,valor_total_fruta))

        # atualizando quantidade disponivel
        quitanda_qnt[fruta] = quitanda_qnt[fruta] - quantidade
    elif quitanda_qnt[fruta] == 0:
        print(f"Desculpe, mas {quitanda_fruta[fruta]} esta em falta!")
    else:
        print(f"Desculpe, mas {quitanda_fruta[fruta]}s sao insuficientes!")

    #imprimindo o valor total do orçamento
    valor_total_orc = 0

    print("\nSeu carrinho de compras esta assim:")
    for fruta, valor_total in zip(lista_fruta, lista_valor_total):
        valor_total_orc += valor_total
        print("{} - Total R$ {},00".format(quitanda_fruta[fruta], valor_total))
    print(f"\nO valor total desta compra eh: R$ {valor_total_orc},00")

    return valor_total_orc


def fechando_a_venda(total_da_compra) :
    venda = input("Vamos fechar o orçamento?(por favor responda S/N): ").upper()
    if venda == "S":
        print("\nSua compra deu R$ {},00".format(total_da_compra))
        print("""Temos as seguintes Formas de pagamento:
                1 - Cartão
                2 - Dinheiro
                3 - Pix""")
    forma_pgto = int(input("Qual será a forma de pagamento? (escolha o numero correspondente): "))
    if forma_pgto == 2:
        valor_pago = int(input("Valor entregue R$? "))
        troco = valor_pago - total_da_compra
        print("Seu troco é R$ {},00\n Obrigada pela preferência {}. \n Volte Sempre".format(troco, fregues)) 
    else:
         print("Obrigada pela preferência {}. \n Volte Sempre".format(fregues)) 


#recepcionando e identificano o fregues
print("\nOi!Estamos muito feliz em telo em nossa quitanda hoje.\n") 
fregues = input("Qual seu nome? ").title()

print("\nOlá", fregues, "! \n   Hoje estamos com frutas fresquinhas, veja abaixo as disponibilidades: \n")

# utilizado no fechamento da compra
total_da_compra = 0

# definindo o loop de compra
compra = "S"
while compra == "S":
    total_da_compra = quitanda()
    compra = input("{} Deseja comprar mais alguma fruta? (por favor responda S/N): ".format(fregues)).upper()

# fechando a compra e realiznado pagamento
fechando_a_venda(total_da_compra)


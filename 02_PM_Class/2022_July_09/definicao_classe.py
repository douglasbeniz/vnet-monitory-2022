"""
Python scripts supporting monitory of students.

Ⓒ 2022 - VNET :: Vida Nova Escola de Tecnologia
"""

# ------------------------------------------------------------------------------
# Orientacao a Objetos
# ------------------------------------------------------------------------------

# A tal da classe...
#
# Classe = Modelo (forma, receita) utilizado para criar objetos (que possuem dados,
#   ou informacoes, e metodos, ou funcoes, que auxiliam os usuarios desses objetos
#   a manipular, modificar, ou recuperar esses dados, informacoes)
# Porquê?
#   - Reusabilidade
#   - Organizacao do codigo
#   - Abstracao (representacao de "coisas" de uma forma simplificada e util para
#       sistemas complexos)
#   - Encapsulamento (como colocar dentro de uma capsula, uma caixa fechada;
#       muitas vezes nao queremos saber como eh implementada, desde que sabemos 
#       como funciona; outro aspecto eh a protecao da informacao)
# Definicao da classe de usuario (ou customizada).
class MinhaClasse:
    def __init__(self, paramTexto, paramNumero):    # assinatura do metodo __init__
        self.meuAtributoTexto = paramTexto
        self.meuAtributoNumero = paramNumero

    def meuMetodo(self):
        print(self.meuAtributoTexto)
        print(self.meuAtributoNumero)
    
    def setAtributoTexto(self, paramTexto):
        self.meuAtributoTexto = paramTexto

    def setAtributoNumero(self, paramNumero):
        self.meuAtributoNumero = paramNumero

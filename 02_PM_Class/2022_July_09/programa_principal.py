"""
Python scripts supporting monitory of students.

Ⓒ 2022 - VNET :: Vida Nova Escola de Tecnologia
"""

# ------------------------------------------------------------------------------
# Orientacao a Objetos
# ------------------------------------------------------------------------------

from definicao_classe import MinhaClasse

# Funcao = Fazer
# Porquê?
#   - Reusabilidade
#   - Organizacao do codigo

def nomeDaFuncao(parametroEntrada):
    print(f"Parametro de entrada eh: {parametroEntrada}")
    return True

def main():
    # Revisando para mostrar que voces ja trabalham com classes, objetos, ha
    #   um bom tempo...
    #
    # Variavel == Objeto do tipo classe ... == Instancia de classe ...
    variavelTexto   = 'Texto'   # class str()
    variavelNumero  = 10        # class int()

    print(variavelTexto)
    print(variavelNumero)

    # Chamada da funcao
    retornoFuncao = nomeDaFuncao("meu parametro")
    if retornoFuncao:
        print("Verdadeiro")

    # ....
    # imagine que aqui voce tem a continuidade do seu programa, mas 
    #   logo precisa novametne daquela funcao (evite copiar trechos longos
    #   de codigo que se repetem, utilize funcoes)
    # ....
    retorno2Funcao = nomeDaFuncao("mudei de ideia")
    if retorno2Funcao: print("Verdadeiro")

    while True:
        # variaveis recebem entradas do usuario
        entradaTexto = input("Texto: ")
        entradaNumero = int(input("Numero: "))
        # Objeto ou instancia da minha classe customizada, informando (passando)
        #   informacoes, dados, que serao utilizados para inicializar os atributos
        objMinhaClasse = MinhaClasse(entradaTexto, entradaNumero)
        print(type(objMinhaClasse))     # verifique o tipo do objeto
        objMinhaClasse.meuMetodo()      # chamada do metodo da classe

        # solicitando novas entradas ao usuario
        entradaTexto = input("Novo texto: ")
        entradaNumero = int(input("Novo numero: "))
        # Alterando as informacoes (dados) especificas do meu objeto, armazenada
        #   nos atributos, atraves de metodos, nao diretamente modificando os
        #   atributos
        objMinhaClasse.setAtributoTexto(entradaTexto)
        objMinhaClasse.setAtributoNumero(entradaNumero)
        objMinhaClasse.meuMetodo()      # chamada do metodo da classe

        # Execute algumas vezes para observar o comportamento
        continua = input("Continuar?")
        if not continua:
            break

if __name__ == "__main__":
    main()  # chamada da funcao principal

#from funcoes import juros_simples

#juros_simples(1000, 5, 6)
#CAPITAL: 1000 taxa: 5 TEMPO: 6

#def juros_simples(capital, taxa,tempo):
    #return capital * (taxa/ 100) * tempo

def decorador_imprimir (funcao):
    def mensagem (*args, **kwargs):
        funcao (*args, **kwargs)
        print (f"Capital: R${capital}, Taxa: {taxa}, Tempo: {tempo}")
        print (f"Resultado: R$ {funcao(*args, **kwargs):.2f}")
    return mensagem


@decorador_imprimir
def juros_simples(capital, taxa, tempo):
    juros_simples = capital * (taxa/100) * tempo    
    return juros_simples

capital = int(input("Digite o valor do capital investido: "))
taxa = int(input("Qual a taxa de Juros (em porcentagem)? "))
tempo = int(input("Qual o prazo de pagamaento (em meses)? "))

resultado = juros_simples (capital, taxa, tempo)

print (resultado)



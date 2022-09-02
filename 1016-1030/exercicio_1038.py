#Missão: descobrir o valor da conta de lanche com os itens tabelados no problema

numeros = input()
lista: list = numeros.split(" ")



def calcula_lanche(lista):
    
    quantidade = int(lista[1])
    produto = int(lista[0])
    
    valor:float = 0
    
    if produto == 1:
        valor = 4.00
    elif produto == 2:
        valor = 4.50
    elif produto == 3:
        valor = 5.00
    elif produto == 4:
        valor = 2.00
    elif produto == 5:
        valor = 1.50
    
    valor_total = quantidade*valor
    
    return (valor_total)

print("Total: R$ %.2f" %calcula_lanche(lista))
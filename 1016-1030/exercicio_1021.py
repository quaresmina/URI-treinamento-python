#Missão: calcular o menor número de notas e moedas possíveis no qual certo valor pode ser decomposto.
#As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.


def main():
    valor: float = float(input())
    valor_notas: int = int(valor)
    moedas: int = round(((valor - valor_notas)*100), 2)
    
    nota_100: int = 0
    nota_50: int = 0
    nota_20: int = 0
    nota_10: int = 0
    nota_5: int = 0
    nota_2: int = 0
    
    #NOTAS
    if (valor_notas >= 100):
        nota_100 = valor_notas//100
        valor_notas = valor_notas%100
    if (valor_notas >= 50):
        nota_50 = valor_notas//50
        valor_notas = valor_notas%50
    if (valor_notas >= 20):
        nota_20 = valor_notas//20
        valor_notas = valor_notas%20
    if (valor_notas >= 10):
        nota_10 = valor_notas//10
        valor_notas = valor_notas%10
    if (valor_notas >= 5):
        nota_5 = valor_notas//5
        valor_notas = valor_notas%5
    if (valor_notas >= 2):
        nota_2 = valor_notas//2
        valor_notas = valor_notas%2
    
    print("NOTAS:")
    print("%d nota(s) de R$ 100.00" %nota_100)
    print("%d nota(s) de R$ 50.00" %nota_50)
    print("%d nota(s) de R$ 20.00" %nota_20)
    print("%d nota(s) de R$ 10.00" %nota_10)
    print("%d nota(s) de R$ 5.00" %nota_5)
    print("%d nota(s) de R$ 2.00" %nota_2)
    
    #MOEDAS
    moeda_1: int = 0
    moeda_50: int = 0
    moeda_25: int = 0
    moeda_10: int = 0
    moeda_05: int = 0
    moeda_01: int = 0
    
    moedas = (valor_notas*100) + moedas
    
    if (moedas >= 100):
        moeda_1 = moedas//100
        moedas = moedas%100
    if (moedas >= 50):
        moeda_50 = moedas//50
        moedas = moedas%50
    if (moedas >= 25):
        moeda_25 = moedas//25
        moedas = moedas%25
    if (moedas >= 10):
        moeda_10 = moedas//10
        moedas = moedas%10
    if (moedas >= 5):
        moeda_05 = moedas//5
        moedas = moedas%5
    if (moedas >= 1):
        moeda_01 = moedas
    
    print("MOEDAS:")
    print("%d moeda(s) de R$ 1.00" %moeda_1)
    print("%d moeda(s) de R$ 0.50" %moeda_50)
    print("%d moeda(s) de R$ 0.25" %moeda_25)
    print("%d moeda(s) de R$ 0.10" %moeda_10)
    print("%d moeda(s) de R$ 0.05" %moeda_05)
    print("%d moeda(s) de R$ 0.01" %moeda_01)

if __name__ == '__main__':
    main()
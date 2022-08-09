#Missão: calcular o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto.
#As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1.
#A seguir mostre o valor lido e a relação de notas necessárias.


def main():
    
    valor_inicial: str = input()
    resultado: int = int(valor_inicial)
    valor_notas: list = [100,50,20,10,5,2,1]
    notas100: int = 0
    notas50: int = 0
    notas20: int = 0
    notas10: int = 0
    notas5: int = 0
    notas2: int = 0
    notas1: int = 0
    
    def resto_divisao(dividendo: int, divisor: int) -> int:
        resultado: int = dividendo//divisor
        resto = dividendo%divisor
        return resultado, resto
        
    for nota in valor_notas:
        resultado, resto = resto_divisao(resultado, nota)
        
        if resultado >= 1:
            if nota == 100:
                notas100 = resultado
            elif nota == 50:
                notas50 = resultado
            elif nota == 20:
                notas20 = resultado
            elif nota == 10:
                notas10 = resultado
            elif nota == 5:
                notas5 = resultado
            elif nota == 2:
                notas2 = resultado
            elif nota == 1:
                notas1 = resultado

        if resto < 1:
            break
        
        resultado = resto
    print(valor_inicial)
    print("%d nota(s) de R$ 100,00" %notas100)
    print("%d nota(s) de R$ 50,00" %notas50)
    print("%d nota(s) de R$ 20,00" %notas20)
    print("%d nota(s) de R$ 10,00" %notas10)
    print("%d nota(s) de R$ 5,00" %notas5)
    print("%d nota(s) de R$ 2,00" %notas2)
    print("%d nota(s) de R$ 1,00" %notas1)
    
if __name__ == '__main__':
    main()
#Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara.
#Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”,
#caso haja uma divisão por 0 ou raiz de numero negativo.


def main():
    
    def delta(a,b,c): 
        result:float  = (b**2) - (4*a*c)
        return (result)

    def verificaRaizes(a,b,delta):
        if (delta < 0 or a == 0):
            return ("Impossivel calcular")
        elif delta >= 0:
            raiz1:float = (-b + (delta**0.5))/(2*a)
            raiz2:float = (-b - (delta**0.5))/(2*a)
            return ("R1 = %.5f\nR2 = %.5f" %(raiz1, raiz2))
        
    variaveis = input()
    variaveis_lista: list = variaveis.split(" ")
    
    a = float(variaveis_lista[0])
    b = float(variaveis_lista[1])
    c = float(variaveis_lista[2])
    
    print(verificaRaizes(a,b,delta(a,b,c)))
    

if __name__ == '__main__':
    main()
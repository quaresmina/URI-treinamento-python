#Missão: Leia 4 valores inteiros A, B, C e D.
#A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D, ambos,
#forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".


def main():
    
    
    valores: list = input()
    valores = valores.split(" ")
   
    a = int(valores[0])
    b = int(valores[1])
    c = int(valores[2])
    d = int(valores[3])
   
   
    if (b > c and d > a):
        if ((c + d) > (a + b)):
            if (c > 0 and d > 0):
                if (a % 2 == 0):
                   print("Valores aceitos")
                else:
                    print("Valores nao aceitos")
            else:
                print("Valores nao aceitos")
        else:
            print("Valores nao aceitos")
    else:
        print("Valores nao aceitos")

if __name__ == '__main__':
    main()
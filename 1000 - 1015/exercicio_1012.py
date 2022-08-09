#Missão: Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C.
#Em seguida, calcule e mostre:
#a) a área do triângulo retângulo que tem A por base e C por altura.
#b) a área do círculo de raio C. (pi = 3.14159)
#c) a área do trapézio que tem A e B por bases e C por altura.
#d) a área do quadrado que tem lado B.
#e) a área do retângulo que tem lados A e B.

def main():
    
    entradas = (input())
    lista: list = entradas.split(" ")
    
    a: float = float(lista[0])
    b: float = float(lista[1])
    c: float = float(lista[2])
    
    pi: float = 3.14159
    
    triangulo_retangulo: float = (a*c)/2
    circulo: float = pi*(c**2)
    trapezio: float = ((a+b)*c)/2
    quadrado: float = b**2
    retangulo: float = a*b
    
    print("TRIANGULO: %.3f" %triangulo_retangulo)
    print("CIRCULO: %.3f" %circulo)
    print("TRAPEZIO: %.3f" %trapezio)
    print("QUADRADO: %.3f" %quadrado)
    print("RETANGULO: %.3f" %retangulo)
   
if __name__ == '__main__':
	main()
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
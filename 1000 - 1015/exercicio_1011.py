#Missão: Calcular o volume de uma esfera a partir do raio
#Fórmula: (4/3) * pi * R**3

def main():
    
    raio: float = float(input())
    pi: float = 3.14159
    volume_esfera: float = (4/3)*pi*(raio**3)
    print("VOLUME = %.3f" %volume_esfera)
    
   
if __name__ == '__main__':
	main()
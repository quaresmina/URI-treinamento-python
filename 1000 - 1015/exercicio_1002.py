#Missão: calcular a área de uma circunferência
#recebendo o valor do raio como parâmetro

def main():

    raio: float = float(input())
    
    area: float = 3.14159 * (raio**2)
    
    print("A=%.4f" % area)

if __name__ == '__main__':
	main()
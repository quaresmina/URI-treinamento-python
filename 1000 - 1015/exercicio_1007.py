#Missão: calcular a diferença entre 4 valores seguindo a fórmula
#DIFERENCA = (A * B - C * D).

def main():
    
    a: int = int(input())
    b: int = int(input())
    c: int = int(input())
    d: int = int(input())
    
    diferenca: int = (a*b - c*d)
    
    print("DIFERENCA = %d" %diferenca)
   
if __name__ == '__main__':
	main()
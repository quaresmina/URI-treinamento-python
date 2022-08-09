#Missão: Calcular a média de um aluno a partir de duas notas
#Sendo que a nota A tem peso 3.5 e a nota B 7.5

def main():

    a: float = float(input())
    b: float = float(input())
    
    nota1: float = (3.5*a)/11
    nota2: float = (7.5*b)/11
    
    media: float = nota1 + nota2
    
    print("MEDIA = %.5f" % media)
    
if __name__ == '__main__':
	main()
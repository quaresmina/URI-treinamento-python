#Missão: Escreva um programa que leia o número de um funcionário, 
#seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário.
#A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

def main():
    
    numero: int = int(input())
    horas: int = int(input())
    valor_hora: float = float(input())
    salario: int
    
    salario = valor_hora * horas
    
    print("NUMBER = %d" %numero)
    
    print("SALARY = U$ %.2f" %salario)
   
if __name__ == '__main__':
	main()
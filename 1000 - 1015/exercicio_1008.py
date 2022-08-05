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
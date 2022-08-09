#Missão: Ler o nome do vendedor, salário fixo e total de vendas;
#Informar o total a receber, sendo que ganha 15% de comissão

def main():
    
    nome_funcionario: str = str(input())
    salario_fixo: float = float(input())
    total_vendas: float = float(input())
    comissao: float =  total_vendas * 0.15
    salario_total: float = salario_fixo + comissao
    
    
    print("TOTAL = R$ %.2f" % (salario_total))
   
if __name__ == '__main__':
	main()
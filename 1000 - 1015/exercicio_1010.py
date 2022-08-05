def main():
    
    entrada1 = (input())
    peça1 = entrada1.split(" ")
    num_peça1: int = int(peça1[0])
    qtd_peça1: int = int(peça1[1])
    valor_peça1: float = float(peça1[2])
    
    entrada2 = (input())
    peça2 = entrada2.split(" ")
    num_peça2: int = int(peça2[0])
    qtd_peça2: int = int(peça2[1])
    valor_peça2: float = float(peça2[2])
    
    valor_total: float = (qtd_peça1*valor_peça1) + (qtd_peça2*valor_peça2)
    
    
    print("VALOR A PAGAR: R$ %.2f" % valor_total)
    
   
if __name__ == '__main__':
	main()
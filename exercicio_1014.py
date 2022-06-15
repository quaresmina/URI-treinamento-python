def main():
    
    x: int = int(input())
    y: float = float(input())
    
    combustivel_gasto: float = x/y
    
    print("%.3f km/l" %(combustivel_gasto))
    
if __name__ == '__main__':
	main()
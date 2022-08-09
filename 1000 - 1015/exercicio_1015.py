#Missão: Calcular a distância entre dois pontos em um plano p1(x1,y1) e p2(x2,y2)

def main():
    
    entrada1 = input()
    coordenadas_1 = entrada1.split(" ")
    
    x1: float = float(coordenadas_1[0])
    y1: float = float(coordenadas_1[1])
    
    entrada2 = input()
    coordenadas_2 = entrada2.split(" ")
    
    x2: float = float(coordenadas_2[0])
    y2: float = float(coordenadas_2[1])
    
    distancia: float = ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    print("%.4f" %(distancia))
    
    
    
    
if __name__ == '__main__':
	main()
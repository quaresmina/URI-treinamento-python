#Missão: Calcular a quantidade de litros gastos em uma viagem, recebendo o tempo gasto na viagem
#e a velocidade média (km/h) da viagem, sendo que o carro faz 12km/L

def main():
    
    tempoViagem: int = int(input())
    velocMedia: int = int(input())
    
    kmTotal: int = tempoViagem * velocMedia
    gasolinaLitros: float = kmTotal/12
    
    print("%.3f" % gasolinaLitros)
    
    
if __name__ == '__main__':
    main()
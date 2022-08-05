from pip import main
def main():
    
    tempoViagem: int = int(input())
    velocMedia: int = int(input())
    
    kmTotal: int = tempoViagem * velocMedia
    gasolinaLitros: float = kmTotal/12
    
    print("%.3f" % gasolinaLitros)
    
    
if __name__ == '__main__':
    main()
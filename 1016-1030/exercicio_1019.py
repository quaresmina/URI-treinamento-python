#Missão: Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica
#e informe-o expresso no formato horas:minutos:segundos.

def main():
    
    seconts: int = int(input())
    horas: int = 0
    min: int = 0
    resto:int = 0
    
    if (seconts >= 3600):
        horas = seconts//3600
        resto = seconts%3600
        if (resto >= 60):
            min = resto//60
            seconts = resto%60
        elif (resto < 60):
            seconts = resto
    if (seconts >=60):
            min = seconts//60
            seconts = seconts%60
    
    print("%i:%i:%i" %(horas, min, seconts))
            
            
    
if __name__ == '__main__':
    main()
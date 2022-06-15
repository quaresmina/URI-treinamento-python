def main():
    
    entradas = (input())
    lista: list = entradas.split(" ")
    
    a: int = int(lista[0])
    b: int = int(lista[1])
    c: int = int(lista[2])
    
    def maior(a,b):
        maior = ((a+b)+abs(a-b))/2
        return maior
    
    maior_de_todos = maior(maior(a,b), c)
    
    print("%d eh o maior" % (maior_de_todos))
    
if __name__ == '__main__':
	main()
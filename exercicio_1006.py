def main():
    
    a: float = float(input())
    b: float = float(input())
    c: float = float(input())
    
    notaA: float = (a*2)/10
    notaB: float = (b*3)/10
    notaC: float = (c*5)/10
    
    media: float = (notaA + notaB + notaC)
    
    print("MEDIA = %.1f" % media)
    
    
if __name__ == '__main__':
	main()
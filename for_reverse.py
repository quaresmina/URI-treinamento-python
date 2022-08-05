def main():
    
    frase: str = "vinicius"
    frase_reversa: list = frase
    
    for i in range((len(frase)-1), -1, -1):
        frase_reversa.append(frase[i])
    
    print(frase_reversa)
    
    frase_reversa: list = []
    
    for i in range((len(frase)-1), -1, -1):
        print(i)
        frase_reversa.append(frase[i])
    frase_nova = ("").join(frase_reversa)
    print(frase_reversa)
    
    

            
            
            
    
if __name__ == '__main__':
    main()
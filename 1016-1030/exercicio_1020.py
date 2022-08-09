#Missão: Leia um valor inteiro correspondente à idade de uma pessoa
#em dias e informe-a em anos, meses e dias

def main():
    days: int = int(input())
    years: int = 0
    months: int = 0
    
    if days >= 365:
        years = days//365
        days = days%365
    if days >= 30:
        months = days//30
        days = days%30
    
    print("%d ano(s)" %years)
    print("%d mes(es)" %months)
    print("%d dia(s)" %days)


if __name__ == '__main__':
    main()
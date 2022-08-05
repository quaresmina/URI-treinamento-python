def main():
    
    list1: list = [4,10,7,15,8]
    
    
    for i in range(len(list1)-1):
        for j in range(len(list1)-1): 
            if(list1[j]>list1[j+1]): 
                temp = list1[j] 
                list1[j] = list1[j+1] 
                list1[j+1] = temp
                
    print(list1)
    

            
            
            
    
if __name__ == '__main__':
    main()
try:
    n=int(input("please enter your number: "))
    number=n
    i=1
    n_list=[]

    while(True) :
        if (n % i == 0) :
            n //= i
            n_list.append(i)    
        else :
            break
        i += 1
        
    if (n == 1) :
        print(f"your number is a factorial of {i-1}") 
        print(f"{i-1}!=",end=" ")
        for x in n_list:
            if x!= len(n_list) :
                print(x,end=" * ")
            else:
                print(x,end="")

        print(f" = {number}")
    else :
        print("No")
except:
    print("you must enter an integer number")
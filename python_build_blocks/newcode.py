print("Enter a number :: ", end = " ")
num = int(input())

if num > 1:
    for i in range(2,int(num/2)):
        if(num%i) == 0:
            print(str(num) + " is not prime")
            break;
    else:
        print(str(num) + " is prime")

else:
    print(str(num) + " is neither prime nor composite.")13
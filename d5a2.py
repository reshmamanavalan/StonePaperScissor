def prime(num):

    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)
lst=list(range(2500))
lst_prime =filter(prime,lst)
print(list(lst_prime))

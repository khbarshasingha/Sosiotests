def difference(sosq, sqos):
    if sosq >= sqos :
        return sosq-sqos
    else :
        return sqos-sosq
   
    
def sumofsquares(n):
    sum=0
    for num in range(1,n+1):
        sum=sum+(num**2)
        # print(sum)
    return sum

def squareofsum(n):
    sum=0
    for num in range(1,n+1):
        sum=sum+num
        # print(sum)
    return sum**2
n=int(input())
sosq=sumofsquares(n)
sqos=squareofsum(n)
res= difference(sosq,sqos)
print(res)
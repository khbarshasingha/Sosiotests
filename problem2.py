def palindrometriangle(n):
    for rows in range(1,n+1):
        for cols in range(1,rows+1):
            print(cols,end=" ")
        for rev in range(rows-1,0,-1):
            print(rev,end=" ")
        print("\n")
n=int(input())
palindrometriangle(n)
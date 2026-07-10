def prime(n):
    for i in range(2, n):
        if n%i==0:
            return(False)
    return(True)

for n in range(2,101):
    if prime(n):
        print(n)

def dtob(n):
    if(n>1):
        dtob(n//2)
    print(n%2)



n = 7
dtob(n)

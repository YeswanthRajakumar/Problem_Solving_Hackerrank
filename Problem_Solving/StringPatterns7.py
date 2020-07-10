n=4

for i  in range(n):
    print(' '*(n-i-1),end='')
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print('')

# i=0  3 spaces 65+0
# i=1  2 spaces 65+0 65+1
# i=2  1 spaces 65+0 65+1 65+2
# i=3  0 spaces 65+0 65+1 65+2 65+3

'''
_ _ _A
_ _ A B
_ A  B  C
A  B  C  D

'''
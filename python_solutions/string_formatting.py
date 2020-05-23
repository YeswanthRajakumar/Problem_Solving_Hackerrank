n = int(input('Enter : '))

for i in range(1,n+1):
    txt = "{0} {0:o} {0:X} {0:b}"
    print(txt.format(i))

s = 'eabEAB'
up = ['A','B','C','D','E']
lw = ['a','b','c','d','e']

s =list(s)

for i in range(len(s)): 
    if s[i] in up:
        index = up.index(s[i])
        s[i] = lw[index]

    else:
        index = lw.index(s[i])
        s[i] = up[index]
        
print(''.join(s))

n = 7
m = 21
greet = 'WELCOME'
s = '.|.'

for i in range(n//2):
    print((s*((i*2)+1)).center(m,'-'))

print(greet.center(m,'-'))

for i in range(n//2-1,-1,-1):
    print((s*((i*2)+1)).center(m,'-'))

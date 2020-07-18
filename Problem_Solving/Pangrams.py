alpha = 'abcdefghijklmnopqrstuvwxyz'
s = 'We promptly judged antique ivory buckles for the next prize'
s = list(s)
answer = ''
f_s=[]

# print(s)
for i in s:
    if i != ' ':
        f_s.append(str(i).lower())
print(f_s)

for i in alpha:
    if i in f_s:
        answer = 'pangram'
    else:
        answer = 'not pangram'
        break

print(answer)
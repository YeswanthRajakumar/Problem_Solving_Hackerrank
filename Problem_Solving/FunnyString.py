s = 'bcxz' 
s_ascii_list = [ord(i) for i in s]
s_ascii_reverse_list = list(reversed(s_ascii_list))

# print(s_ascii_list)

answer = ''

value_1 = []
value_2 = []

for i in range(0,len(s_ascii_list)-1):
    value_1.append(abs(s_ascii_list[i] - s_ascii_list[i+1]))
    value_2.append(abs(s_ascii_reverse_list[i] - s_ascii_reverse_list[i+1]))
  
for i in range(len(value_1)):
    if value_1[i] == value_2 [i]:
        answer = 'Funny'
    else:
        answer = 'Not Funny'
        break

print(answer)

s ='07:05:45PM'
a  = s[-3:0:-1]
a  = list(reversed(a))
s = ''.join(a)

s_list =s.split(':')
x  = int(s_list[0])
s_list[0] = str(x+12)
s_final = ':'.join(s_list)
print(s_final)
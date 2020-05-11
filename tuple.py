'''
n = int(input())
integer_list = tuple(map(int,input().split()))
print(hash(integer_list))

'''
small = 'abcdefghijklmnopqrstuvwxyz'
caps = small.upper()

small_list = list(small)
caps_list = list(caps)

string ='HelLo'

s = list(string)

for i in range(0,len(string)):
	if s[i] in small_list:
		s[i] = s[i].upper()
	elif s[i] in caps_list:
		s[i] = s[i].lower()
	else:
		s[i]=s[i]
		

s =''.join(s)
print(s)

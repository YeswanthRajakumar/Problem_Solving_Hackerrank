'''

s ='this is a string'
s_list = s.split(' ')
hyp = '-'.join(s_list)
return hyp

'''
'''
s = 'qA2'
numlist = [0,1,2,3,4,5,6,7,8,9]

print(s)

print(s.isalnum())

print(s.isalpha())
print(s.isdigit())
print(s.islower())
print(s.isupper())
'''

# s = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
# i = 0
# w = 4
# while w < len(s):
    
#     print(s[i: w])
#     i = w
#     w = w + 4

import textwrap

def wrap(string, max_width):
   l = list()
   for i in range(0,len(string),max_width):
       l.append(string[i:i+max_width]) 
   return "\n".join(l)

if __name__ == '__main__':
    #string, max_width = input(), int(input())
    string = 'ABCDEFGHIJKLI'
    max_width = 4
    result = wrap(string, max_width)
    print(result)








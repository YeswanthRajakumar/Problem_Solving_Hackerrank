s = 'goxg'
numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

count_dict ={
    'num_count' : 0,
    'up_count': 0,
    'low_count' : 0,
    'spc_count' : 0
}

chars_should_add = 0  
check = 0 

if len(s) > 0:
    for i in s: 
        if i in numbers:
           count_dict['num_count']+=1
        if i in upper_case:
            count_dict['up_count']+=1
        if i in lower_case:
            count_dict['low_count']+=1
        if i in special_characters:
             count_dict['spc_count']+=1
else:
    print(6)

print(count_dict)

for i in count_dict:
    if count_dict[i] == 0:
        chars_should_add+=1

for i in count_dict:
    check +=count_dict[i]

if chars_should_add + len(s) >=6:
    print(chars_should_add)


if len(s)>=6:
    print(chars_should_add)
else:
    print(abs(check - 6))
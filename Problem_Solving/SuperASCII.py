s = 'bba'

s_list = []
s_dict = dict()
letters = [chr(i) for i in range(97,123)]
flag ='No'

for i in s:
    if i not in s_list:
        s_list.append(i)
        s_dict[i] = s.count(i)

for item in s_dict:
    if letters.index(item)+1 == s_dict[item]:
        print(letters.index(item)+1 ,s_dict[item])
        flag = 'Yes'
    else:
        break

print(flag)
                 
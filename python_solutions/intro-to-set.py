#print(set('Hackerrank'))
#print(set(set('Hackerrank')))

#print(set(enumerate('Hackerrank')))

n = int(input('no.of  plants : '))
p_set = list(set (input('enter heights :').split(' ')))

p_int_list =[int(i) for i in p_set]

n = len(p_int_list)
p_sum = sum(p_int_list)

print(p_sum/n)
def cap(name):
	name_list = name.rstrip()
	name_list = name.split(' ')
	cap_list = []
	space =' '	
	for i in name_list:
	   cap_list.append(i.capitalize())
	join_list = space.join(cap_list)
	return join_list
s = input('Enter the name : ')

cap_list = cap(s)
print(cap_list+" ")

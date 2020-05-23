string = 'BlUeBe1Bl*fjal9jkl'
substr = 'Bl'

print(string,substr)

flag = len(substr)
key = substr[0]

counter = 0
while True:
	pos = string.find(substr)
	if pos !=-1:
		counter += 1
		print('posistion :' ,pos)
		lists = list(string)
		
		#print(lists)
		lists .remove(key)
		#print(lists)
		string = ''.join(lists)
		#print(string)
	else:
		break
print(counter)
			



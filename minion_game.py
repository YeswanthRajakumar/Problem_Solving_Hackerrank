s = input('Enter the input : ')

vowels = ['A','E','I','O','U']
Stuart = 0
Kevin  = 0
for i in range(len(s)):
	if s[i] in vowels:
		Kevin += (len(s[i:]))
	else:
		Stuart += (len(s[i:]))




if Stuart > Kevin:
	print('Stuart ',Stuart )

if Stuart < Kevin:
	print('Kevin :',Kevin )

'''
n = int(input())
student_marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input() 

score_list = student_marks[query_name]
score_sum = sum(score_list)
average = Decimal(score_sum)/Decimal(n)


score_list =[25,26.5,28]
score_sum = sum(score_list)
'''


no_of_lists = 3
modulo = 1000
all_lists = []

for i in range(1,no_of_lists+1):
	print('input for list '+str(i)+': ')
	for j in range():	
		a = int(input('input for list '+str(i)+' : '))
		all_lists.append(a)

print(all_lists)
'''
final_list = [max(l1),max(l2),max(l3)]
sqaure_list = [i**2 for i in final_list]
print(sum(sqaure_list))
'''

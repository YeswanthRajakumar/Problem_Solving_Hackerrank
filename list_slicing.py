'''
mylist  = 'www.google.com'


start = -3
end = -1
step=1

print(mylist[start::step])

'''


students_info =[]

for i in range(int(input())):
        name = input()
        score = float(input())
        students_info.append([name,score])



score_list =[]
name_list =[]

for students_object in students_info:
    name_list.append(students_object[0])
    score_list.append(students_object[1])
        

unique_score_list = list(set(score_list))
minimum_value =min(unique_score_list)
unique_score_list.remove(minimum_value)

second_minimum_value =min(unique_score_list)

final_list =[]
for i  in students_info:
    if i[1] == second_minimum_value:
        final_list.append(i[0])
        

final_list = sorted(final_list)

for i in final_list:
    print(i)



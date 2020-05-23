strenght  = int(input('Enter the strenght of class : '))

all_stud_info =[]
stud_info =[]

for i in range(0,strenght):
     name = input('Enter name  :')
     cgpa = float(input('Enter CGPA  :'))
     stud_info =[name,cgpa]
     all_stud_info.append(stud_info)

print(all_stud_info)


# all_stud_info = [['yas', 12.3], ['tim', 2.3],['ravi',10.2],['nithin',5.4]]
# eligible =[]
# not_eligible =[]

# for i in all_stud_info:
#     if i[1] > 7:
#         eligible.append(i[0])
#     else:
#         not_eligible.append(i[0])

# print('Eligible List : ',eligible)

# print(' Not Eligible List : ',not_eligible)



m = int(input())
m_set = set(input().split(' ')) 

n = int(input())
n_set = set(input().split(' ')) 

m_list = list(map(int,m_set.difference(n_set)))
n_list = list(map(int,n_set.difference(m_set)))

f_list =[]

for i in range(0,len(m_list)):
    f_list.append(m_list[i])

for i in range(0,len(n_list)):
     f_list.append(n_list[i])

f_list = sorted(f_list)

for i  in range(f_list):
    print(i)

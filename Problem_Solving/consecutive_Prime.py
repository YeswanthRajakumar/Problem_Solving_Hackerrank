n = 15
count =0

for k in range(3,n):
    upper = k
    sum_temp = 0
    print('For k = ',upper)     
    for num in range(1,upper):
        if num > 1:  
            for i in range(2,num):  
                if (num % i) == 0:  
                    break  
            else:
                print('For prime num = ',num)     
                sum_temp+=num       
                # print(num)
                if sum_temp == k:
                    count+=1
                    # print('---',sum_temp)
                    break
        
        
# n = 15
# low = 2                              
# for num in range(low,n+1):
#     if num > 1:
#         for j in range(2,num):
#             if num % j == 0:
#                 break
#         else:
#             print(num)         

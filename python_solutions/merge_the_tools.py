def merge_the_tools(string, k):
    ctr =0
    unique_l =[]
    for i in range(k,len(string)+1,k):
        l =list(string[ctr:i])  
        ctr+=k
        for o in l :
            if o not in unique_l:
                unique_l.append(o)
        for j in unique_l:
            print(j ,end='')
        unique_l.clear()



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
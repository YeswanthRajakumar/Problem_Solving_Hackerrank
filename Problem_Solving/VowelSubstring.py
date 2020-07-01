def vow_sub(substr):
    s_list = list(substr)
    vowel_list_answer =[]
    for i in range(len(s_list)):
        if s_list[i] in 'aeiou':
            vowel_list_answer.append(s_list[i])
    return vowel_list_answer




s= "aeiouia"
n = 3
vowels =['a','e','i','o','u']
max_count =0
max_list=[]
min_index=0 
final_str =''
for i in range(len(s)):
    substr = s[i:n+i:]
    if len(substr) == n:
        # print(substr)
        vowel_list = vow_sub(substr)
        # print(vowel_list)
        if len(vowel_list) > max_count:
            max_count = len(vowel_list)
            max_list = list(substr)
            min_index =i
            final_str = ''.join(max_list)
        elif len(vowel_list) ==0:
            final_str = 'Not found!'



print(final_str)
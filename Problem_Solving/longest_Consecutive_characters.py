sequence = 'AABCDDBBBEA'
prev_char = '' #B
count = 0   #1
max_count = 0
max_char = '' 

for curr_char in sequence:#A,A,B
    if curr_char ==  prev_char:
        count+=1
    else:
        prev_char = curr_char
        count = 1
    if count > max_count:
        max_count = count
        max_char = curr_char

print(max_char,max_count)
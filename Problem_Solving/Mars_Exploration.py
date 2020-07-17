s = 'SOSSOT'
count=0
original_len = len(s)//3
original_msg = 'SOS'*original_len
for i in range(len(s)):
    if s[i] != original_msg[i]:
        count+=1

print(count)
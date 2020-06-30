ip = list(map(int,input().split(' ')))
no_of_items = ip[0]
unordered_item = ip[1]

ordered_items = list(map(int,input().split(' ')))
charged_bill = int(input())

anna_sum = 0
for i in range(len(ordered_items)):
    if i != unordered_item:
       anna_sum += ordered_items[i]

anna_bill = anna_sum//2

if (charged_bill - anna_bill) == 0:
    print("Bon Appetit")
else:
    print(charged_bill - anna_bill)

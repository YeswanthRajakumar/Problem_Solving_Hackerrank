ip = list(map(int,input().split()))
budget = ip[0]
keyboards = list(map(int,input().split()))
usb = list(map(int,input().split()))
value =-1
for i in range(len(keyboards)):
    for j in range(len(usb)):
        if keyboards[i] < budget:
            if usb[j] < budget:
                if keyboards[i] + usb[j] <= budget:
                    value = max(value,keyboards[i] + usb[j])

print(value)
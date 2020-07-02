# HCF is also called as Greatest common Divisor(GCD)

n1 =4
n2 =6
min =0
hcf =0
lcm =0
if n1<n2 :
    min = n1
else:
    min =n2

#HCF
for i in range(1,min+1):
    if n1%i==0 and n2%i==0:
        hcf = i

#LCM
while(1):
    if min%n1==0 and min%n2 ==0 :
        lcm =min
        break
    lcm+=1



print(hcf)
print(lcm)




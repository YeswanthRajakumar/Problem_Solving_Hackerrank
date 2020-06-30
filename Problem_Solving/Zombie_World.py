try:
    Bob_energy , no_of_zombies = input().split()
    Bob_energy = int(Bob_energy)
    no_of_zombies =int(no_of_zombies)

    Z = list(map(int,input().split()))
    Z = sorted(Z)
    damage_sum =0
    for i in range(len(Z)):
        attack = (Z[i]%2) +(Z[i]//2) 
        damage_sum+=attack

    if damage_sum < Bob_energy:
        print("Yes")
    else:
        print("No")
except:
    print("Invalid Input" )
locations = [1,3,2]
cat_A = locations[0]
cat_B = locations[1]
mouse = locations[2]

dis_A = abs(mouse-cat_A)
dis_B = abs(mouse-cat_B)

if dis_A < dis_B:
    print('Cat A')

elif dis_B < dis_A:
    print('Cat B')

elif dis_A == dis_B:
    print('Mouse C')

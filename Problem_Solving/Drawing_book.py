n = 6
page_no = 2

Front_To_Back = n//2 # 3

Front_To_page = page_no//2 # 1

Back_To_page = Front_To_Back - Front_To_page # 2


if Front_To_page < Back_To_page:
    print(Front_To_page)
else:
     print(Back_To_page)









products = [] # 二維清單的大清單
while True:
    name = input('請輸入名稱: ')
    if name == 'q':
        break # 終止迴圈
    price = input('請輸入價格: ')
    products.append([name, price])

for p in products:
    print(p[0], '的價格是', p[1]) # for loop 存取二維清單





        
        
        



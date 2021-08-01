products = [] # 二維清單的大清單
while True:
    name = input('請輸入名稱: ')
    if name == 'q':
        break # 終止迴圈
    price = input('請輸入價格: ')
    products.append([name, price])

for p in products:
    print(p[0], '的價格是', p[1]) # for loop 存取二維清單
    
with open ('products.txt', 'w') as f: # 打開欲寫入或創造的檔案，txt改成其他副檔名也可以(如csv)
    for p in products:
        f.write(p[0], ',', p[1], '/n') # 檔案真正寫入動作的程式碼





        
        
        



import os # operating system

# 讀取檔案
products = [] # 二維清單的大清單
if os.path.isfile('products.csv'): # 檢查檔案在不在
    print('找到檔案')
    with open ('products.csv', 'r', encoding='utf-8') as f: # 欲讀取的檔案+編碼
        for line in f: # for loop
            if '商品,價格' in line: #如果商品,價格在檔案中的話
                continue # 跳過這一迴，執行下一迴，continue只能在迴圈使用
            name, price = line.strip().split(',') # 等號前面小清單；strip取消分行；split遇逗號切割
            products.append([name, price]) # 把小清單加到大清單中
    print(products)
else:
    print('找不到檔案')
    
# 讓使用者輸入    
while True:
    name = input('請輸入名稱: ')
    if name == 'q':
        break # 終止迴圈
    price = input('請輸入價格: ')
    price = int(price) # 把price字串轉換為整數
    products.append([name, price]) # 把小清單加到大清單中
print(products)

# 印出所有購買紀錄
for p in products:
    print(p[0], '的價格是', p[1]) # for loop 存取二維清單

# 寫入檔案    
with open ('products.csv', 'w', encoding='utf-8') as f: # 欲寫入的檔案+編碼
    for p in products:
        f.write(p[0], + ',' + str(p[1]) + '/n') # 檔案真正寫入動作的程式碼





        
        
        



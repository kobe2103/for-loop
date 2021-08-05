data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))


sum_len = 0
for d in data:
    sum_len += len(d) # sum_len = sum_len + len(d)
print(sum_len)
print('每筆留言的平均長度為', sum_len/len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d) 
print('總共有', len(new), '筆留言字數小於100')


# 文字計數
wc = {} # word_count
for d in data:
    words = d.split() # spilt的預設值即為空白鍵，且會跳過連續空白鍵
    for word in words:
        if word in wc:
            wc[word] += 1 # 當字典有word時，就+1
        else:
            wc[word] = 1 # 新增新的key進wc字典
            
for word in wc: # wc字典裡的每一個key
    if wc[word] > 100:
        print(word, wc[word]) #左邊是key，右邊是value

print(len(wc)) # 整個字典有多少個key的意思
print(wc['Allen']) # 查找字典裡allen這個key

while True:
    word = input('請問你想查找什麼字 ')
    if word == 'q':
        break # 終止迴圈
    if word in wc:
        print(word, '出現過的次數為: ', wc[word]) # 左邊是key，右邊是value           
    else:
        print('這個字沒有出現過')
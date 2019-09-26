data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #count = count + 1
		if count % 1000 == 0: # %: 求餘數。
			print(len(data),'/1000000')
print('檔案讀取完了,總共有', len(data), '筆資料。')
print(data[999999])
 
#算留言平均長度：
sum_len = 0
for d in data:
	sum_len += len(d) #sum_len = sum_len +len(d)
print('平均每筆留言字數為', sum_len / len(data), '字。')

#篩選：
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
		
print('總共有', len(new), '筆資料字數小於100')
print(new[0])
print('-----------')
print(new[21740])

#篩選2:
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('總共有', len(good), '筆留言包含good')
print(good[0])
#list comprehension : 清單快寫法1
bad = [d for d in data if 'bad' in d]
print('總共有', len(bad), '筆留言包含bad')
#print(bad[0])
#print(bad)
#list comprehension : 清單快寫法2
bad = ['bad' in d for d in data]
print(len(bad))
#print(bad)
#bb = [b for b in data if 'True' in b]

# 文字計數
wc = {} # word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1  

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))
print(wc['Sophie'])

while True:
	word = input('請問您想查詢什麼字： ')
	if word == 'q':
		print('感謝使用。')
		break
	if word in wc:
		print(word, '總共出現', wc[word], '次。' )
	else:
		print('這個字沒有出現過喲')










		

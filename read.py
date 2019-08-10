data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #count = count + 1
		if count % 1000 == 0: # %: 求餘數。
			print(len(data),'/1000000')
print('檔案讀取完了,總共有', len(data), '筆資料。')
#算留言平均長度：
sum_len = 0
for d in data:
	sum_len += len(d) #sum_len = sum_len +len(d)
print('平均每筆留言字數為', sum_len / len(data), '字。')









		

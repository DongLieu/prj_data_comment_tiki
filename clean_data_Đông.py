file = open("Đông_cleandata.csv", "r")

datas = file.read().split("\n")

head = datas[:1]

datas = datas[1:len(datas)-1]

rating = []
comment = []

# chia du lieu
for x in datas:
	rating.append(x[-1:])

	cmt_tmp = len(x[0:len(x)-1]) #vi tri cuoi 
	k = 0

	for x1 in range(len(x[0:len(x)-1])): 
		if k == 2: 
			cmt_tmp -= x1 
			break

		if x[cmt_tmp - x1 - 1] == ";": 
			k += 1
			

	comment.append(x[0:cmt_tmp ])

filee = open("Đông_data_clean.txt", "w")
for x in range(len(comment)):
	filee.write(rating[x] + "," + comment[x]  +  "\n")
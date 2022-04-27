file = open("comment.csv", "r")

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

#xoa ki tu str_delete trong ki tu str
def xoakitu(str, str_delete):

	do_dai_str_delete = len(str_delete)
	return_str = ''
	key = 0

	for x in range(len(str)):
		if key != 0:
			key -= 1
			continue

		if str[x:x+do_dai_str_delete] == str_delete:
			key = do_dai_str_delete - 1
			x = x + do_dai_str_delete
		else :
			return_str = return_str + str[x]

	return return_str


def thaykitu_a_la_b(str, a, b):

	do_dai_a = len(a)
	return_str = ''
	key = 0

	for x in range(len(str)):
		if key != 0: # 2/ 1
			key -= 1
			continue

		# tim duoc a
		if str[x:x+do_dai_a] == a:
			key = do_dai_a - 2 # 2
			return_str = return_str + b
			
		else :
			return_str = return_str + str[x]

	return return_str

a = "4,đặt hàng ngày 13/1 hnay 18/1 mới nhận được hàng máy nguyên seal rất đẹp cám ơn tiki"
b = "/"

print(xoakitu(a, b))
for x in range(len(comment)):
	comment[x] = xoakitu(comment[x], '(')
	comment[x] = xoakitu(comment[x], ')')
	comment[x] = xoakitu(comment[x], ':')
	comment[x] = xoakitu(comment[x], '=')
	comment[x] = xoakitu(comment[x], '>')
	comment[x] = xoakitu(comment[x], '<')
	comment[x] = xoakitu(comment[x], '"')
	comment[x] = xoakitu(comment[x], ';')
	comment[x] = xoakitu(comment[x], '/')
	comment[x] = xoakitu(comment[x], '\\')
	# iconxemco nhung icon nào
	comment[x] = xoakitu(comment[x], '😄')
	comment[x] = xoakitu(comment[x], '😂')
	comment[x] = xoakitu(comment[x], '😓')
	comment[x] = xoakitu(comment[x], '🥴')
	comment[x] = xoakitu(comment[x], '😡')
	comment[x] = xoakitu(comment[x], '❤️')
	comment[x] = xoakitu(comment[x], '😅')
	comment[x] = xoakitu(comment[x], '😻')
	comment[x] = xoakitu(comment[x], '🧐')
	comment[x] = xoakitu(comment[x], '😁')
	comment[x] = xoakitu(comment[x], '🥰')
	comment[x] = xoakitu(comment[x], '👍🏽')
	comment[x] = xoakitu(comment[x], '😘')
	comment[x] = xoakitu(comment[x], '👍')
	comment[x] = xoakitu(comment[x], '😜')
	comment[x] = xoakitu(comment[x], '🥲')
	comment[x] = xoakitu(comment[x], '😆')
	comment[x] = xoakitu(comment[x], '⭐')
	comment[x] = xoakitu(comment[x], '😊')
	comment[x] = xoakitu(comment[x], '😍')
	comment[x] = xoakitu(comment[x], '👌')
	comment[x] = xoakitu(comment[x], '😀')
	comment[x] = xoakitu(comment[x], '🥺')
	comment[x] = xoakitu(comment[x], '🤩')
	comment[x] = xoakitu(comment[x], '♥️')
	comment[x] = xoakitu(comment[x], '💗')
	comment[x] = xoakitu(comment[x], '✌️')
	comment[x] = xoakitu(comment[x], '💙')
	comment[x] = xoakitu(comment[x], '✨')
	comment[x] = xoakitu(comment[x], '👎')
	comment[x] = xoakitu(comment[x], '💯')
	comment[x] = xoakitu(comment[x], '🌞')
	comment[x] = xoakitu(comment[x], '🤗')
	comment[x] = xoakitu(comment[x], '😑')
	comment[x] = xoakitu(comment[x], '😞')
	comment[x] = xoakitu(comment[x], '😋')
	comment[x] = xoakitu(comment[x], '😳')
	comment[x] = xoakitu(comment[x], '😔')
	comment[x] = xoakitu(comment[x], '🙂')
	comment[x] = xoakitu(comment[x], '😌')
	comment[x] = xoakitu(comment[x], '☘️')
	comment[x] = xoakitu(comment[x], '😛')
	comment[x] = xoakitu(comment[x], '😭')
	comment[x] = xoakitu(comment[x], '😉')
	comment[x] = xoakitu(comment[x], '🤣')
	comment[x] = xoakitu(comment[x], '🤧')
	comment[x] = xoakitu(comment[x], '😢')
	comment[x] = xoakitu(comment[x], '😃')








	comment[x] = thaykitu_a_la_b(comment[x], " k "," không ")
	comment[x] = thaykitu_a_la_b(comment[x], " ko "," không ")
	comment[x] = thaykitu_a_la_b(comment[x], " takako "," takahisizua ")

	comment[x] = thaykitu_a_la_b(comment[x], " sp "," sản phẩm ")
	comment[x] = thaykitu_a_la_b(comment[x], "sp "," sản phẩm ")
	comment[x] = thaykitu_a_la_b(comment[x], " mk "," mình ")
	comment[x] = thaykitu_a_la_b(comment[x], " m "," mình ")
	comment[x] = thaykitu_a_la_b(comment[x], " mh "," mình ")
	comment[x] = thaykitu_a_la_b(comment[x], " nhìu "," nhiều ")
	comment[x] = thaykitu_a_la_b(comment[x], " nhìuu "," nhiều ")
	comment[x] = thaykitu_a_la_b(comment[x], " nhìu"," nhiều ")
	comment[x] = thaykitu_a_la_b(comment[x], " nhìuu"," nhiều ")
	comment[x] = thaykitu_a_la_b(comment[x], " mn "," mọi người ")
	comment[x] = thaykitu_a_la_b(comment[x], " mng "," mọi người ")
	comment[x] = thaykitu_a_la_b(comment[x], " r "," rồi ")
	comment[x] = thaykitu_a_la_b(comment[x], " tks "," thanks ")
	comment[x] = thaykitu_a_la_b(comment[x], "aa ","a ")
	comment[x] = thaykitu_a_la_b(comment[x], "aaa ","a ")
	comment[x] = thaykitu_a_la_b(comment[x], "1k ","1 nghìn ")
	comment[x] = thaykitu_a_la_b(comment[x], "2k ","2 nghìn ")
	comment[x] = thaykitu_a_la_b(comment[x], "3k ","3 nghìn ")
	comment[x] = thaykitu_a_la_b(comment[x], "4k ","4 nghìn ")
	comment[x] = thaykitu_a_la_b(comment[x], "5k ","5 nghìn ")
	comment[x] = thaykitu_a_la_b(comment[x], "6k ","6 nghìn ")
	comment[x] = thaykitu_a_la_b(comment[x], "7k ","7 nghìn ")
	comment[x] = thaykitu_a_la_b(comment[x], "8k ","8 nghìn ")
	comment[x] = thaykitu_a_la_b(comment[x], "9k ","9 nghìn ")
	comment[x] = thaykitu_a_la_b(comment[x], "0k ","10 nghìn ")
	comment[x] = thaykitu_a_la_b(comment[x], "5*"," 5 sao")
	comment[x] = thaykitu_a_la_b(comment[x], "1*","1 sao")
	comment[x] = thaykitu_a_la_b(comment[x], "2*","2 sao")
	comment[x] = thaykitu_a_la_b(comment[x], "3*","3 sao")
	comment[x] = thaykitu_a_la_b(comment[x], "4*","4 sao")
	comment[x] = thaykitu_a_la_b(comment[x], " sao*"," sao")
	comment[x] = thaykitu_a_la_b(comment[x], "1tr ","1 triệu ")
	comment[x] = thaykitu_a_la_b(comment[x], "2tr ","2 triệu ")
	comment[x] = thaykitu_a_la_b(comment[x], "3tr ","3 triệu ")
	comment[x] = thaykitu_a_la_b(comment[x], "4tr ","4 triệu ")
	comment[x] = thaykitu_a_la_b(comment[x], "5tr ","5 triệu ")
	comment[x] = thaykitu_a_la_b(comment[x], "6tr ","6 triệu ")
	comment[x] = thaykitu_a_la_b(comment[x], "7tr ","7 triệu ")
	comment[x] = thaykitu_a_la_b(comment[x], "8tr ","8 triệu ")
	comment[x] = thaykitu_a_la_b(comment[x], "9tr ","9 triệu ")
	comment[x] = thaykitu_a_la_b(comment[x], "0tr ","0 triệu ")
	comment[x] = thaykitu_a_la_b(comment[x], "-"," ")
	comment[x] = thaykitu_a_la_b(comment[x], "1% ","1 % ")
	comment[x] = thaykitu_a_la_b(comment[x], "2% ","2 % ")
	comment[x] = thaykitu_a_la_b(comment[x], "3% ","3 % ")
	comment[x] = thaykitu_a_la_b(comment[x], "4% ","4 % ")
	comment[x] = thaykitu_a_la_b(comment[x], "5% ","5 % ")
	comment[x] = thaykitu_a_la_b(comment[x], "6% ","6 % ")
	comment[x] = thaykitu_a_la_b(comment[x], "7% ","7 % ")
	comment[x] = thaykitu_a_la_b(comment[x], "8% ","8 % ")
	comment[x] = thaykitu_a_la_b(comment[x], "9% ","9 % ")
	comment[x] = thaykitu_a_la_b(comment[x], "0% ","0 % ")
	comment[x] = thaykitu_a_la_b(comment[x], "oki","ok")
	comment[x] = thaykitu_a_la_b(comment[x], " 3h "," 3 giờ ")
	comment[x] = thaykitu_a_la_b(comment[x], " 1h "," 1 giờ ")
	comment[x] = thaykitu_a_la_b(comment[x], " 2h "," 2 giờ ")
	comment[x] = thaykitu_a_la_b(comment[x], " 4h "," 4 giờ ")
	comment[x] = thaykitu_a_la_b(comment[x], " 5h "," 5 giờ ")
	comment[x] = thaykitu_a_la_b(comment[x], " 6h "," 6 giờ ")
	comment[x] = thaykitu_a_la_b(comment[x], " 7h "," 7 giờ ")
	comment[x] = thaykitu_a_la_b(comment[x], " 8h "," 8 giờ ")
	comment[x] = thaykitu_a_la_b(comment[x], " 9h "," 9 giờ ")
	comment[x] = thaykitu_a_la_b(comment[x], " 0h "," 0 giờ ")
	# comment[x] = thaykitu_a_la_b(comment[x], "/"," ")
	comment[x] = thaykitu_a_la_b(comment[x], " 5sao"," 5 sao")
	comment[x] = thaykitu_a_la_b(comment[x], "+"," + ")



filee = open("data_tiki_clean.txt", "w")
for x in range(len(comment)):
	filee.write(rating[x] + "," + comment[x]  +  "\n")

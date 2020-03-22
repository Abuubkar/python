

def Sortm(sub_li): 
	l = len(sub_li)
	for i in range(0, l):
		for j in range(0, l-i-1):
			if (sub_li[j][1] < sub_li[j + 1][1]):
				tempo = sub_li[j]
				sub_li[j]= sub_li[j + 1]
				sub_li[j + 1]= tempo
	return sub_li


def calculate(filename):
	with open(filename, "rt") as fin:
		lines = fin.readlines()

	totalBooks, totalLibraries, totalDays = list(map(int, lines[0].split()))
	booksScores = list(map(int, lines[1].split()))

	# print(totalBooks,totalLibraries,totalDays);
	# print(booksScores)
	
	#libraries = list(for i in range(totalLibraries) i)
	libraries = list()

	for i in range(0,totalLibraries):
		noOfBooks, signupDays, bookShipLimit = list(map(int, lines[(i*2)+2].split()))
		bookList = list(map(int, lines[(i*2)+3].split()))
		libraries.append(dict({"lid":i,"nob":noOfBooks,"sud":signupDays,"bsl":bookShipLimit,"bookList":bookList}))

		temp = []
		for j in libraries[i]["bookList"]:
			temp.append([j,booksScores[j]])
		
		libraries[i]["bookList"]=temp
		
		Sortm(libraries[i]["bookList"])

		#print(libraries[i])


	libraries = sorted(libraries, key = lambda i: (i['sud'],-i['bsl']))

	for i in range(0,totalLibraries):
		print(libraries[i])
	
	

	sol=[]

	tempDays = totalDays

	print("done till this")

	for i in range(totalLibraries):
		tempDays -= libraries[i]['sud']

		#if(tempDays>0):
			
		# for val in sol:
		# 	for j in range(0,len(libraries[i]['bookList'])):
		# 		if(j > len(libraries[i]['bookList'])-1):
		# 			break
				
		# 		if(val==libraries[i]['bookList'][j]):
					
		# 			libraries[i]['bookList'].remove(libraries[i]['bookList'][j])

		for val in libraries[i]['bookList'][0:tempDays*libraries[i]['bsl']]:
			#print("there it is")
			sol.append(val)
		#sol.append(libraries[i]['bookList'][0:tempDays*libraries[i]['bsl']])


	# print(sol)

	# for i in range(totalLibraries):
	# 	print(libraries[i])

	sum=0
	for i in sol:
		sum+=i[1];
	print(sum)

	#with open(fileNames[i][0:fileNames[i].find('.')]+".out", "wt") as out:

	print("writing file ...")

	with open("Output/"+filename[0:filename.find('.')]+".out", "wt") as out:
		out.write(str(totalLibraries) + '\n')

		for i in range(totalLibraries):
			out.write(str(libraries[i]['lid'])+" "+str(len(libraries[i]['bookList']))+"\n")
			for j in range(len(libraries[i]['bookList'])):
				if(j != len(libraries[i]['bookList'])-1):
					out.write(str(libraries[i]['bookList'][j][0])+" ")
				else:
					out.write(str(libraries[i]['bookList'][j][0])+"\n")




filenames = [ "a_example.txt", "b_read_on.txt", "c_incunabula.txt", "d_tough_choices.txt", "e_so_many_books.txt", "f_libraries_of_the_world.txt" ];


calculate(filenames[2]);
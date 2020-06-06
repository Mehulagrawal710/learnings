import os

def renameLogic(i, curr_name):
	return str(i+1)+".png"

directory = "C:\\Users\\Hi\\Desktop\\learning\\ml\\Random Forest\\resources\\"

for index, filename in enumerate(os.listdir(directory)):
	new_name = renameLogic(index, filename)
	src = directory + filename
	dst = directory + new_name
	os.rename(src, dst)
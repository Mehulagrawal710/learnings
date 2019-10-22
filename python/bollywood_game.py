import random
import math

#generating dashes
def get_dashes(movie):
	length = len(movie)
	dashed_string = []
	for i in range(length):
			if movie[i] is " ":
				dashed_string.append(" ")
			else:
				dashed_string.append("-")
	return dashed_string			


#test code========================================================================

#List of movies
movies = ["3 idiots", "kahaani", "jab we met", "sanju", "sholay", "dangal", "dil se", "gol mal"]

#selecting a random movie from the list
movie = random.choice(movies)

dashed_string = get_dashes(movie)
length = len(movie)
chances = length*2

for chance in range(chances):
	for x in dashed_string:
		print(x, end="")
	print("\n")
	print("chances left:", chances-chance)

	guess = input("your guess: ")
	if len(guess) is 1:
		found = 0
		for i in range(length):
			if movie[i] is guess:
				found = 1
				dashed_string[i] = guess
				if ("".join(dashed_string)) == movie:
					print("winner winner")
					exit()
		
		if found is 0:
			print("no match")

	else:
		if guess.split() is movie.split():
			print("correct movie guess")
		else:
			print("wrong movie guess")					
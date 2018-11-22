from data import *
from fonctions import * 

scores = retreive_score()
user = retreive_user_name()

if user not in scores.keys():
	scores[user] = 0
continuer_partie = 'o'

while continuer_partie != 'n':
	print ("(player{@} : {} point(s)" .format(user, scores[user])) 
	word_to_find= choose_word()
	found_words = []
	find_word = retreive_mask_word(complete_word,found_letter)
	nb_try =nb_coups
    while word_to_find != find_word and nb_try > 0:
		print ( "words to find {@} (encore {1} chances)" .format(find_word,nb_try))
		letter = retreive_letter()
		if letter in found_words:
			print ("you have already found this letter ") 
		elif letter in word_to_find:
			found_words.append(letter)
			print ("good job")
		
		else: 
			nb_chances -= 1
			print (".. non , this letter is not is this word ")
			find_word = retreive_mask_word(complete_word,found_letter)
		if word_to_find == find_word:
			print ("bravo you have find{0}." .format(word_to_find))
		else:
			print ("lost you have been hanged")
		
		scores[user] +=nb_try
		continuer_partie = input ("do you want to continue o/n")
		continuer_partie = continuer_partie.lower()
save_score(scores)

print ("you finish the game with {0} points ". format(scores[user]))
		
		
	



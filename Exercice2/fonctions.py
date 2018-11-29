import os 
import pickle
from data import * 
from random import choice

def retreive_score(): 
	if os.path.exists(score_file):
		score = open(score_file, "rb")
		unpickle_file = pickle.Unpickler(score)
		scores = unpickle_file.load()
		score.close()
	else:
		scores ={}
	return scores

	
def save_score(scores):
		score = open (score_file, "wb")
		mypickler = pickle.Pickler(score)
		mypickler.dump(scores)
		score.close()
	
	
def retreive_user_name():
	username = input("Enter your user name!")
	username = username.capitalize()
	while len(username)<5 or len(username)>10:
		print ("username should be above 5 and 10 caraceters")
		return retreive_user_name()
	if  not username.isalnum():
		print("username should be alpha or alphanumeric caracters")
		return retreive_user_name()
	
	else:
		return username
		
		
		
		
	
def choose_word():
	return choice(liste_mots)

	
def retreive_mask_word(complete_word,found_letter):
	mask_word=""
	for letters in complete_word: 
		if letters in found_letter:
			mask_word += letters
		else:
			mask_word +="*"
	return mask_word
	

	
	
def retreive_letter(): 
	letter = input("enter the letter")
	letter = letter.lower()
	if  not letter.isalnum()or len(letter)>1:
		print("numeric and special carcaters are not allowed ,enter only 1 caracter ")
		return retreive_letter()
	else: 
		return letter
	
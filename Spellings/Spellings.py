
##
#  SPELL CHECKER
#		-- module has a function to check and grade spellings
#
#		@author Apoorva Rao		@date 14 March 2012
#
##

import enchant
import re

# @brief function which checks spellings
# 		INPUT : essay
# 		OUTPUT: returns the number of misspelt words AND key-value pairs of missplet words and suggestions to correct them

def spellCheck(text):
	#choose the dictionary
	d = enchant.Dict("en_US")
	
	#keep track of the number of misspelt words
	numIncorrect=0
	
	#split the text into words
	wordList = re.findall(r'\w+', text)
	
	misspelt = {}
	
	#Checking for misspelt words...
	for word in wordList:
		#print word, d.check(word)
		if d.check(word)==False:
			misspelt[word] = d.suggest(word)	#store the word and its suggestions as a key value pair
			numIncorrect += 1
			
	return numIncorrect, misspelt




#test driver to independently test the module
if __name__ == '__main__' :
	
	text = "Hi lets see fi iti cahn check miy sepllings?? Apoorva\n"
	#incorr1, misspelt1 = spellChecker(text)
	#print "\n\nIncorrectly spelled count: ", incorr1
	############################
	
	#open essay
	sourceFileName = "../Sample_Essays/essay4.txt"
	sourceFile = open(sourceFileName, "r")
	
	#read essay
	text = sourceFile.read()
	
	incorr2, misspelt2 = spellCheck(text)
	print "\n\nIncorrectly spelled count: ", incorr2, "\n"
	
	for key in misspelt2:
		print key, " :: ",  misspelt2[key], "\n\n"
	
	

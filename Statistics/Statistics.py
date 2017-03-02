##
#  STATISTICS GENERATOR
#		-- module has functions whic returns the various statistics of the essay
#	
#		@author aparna		@date 09 March 2012
#		@author karthik		@date 11 March 2012 - modularization
#
##


import nltk
import math
import re


class Node:
	def __init__(self, word):
		self.word = w
		self.deg = 0
		




def getWordCount(text):
	#split the text into words
	wordList = re.findall(r'\w+', text)

	#print wordList
	#print len(wordList)
	return len(wordList)
	
	
	
def getSentenceCount(text):
	#split the essay into sentences
	sentList = nltk.sent_tokenize(text)
	#print sentList
	return len(sentList)



def getParaCount(text):
	#split the text into paragraphs
	paraList = text.splitlines()
	#remove blank lines from the list of paragraphs
	paraList[:] = [element for element in paraList if element != ""]
	#print paraList
	return len(paraList)
	
	
	
def getAvgSentenceLength(text):
	#split the essay into sentences
	sentList = nltk.sent_tokenize(text)

	sumSentLength = 0
	for sent in sentList:
		sumSentLength = sumSentLength + getWordCount(sent)

	#print float(sumSentLength)/len(sentList)
	return float(sumSentLength)/len(sentList)



def getStdDevSentenceLength(text):
	#split the essay into sentences
	sentList = nltk.sent_tokenize(text)
	
	#mean sentence length
	mean = getAvgSentenceLength(text)
	
	nr=0.0
	for sent in sentList:
		nr = nr + (getWordCount(sent) - mean)**2
	#print math.sqrt(nr/len(sentList))
	return math.sqrt(nr/len(sentList))
	
	

########################################################################

#test driver to independently test the module
if __name__ == '__main__' :
	
	text = "hi there!\n\tmy name is - u know what?, kp. \n\nhell yeah!"
	
	# getWordCount(text)
	# getSentenceCount(text)
	# getParaCount(text)
	# getAvgSentenceLength(text)
	# getStdDevSentenceLength(text)
	
	############################
	#open essay
	sourceFileName = "../Sample_Essays/essay3.txt"
	sourceFile = open(sourceFileName, "r")
	
	#read essay
	text = sourceFile.read()
	
	getWordCount(text)
	getSentenceCount(text)
	#getParaCount(text)
	#getAvgSentenceLength(text)
	#getStdDevSentenceLength(text)

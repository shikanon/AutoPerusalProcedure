##
#	GRAMMAR GRADER
#		-- assigns a score based on the grammar and structure of the essay
#	
#	@author karthik
#	@date 06 March 2012
##

import nltk
from pylinkgrammar import clinkgrammar as clg


# range() for float values...used by parseSentence()
def frange(x, a, b):
	if x > a and x <= b:
		return True
	else:
		return False



# @brief function to parse sentence
# 		INPUT : sentence and dictionary of links
#		OUTPUT: sentence score

def parseSentence(sentence, lgDict):
	
	#make sentence readable to the parser
	lgSentence = clg.sentence_create(sentence, lgDict)
	
	#set options (default)
	lgOpts = clg.parse_options_create()
	
	#parse  sentence
	numOfLinkages = clg.sentence_parse(lgSentence, lgOpts)
	
	#################################################
	#print sentence + " :: " + str(numOfLinkages)
	#print
	#################################################
	
	# DETERMINING IF SENTENCE IS NON GRAMMATICAL OR NOT
	if numOfLinkages > 0:
		#print 'All linkages found. Grammatically correct'
		score = 5
	#end of if construct	
	
	elif numOfLinkages == 0:
		#print 'Sentence may be ungrammatic...needs to be checked... \n'
		
		#relaxing options
		clg.parse_options_set_min_null_count(lgOpts, 1);
		clg.parse_options_set_max_null_count(lgOpts,1000);
		
		#parsing again
		numOfLinkages = clg.sentence_parse(lgSentence, lgOpts)
		
		numOfWords = clg.sentence_length(lgSentence) - 2;
		numOfNullWords = clg.sentence_null_count(lgSentence)
		
		linkRatio = float(numOfLinkages) / numOfWords
		nullRatio = float(numOfNullWords) / numOfWords


		#################################################
		#print sentence + '\nnew num of linkages::' + str(numOfLinkages)
		#print 'Num of words ::' + str(numOfWords)
		#print 'Num of null words ::' + str(numOfNullWords)
		#print
		#print 'Link Ratio :: ' + str(linkRatio)
		#print 'nullRatio :: ' + str(nullRatio)
		
		#################################################	
		
		
		# scoring the sentences for score < 6
		if linkRatio >= 1.0:
			if nullRatio <= 0.1:
				score = 4
			elif frange(nullRatio, 0.1,0.2):
				score = 3
			elif frange(nullRatio, 0.2,0.3):
				score = 2
			elif nullRatio > 0.3:
				score = 1
			else:
				score = 1

		elif frange(linkRatio, 0.5,1.0):
			if nullRatio < 0.05:
				score = 3
			elif frange(nullRatio, 0.05, 0.1):
				score = 2
			elif frange(nullRatio, 0.1, 0.15):
				score = 1
			elif nullRatio > 0.15:
				score = 1
			else:
				score = 3
		
		elif frange(linkRatio, 0.25, 0.5):
			if nullRatio < 0.05:
				score = 3
			elif frange(nullRatio, 0.05, 0.1):
				score = 2
			elif frange(nullRatio, 0.1, 0.15):
				score = 1
			else:
				score = 1
		
		elif frange(linkRatio, 0.125, 0.25):
			if nullRatio < 0.05:
				score = 2
			elif frange(nullRatio, 0.05, 0.1):
				score = 1
			else:
				score = 1

		elif linkRatio < 0.125:
			if nullRatio > 0.1:
				score = 1
			else:
				score = 3
		
		else:
			score = 1
	#end of elif construct
	
	else:
		#illegal sentence
		score = -1
	#end of else construct
	
    #delete snetence and options
	clg.sentence_delete(lgSentence);
	clg.parse_options_delete(lgOpts);
	
	return score


# @brief main function to be called
#		 INPUT : essay
#		 OUTPUT: cumulative score(which is the avg sentence score) AND key-value pairs of sentences and its scores

def getGrammarScore(essay):
	#make dictionary
	lgDict = clg.dictionary_create("data/4.0.dict", "data/4.0.knowledge", 'data/4.0.constituent-knowledge', "data/4.0.affix");
	
	#a dictionary to hold sentence and its score
	sentScore = {}
	
	#split the essay into sentences
	sentences = nltk.sent_tokenize(essay)
	for sentence in sentences:
		sentScore[sentence] = parseSentence(sentence, lgDict)
		#print '________________________________________________________\n'
	
	#delete dictionary
	clg.dictionary_delete(lgDict)
	
	#computing cumulative score
	cumScore = float(sum(sentScore.values()))/len(nltk.sent_tokenize(essay))
	
	return cumScore, sentScore
	



# TEST DRIVER FOR TESTING THE MODULE INDEPENDENTLY
if __name__ == '__main__':

	#open essay
	sourceFileName = "../Sample_Essays/essay3.txt"
	sourceFile = open(sourceFileName, "r")
	
	#read essay
	essay = sourceFile.read()
	
	cumscore, sentscore  = getGrammarScore(essay)
	
	for key in sentscore.keys():
		print key + " :: " + str(sentscore[key])
		print
	
	print cumscore

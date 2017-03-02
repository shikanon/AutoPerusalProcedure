#!/usr/bin/python

##
#	MAIN EXECUTING SCRIPT
#	@author karthik
#

from Statistics.Statistics import *
from Spellings.Spellings import *
from Grammar.Grammar import *
#from Coherence.Coherence import *
import sys
import webbrowser
from operator import itemgetter
import os



print "***************************************************************************"
print "***************************************************************************"

print '''
\t        ##            ########       ########
\t      ##  ##          ##             ##
\t     ##    ##         #####          ##
\t    ##########        #####          ##    ##
\t   ##        ##       ##             ##    ##
\t  ##          ##      #########      ########

'''

print '''
\t  DEVELOPED BY :-             GUIDED BY :-
\t
\t  Karthik R Prasad
\t  Aparna N                    Dr. B Narsing Rao
\t  Apoorva Rao B

'''

print "***************************************************************************\n\n"


#open essay
print "Enter the name(path) of file containing the Essay to be graded :: "
sourceFileName = str(raw_input(" >> "))
	#sourceFileName = str(sys.argv[1])
	#sourceFileName = "./Sample_Essays/essay2.txt"
sourceFile = open(sourceFileName, "r")

print
print

	#print "Enter the name(path) for the generated html report file :: "
	#outputFileName = str(raw_input(" >> "))
	#outputFileName = str(sys.argv[2])
	#outputFileName = sourceFileName.replace(".txt", ".html")
sourceFileBaseName = os.path.basename(sourceFileName)
outputFileName = "./Reports/" + os.path.splitext(sourceFileBaseName)[0] + ".html"

	


#read essay
essay = sourceFile.read()

print
print

print "::::::::::::::::::::::::::::::::YOUR ESSAY:::::::::::::::::::::::::::::::::::::"
print
print essay
print
print ":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
print
print "Please Wait while we generate statistics for your essay........"

#Statistics
wordCount = getWordCount(essay)
sentCount = getSentenceCount(essay)
paraCount = getParaCount(essay)
avgSentLen = getAvgSentenceLength(essay)
stdDevSentLen = getStdDevSentenceLength(essay)


print
print "Please Wait while we perform spell check on your essay........"

#Spellings
numMisspelt, misspeltWordSug = spellCheck(essay)


print
print "Please Wait while we analyse the Grammar and Structure of your essay........\n"

#Grammar
grammarCumScore, grammarSentScore = getGrammarScore(essay)


print
print "Please Wait while we analyse the Coherence of your essay........"

#Coherence
coherenceScore = 3 #getCoherenceMeasure(essay)

#Overall
overallScore = str(format((((1-(float(numMisspelt)/wordCount))*5) + grammarCumScore + coherenceScore)/3, '.2f'))
print ":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"



s = '''<!DOCTYPE html>
<html lang="en">

<head>
	<title>Automated Essay Grader</title>
	<meta charset ="utf-8" />
	<link type="text/css" rel = "stylesheet" href = "../style.css" />
</head>

<body>
	<div id = "canvas">
	<div>
		<div id = "heading"> <h1><center> AUTOMATED ESSAY GRADER </center></h1></div>
		<br />'''
	

s = s + '''<br /> <hr /> <hr /> <br />

		<div style="float:left; font-size:18pt" id = "scoretable">
			<img src = "../images/grade.jpg" />
			<h2> Overall Score</h2>
			<table border="1" align="right">
				<tr> <th class = "big">GRADE (0-5)</th> <th class = "big">''' + str(overallScore) + '''</th></tr>
				<tr> <th>Spelling(0-5)</th> <td>'''+str(format((1-(float(numMisspelt)/wordCount))*5,'.2f'))+'''</td></tr>
				<tr> <th>Grammar(0-5)</th> <td>'''+str(format(grammarCumScore,'.2f'))+'''</td></tr>
				<tr> <th>Coherence(0-5)</th> <td>'''+str(format(coherenceScore,'.2f'))+'''</td></tr>
			</table>
		</div>
		
		<div style="float:right" id = "statistics">
			<img src = "../images/stats.jpg" />
			<h2> Essay Statistics</h2>
			<table border = "1" align="left">
				<tr align='left'> <th>Word Count</th> <td>'''+ str(wordCount) + '''</td></tr>
				<tr align='left'> <th>Sentence Count</th> <td>'''+ str(sentCount) + '''</td></tr>
				<tr align='left'> <th>Paragraph Count</th> <td>'''+ str(paraCount) + '''</td></tr>
				<tr align='left'> <th>Average Sentence Length</th> <td>'''+ str(format(avgSentLen,'.2f')) + '''</td> </tr>
				<tr align='left'> <th>Standard Deviation from the Average Sentence Length</th> <td>'''+ str(format(stdDevSentLen,'.2f')) + '''</td> </tr>
			</table>
		</div>
	    </div>		
		
		<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /> <hr /> <hr /> <br />
		
		<div id = "spellings"> 
			<img src = "../images/spell.jpg" />
			<h2> Spellings </h2>
			<h3 style="text-align:left">Number of Misspelt Words ::''' + str(numMisspelt) + '''</h3>
			<h2 style="text-align:right" class="score" >Score :: ''' + str(format((1-(float(numMisspelt)/wordCount))*5,'.2f')) + '''</h2>
			
			<table border="1">
				<thead> <tr> <th>Misspelt Word</th> <th> Spelling Suggestions</th> </tr> </thead>
				<tbody>'''

for key in misspeltWordSug:
	s = s + "<tr> <td>" + key + "</td> <td> " + str(misspeltWordSug[key]) + "</td> </tr>"


s = s + '''</tbody>
			</table>
		</div>
		<br /> <hr /> <hr /> <br />
		
		<div id ="grammar">
			<img src = "../images/grammar.jpg" />
			<h2> Grammar </h2>
			<h2 style="text-align:right" class = "score" >Score :: ''' + str(format(grammarCumScore,'.2f')) + '''</h2>
			
			<table border="0">
				<thead> <tr> <th>Sentences</th> <th> Score</th> </tr> </thead>
				<tbody>'''
				
#for key in grammarSentScore:
#	s = s + "<tr> <td>" + key + "</td> <td> " + str(grammarSentScore[key]) + "</td> </tr>"

#prints sorted table
for key in reversed(sorted(list(grammarSentScore.items()), key=itemgetter(1))):
	s = s + "<tr> <td>" + key[0] + "</td> <td> " + str(key[1]) + "</td> </tr>"	
	
s = s + ''' </tbody>
			</table>
		</div>
		<br /> <hr /> <hr /> <br />
		
		<div id = "coherence">
			<img src = "../images/coherence.jpg" />
			<h2> Coherence </h2>
			<h2 class = "score" style="text-align:right"> Score :: ''' + str(format(coherenceScore,'.2f')) + '''</h2>'''
			
s = s + '''
			</div> <br /> <hr /> <hr /> <br />
		<div> 
		<img src = "../images/essay.jpg" />
		
		<h2> Essay </h2> <div id = "essay">'''

for para in essay.splitlines():
	if para == "":
		s = s + "<br /> <br />"
	else:
		s = s + para
	

s = s + '''</div></div> <br /> <hr /> <hr /> <br />
		<div id="conclusion">
			Karthik R Prasad, Aparna N, Apoorva Rao B<br /> Guide: Dr.B Narsing Rao
		</div>
		
	</div>
	
</body>

</html>


'''

outputFile = open(outputFileName,"w")
outputFile.write(s)

print
print

print "Essay has been Graded and the Score Report has been generated!!"
print "\n\nThank You for using our Automated Essay Grader\n"

print "***************************************************************************"
print "***************************************************************************"

webbrowser.open(outputFileName)



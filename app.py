#coding:utf8
from AutoPersual import check_essay
from flask import Flask
from flask import request, send_from_directory
from flask.ext.mako import MakoTemplates, TemplateError, render_template
import time
import codecs
import os

static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

mako = MakoTemplates()
app = Flask(__name__, static_url_path='')
mako.init_app(app)
app.config.setdefault('MAKO_TRANSLATE_EXCEPTIONS', False)

test = {'grammar': {'grammarCumScore': 2.8947368421052633, 'grammarSentScore': {'Dogs perform many roles for people, such as hunting, herding, pulling loads, protection, assisting police and military, companionship, and, more recently, aiding handicapped individuals.': 3, 'Through this selective breeding, the dog has developed into hundreds of varied breeds, and shows more behavioral and morphological variation than any other land mammal.': 3, 'The word "dog" may also mean the male of a canine species, as opposed to the word "bitch" for the female of the species.': 4, 'Most breeds of dogs are at most a few hundred years old, having been artificially selected for particular morphologies and behaviors by people for specific functional roles.': 4, 'In some cultures, dogs are also an important source of meat.': 5, 'The present lineage of dogs was domesticated from gray wolves about 15,000 years ago.': 2, 'The earlier specimens not only show shortening of the snout but widening of the muzzle and some crowding of teeth making them clearly domesticated dogs and not wolves.': 3, 'None of these early domestication lineages seem to have survived the Last Glacial Maximum.': 5, 'Although mDNA suggest a split between dogs and wolves around 100,000 years ago no specimens predate 33,000 years ago that are clearly morphologically domesticated dog.': 1, 'This impact on human society has given them the nickname "Man\'s Best Friend" in the Western world.': 5, 'The term "domestic dog" is generally used for both domesticated and feral varieties.': 2, 'For example, height measured to the withers ranges from a 2 inches (51 mm) in the Chihuahua to a 2 feet (0.61 m) in the Irish Wolfhound; color varies from white through grays (usually called "blue") to black, and browns from light (tan) to dark ("red" or "chocolate") in a wide variation of patterns; coats can be short or long, coarse-haired to wool-like, straight, curly, or smooth.': 1, "Dogs' value to early human hunter-gatherers led to them quickly becoming ubiquitous across world cultures.": 5, 'Dog\n\nThe domestic dog (Canis lupus familiaris), is a subspecies of the gray wolf (Canis lupus), a member of the Canidae family of the mammilian order "Carnivora".': 1, 'There are more sites of varying ages in and around Europe and Asia younger than 33,000 years ago but significantly older than 15,000 years ago.': 1, 'The dog may have been the first animal to be domesticated, and has been the most widely kept working, hunting, and companion animal in human history.': 3, 'In 2001, there were estimated to be 400 million dogs in the world.': 1, 'It is common for most breeds to shed this coat.': 5, 'Remains of domesticated dogs have been found in Siberia and Belgium from about 33,000 years ago.': 1}}, 'statistics': {'stdDevSentLen': 12.731403797668182, 'wordCount': 432, 'paraCount': 5, 'sentCount': 19, 'avgSentLen': 22.736842105263158}, 'spellings': {'Spellings': 5, 'misspeltWordSug': {'Canidae': ['Candidate', 'Candida', 'Candide', 'Canine', 'Canadian', 'Candle'], 'mammilian': ['mammalian', 'Maximilian', 'militiaman', 'Massimiliano', 'Macmillan', 'MacMillan', 'Maximilien'], 'mDNA': ['DNA', 'm DNA', 'myna', 'Edna', 'Medina', 'Medan'], 'Carnivora': ['Carnivore', 'Carnivorous', 'Carnival', 'California', 'Careworn', 'Canaveral', 'Conferral'], 'familiaris': ['familiars', 'familiar is', 'familiar-is', 'familiarizes', 'familiarize', 'familiarity', 'familiarness', 'familiarizing', 'malarious']}}, 'orgin_paper': 'Dog\n\nThe domestic dog (Canis lupus familiaris), is a subspecies of the gray wolf (Canis lupus), a member of the Canidae family of the mammilian order "Carnivora". The term "domestic dog" is generally used for both domesticated and feral varieties. The dog may have been the first animal to be domesticated, and has been the most widely kept working, hunting, and companion animal in human history. The word "dog" may also mean the male of a canine species, as opposed to the word "bitch" for the female of the species.\n\nThe present lineage of dogs was domesticated from gray wolves about 15,000 years ago. Remains of domesticated dogs have been found in Siberia and Belgium from about 33,000 years ago. The earlier specimens not only show shortening of the snout but widening of the muzzle and some crowding of teeth making them clearly domesticated dogs and not wolves. There are more sites of varying ages in and around Europe and Asia younger than 33,000 years ago but significantly older than 15,000 years ago. None of these early domestication lineages seem to have survived the Last Glacial Maximum. Although mDNA suggest a split between dogs and wolves around 100,000 years ago no specimens predate 33,000 years ago that are clearly morphologically domesticated dog.\n\nDogs\' value to early human hunter-gatherers led to them quickly becoming ubiquitous across world cultures. Dogs perform many roles for people, such as hunting, herding, pulling loads, protection, assisting police and military, companionship, and, more recently, aiding handicapped individuals. This impact on human society has given them the nickname "Man\'s Best Friend" in the Western world. In some cultures, dogs are also an important source of meat. In 2001, there were estimated to be 400 million dogs in the world.\n\nMost breeds of dogs are at most a few hundred years old, having been artificially selected for particular morphologies and behaviors by people for specific functional roles. Through this selective breeding, the dog has developed into hundreds of varied breeds, and shows more behavioral and morphological variation than any other land mammal. For example, height measured to the withers ranges from a 2 inches (51 mm) in the Chihuahua to a 2 feet (0.61 m) in the Irish Wolfhound; color varies from white through grays (usually called "blue") to black, and browns from light (tan) to dark ("red" or "chocolate") in a wide variation of patterns; coats can be short or long, coarse-haired to wool-like, straight, curly, or smooth. It is common for most breeds to shed this coat.\n'}




@app.route('/upload', methods=["GET", "POST"])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        eassy = file.read()
        if not eassy:
            return render_template('index.html')
        if eassy[:3] == codecs.BOM_UTF8:
            eassy = eassy[3:]
        check_result = check_essay(eassy)
        print(check_result)
        try:
            return render_template('demo.html', **check_result)
        except Exception as e:
            print(e.text)


    return render_template('index.html')

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('templates/css', path)

@app.route('/image/<path:path>')
def send_image(path):
    return send_from_directory('templates/image', path)
        

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=10101,debug=True)

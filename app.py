#coding:utf8
# from Statistics.Statistics import *
# from Spellings.Spellings import *
# from Grammar.Grammar import *
from flask import Flask
import json
import time
import sys
from operator import itemgetter
import os
from flask import render_template, request, send_from_directory

static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

app = Flask(__name__, static_url_path='')

def strQ2B(ustring):
    """全角转半角"""
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 12288:#全角空格直接转换
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374): #全角字符（除空格）根据关系转化
            inside_code -= 65248

        rstring += unichr(inside_code)
    rstring = rstring.encode("utf-8")
    return rstring

def deal_txt(ustring):
    rstring = ""
    for uchar in ustring:
        if ord(uchar) < 9632:
            rstring += uchar
    return rstring

@app.route('/')
# def hello_world():
#     #性能测试
#     start_time = time.time()
#     # 读取文件
#     with open('./Sample_Essays/dog.txt', 'r') as f:
#         essay = f.read()
#     # 文本处理
#     essay = strQ2B(essay)
#     essay = deal_txt(essay)
#     result = dict()
#     result['orgin_paper'] = essay
#     # 统计信息
#     wordCount = getWordCount(essay)
#     sentCount = getSentenceCount(essay)
#     paraCount = getParaCount(essay)
#     avgSentLen = getAvgSentenceLength(essay)
#     stdDevSentLen = getStdDevSentenceLength(essay)
#     result['statistics'] = {
#         'wordCount': wordCount,
#         'sentCount': sentCount,
#         'paraCount': paraCount,
#         'avgSentLen': avgSentLen,
#         'stdDevSentLen': stdDevSentLen
#     }
#     # 拼写检查
#     numMisspelt, misspeltWordSug = spellCheck(essay)
#     result['spellings'] = {
#         'Spellings': numMisspelt,
#         'misspeltWordSug': misspeltWordSug
#     }
#     # 语法检查
#     grammarCumScore, grammarSentScore = getGrammarScore(essay)
#     result['grammar'] = {
#         'grammarCumScore': grammarCumScore,
#         'grammarSentScore': grammarSentScore
#     }
#     print('total time:%f'%(time.time()-start_time))
#
#     return json.dumps(result)

@app.route('/upload', methods=["GET", "POST"])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        eassy = file.read()
        print eassy

    return render_template('demo.html')

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('templates/css', path)

@app.route('/image/<path:path>')
def send_image(path):
    return send_from_directory('templates/image', path)
        

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=10101,debug=True)

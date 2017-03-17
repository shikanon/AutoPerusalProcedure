# coding:utf8
from Statistics.Statistics import *
from Spellings.Spellings import *
from Grammar.Grammar import *
import time


def strQ2B(ustring):
    """全角转半角"""
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 12288:  # 全角空格直接转换
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374):  # 全角字符（除空格）根据关系转化
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


def mark_score(check_result):
    check_result['grammar']['grammarCumScore'] = check_result['grammar']['grammarCumScore'] * 100 / 5
    if check_result['statistics']['avgSentLen'] > 10:
        check_result['statistics']['statisticsScore'] = 100
    else:
        check_result['statistics']['statisticsScore'] = check_result['statistics']['avgSentLen'] * 10
    if check_result['spellings']['Spellings'] > 10:
        check_result['spellings']['spellingScore'] = 0
    else:
        check_result['spellings']['spellingScore'] = (10 - check_result['spellings']['Spellings']) * 10
    check_result['totalScore'] = (check_result['grammar']['grammarCumScore'] + check_result['statistics'][
        'statisticsScore'] + \
                                  check_result['statistics']['statisticsScore']) / 3
    return check_result


def check_essay(essay):
    # 性能测试
    start_time = time.time()
    # 文本处理
    print(type(essay))
    if isinstance(essay, str):
        essay = essay.decode('utf8')
    essay = strQ2B(essay)
    essay = deal_txt(essay)
    print(essay)
    result = dict()
    result['orgin_paper'] = essay
    # 统计信息
    wordCount = getWordCount(essay)
    sentCount = getSentenceCount(essay)
    paraCount = getParaCount(essay)
    avgSentLen = getAvgSentenceLength(essay)
    stdDevSentLen = getStdDevSentenceLength(essay)
    result['statistics'] = {
        'wordCount': wordCount,
        'sentCount': sentCount,
        'paraCount': paraCount,
        'avgSentLen': avgSentLen,
        'stdDevSentLen': stdDevSentLen
    }
    # 拼写检查
    numMisspelt, misspeltWordSug = spellCheck(essay)
    result['spellings'] = {
        'Spellings': numMisspelt,
        'misspeltWordSug': misspeltWordSug
    }
    # 语法检查
    grammarCumScore, grammarSentScore = getGrammarScore(essay)
    result['grammar'] = {
        'grammarCumScore': grammarCumScore,
        'grammarSentScore': grammarSentScore
    }
    result = mark_score(result)
    print('total time:%f' % (time.time() - start_time))

    return result


def wechat_check_essay(essay):
    check_result = check_essay(essay)
    totalScore = u'总得分:' + str(check_result['totalScore']) + ';\n'
    spellingScore = u'拼写得分:' + str(check_result['spellings']['spellingScore']) + ';\n'
    return [totalScore, spellingScore, u'详细报告见：useease英文作文评分网 http://aeg.useease.com:9000/upload']

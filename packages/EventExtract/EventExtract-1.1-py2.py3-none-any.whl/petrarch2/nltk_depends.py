# coding=utf-8


'''
本代码块主要用于 ：
       1.获取依存关系
       2.依存conll数据与原句映射
'''

import os
from nltk.parse.stanford import StanfordDependencyParser   # # 依存句法分析

# 指定stanford环境变量,jar包的存放目录
path = os.getcwd()
path = path + '\\jars\\stnlkt\\'
# print path
os.environ['STANFORD_PARSER'] = path
os.environ['STANFORD_MODELS'] = path

# 英文依存关系实例化，StanfordDependencyParser init ...
dep_parser = StanfordDependencyParser(model_path=u'edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz')


def nltk_st_depends(sent):
    ''' 输出依存关系 '''
    conll_dict, word_dict = {}, {}
    if sent:
        parse, = dep_parser.raw_parse(sent)
        # conll4 依赖格式 # conll_4数据 = [词，词性，父序，关系]
        conll_4 = parse.to_conll(4).split('\n')
        conll_4.pop()  # 删除最后一个空元素
        # conll10 依赖格式
        conll_10 = parse.to_conll(10).split('\n')
        conll_10.pop()  # 删除最后一个空元素

        for i, row_10 in enumerate(conll_10):
            row_10 = row_10.split('\t')
            row_4 = conll_4[i].split('\t')
            # conll词序 = {conll_10词序：conll_4数据}
            conll_dict[row_10[0]] = row_4
            # 顺序词序 = {原句顺序：conll_10词序，conll_4数据}
            word_dict[i + 1] = [row_10[0]]
            word_dict[i + 1] += row_4
            # print word_dict[i + 1]
    return conll_dict, word_dict


def modify_order(sentorder):
    ''' 修正句子的词序 与 依存关系词序匹配
        依存词中缺少标点，所以排序词比原句排序少.
        去掉标点的重新排序
        返回： 原句No --> conll No
        结果从1开始
    '''
    w_dict = {}
    if sentorder and isinstance(sentorder, list):
        word_no = 1
        for v_word in sentorder:
            if v_word[1] != '' and isinstance(v_word, tuple):
                if v_word[1] in ['``', '`', '-', ',', '!', '?', '\"', '\'', '.', ':', '\'\'', '-LRB-', '-RRB-']:
                    continue
                w_dict[v_word[0]] = (word_no, v_word[1])
                # print word_no, w_dict[v_word[0]] #对应关系检查
                word_no += 1
    return w_dict


if __name__ == '__main__':
    # 原始测试代码：
    text = "Croatia also counts on Italy's support for Croatia's bid to join the OECD."
    print "需要分析的句子：\n", text

    print "===================> 英文依存关系实例化，StanfordDependencyParser init ..."
    dep_parser = StanfordDependencyParser(model_path=u'edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz')
    print "===================> 依赖分析器"
    parse, = dep_parser.raw_parse(text)
    print "===================> parse.to_conll(n=4)"
    print(parse.to_conll(4))
    print "===================> parse.to_conll(n=10)"
    print(parse.to_conll(10))
    print "依存树打印："
    test_tree = parse.tree()
    print(parse.tree())

    # print "测试 nltk_st_depends()："
    # text = "A task force created by the College acknowledged that the drug industry's interests are \"not always aligned with the best interests\" of family doctors or their patients."
    # conll_dc, word_dc = nltk_st_depends(text)
    # print "============================> conll依存排序:"
    # print "conll order: ", conll_dc
    # for key in conll_dc:
    #     print key, conll_dc[key]
    # print "============================> conll顺序排序:"
    # print "word order: ", word_dc
    # for key in word_dc:
    #     print key, word_dc[key]
    #
    # print "测试 change_order_to_depends():"
    # sentorder = [(1, u'A'), (2, u'TASK'), (3, u'FORCE'), (4, u'CREATED'), (5, u'BY'), (6, u'THE'), (7, u'COLLEGE'), (8, u'ACKNOWLEDGED'), (9, u'THAT'), (10, u'THE'), (11, u'DRUG'), (12, u'INDUSTRY'), (13, u"'S"), (14, u'INTERESTS'), (15, u'ARE'), (16, u'``'), (17, u'NOT'), (18, u'ALWAYS'), (19, u'ALIGNED'), (20, u'WITH'), (21, u'THE'), (22, u'BEST'), (23, u'INTERESTS'), (24, u"''"), (25, u'OF'), (26, u'FAMILY'), (27, u'DOCTORS'), (28, u'OR'), (29, u'THEIR'), (30, u'PATIENTS'), (31, u'.')]
    # # for v_row in sentorder:
    # #     print v_row
    # print "============================> 原句修正排序:"
    # xz_order = modify_order(sentorder)
    # for key in xz_order:
    #     print key, " = ", xz_order[key]



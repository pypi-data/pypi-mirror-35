# coding=utf-8

from nltk_depends import nltk_st_depends, modify_order

# 1 # 人称代词 Personal Pronouns
PRP_dict = {
    'frist': ['I', 'me', 'we', 'us'],
    'second': ['you'],
    'third': ['she', 'her', 'he','him', 'they', 'them','it']
}
# 说明 :人称代词是表示"我"、"你"、"他"、"她"、"它"、"我们"、"你们"、"他们"的词。是表示自身或人称的代词。
# She is a little girl.她是一个小女孩。

# 2 # 物主代词 Possessive Pronouns : 形容词性物主代词， 名词性物主代词
POP_dict = {
    'frist': ['my', 'mine'],
    'second': ['your','yours'],
    'third': ['his', 'her', 'hers','its', 'our', 'ours','their','theirs']
}
# 说明 :表示所有关系的代词叫做物主代词,可分为两种。
# I love my country.我热爱我的国家。
# That car is mine,not yours.那辆汽车是我的，不是你的。

# 3 # 反身代词
POP_dict = {
    'frist': ['myself', 'ourselves'],
    'second': ['yourself','yourselves'],
    'third': ['himself', 'herself', 'themselves','itself']
}
# 说明 :反身代词可用作宾语，表语，主语的同位语和宾语的同位语。用作同位语时表示强调"本人，自己"。
# You should ask the children themselves.你应该问一问孩子们自己。

# 4 # 指示代词 this, that, these, those, such, some
# 5 # 疑问代词 who, whom, whose, which, what, whoever, whichever, whatever
# 6 #  关系代词 that, which, who, whom, whose, as
# 7 #  不定代词 one/ some/ any, each/ every, none/ no, many/ much, few/ little/ a few/ a little, other/ another, all/ both, neither/ either


def sent_model_judge(verb_info, conll_dict, word_dict, sent_dict):
    ''' 判断特殊句式 '''
    # 是否verb 是否 say said
    pass


def RBP_find(RBPword, verb_info, conll_dict, word_dict, sent_dict):
    ''' 寻找人称代词的root '''
    pass


def evt_loc_judge(RBPword, verb_info, conll_dict, word_dict, sent_dict):
    ''' 判断发生地 '''
    pass


def sent_NP_dind(actorType, verb_info, conll_dict, word_dict, sent_dict):
    ''' 寻找特定的名词 '''
    actor_str = []
    if actorType == 'ACT':
        pass
    elif actorType == 'TAR':
        pass
    return actor_str

def evt_verb_judge(actorStr, targetStr, verb_info, evtloc):
    '''
    四要素: 发起者，承受者，性质verb，地点
    当只识别了性质verb时，判断时间是否有效事件
    返回：
        True 无效事件
    '''
    flag_evt = False
    # 非特定动词，且没有事件发生地
    # 暂时未实现该分支
    pass
    # 发起者，承受者，地点 不存在，返回数据为事件为无效
    if not (actorStr or targetStr or evtloc):
        flag_evt = True

    return flag_evt


if __name__ == '__main__':
    print "gogo"
    # A say B attact C  -->  A SAY B, A SAY C, B attact C
    test_sent = "The Foreign Minister said \"Japan's army attacked the United States.\""

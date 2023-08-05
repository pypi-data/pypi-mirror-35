# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import os
import sys
import glob
import time
import random
import logging
import threading
from queue import Queue
import jpype
import argparse
from multiprocessing import Process, freeze_support, Queue, Lock

from constants import MULTI_PROCESS_CONFIG, MULTI_PROCESS_LOG_DIR
from session_factory import Session
from langid.langid import LanguageIdentifier, model

# petrarch.py
##
# Automated event data coder
##
# SYSTEM REQUIREMENTS
# This program has been successfully run under Mac OS 10.10; it is standard Python 2.7
# so it should also run in Unix or Windows.
#
# INITIAL PROVENANCE:
# Programmers:
#             Philip A. Schrodt
#			  Parus Analytics
#			  Charlottesville, VA, 22901 U.S.A.
#			  http://eventdata.parusanalytics.com
#
#             John Beieler
#			  Caerus Associates/Penn State University
#			  Washington, DC / State College, PA, 16801 U.S.A.
#			  http://caerusassociates.com
#             http://bdss.psu.edu
#
# GitHub repository: https://github.com/openeventdata/petrarch
#
# Copyright (c) 2014	Philip A. Schrodt.	All rights reserved.
#
# This project is part of the Open Event Data Alliance tool set; earlier developments
# were funded in part by National Science Foundation grant SES-1259190
#
# This code is covered under the MIT license
#
# Report bugs to: schrodt735@gmail.com
#
# REVISION HISTORY:
# 22-Nov-13:	Initial version
# Summer-14:	Numerous modifications to handle synonyms in actor and verb dictionaries
# 20-Nov-14:	write_actor_root/text added to parse_Config
# ------------------------------------------------------------------------

import PETRglobals  # global variables
import PETRreader  # input routines
import PETRwriter
import utilities
import PETRtree
import databasewriter
import access_solr
import GetInfo
import constants
from write_file import write_multiprocess_log
from read_file import read_key_value_file, read_other

# ========================== VALIDATION FUNCTIONS ========================== #

def get_version():
    return "1.2.0"


# ========================== OUTPUT/ANALYSIS FUNCTIONS ========================== #

def open_tex(filename):
    fname = open(filename, 'w')
    '''fname.write('Run time: ',
    print("""
\\documentclass[11pt]{article}
\\usepackage{tikz-qtree}
\\usepackage{ifpdf}
\\usepackage{fullpage}
\\usepackage[landscape]{geometry}
\\ifpdf
    \\pdfcompresslevel=9
    \\usepackage[pdftex,     % sets up hyperref to use pdftex driver
            plainpages=false,   % allows page i and 1 to exist in the same document
            breaklinks=true,    % link texts can be broken at the end of line
            colorlinks=true,
            pdftitle=My Document
            pdfauthor=My Good Self
           ]{hyperref}
    \\usepackage{thumbpdf}
\\else
    \\usepackage{graphicx}       % to include graphics
    \\usepackage{hyperref}       % to simplify the use of \href
\\fi

\\title{Petrarch Output}
\\date{}

\\begin{document}
""", file = fname)'''

    return fname


def close_tex(fname):

    return
    print("\n\\end{document})", file=fname)


# ========================== PRIMARY CODING FUNCTIONS ====================== #


def check_discards(SentenceText):
    """
    Checks whether any of the discard phrases are in SentenceText, giving
    priority to the + matches. Returns [indic, match] where indic
       0 : no matches
       1 : simple match
       2 : story match [+ prefix]
    """
    sent = SentenceText.upper().split()  # case insensitive matching
    #size = len(sent)
    level = PETRglobals.DiscardList
    depart_index = [0]
    discardPhrase = ""

    for i in range(len(sent)):

        if '+' in level:
            return [2, '+ ' + discardPhrase]
        elif '$' in level:
            return [1, ' ' + discardPhrase]
        elif sent[i] in level:
            # print(sent[i],SentenceText.upper(),level[sent[i]])
            depart_index.append(i)
            level = level[sent[i]]
            discardPhrase += " " + sent[i]
        else:
            if len(depart_index) == 0:
                continue
            i = depart_index[0]
            level = PETRglobals.DiscardList
    return [0, '']


def get_issues(SentenceText):
    """
    Finds the issues in SentenceText, returns as a list of [code,count]

    <14.02.28> stops coding and sets the issues to zero if it finds *any*
    ignore phrase

    """
    def recurse(words, path, length):
        if '#' in path:  # <16.06.06 pas> Swapped the ordering if these checks since otherwise it crashes when '#' is a "word" in the text
            return path['#'], length
        elif words and words[0] in path:
            return recurse(words[1:], path[words[0]], length + 1)
        return False

    sent = SentenceText.upper().split()  # case insensitive matching
    issues = []

    index = 0
    while index < len(sent):
        match = recurse(sent[index:], PETRglobals.IssueList, 0)
        if match:
            index += match[1]
            code = PETRglobals.IssueCodes[match[0]]
            if code[0] == '~':  # ignore code, so bail
                return []
            ka = 0
            #gotcode = False
            while ka < len(issues):
                if code == issues[ka][0]:
                    issues[ka][1] += 1
                    break
                ka += 1
            if ka == len(issues):  # didn't find the code, so add it
                issues.append([code, 1])
        else:
            index += 1
    return issues


def do_coding(event_dict):
    """
    Main coding loop Note that entering any character other than 'Enter' at the
    prompt will stop the program: this is deliberate.
    <14.02.28>: Bug: PETRglobals.PauseByStory actually pauses after the first
                sentence of the *next* story
    """

    treestr = ""

    NStory = 0
    NSent = 0
    NEvents = 0
    NEmpty = 0
    NDiscardSent = 0
    NDiscardStory = 0

    logger = logging.getLogger('petr_log')
    times = 0
    sents = 0
    for key, val in sorted(event_dict.items()):
        NStory += 1
        prev_code = []

        SkipStory = False
        print('\n\nProcessing story {}'.format(key))
        StoryDate = event_dict[key]['meta']['date']
        for sent in val['sents']:
            NSent += 1
            if 'parsed' in event_dict[key]['sents'][sent]:
                if 'config' in val['sents'][sent]:
                    for _, config in event_dict[key]['sents'][sent]['config'].items():
                        change_Config_Options(config)

                SentenceID = '{}_{}'.format(key, sent)
                SentenceText = event_dict[key]['sents'][sent]['content']
                SentenceDate = event_dict[key]['sents'][sent][
                    'date'] if 'date' in event_dict[key]['sents'][sent] else StoryDate
                Date = PETRreader.dstr_to_ordate(SentenceDate)

                print("\n", SentenceID)
                parsed = event_dict[key]['sents'][sent]['parsed']
                treestr = parsed
                # disc = check_discards(SentenceText)
                # if disc[0] > 0:
                #     if disc[0] == 1:
                #         print("Discard sentence:", disc[1])
                #         logger.info('\tSentence discard. {}'.format(disc[1]))
                #         NDiscardSent += 1
                #         continue
                #     else:
                #         print("Discard story:", disc[1])
                #         logger.info('\tStory discard. {}'.format(disc[1]))
                #         SkipStory = True
                #         NDiscardStory += 1
                #         break

                # 20171202 ner
                nerjson = event_dict[key]['sents'][sent]['ner_list']
                t1 = time.time()
                sentence = PETRtree.Sentence(treestr, SentenceText, Date, nerjson)
                code_env = read_other('Solr_info.ini', 'WINCODE', 'CMDcode')
                if code_env:
                   print(sentence.txt.encode(code_env, 'ignore'))
                # this is the entry point into the processing in PETRtree
                coded_events, meta = sentence.get_events()
                code_time = time.time() - t1
                if PETRglobals.NullVerbs or PETRglobals.NullActors:
                    event_dict[key]['meta'] = meta
                    event_dict[key]['text'] = sentence.txt
                elif PETRglobals.NullActors:
                    event_dict[key]['events'] = coded_events
                    coded_events = None   # skips additional processing
                    event_dict[key]['text'] = sentence.txt
                else:
                    # 16.04.30 pas: we're using the key value 'meta' at two
                    # very different
                    event_dict[key]['meta']['verbs'] = meta
                    # levels of event_dict -- see the code about ten lines below -- and
                    # this is potentially confusing, so it probably would be useful to
                    # change one of those

                # 取出event_verbno字典 20171227
                event_verbno = sentence.event_verbno

                del(sentence)
                times += code_time
                sents += 1
                # print('\t\t',code_time)

                if coded_events:
                    event_dict[key]['sents'][sent]['events'] = coded_events
                    event_dict[key]['sents'][sent]['meta'] = meta
                    # 将event_verbno字典存储到event_dict当中 20171227
                    event_dict[key]['sents'][sent]['event_verbno'] = event_verbno
                    #print('DC-events:', coded_events) # --
                    #print('DC-meta:', meta) # --
                    #print('+++',event_dict[key]['sents'][sent])  # --
                    if PETRglobals.WriteActorText or PETRglobals.WriteEventText or PETRglobals.WriteActorRoot:
                        text_dict = utilities.extract_phrases(event_dict[key]['sents'][sent], SentenceID)

                        ##########################################
                        PETRglobals.detail_dict.append(text_dict)
                        ##########################################

# --                        print('DC-td1:',text_dict) # --
                        if text_dict:
                            event_dict[key]['sents'][sent][
                                'meta']['actortext'] = {}
                            event_dict[key]['sents'][sent][
                                'meta']['eventtext'] = {}
                            event_dict[key]['sents'][sent][
                                'meta']['actorroot'] = {}
# --                            print('DC1:',text_dict) # --
                            for evt in coded_events:
                                if evt in text_dict:  # 16.04.30 pas bypasses problems with expansion of compounds
                                    event_dict[key]['sents'][sent]['meta'][
                                        'actortext'][evt] = text_dict[evt][:2]
                                    event_dict[key]['sents'][sent]['meta'][
                                        'eventtext'][evt] = text_dict[evt][2]
                                    event_dict[key]['sents'][sent]['meta'][
                                        'actorroot'][evt] = text_dict[evt][3:5]

                if coded_events and PETRglobals.IssueFileName != "":
                    event_issues = get_issues(SentenceText)
                    if event_issues:
                        event_dict[key]['sents'][sent]['issues'] = event_issues

                if PETRglobals.PauseBySentence:
                    if len(input("Press Enter to continue...")) > 0:
                        sys.exit()
                prev_code = coded_events
                # 修改coded_events为None时无法计算len的场景 20180103
                if coded_events:
                    NEvents += len(coded_events)
                else:
                    # if len(coded_events) == 0
                    NEmpty += 1
            else:
                logger.info('{} has no parse information. Passing.'.format(SentenceID))
                pass

        if SkipStory:
            event_dict[key]['sents'] = None

    print("\nSummary:")
    print(
        "Stories read:",
        NStory,
        "   Sentences coded:",
        NSent,
        "  Events generated:",
        NEvents)
    print(
        "Discards:  Sentence",
        NDiscardSent,
        "  Story",
        NDiscardStory,
        "  Sentences without events:",
        NEmpty)
    print("Average Coding time = ", times / sents if sents else 0)
# --    print('DC-exit:',event_dict)
    return event_dict


def parse_cli_args():
    """Function to parse the command-line arguments for PETRARCH2."""
    __description__ = """
PETRARCH2
(https://openeventdata.github.io/) (v. 1.0.0)
    """
    aparse = argparse.ArgumentParser(prog='petrarch2',
                                     description=__description__)

    sub_parse = aparse.add_subparsers(dest='command_name')

    parse_command = sub_parse.add_parser('parse', help=""" DEPRECATED Command to run the
                                         PETRARCH parser. Do not use unless you've used it before. If you need to
                                         process unparsed text, see the README""",
                                         description="""DEPRECATED Command to run the
                                         PETRARCH parser. Do not use unless you've used it before.If you need to
                                         process unparsed text, see the README""")
    parse_command.add_argument('-i', '--inputs',
                               help='File, or directory of files, to parse.',
                               required=True)
    parse_command.add_argument('-P', '--parsed', action='store_true',
                               default=False, help="""Whether the input
                               document contains StanfordNLP-parsed text.""")
    parse_command.add_argument('-o', '--output',
                               help='File to write parsed events.',
                               required=True)
    parse_command.add_argument('-c', '--config',
                               help="""Filepath for the PETRARCH configuration
                               file. Defaults to PETR_config.ini""",
                               required=False)

    batch_command = sub_parse.add_parser('batch', help="""Command to run a batch
                                         process from parsed files specified by
                                         an optional config file.""",
                                         description="""Command to run a batch
                                         process from parsed files specified by
                                         an optional config file.""")
    batch_command.add_argument('-c', '--config',
                               help="""Filepath for the PETRARCH configuration
                               file. Defaults to PETR_config.ini""",
                               required=False)

    batch_command.add_argument('-i', '--inputs',
                               help="""Filepath for the input XML file. Defaults to
                               data/text/Gigaword.sample.PETR.xml""",
                               required=False)

    batch_command.add_argument('-o', '--outputs',
                               help="""Filepath for the input XML file. Defaults to
                               data/text/Gigaword.sample.PETR.xml""",
                               required=False)

    batch_command = sub_parse.add_parser('javainfo', help="""This command is called by the java program.""",
                                         description="""Command to input story information""")
    batch_command.add_argument('-c', '--config',
                               help="""Filepath for the PETRARCH configuration
                               file. Defaults to PETR_config.ini""",
                               required=False)

    batch_command.add_argument('-i', '--inputs',
                               help="""Filepath for the input XML file. Defaults to
                               data/text/Gigaword.sample.PETR.xml""",
                               required=False)

    batch_command.add_argument('-o', '--outputs',
                               help="""Filepath for the input XML file. Defaults to
                               data/text/Gigaword.sample.PETR.xml""",
                               required=False)

    # add cmd to java info ,begin
    javainfo_command = sub_parse.add_parser('javainfo', help="""This command is called by the java program.""",
                                            description="""Command to get story information""")
    javainfo_command.add_argument('-c', '--config',
                                   help="""Filepath for the PETRARCH configuration
                                   file. Defaults to PETR_config.ini""",
                                   required=False)
    javainfo_command.add_argument('-i', '--inputs',
                                   help='File, or directory of files, to parse.',
                                   required=False)
    javainfo_command.add_argument('-o', '--outputs',
                                  help='File to write parsed events.',
                                  required=False)
    javainfo_command.add_argument('story_id')
    javainfo_command.add_argument('story_url')
    javainfo_command.add_argument('story_date')
    javainfo_command.add_argument('story_src')
    javainfo_command.add_argument('story_title')
    javainfo_command.add_argument('story_content')
    # add cmd to java info ,end

    # miaoweixin added begin
    background_command = sub_parse.add_parser('background', help="""This command is called by the calling program.""",
                                              description="""Command to run in background in an infinite loop""")
    background_command.add_argument('-c', '--config',
                                    help="""Filepath for the PETRARCH configuration
                                    file. Defaults to PETR_config.ini""",
                                    required=False)
    background_command.add_argument('-i', '--inputs',
                                    help='File, or directory of files, to parse.',
                                    required=False)
    background_command.add_argument('-o', '--outputs',
                                    help='File to write parsed events.',
                                    required=False)
    # miaoweixin added end

    nulloptions = aparse.add_mutually_exclusive_group()

    nulloptions.add_argument(
        '-na',
        '--nullactors', action='store_true', default=False,
        help="""Find noun phrases which are associated with a verb generating  an event but are
                                not in the dictionary; an integer giving the maximum number of words follows the command.
                                Does not generate events. """,
        required=False)

    nulloptions.add_argument('-nv', '--nullverbs',
                             help="""Find verb phrases which have source and
                               targets but are not in the dictionary. Does not generate events. """,
                             required=False, action="store_true", default=False)

    args = aparse.parse_args()
    return args


def main():
    print("=============> main() ==> run start, get cmd.")
    cli_args = parse_cli_args()

    # miaoweixin added begin
    # 作为后台程序无限循环运行
    if cli_args.command_name == 'background':
        try:
              
            # infinite loop
            run_in_background(cli_args)
        except KeyboardInterrupt:
            print("Program exited due to keyboard interrupt.\n")
            return None
    # miaoweixin added end

    print("Finished")


Thread_id = 1
Thread_num = 3
class consumer(threading.Thread):
    def __init__(self, q,cli_args,multi_log_lock,identifier,session,out,threadLock,jvm_started):
        global Thread_id
        threading.Thread.__init__(self)
        self.q = q
        self.Thread_id = Thread_id
        self.cli_args=cli_args
        self.multi_log_lock=multi_log_lock
#         self.obj_EvtInfo=obj_EvtInfo
        self.identifier=identifier
        Thread_id = Thread_id + 1
        self.session=session
        self.out=out
        self.threadLock=threadLock
        self.jvm_started=jvm_started
        print("=====线程id",Thread_id)
    def run(self):
#         print("======>create a jvm")   
#         obj_EvtInfo = GetInfo.GetInfoForEvt(jars=constants.JARS_DIR, mark_time_ranges=True)  
#         print("======>jvm is ok")
        while True:
            try:
                                
                task = self.q.get(block = True, timeout = 50) #不设置阻塞的话会一直去尝试获取资源
                print("cosumer",task)
                if not self.jvm_started:
                    _classpath = create_classpath()
                    start_jvm(_classpath)
                    EvtInfoWrapper = jpype.JClass('cetc28.stanfordutils.StanfordUtils')
                    
                    self.getinfo = EvtInfoWrapper
#                 self.threadLock.acquire()                      
                process_task(task, self.out, self.multi_log_lock, self.session, self.identifier,self.getinfo)
                self.jvm_started = True
#                 self.threadLock.release()
                              
            except self.q.empty():
                continue

class producer(threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q
        self.i=1
        self.id="1"
#         self.threadLock=threadLock
    def run(self):
        while True: 
            self.i+=1
            print("===producer",self.i)
            tmp_list = access_solr.read_stories(1,self.id)
#             self.threadLock.release()
            print("tmplist",tmp_list[0])     
            self.q.put(tmp_list[0],block = True)
            
            self.id=tmp_list[0]["id"]
            
            print ("===========>id",self.id)
#             time.sleep(8)
            


def run_in_background(cli_args):
    print("=============> run_in_background() ==> start")
    threadLock = threading.Lock()
    multi_log_lock = Lock()      
    q = Queue(10)
    
#向资源池里面放10个数用作测试
    pro = producer(q)
    pro.start()
    
    
    print("======>process_target() ==> start ")
    # 打印子进程启动消息
    write_multiprocess_log(multi_log_lock, '{}Process {}: {}'.format(u'', os.getpid(), u'started.'))

    # 子进程先读取进程运行所需各种信息
    utilities.init_logger()
    logger = logging.getLogger('petr_log')

    PETRglobals.RunTimeString = time.asctime()

    if cli_args.config:
        print('Using user-specified config: {}'.format(cli_args.config))
        logger.info(
            'Using user-specified config: {}'.format(cli_args.config))
        PETRreader.parse_Config(cli_args.config)
    else:
        logger.info('Using default config file.')
        PETRreader.parse_Config(utilities._get_data('data/config/',
                                                    'PETR_config.ini'))

    if cli_args.nullverbs:
        print('Coding in null verbs mode; no events will be generated')
        logger.info(
            'Coding in null verbs mode; no events will be generated')
        # Only get verb phrases that are not in the dictionary but are
        # associated with coded noun phrases
        PETRglobals.NullVerbs = True
    elif cli_args.nullactors:
        print('Coding in null actors mode; no events will be generated')
        logger.info(
            'Coding in null verbs mode; no events will be generated')
        # Only get actor phrases that are not in the dictionary but
        # associated with coded verb phrases
        PETRglobals.NullActors = True
        PETRglobals.NewActorLength = int(cli_args.nullactors)
    print("======>process_target() ==> read_dictionaries() ")
    read_dictionaries()
    print('\n\n')
    out = ""  # PETRglobals.EventFileName
    if cli_args.outputs:
        out = cli_args.outputs   

    identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True) 
    print("======>create a db session")
    session = Session()
    print("======>db session is ok") 
#开Thread_num个线程 
    print("consumer")
    
    for i in range(0, 1): 
        jvm_started=False       
        worker = consumer(q,cli_args,multi_log_lock,identifier,session,out,threadLock,jvm_started)
        worker.start() 




def process_target(queue, cli_args, multi_log_lock):
    print("======>process_target() ==> start ")
    # 打印子进程启动消息
    write_multiprocess_log(multi_log_lock, '{}Process {}: {}'.format(u'', os.getpid(), u'started.'))

    # 子进程先读取进程运行所需各种信息
    utilities.init_logger()
    logger = logging.getLogger('petr_log')

    PETRglobals.RunTimeString = time.asctime()

    if cli_args.config:
        print('Using user-specified config: {}'.format(cli_args.config))
        logger.info(
            'Using user-specified config: {}'.format(cli_args.config))
        PETRreader.parse_Config(cli_args.config)
    else:
        logger.info('Using default config file.')
        PETRreader.parse_Config(utilities._get_data('data/config/',
                                                    'PETR_config.ini'))

    if cli_args.nullverbs:
        print('Coding in null verbs mode; no events will be generated')
        logger.info(
            'Coding in null verbs mode; no events will be generated')
        # Only get verb phrases that are not in the dictionary but are
        # associated with coded noun phrases
        PETRglobals.NullVerbs = True
    elif cli_args.nullactors:
        print('Coding in null actors mode; no events will be generated')
        logger.info(
            'Coding in null verbs mode; no events will be generated')
        # Only get actor phrases that are not in the dictionary but
        # associated with coded verb phrases
        PETRglobals.NullActors = True
        PETRglobals.NewActorLength = int(cli_args.nullactors)
    print("======>process_target() ==> read_dictionaries() ")
    read_dictionaries()
    print('\n\n')

    out = ""  # PETRglobals.EventFileName
    if cli_args.outputs:
        out = cli_args.outputs

    # 创建一个和数据库交流的session
    print("======>create a db session")
    session = Session()
    print("======>db session is ok")

    # 创建 jvm
    print("======>create a jvm")
    obj_EvtInfo = GetInfo.GetInfoForEvt(jars=constants.JARS_DIR, mark_time_ranges=True)
    print("======>jvm is ok")

    # load model
    identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)

    print("======>Start assigning tasks to child processes.")
    while True:
        if queue.qsize > 0:
            # 从队列中获取一个任务
            print("======> begin ======>Get a story from the queue.")
            task = queue.get()
            print("======> end ======>Get a story from the queue.")
            # 打印日志，获取到了任务
            write_multiprocess_log(multi_log_lock, '{}Process {} get one task: {}'.format(u'', os.getpid(), task))
            # 执行任务
            print("======>go to process_task() ")
            process_task(task, out, multi_log_lock, session, obj_EvtInfo, identifier)
        else:
            time.sleep(0.5 * random.random())
            continue

# def create_classpath():
#         required_jars = {
#             'StanfordUtil-1.0.0-jar-with-dependencies.jar'
#         }
#         
#         jars1=constants.JARS_DIR
#         sutime_jar = os.getcwd() + '\\jars'
# 
#         jars = [sutime_jar]
#         jar_file_names = []
#         for top, dirs, files in os.walk(jars1):
#             for file_name in files:
#                 if file_name.endswith('.jar'):
#                     jars.append(os.path.join(top, file_name))
#                     jar_file_names.append(file_name)
#         if not required_jars.issubset(jar_file_names):
#             raise RuntimeError('Not all necessary Java dependencies have been downloaded!')
#         return os.pathsep.join(jars)
#     
# def start_jvm(_classpath):
#         if jpype.isJVMStarted() is not 1:
#             jpype.startJVM(
#                 jpype.getDefaultJVMPath(),
#                 '-Djava.class.path={classpath}'.format(
#                     classpath=_classpath)
#             )






def process_task(one_task, out_file, multi_log_lock, session, identifier, getinfo):
    events = {}
    # story_date = str(one_task['publishDate'])
    print("======>story processing is starting")
    story_date = one_task['publishDate']
    try:
        story_date = time.strptime(story_date, "%Y%m%d%H%M%S")
    except Exception:
        story_date = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))   #todo

    # story_content, story_title, story_date, story_src, story_url
#     print("======>create a jvm")
#     obj_EvtInfo = GetInfo.GetInfoForEvt(jars=constants.JARS_DIR, mark_time_ranges=True)  
#     print("======>jvm is ok")
    
        
         
    one_task['content']=one_task['content'].replace('-',' ')
    events = PETRreader.read_story_input(one_task['content'],
                                         one_task['title'],
                                         story_date,
                                         one_task['siteName'],
                                         one_task['pageUrl'],
                                         one_task['id'],
                                         getinfo,
                                         identifier)
    # The StanfordCoreNLP calling in read_story_input has a side effect that a StreamHandler was left,
    # which is owned by the root logger.
    # Remove all handlers associated with the root logger object.
    while len(logging.root.handlers) > 0:
        logging.root.removeHandler(logging.root.handlers[-1])

    # story没有内容,回写solr
    if not events:
        print("======> prompt ======> The story is invalid and can not be written to the log.")
        # write log
        write_multiprocess_log(multi_log_lock, '{}Process {} get discard task: {}'.format(u'', os.getpid(), one_task))
        # write solr
        result = access_solr.write_to_solr(one_task['id'])
        if result is False:
            write_multiprocess_log(multi_log_lock, u'Process ' + unicode(
                os.getpid()) + u': ' + u'Something goes wrong in solr write, please check the log3' + u'id:story_id:%s' % story_id + u'       records_insert:%s' % (
                                   ','.join(records_insert)))
        return None

    print("======>do_coding() function to start running.")
    updated_events = do_coding(events)
    print("======>do_coding() function has been completed.")


    if PETRglobals.NullVerbs:
        PETRwriter.write_nullverbs(updated_events, 'nullverbs.' + out_file)
    elif PETRglobals.NullActors:
        PETRwriter.write_nullactors(updated_events, 'nullactors.' + out_file)
    else:
        print("======>databasewriter.write_events() function to start running.")
        databasewriter.write_events(getinfo, updated_events, multi_log_lock, session, True)
        print("======>databasewriter.write_events() function has been completed.")
    print("======>story processing is completed")



def read_dictionaries(validation=False):

    print('Verb dictionary:', PETRglobals.VerbFileName)
    verb_path = utilities._get_data(
        'data/dictionaries',
        PETRglobals.VerbFileName)
    PETRreader.read_verb_dictionary(verb_path)

    print('Actor dictionaries:', PETRglobals.ActorFileList)
    for actdict in PETRglobals.ActorFileList:
        actor_path = utilities._get_data('data/dictionaries', actdict)
        PETRreader.read_actor_dictionary(actor_path)

    print('Agent dictionary:', PETRglobals.AgentFileName)
    agent_path = utilities._get_data('data/dictionaries',
                                     PETRglobals.AgentFileName)
    PETRreader.read_agent_dictionary(agent_path)

    print('Discard dictionary:', PETRglobals.DiscardFileName)
    discard_path = utilities._get_data('data/dictionaries',
                                       PETRglobals.DiscardFileName)
    PETRreader.read_discard_list(discard_path)

    if PETRglobals.IssueFileName != "":
        print('Issues dictionary:', PETRglobals.IssueFileName)
        issue_path = utilities._get_data('data/dictionaries',
                                         PETRglobals.IssueFileName)
        PETRreader.read_issue_list(issue_path)


def run(filepaths, out_file, s_parsed, sub_command_args):
    # this is the routine called from main()
    events = []
    if filepaths == 'javainfo':
        events = PETRreader.read_story_input(sub_command_args.story_content,
                                             sub_command_args.story_title,
                                             sub_command_args.story_date,
                                             sub_command_args.story_src,
                                             sub_command_args.story_url,
                                             sub_command_args.story_id)
        # The StanfordCoreNLP calling in read_story_input has a side effect that a StreamHandler was left,
        # which is owned by the root logger.
        # Remove all handlers associated with the root logger object.
        while len(logging.root.handlers) > 0:
            logging.root.removeHandler(logging.root.handlers[-1])
    else:
        events = PETRreader.read_xml_input(filepaths, s_parsed)
    print("events before coding:", events)
    if not s_parsed:
        events = utilities.stanford_parse(events)
    updated_events = do_coding(events)
    print("updated_events after coding:", updated_events)
    if PETRglobals.NullVerbs:
        PETRwriter.write_nullverbs(updated_events, 'nullverbs.' + out_file)
    elif PETRglobals.NullActors:
        PETRwriter.write_nullactors(updated_events, 'nullactors.' + out_file)
    else:
#         PETRwriter.write_events(updated_events, 'evts.' + out_file)
#         databasewriter.write_events_to_db(updated_events, 'evts.' + out_file)
        print("updated_events:")
        print(updated_events)
        databasewriter.write_events(updated_events, None, False, obj_EvtInfo)


def run_pipeline(data, out_file=None, config=None, write_output=True,
                 parsed=False):
    # this is called externally
    utilities.init_logger('PETRARCH.log')
    logger = logging.getLogger('petr_log')
    if config:
        print('Using user-specified config: {}'.format(config))
        logger.info('Using user-specified config: {}'.format(config))
        PETRreader.parse_Config(config)
    else:
        logger.info('Using default config file.')
        logger.info(
            'Config path: {}'.format(
                utilities._get_data(
                    'data/config/',
                    'PETR_config.ini')))
        PETRreader.parse_Config(utilities._get_data('data/config/',
                                                    'PETR_config.ini'))

    read_dictionaries()

    logger.info('Hitting read events...')
    events = PETRreader.read_pipeline_input(data)
    if parsed:
        logger.info('Hitting do_coding')
        updated_events = do_coding(events)
    else:
        events = utilities.stanford_parse(events)
        updated_events = do_coding(events)
    if not write_output:
        output_events = PETRwriter.pipe_output(updated_events)
        return output_events
    elif write_output and not out_file:
        print('Please specify an output file...')
        logger.warning('Need an output file. ¯\_(ツ)_/¯')
        sys.exit()
    elif write_output and out_file:
        PETRwriter.write_events(updated_events, out_file)


if __name__ == '__main__':
    freeze_support()
    main()

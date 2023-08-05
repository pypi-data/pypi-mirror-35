# -*- coding: utf-8 -*-

import os
import time
import logging
import requests
import json
from datetime import datetime
try:
    from ConfigParser import ConfigParser
except ImportError:
    from configparser import ConfigParser

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import constants
import PETRglobals
import ParseRoleCode
from read_file import read_solr_address, read_key_value_file, read_db_ini
from access_solr import query_info_by_solr, alpha2_to_alpha3
from write_file import write_multiprocess_log
from access_solr import write_to_solr
from session_factory import PetrarchEvents2
from simpleRegexNER import evt_verb_judge


os.environ['NLS_LANG'] = "SIMPLIFIED CHINESE_CHINA.UTF8"


def do_write_db(obj_list):
    """write objects to database"""

    logger = logging.getLogger('petr_log')

    # database connection string
    con_str = read_db_ini()
    
    # Lazy Connecting
    engine = create_engine(con_str)
    
    session = None
    flag = True
    try:
        # Create a Schema. If the relevant table doesn't exist in database, it will be created automatically.
        # Base.metadata.create_all(engine)
        
        # Creating a Session
        session_maker = sessionmaker(bind=engine)
        session = session_maker()
        
        # Adding and Updating Objects
        session.add_all(obj_list)
        
        # Commit the transaction
        session.commit()
    except Exception as e:
        print('{}'.format(e).decode("utf-8", errors="ignore"))
        logger.warning('{}'.format(e).decode("utf-8", errors="replace"))
        flag = False
    finally:
        # Close the Session
        if session:
            session.close()

    return flag


def do_write_db_multiprocess(session, obj_list):
    """write objects to database"""

    process_id = os.getpid()

    error_msg_ignore = ""
    error_msg_replace = ""
    flag = True

    # Adding and Updating Objects
    session.add_all(obj_list)

    try:
        # Commit the transaction
        session.commit()
    except Exception as e:
        session.rollback()
        flag = False
        error_msg_ignore = '{}'.format(e).decode("utf-8", errors="ignore")
        error_msg_replace = '{}'.format(e).decode("utf-8", errors="replace")
        print(error_msg_ignore)
#         write_multiprocess_log(multi_log_lock, u'Process ' + unicode(process_id) + u': ' + error_msg_replace)
#     else:
        # 执行成功
#         write_multiprocess_log(multi_log_lock,
#                                'Process {}: {}'.format(process_id, u"Write to database successfully."))
    finally:
        # Close the Session
        if session:
            session.close()

    return flag


def write_events(time0, updated_events, session, multi_process_flag=False):
    """
    write events to database
    parameter updated_events is a dictionary that contains all coded information and original information
    """

    records_insert = []
    for story_id in updated_events:
        # story's meta data
        story_meta = updated_events[story_id]["meta"]
        story_title = story_meta["title"]
        story_date = story_meta["date"]
        story_source = story_meta["source"]
        story_url = story_meta["url"]

        # all sentences in a story
        sents = updated_events[story_id]["sents"]

        # if the story was discarded when do_coding, no records will be generated to db
        if sents is None:
            break

        # sent_no表示当前句子在story中的编号
        for sent_no in sents:

            # the current sentence
            sent = sents[sent_no]

            # if a sentence has no events, skip it
            if "events" not in sent:
                continue
            
            # the sentenct's original content
            sent_content = sent['content']
            sent_parsed = sent['parsed']  # parsed by stanfordnlp 20171227
            # all events extracted from the sentence
            sent_events = sent['events']
            # sentence ner info
            sent_ner = sent['ner_list']
            # 每个事件的核心动词的文本，在句子原文中的序号 20171227
            event_verbno = sent['event_verbno']

            # event_no表示当前事件在句子中的编号
            # event表示当前事件
            for event_no, event in enumerate(sent_events):
                # 未实际应用 20171227
                verb_no = event_verbno[id(event)]
                location_relevant = sent_content, sent_parsed, verb_no

                one_record = None
                # generate one record to be inserted into database
                one_record = generate_one_record(sent, event, story_id, sent_no, event_no, sent_content, time0, sent_ner, location_relevant)
                if one_record:
                    records_insert.append(one_record)

    # write to db
    if records_insert:
        if multi_process_flag:
            flag = do_write_db_multiprocess(session, records_insert)
            if flag:
                for story_id in updated_events:
                    result = write_to_solr(story_id)
#                     if result is False:
#                         write_multiprocess_log(multi_log_lock, u'Process ' + unicode(os.getpid()) + u': ' + u'Something goes wrong in solr write, please check the log1'+u'id:story_id:%s'%story_id)
        else:
            flag = do_write_db(records_insert)
            if flag:
                for story_id in updated_events:
                    result = write_to_solr(story_id)
                    if result is False:
                        logging.warn('something goes wrong in solr write,please check the log2'+'id:story_id:%s'%story_id)
    else:
        # write to solr
        result = write_to_solr(story_id)
#         if result is False:
#             write_multiprocess_log(multi_log_lock, u'Process ' + unicode(
#                 os.getpid()) + u': ' + u'Something goes wrong in solr write, please check the log3'+u'id:story_id:%s'%story_id +u'       records_insert:%s'%(','.join(records_insert)))


def get_location(location_relevant):
    # 未实际应用 20171227
    sent_content = location_relevant[0]
    sent_parsed = location_relevant[1]
    verb_no = location_relevant[2]


def generate_one_record(sent, event, story_id, sent_no, event_no, sent_content, time0, sent_ner, location_relevant):
    """
    sent 当前句子
    event 当前事件
    """

    one_record = None

    # 获取时间
    the_time = get_time(sent_content, time0)

    # 事件的全局唯一ID
    global_event_id = "{}_{}_{}".format(story_id, sent_no, event_no)

    # 事件发生时间，事件发生年月，事件发生年份
    sql_date = datetime.date(datetime.today())
    month_year = None
    the_year = None
    if 'YMD' in the_time:
        sql_date = datetime.date(datetime.strptime(the_time['YMD'], '%Y%m%d'))
        month_year = the_time['YMD'][:-2]
        the_year = the_time['YMD'][:-4]

    elif 'YM' in the_time:
        try:
            sql_date = datetime.date(datetime.strptime(the_time['YM'], '%Y%m'))
            month_year = the_time['YM']
            the_year = the_time['YM'][:-2]
        except Exception:
            print(the_time)
    elif 'Y' in the_time:
        sql_date = datetime.date(datetime.strptime(the_time['Y'], '%Y'))
        month_year = the_time['Y']
        the_year = the_time['Y']

    # 测试地点，未实际应用 20171227
    location_in_sent = get_location(location_relevant)

    # 获取地点
    the_location = []
    for s_ner in sent_ner:
        if s_ner['ner_type'] == 'LOCATION':
            the_location.append(s_ner['ner_name'])

    # 事件发生地的全称
    action_geo_fullname = None
    # 事件发生地国家代码（Alpha2）
    action_geo_countrycode = None
    # 事件发生地一级行政区代码
    action_geo_adm1code = None
    # 事件发生地二级行政区代码
    action_geo_adm2code = None
    # 事件发生地纬度
    action_geo_lat = None
    # 事件发生地经度
    action_geo_long = None
    # 事件发生地地理信息在geonames中的ID
    action_geo_featureid = None
    if the_location:
        action_geo = get_action_geo_detail(the_location[0])
        action_geo_fullname = action_geo["ACTIONGEO_FULLNAME"]
        action_geo_countrycode = action_geo["ACTIONGEO_COUNTRYCODE"]
        action_geo_adm1code = action_geo["ACTIONGEO_ADM1CODE"]
        action_geo_adm2code = action_geo["ACTIONGEO_ADM2CODE"]
        action_geo_lat = float(action_geo["ACTIONGEO_LAT"]) if action_geo["ACTIONGEO_LAT"] is not None else None
        action_geo_long = float(action_geo["ACTIONGEO_LONG"]) if action_geo["ACTIONGEO_LONG"] is not None else None
        action_geo_featureid = action_geo["ACTIONGEO_FEATUREID"]

    # 发起者的名称，承受者的名称
    source_name = None
    target_name = None
    if PETRglobals.WriteActorText:
        actors = sent['meta']['actortext'][event]
        # source_name = actors[0]
        # target_name = actors[1]
        # 20171207 add ,如果发起者为辨别出来的实体，则将name与code置换位置
        if event[0] and actors[0] == '---':
            source_name = event[0]
        else:
            source_name = actors[0]

        if event[1] and actors[1] == '---':
            target_name = event[1]
        else:
            target_name = actors[1]

    # 20171207 add ,如果发起者为辨别出来的实体，则将name与code置换位置
    # 发起者的编码
    if event[0] and actors[0] == '---':
        source_code = '---'
    else:
        source_code = event[0]

    # 承受者的编码
    if event[1] and actors[1] == '---':
        target_code = '---'
    else:
        target_code = event[1]

    # 按照四个要素判断事件是否有效
    sent = location_relevant[0]
    struct_tree = location_relevant[1]
    verb_no = location_relevant[2]
    flag_evt = evt_verb_judge(source_name, target_name, verb_no, the_location)
    if flag_evt:
        return None

    # read (person, country) dictionary
    person_country = read_key_value_file(constants.PERSON_COUNTRY_FILE)
    # read (country alias, country) dictionary
    country_country = read_key_value_file(constants.COUNTRY_COUNTRY_FILE)

    # source's info by solr
    source_countrycode = None
    if source_name is not None and source_name.upper() in country_country:
        source_country = country_country[source_name.upper()]
        # 发起者的国家代码（Alpha3标准）
        source_countrycode = query_info_by_solr(source_country)
        # translate countrycode from alpha2 to alpha3 standard
        source_countrycode = alpha2_to_alpha3(source_countrycode)
    elif source_name is not None and source_name.upper() in person_country:
        source_country = person_country[source_name.upper()]
        # 发起者的国家代码（Alpha3标准）
        source_countrycode = query_info_by_solr(source_country)
        # translate countrycode from alpha2 to alpha3 standard
        source_countrycode = alpha2_to_alpha3(source_countrycode)

    # target's info by solr
    target_countrycode = None
    if target_name is not None and target_name.upper() in country_country:
        target_country = country_country[target_name.upper()]
        # 承受者的国家代码（Alpha3标准）
        target_countrycode = query_info_by_solr(target_country)
        # translate countrycode from alpha2 to alpha3 standard
        target_countrycode = alpha2_to_alpha3(target_countrycode)
    elif target_name is not None and target_name.upper() in person_country:
        target_country = person_country[target_name.upper()]
        # 承受者的国家代码（Alpha3标准）
        target_countrycode = query_info_by_solr(target_country)
        # translate countrycode from alpha2 to alpha3 standard
        target_countrycode = alpha2_to_alpha3(target_countrycode)

    # 发起者的编码
    # source_code = event[0]

    # 发起者 - 所属组织编码 , 宗教编码 , 国内角色编码
    skg_code = None
    srrc_dict = dict(RELIGION1CODE='', RELIGION2CODE='')
    srtc_dict = dict(TYPE1CODE='', TYPE2CODE='', TYPE3CODE='')
    if source_code:
        skg_code, srrc_dict, srtc_dict = ParseRoleCode.resolve_role_encoding(source_code)

    # 承受者的编码
    # target_code = event[1]

    # 承受者 - 所属组织编码 , 宗教编码 , 国内角色编码
    tkg_code = None
    trrc_dict = dict(RELIGION1CODE='', RELIGION2CODE='')
    trtc_dict = dict(TYPE1CODE='', TYPE2CODE='', TYPE3CODE='')
    if target_code:
        tkg_code, trrc_dict, trtc_dict = ParseRoleCode.resolve_role_encoding(target_code)

    # 事件小类编码
    event_code = event[2]
    # EVENTBASECODE
    event_base_code = event_code[:3]
    # 事件大类编码
    event_root_code = event_code[:2]
    # 四大类编码
    evtQuadClass = ParseRoleCode.resolve_quadclass(event_root_code)
    # 事件类型得分
    evtClassScore = ParseRoleCode.get_goldsteinscale(event_code)


    # one record to be inserted to database
    one_record = PetrarchEvents2(
        globaleventid=global_event_id, sqldate=sql_date, monthyear=month_year,
        year=the_year, actor1code=source_code, actor1name=source_name,
        actor1countrycode=source_countrycode, actor1knowngroupcode=skg_code, actor1religion1code=srrc_dict['RELIGION1CODE'],
        actor1religion2code=srrc_dict['RELIGION2CODE'], actor1type1code=srtc_dict['TYPE1CODE'], actor1type2code=srtc_dict['TYPE2CODE'],
        actor1type3code=srtc_dict['TYPE3CODE'], actor2code=target_code, actor2name=target_name, actor2countrycode=target_countrycode,
        actor2knowngroupcode=tkg_code, actor2religion1code=trrc_dict['RELIGION1CODE'],
        actor2religion2code=trrc_dict['RELIGION2CODE'], actor2type1code=trtc_dict['TYPE1CODE'], actor2type2code=trtc_dict['TYPE2CODE'],
        actor2type3code=trtc_dict['TYPE3CODE'], eventcode=event_code,
        eventbasecode=event_base_code, eventrootcode=event_root_code,
        quadclass=evtQuadClass,
        goldsteinscale=evtClassScore, avgtone=None,
        actor1geo_fullname=None, actor1geo_countrycode=None, actor1geo_adm1code=None,
        actor1geo_adm2code=None, actor1geo_lat=None, actor1geo_long=None, actor1geo_featureid=None,
        actor2geo_fullname=None, actor2geo_countrycode=None, actor2geo_adm1code=None,
        actor2geo_adm2code=None, actor2geo_lat=None, actor2geo_long=None, actor2geo_featureid=None,
        actiongeo_type=None,
        actiongeo_fullname=action_geo_fullname, actiongeo_countrycode=action_geo_countrycode,
        actiongeo_adm1code=action_geo_adm1code, actiongeo_adm2code=action_geo_adm2code,
        actiongeo_lat=action_geo_lat, actiongeo_long=action_geo_long,
        actiongeo_featureid=action_geo_featureid,
        dateadded=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        sourceurl=story_id, event_sentence=sent_content, language_flag=0)

    return one_record


def get_time(content, time0):
    """
    content is the original sentence
    """

    # obj_EvtInfo = GetInfo.GetInfoForEvt(jars=constants.JARS_DIR, mark_time_ranges=True)
    tempsent = [content]
    if time0 :
        strEvtTime = time0
#         print("time0",time0)
    else:
        strEvtTime = str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
#         print ("================>",strEvtTime)
    if len(strEvtTime) > 10:
        strEvtTime = strEvtTime[:10]

    #tmp = [{'value': '2017-09-22'}]
    tmp = [{'value': strEvtTime}]
    ## 20170925 modified end

    the_time = dict()
    for each in tmp:
        try:
            if '-' in each['value']:
                if each['value'].count('-') == 2:
                    times = datetime.strptime(each['value'], '%Y-%m-%d')
                    the_time['YMD'] = format(times, '%Y%m%d')
                    #the_time['YMD'] = each['value']
                elif each['value'].count('-') == 1:
                    times = datetime.strptime(each['value'], '%Y-%m')
                    the_time['YM'] = format(times, '%Y%m')
                    #the_time['YM'] = each['value']
            elif type(each['value']) == dict:
                #the_time['H'] = datetime.strptime(each['value']['begin'])
                pass  #事件发生的小时,暂时不需要存入数据库
            elif len(each['value']) == 4:
                times = datetime.strptime(each['value'], '%Y-%m-%d')
                the_time['Y'] = format(times, '%Y')
        except Exception:
            pass

    return the_time


def get_info_from_solr(solr_instance, cond_string, timeout=5):
    # True: 正常
    # False: 异常
    flag = True
    holding = {}
    request_string = solr_instance + cond_string

    try:
        result = requests.get(request_string, timeout).text
        result = json.loads(result)
    except Exception:
        # write log ...
        flag = False
    else:
        # 返回结果列表中的第一个元素，认为它是最准确的
        # 修正获取数据是的判断条件，在异常情况准确获取数据 20180102
        if result['responseHeader']['status'] == 0:
            if result['response']['docs']:
                holding = result['response']['docs'][0]

    return flag, holding

def get_action_geo_detail(geo_string):
    holding = {"ACTIONGEO_FULLNAME": None,
               "ACTIONGEO_COUNTRYCODE": None,
               "ACTIONGEO_ADM1CODE": None,
               "ACTIONGEO_ADM2CODE": None,
               "ACTIONGEO_LAT": None,
               "ACTIONGEO_LONG": None,
               "ACTIONGEO_FEATUREID": None}

    solr_instance = read_solr_address('geo')

    query_string = geo_string + " AND featureclass:A"
    condition_str = '/select?indent=on&q=%s&wt=json' % query_string
    # 首次查找
    solr_flag, solr_result = get_info_from_solr(solr_instance, condition_str)
    if not solr_flag:
        return holding
    elif not solr_result:
        # 通过条件 “地点” + “featureclass:A” 没有找到东西，则去掉“featureclass:A”进行二次查找
        query_string = geo_string
        condition_str = '/select?indent=on&q=%s&wt=json' % query_string
        solr_flag, solr_result = get_info_from_solr(solr_instance, condition_str)
        if not solr_flag or not solr_result:
            # 二次查找的结果集为空
            return holding
        else:
            # 二次查找的结果不为空
            country_code = solr_result["countrycode"]
            admin1_code = solr_result["admin1code"]
            admin2_code = solr_result["admin2code"]
            holding["ACTIONGEO_LAT"] = solr_result["latitude"]
            holding["ACTIONGEO_LONG"] = solr_result["longitude"]
            holding["ACTIONGEO_FEATUREID"] = solr_result["id"]
            if admin2_code != "":
                holding["ACTIONGEO_COUNTRYCODE"] = solr_result["countrycode"]
                holding["ACTIONGEO_ADM1CODE"] = solr_result["admin1code"]
                holding["ACTIONGEO_ADM2CODE"] = solr_result["admin2code"]
                # 查找admin1code对应的一级行政区名
                query_string = "featurecode:ADM1 AND countrycode:" + country_code + " AND admin1code:" + admin1_code
                condition_str = '/select?indent=on&q=%s&wt=json' % query_string
                solr_flag, solr_result = get_info_from_solr(solr_instance, condition_str)
                if not solr_flag or not solr_result:
                    return holding
                else:
                    admin1_asciiname = solr_result["asciiname"]
                # 查找countrycode对应的国家名
                query_string = "featurecode:PCLI AND countrycode:" + country_code
                condition_str = '/select?indent=on&q=%s&wt=json' % query_string
                solr_flag, solr_result = get_info_from_solr(solr_instance, condition_str)
                if not solr_flag or not solr_result:
                    return holding
                else:
                    country_asciiname = solr_result["asciiname"]
                    # 事件发生地的全称
                    holding["ACTIONGEO_FULLNAME"] = geo_string + ", " + admin1_asciiname + ", " + country_asciiname
                    return holding
            elif admin1_code != "" and admin1_code != "00":
                holding["ACTIONGEO_COUNTRYCODE"] = solr_result["countrycode"]
                holding["ACTIONGEO_ADM1CODE"] = solr_result["admin1code"]
                admin1_asciiname = solr_result["asciiname"]
                # 查找countrycode对应的国家名
                query_string = "featurecode:PCLI AND countrycode:" + country_code
                condition_str = '/select?indent=on&q=%s&wt=json' % query_string
                solr_flag, solr_result = get_info_from_solr(solr_instance, condition_str)
                if not solr_flag or not solr_result:
                    return holding
                else:
                    country_asciiname = solr_result["asciiname"]
                    # 事件发生地的全称
                    holding["ACTIONGEO_FULLNAME"] = geo_string + ", " + admin1_asciiname + ", " + country_asciiname
                    return holding
            elif country_code != "":
                holding["ACTIONGEO_COUNTRYCODE"] = solr_result["countrycode"]
                # 查找countrycode对应的国家名
                query_string = "featurecode:PCLI AND countrycode:" + country_code
                condition_str = '/select?indent=on&q=%s&wt=json' % query_string
                solr_flag, solr_result = get_info_from_solr(solr_instance, condition_str)
                if not solr_flag or not solr_result:
                    return holding
                else:
                    country_asciiname = solr_result["asciiname"]
                    # 事件发生地的全称
                    holding["ACTIONGEO_FULLNAME"] = geo_string + ", " + "" + ", " + country_asciiname
                    return holding
    else:
        # 通过条件 “地点” + “featureclass:A” 找到了东西，则判断featurecode
        feature_code = solr_result["featurecode"]
        # 类型为国家，则只获取国家相关的信息
        if feature_code == "PCLI":
            holding["ACTIONGEO_FULLNAME"] = geo_string + ", , " +solr_result["asciiname"]
            holding["ACTIONGEO_COUNTRYCODE"] = solr_result["countrycode"]
            holding["ACTIONGEO_LAT"] = solr_result["latitude"]
            holding["ACTIONGEO_LONG"] = solr_result["longitude"]
            holding["ACTIONGEO_FEATUREID"] = solr_result["id"]
            return holding
        elif feature_code == "ADM1":
            holding["ACTIONGEO_COUNTRYCODE"] = solr_result["countrycode"]
            holding["ACTIONGEO_ADM1CODE"] = solr_result["admin1code"]
            holding["ACTIONGEO_LAT"] = solr_result["latitude"]
            holding["ACTIONGEO_LONG"] = solr_result["longitude"]
            holding["ACTIONGEO_FEATUREID"] = solr_result["id"]
            country_code = solr_result["countrycode"]
            admin1_asciiname = solr_result["asciiname"]
            # 查找countrycode对应的国家名
            query_string = "featurecode:PCLI AND countrycode:" + country_code
            condition_str = '/select?indent=on&q=%s&wt=json' % query_string
            solr_flag, solr_result = get_info_from_solr(solr_instance, condition_str)
            if not solr_flag or not solr_result:
                return holding
            else:
                # 国家名
                country_asciiname = solr_result["asciiname"]
                # 事件发生地的全称
                holding["ACTIONGEO_FULLNAME"] = admin1_asciiname + ', ' + country_asciiname
                return holding
        elif feature_code == "ADM2" or feature_code != "ADM2":
            # 剩下的都当成ADM2处理
            holding["ACTIONGEO_COUNTRYCODE"] = solr_result["countrycode"]
            holding["ACTIONGEO_ADM1CODE"] = solr_result["admin1code"]
            holding["ACTIONGEO_ADM2CODE"] = solr_result["admin2code"]
            holding["ACTIONGEO_LAT"] = solr_result["latitude"]
            holding["ACTIONGEO_LONG"] = solr_result["longitude"]
            holding["ACTIONGEO_FEATUREID"] = solr_result["id"]
            admin1_code = solr_result["admin1code"]
            country_code = solr_result["countrycode"]
            # 查找admin1code对应的一级行政区名
            query_string = "featurecode:ADM1 AND countrycode:" + country_code + " AND admin1code:" + admin1_code
            condition_str = '/select?indent=on&q=%s&wt=json' % query_string
            solr_flag, solr_result = get_info_from_solr(solr_instance, condition_str)
            if not solr_flag or not solr_result:
                return holding
            else:
                admin1_asciiname = solr_result["asciiname"]
            # 查找countrycode对应的国家名
            query_string = "featurecode:PCLI AND countrycode:" + country_code
            condition_str = '/select?indent=on&q=%s&wt=json' % query_string
            solr_flag, solr_result = get_info_from_solr(solr_instance, condition_str)
            if not solr_flag or not solr_result:
                return holding
            else:
                country_asciiname = solr_result["asciiname"]
                # 事件发生地的全称
                holding["ACTIONGEO_FULLNAME"] = geo_string + ", " + admin1_asciiname + ", " + country_asciiname
                return holding

    # 没有走以上所有分支， add modify bug 20180103
    return holding

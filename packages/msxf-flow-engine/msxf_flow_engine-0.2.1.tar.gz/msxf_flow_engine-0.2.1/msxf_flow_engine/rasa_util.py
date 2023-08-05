import itertools
import json
import codecs
import pickle
import yaml
import os
import re
import importlib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from botagent.db.mysql_engine import get_mysql_engine, get_orm_session
from botagent.db.rasa.rasa_config import Rasa_flow, Rasa_domain, Rasa_stories
from msxf_flow_engine.actions.action import Action
from msxf_flow_engine.agent import Agent
from msxf_flow_engine.policies.keras_policy import KerasPolicy
from msxf_flow_engine.events import SlotSet
from msxf_flow_engine.policies.memoization import MemoizationPolicy
from botagent.db.mysql_ins import db
import wget
import zipfile
import shutil
import keras.backend as K


def flow_to_db(name, robotId, url=None):
    """convert flow info  to data write in database.
    # Params
        robotId: robot id
        name: flow name .
        url: rasa train file url 
    """
    flow_id = self.get_flow_id(name, robotId)
    if flow_id == -1:
        r_f = Rasa_flow(robot_id=robotId, name=name, url=url)
        db.session.add(r_f)
        db.session.commit()
        return getFlowId(name, robotId)
    else:
        return -1

# second version


class storyNote:

    def __init__(self, Id):
        self.Id = Id
        self.nodeList = []

# second version


class domainNote:
    """rasa config domian structure"""

    def __init__(self, value, type, template=None, template_type=None):
        self.value = value 	# domain elem value
        self.type = type 	# domain elem type as intents , action, slots
        self.template = template  # action template
        self.template_type = template_type  # action template type:text

# second version


def story_to_db(flow_id, yml_file, story_file):
    """convert story to data write in database.
    # Params
        robotId: robot id
        name: flow name .
    """
    f = open(yml_file, 'r', encoding="utf-8")
    x = yaml.load(f)
    allNodesList = []
    valueList = []
    for i in x['slots'].keys():
        if x['slots'][i]['type'] == 'categorical':
            for elem in x['slots'][i]['values']:
                join_text = 'slot{"' + i + '":"' + elem + '"}'
                dn = domainNote(join_text, 0)
                valueList.append(dn)
        if x['slots'][i]['type'] == 'text':
            join_text = '{"' + i + '":"text"}'
            dn = domainNote(join_text, 0)
            valueList.append(dn)

    for i, v in enumerate(x['actions']):
        if v in x['templates']:
            dn = domainNote(v, 2, '+++'.join(i['text']
                                             for i in x['templates'][v]), 'text')
            valueList.append(dn)
        else:
            ssde = domainNote(v, 2)
            valueList.append(ssde)
    for i, v in enumerate(x['intents']):
        dn = domainNote(v, 1)
        valueList.append(dn)

    for i, v in enumerate(valueList):
        r_d = Rasa_domain(flow_id=flow_id,
                          type=v.type,
                          position=i,
                          name=v.value,
                          template=v.template,
                          template_type=v.template_type)
        db.session.add(r_d)
    db.session.commit()

    with open(story_file, 'r', encoding="utf-8") as f:
        forwoad_line = ''
        cur_line = ''
        story_id = 0
        for line in f.readlines():
            line = line.strip()
            line = line.lstrip()
            if '##' in line:
                node = storyNote(story_id)
                allNodesList.append(node)
                story_id = story_id + 1
            try:
                if '*' in line or '-' in line:
                    line = line[2:]
                    index = '-1'
                    if '"text"' in line:
                        for i, v in enumerate(valueList):
                            if v.value in line and index == '-1':
                                index = str(i)
                                continue
                            if v.value in line and index != '-1':
                                index = index + '+' + str(i)
                                break
                    else:
                        for i, v in enumerate(valueList):
                            if v.value in line:
                                index = str(i)
                                break
                    if index == '-1' and 'action' in line:
                        temp = line.replace('_', '')
                        temp = temp.lower()
                        for i, v in enumerate(valueList):
                            if v.type == 2 and temp in v.value.lower():
                                index = str(i)
                                break
                    # index = valueList.index(line)
                    allNodesList[story_id - 1].nodeList.append(index)
            except Exception as e:
                continue

    for anl in allNodesList:
        r_s = Rasa_stories(flow_id=flow_id,
                           story=','.join(i for i in anl.nodeList))
        db.session.add(r_s)
    db.session.commit()


def get_flow_id(name, robotId):
    """get flow id 
    # Params
        name: flow name
        robotId: robot id
    """
    try:
        flow = db.session.query(Rasa_flow).filter(Rasa_flow.robot_id == robotId)\
            .filter(Rasa_flow.name == name).first()
    except Exception as e:
        return -1
    if not flow:
        return -1
    else:
        return flow.id


def get_flow_id_url(name, robotId):
    """get flow id and url .
    # Params
        name: flow name
        robotId: robot id
    """
    try:
        flow = db.session.query(Rasa_flow).filter(Rasa_flow.robot_id == robotId)\
            .filter(Rasa_flow.name == name).first()
    except Exception as e:
        return -1, None
    return flow.id, flow.url

# second version


def db_to_story(flow_id):
    """convert data in database to story .
    # Params
        flow_id: flow id
    """
    path = 'rasa_config_{}'.format(flow_id)
    os.mkdir(path)
    ymlFile = os.path.join(path, 'yml.yml')
    mdFile = os.path.join(path, 'md.md')

    stat_results = db.session.query(Rasa_domain).filter(
        Rasa_domain.flow_id == flow_id).all()

    ymal_dic = {}
    temp_ymal = {}
    ymal_dic['slots'] = {}
    ymal_dic['templates'] = {}
    ymal_index = {}
    ymal_type = {}
    for stats in stat_results:
        ymal_index.update({str(stats.position): stats.name})
        ymal_type.update({str(stats.position): stats.type})
        if stats.type == 0:
            text = stats.name
            if text[0:4] != 'slot':
                ymal_dic['slots'].update({text[2:-9]: {'type': 'text'}})
            else:
                temp = text[6:-2].split('":"')
                temp_array = []
                if temp[0] in temp_ymal:
                    temp_array = temp_ymal[temp[0]]
                temp_array.append(temp[1])
                temp_ymal = {temp[0]: temp_array}
                ymal_dic['slots'].update(
                    {temp[0]: {'type': 'categorical', 'values': temp_array}})
        elif stats.type == 1:
            text = stats.name
            temp_array = []
            if 'intents' in ymal_dic:
                temp_array = ymal_dic['intents']
            temp_array.append(text)
            ymal_dic['intents'] = temp_array
        elif stats.type == 2:
            text = stats.name
            temp_array = []
            if 'actions' in ymal_dic:
                temp_array = ymal_dic['actions']
            temp_array.append(text)
            ymal_dic['actions'] = temp_array
            templates_array = []
            if 'Action' not in text:
                if text in ymal_dic['templates']:
                    templates_array = ymal_dic['templates'][text]
                tt = stats.template
                tt_type = stats.template_type
                tt_dic = {tt_type: tt}
                templates_array.append(tt_dic)
                ymal_dic['templates'].update({text: templates_array})

    with open(ymlFile, 'w') as f:
        yaml.dump(ymal_dic, f)

    stat_results1 = db.session.query(Rasa_stories).filter(
        Rasa_stories.flow_id == flow_id).all()

    with open(mdFile, 'w', encoding="utf-8") as f:
        for i, stats in enumerate(stat_results1):
            story = stats.story.split(',')
            f.write('## story_{}\n'.format(i))
            for ss in story:
                sc = ''
                if '+' in ss:
                    one = ''
                    two = ''
                    aa = ss.split('+')
                    if ymal_type[aa[0]] == 0:
                        two = ymal_index[aa[0]]
                        one = ymal_index[aa[1]]
                    else:
                        one = ymal_index[aa[0]]
                        two = ymal_index[aa[1]]
                    sc = '* ' + one + two + '\n'
                elif ymal_type[ss] == 0:
                    sc = '\t- ' + ymal_index[ss] + '\n'
                elif ymal_type[ss] == 1:
                    sc = '* ' + ymal_index[ss]
                elif ymal_type[ss] == 2:
                    if 'Action' in ymal_index[ss]:
                        ss_t = ymal_index[ss].split('.')
                        pattern = "[A-Z]"
                        new_string = re.sub(
                            pattern, lambda x: "_" + x.group(0), ss_t[1])
                        sc = '\t- ' + new_string[1:].lower() + '\n'
                    else:
                        sc = '\t- ' + ymal_index[ss] + '\n'
                f.write(sc)
            f.write('\n')
            f.write('\n')


def train_dialogue_from_url(robotId, name):
    """train rasa model from robot_id ,name.
    # Params
        robotId: robot id
        name: flow name .
    """

    # get flow_id ,url from db
    flow_id, url = getFlowIdUrl(name, robotId)

    # create temp file to save rasa config file from file url
    config_path = 'rasa_config_{}'.format(flow_id)
    if not os.path.exists(config_path):
        os.mkdir(config_path)
    outfileName = config_path + '.zip'
    wget.download(url, out=outfileName)
    zip_ref = zipfile.ZipFile(outfileName, 'r')
    zip_ref.extractall(config_path)
    zip_ref.close()

    # get the .yml file .md file .py file to train
    lastStr = (url.split('/')[-1]).split('.')[0]
    domain_file = ''
    training_data_file = ''
    f_list = os.listdir(os.path.join(config_path, lastStr))
    for i in f_list:
        if os.path.splitext(i)[1] == '.yml':
            domain_file = os.path.join(config_path, lastStr, i)
        elif os.path.splitext(i)[1] == '.md':
            training_data_file = os.path.join(config_path, lastStr, i)
        elif os.path.splitext(i)[1] == '.py':
            scriptfile = os.path.join(config_path, lastStr, i)
            current_py = i

    # move .py file to current file path
    shutil.move(scriptfile, './')

    # rasa train
    agent = Agent(processerId='default', domain=domain_file, policies=[
                  MemoizationPolicy(max_history=15), KerasPolicy()])
    training_data = agent.load_data(training_data_file)
    agent.train(
        training_data,
        augmentation_factor=200,
        max_history_len=15,
        epochs=30,
        batch_size=20,
        validation_split=0.1
    )
    model_path = 'model_{}'.format(flow_id)
    agent.persist(model_path)

    # remove temp file
    try:
        os.remove(domain_file)
        os.remove(training_data_file)
        os.rmdir(os.path.join(config_path, lastStr))
        os.remove(current_py)
        os.rmdir(config_path)
        os.remove(outfileName)
    except Exception as e:
        return agent
    return agent

# second version


def train_dialogue(flow_id):
    """train rasa model from flow_id
    # Params
        flow_id: flow id
    """
    config_path = 'rasa_config_{}'.format(flow_id)
    f_list = os.listdir(config_path)
    domain_file = ''
    model_path = 'model_{}'.format(flow_id)
    training_data_file = ''
    for i in f_list:
        if os.path.splitext(i)[1] == '.yml':
            domain_file = os.path.join(config_path, i)
        elif os.path.splitext(i)[1] == '.md':
            training_data_file = os.path.join(config_path, i)

    agent = Agent(processerId='default', domain=domain_file, policies=[
                  MemoizationPolicy(max_history=15), KerasPolicy()])
    training_data = agent.load_data(training_data_file)
    agent.train(
        training_data,
        augmentation_factor=200,
        max_history_len=15,
        epochs=30,
        batch_size=20,
        validation_split=0.1
    )
    agent.persist(model_path)
    return agent


def get_query_flow_id(query):
    # mock flow id
    return 1


def get_query_answer(flow_id, query):
    """get result that the rasa model predict result .
    # Params
        flow_id: flow id
        query: query string .
    """
    model_path = 'model_{}'.format(flow_id)
    K.clear_session()
    agent = Agent.load(processerId='default', path=model_path)
    text = agent.handle_message(query)
    return text

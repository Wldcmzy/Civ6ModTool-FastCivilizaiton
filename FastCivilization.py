sql_output_folder = 'output'
xml_output_folder = 'output/Text'
from _FCutils.patternsSQL import *
from _FCutils.format_sql_columns import format_sql_columns
import os
import re

# 如果此变量为True, Deplo文本将大部分使用默认文本（文件前面有五句话需要改）
# 如果此变量为False, Deplo文本为空字符串
APPLY_DEFAULT_LEADER_DEPLO = False

# Text文件语言
ModLanguages = ['zh_Hans_CN', 'zh_Hant_HK', 'en_US']

# 文明名称
CivilizaitonName = 'CIVILIZATION_HOLLOWNEST'

# 领袖名称以及首都文本
LeadersList = [
    ('LEADER_RADIANCE', 'LOC_CITY_NAME_DREAM_REALM'),
    ('LEADER_THE_KNIGHT_GOD_OF_GODS', 'LOC_CITY_NAME_GODHOME'),
    ('LEADER_THE_KNIGHT_WANDERER', 'LOC_CITY_NAME_DIRTMOUTH'),
    ('LEADER_WYRMS', 'LOC_CITY_NAME_WHITE_PALACE'),
    ('LEADER_GRIMM', 'LOC_CITY_NAME_HOWLING_CLIFFS'),
]


def writeNewSQL(filenameRow: str, text: str):
    filename = ''
    for each in filenameRow.split('_'):
        filename += f'_{each.title()}'
    filename = filename[1 : ] + '.sql'
    if not os.path.exists(f'./{sql_output_folder}'): os.makedirs(f'./{sql_output_folder}')
    with open(f'./{sql_output_folder}/{filename}', 'w', encoding = 'utf-8') as f:
        f.write(format_sql_columns(text))

def writeNewXML_Text(filenameRow: str, text: str, language: str):
    filename = ''
    for each in filenameRow.split('_'):
        filename += f'_{each.title()}'
    filename = f'{language}#' + filename[1 : ] + '.xml'
    if not os.path.exists(f'./{xml_output_folder}/{language}'): os.makedirs(f'./{xml_output_folder}/{language}')
    with open(f'./{xml_output_folder}/{language}/{filename}', 'w', encoding = 'utf-8') as f:
        f.write(text)
        
        
def CivilizationSQL():
    sql_civ = SQL_CIVILIZAITON.replace(CUSTOM_CIVILIZATION_NAME, CivilizaitonName)
    writeNewSQL(CivilizaitonName, sql_civ)

def LeadersSQL():
    sql_leaderConfigs = ''
    for leaderName, CapitalCityName in LeadersList:
        sql_leader = SQL_LEADERS
        sql_leader = sql_leader.replace(CUSTOM_CIVILIZATION_NAME,CivilizaitonName)
        sql_leader = sql_leader.replace(CUSTOM_LEADER_NAME,leaderName)
        sql_leader = sql_leader.replace(CUSTOM_LEADER_CAPITAL_CITY_NAME,CapitalCityName)
        writeNewSQL(leaderName, sql_leader)

        sql_cfg = SQL_LEADERS_CONFIG_PLAYERS
        sql_cfg = sql_cfg.replace(CUSTOM_CIVILIZATION_NAME,CivilizaitonName)
        sql_cfg = sql_cfg.replace(CUSTOM_LEADER_NAME,leaderName)
        sql_leaderConfigs += f'{sql_cfg},\n'
        
        sql_leader_agenda = SQL_LEADER_AGENDAS
        sql_leader_agenda = sql_leader_agenda.replace(CUSTOM_LEADER_NAME,leaderName)
        writeNewSQL(f'{leaderName}_Agenda', sql_leader_agenda)
        
        sql_leader_ai = SQL_LEADER_AI
        sql_leader_ai = sql_leader_ai.replace(CUSTOM_LEADER_NAME,leaderName)
        writeNewSQL(f'{leaderName}_AI', sql_leader_ai)
    
    sql_leaderConfigs = SQL_LEADERS_CONFIG.format(
        Players = sql_leaderConfigs.strip()[ : -1] + ';'
    )
    writeNewSQL(f'{CivilizaitonName}_Config', sql_leaderConfigs)

def Text():
    PATTERN_LEADER_NAME = 'LEADER_STELLARIS_GREY'
    PATTERN_CIVILIAZATION_NAME = 'CIVILIZATION_ORIGINALSTELLARIS'
    PATTERN_LANGUAGE_US = 'en_US'
    PATTERN_LANGUAGE_HANS_CN = 'zh_Hans_CN'
    
    def __CivilizaitonText(CivilizationName: str, Language: str):
        with open('./_FCutils./patternsTextCivilization.xml', 'r', encoding = 'utf-8') as f:
            text = f.read()
        text = text.replace(PATTERN_CIVILIAZATION_NAME, CivilizationName)
        text = text.replace(PATTERN_LANGUAGE_HANS_CN, Language)
        text = re.sub('<Text>.+?</Text>', '<Text></Text>', text)
        writeNewXML_Text(f'Text_{CivilizationName}', text, Language)
        
    def __LeaderText(LeaderName: str, Language: str):
        with open('./_FCutils./patternsTextLeader.xml', 'r', encoding = 'utf-8') as f:
            text = f.read()
        text = text.replace(PATTERN_LEADER_NAME, LeaderName)
        text = text.replace(PATTERN_LANGUAGE_HANS_CN, Language)
        text = re.sub('<Text>.+?</Text>', '<Text></Text>', text)
        writeNewXML_Text(f'Text_{LeaderName}', text, Language)
    
    def __LeadersTextDiplo(LeaderName: str, Language: str):
        with open('./_FCutils./patternsTextLeaderDiploAlmostDefault.xml', 'r', encoding = 'utf-8') as f:
            diplo = f.read()
        diplo = diplo.replace(PATTERN_LEADER_NAME, LeaderName)
        diplo = diplo.replace(PATTERN_LANGUAGE_US, Language)
        if not APPLY_DEFAULT_LEADER_DEPLO:
            diplo = re.sub('<Text>.+?</Text>', '<Text></Text>', diplo)
        writeNewXML_Text(f'Text_{LeaderName}_Diplo', diplo, Language)
        
    def __LeadersTextPedia(LeaderName: str, Language: str):
        with open('./_FCutils./patternsTextLeaderPedia.xml', 'r', encoding = 'utf-8') as f:
            pedia = f.read()
        pedia = pedia.replace(PATTERN_LEADER_NAME, LeaderName)
        pedia = pedia.replace(PATTERN_LANGUAGE_HANS_CN, Language)
        pedia = re.sub('<Text>.+?</Text>', '<Text></Text>', pedia)
        writeNewXML_Text(f'Text_{LeaderName}_Pedia', pedia, Language)
        
    def __LeadersTextAgenda(LeaderName: str, Language: str):
        with open('./_FCutils./patternsTextLeaderAgenda.xml', 'r', encoding = 'utf-8') as f:
            agenda = f.read()
        agenda = agenda.replace(PATTERN_LEADER_NAME, LeaderName)
        agenda = agenda.replace(PATTERN_LANGUAGE_HANS_CN, Language)
        agenda = re.sub('<Text>.+?</Text>', '<Text></Text>', agenda)
        writeNewXML_Text(f'Text_{LeaderName}_Agenda', agenda, Language)
        
    
    for lang in ModLanguages:
        __CivilizaitonText(CivilizaitonName, lang)
        for leaderName, _ in LeadersList:
            __LeaderText(leaderName, lang)
            __LeadersTextDiplo(leaderName, lang)
            __LeadersTextPedia(leaderName, lang)
            __LeadersTextAgenda(leaderName, lang)

def main():
    CivilizationSQL()
    LeadersSQL()
    Text()

if __name__ == '__main__':
    main()
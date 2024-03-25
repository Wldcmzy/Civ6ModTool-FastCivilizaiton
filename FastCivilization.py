sql_output_folder = 'output'
xml_output_folder = 'output/text'
from _FCutils.patternsSQL import *
from _FCutils.format_sql_columns import format_sql_columns
import os
import re

# 如果此变量为True, Deplo文本将大部分使用默认文本（文件前面有五句话需要改）
# 如果此变量为False, Deplo文本为空字符串
APPLY_DEFAULT_LEADER_DEPLO_ALMOST = False

# Text文件语言
ModLanguages = ['zh_Hans_CN', 'en_US']

# 文明名称
CivilizaitonName = 'CIVILIZATION_X'

# 领袖名称以及首都文本
LeadersList = [
    ('LEADER_A', 'LOC_CITY_NAME_A'),
    ('LEADER_AB', 'LOC_CITY_NAME_AB'),
    ('LEADER_ABC', 'LOC_CITY_NAME_ABC'),
    ('LEADER_ABCD', 'LOC_CITY_NAME_ABCD'),
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
    if not os.path.exists(f'./{xml_output_folder}'): os.makedirs(f'./{xml_output_folder}')
    with open(f'./{xml_output_folder}/{filename}', 'w', encoding = 'utf-8') as f:
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
    
    sql_leaderConfigs = SQL_LEADERS_CONFIG.format(
        Players = sql_leaderConfigs.strip()[ : -1] + ';'
    )
    writeNewSQL(f'{CivilizaitonName}_Config', sql_leaderConfigs)

def LeadersText():
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
        if not APPLY_DEFAULT_LEADER_DEPLO_ALMOST:
            diplo = re.sub('<Text>.+?</Text>', '<Text></Text>', diplo)
        writeNewXML_Text(f'Text_{LeaderName}_Diplo', diplo, Language)
        
        
    for lang in ModLanguages:
        __CivilizaitonText(CivilizaitonName, lang)
        for leaderName, _ in LeadersList:
            __LeaderText(leaderName, lang)
            __LeadersTextDiplo(leaderName, lang)
        

def main():
    CivilizationSQL()
    LeadersSQL()
    LeadersText()

if __name__ == '__main__':
    main()
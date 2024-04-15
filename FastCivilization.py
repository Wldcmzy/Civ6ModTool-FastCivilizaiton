#----------------------------------------------------------------------------
# 请修改以下内容
#----------------------------------------------------------------------------

# 如果此变量为True, Deplo文本将使用默认文本
# 如果此变量为False, Deplo文本为空字符串
APPLY_DEFAULT_LEADER_DEPLO = False

# Mod作者的名称
author: str = 'StarsWhisper'

# Text文件语言
ModLanguages: list[str] = ['zh_Hans_CN', 'zh_Hant_HK', 'en_US']

# 文明名称
CivilizaitonName: str = 'CIVILIZATION_CELESTE'

# 领袖名称以及首都文本Tag
LeadersList: list[tuple[str, str]] = [
    ('LEADER_MADELINE', 'LOC_CITY_NAME_MADELINECAP'),
]

#----------------------------------------------------------------------------
# 修改到此为止
#----------------------------------------------------------------------------

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#----------------------------------------------------------------------------
# 以下内容可改可不改
#----------------------------------------------------------------------------

# database内容输出目录
database_output_folder = 'output'

# text内容输出目录
text_output_folder = 'output/Text'

#----------------------------------------------------------------------------
# 修改到此为止
#----------------------------------------------------------------------------

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#----------------------------------------------------------------------------
# 以下内容不需要修改
#----------------------------------------------------------------------------

from _FCutils.authordata import *
from _FCutils.patternsSQL import *
from _FCutils.patternsXML import *
from _FCutils.format_sql_columns import format_sql_columns
from datetime import datetime
import os
import re


citiesNameList = [x[1] for x in LeadersList]
citiesNameList.extend([f'LOC_CITY_OF_{CivilizaitonName}_{idx}' for idx in range(1, 21)])

def writeNewSQL(filenameRow: str, text: str) -> None:
    head = authorSQL.format(Author = author, DateCreated = datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
    filename = ''
    for each in filenameRow.split('_'):
        filename += f'_{each.title()}'
    filename = filename[1 : ] + '.sql'
    if not os.path.exists(f'./{database_output_folder}'): os.makedirs(f'./{database_output_folder}')
    with open(f'./{database_output_folder}/{filename}', 'w', encoding = 'utf-8') as f:
        f.write(head + format_sql_columns(text))
        
def writeNewXML(filenameRow: str, text: str) -> None:
    head = authorXML.format(Author = author, DateCreated = datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
    filename = ''
    for each in filenameRow.split('_'):
        filename += f'_{each.title()}'
    filename = filename[1 : ] + '.xml'
    if not os.path.exists(f'./{database_output_folder}'): os.makedirs(f'./{database_output_folder}')
    with open(f'./{database_output_folder}/{filename}', 'w', encoding = 'utf-8') as f:
        f.write(head + text)

def writeNewXML_Text(filenameRow: str, text: str, language: str) -> None:
    head = authorXML.format(Author = author, DateCreated = datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
    filename = ''
    for each in filenameRow.split('_'):
        filename += f'_{each.title()}'
    filename = filename[1 : ] + '.xml'
    if not os.path.exists(f'./{text_output_folder}/{language}'): os.makedirs(f'./{text_output_folder}/{language}')
    with open(f'./{text_output_folder}/{language}/{filename}', 'w', encoding = 'utf-8') as f:
        f.write(head + text)
        
        
def CivilizationDB() -> None:
    def __Civilization() -> None:
        sql_civ = SQL_CIVILIZAITON.replace(CUSTOM_CIVILIZATION_NAME, CivilizaitonName)
        writeNewSQL(CivilizaitonName, sql_civ)

    def __CivilizationCtiiesTag(Civilization: str, CitiesName: list[str]) -> None:
        rows = ''
        for cityName in CitiesName:
            rows += XML_CITIES_TAG_ROW.format(civType = Civilization,cityName = cityName,)
        xml = XML_TABLE_BASE.format(table = 'CityNames',rows = rows,)
        xml = XML_BASE.format(xml = xml)
        writeNewXML(f'{CivilizaitonName}_Cities_TAG', xml)
    
    def __CivilizationColors(Civilization: str, LeadersList: list[tuple[str, str]]) -> None:
        Colors = XML_TABLE_BASE.format(table = 'Colors', rows = XML_CUSTOM_COLOR_ROW__CONST * 3)
        pcr = ''
        for leaderName, _ in LeadersList:
            pcr += XML_PLAYERCOLORS_PATTERN_ROW.format(leader = leaderName)
        PlayerColors = XML_TABLE_BASE.format(table = 'PlayerColors', rows = pcr)
        xml = XML_BASE.format(xml = Colors + PlayerColors)
        writeNewXML(f'{CivilizaitonName}_Colors', xml)

    __Civilization()
    __CivilizationCtiiesTag(CivilizaitonName, citiesNameList)
    __CivilizationColors(CivilizaitonName, LeadersList)

def LeadersDB() -> None:
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

def Text() -> None:
    PATTERN_LEADER_NAME = 'LEADER_STELLARIS_GREY'
    PATTERN_CIVILIAZATION_NAME = 'CIVILIZATION_ORIGINALSTELLARIS'
    PATTERN_LANGUAGE_US = 'en_US'
    PATTERN_LANGUAGE_HANS_CN = 'zh_Hans_CN'
    
    def __CivilizaitonText(CivilizationName: str, Language: str) -> None:
        with open('./_FCutils./patternsTextCivilization.xml', 'r', encoding = 'utf-8') as f:
            text = f.read()
        text = text.replace(PATTERN_CIVILIAZATION_NAME, CivilizationName)
        text = text.replace(PATTERN_LANGUAGE_HANS_CN, Language)
        text = re.sub('<Text>.+?</Text>', '<Text></Text>', text)
        writeNewXML_Text(f'Text_{CivilizationName}', text, Language)
        
    def __LeaderText(LeaderName: str, Language: str) -> None:
        with open('./_FCutils./patternsTextLeader.xml', 'r', encoding = 'utf-8') as f:
            text = f.read()
        text = text.replace(PATTERN_LEADER_NAME, LeaderName)
        text = text.replace(PATTERN_LANGUAGE_HANS_CN, Language)
        text = re.sub('<Text>.+?</Text>', '<Text></Text>', text)
        writeNewXML_Text(f'Text_{LeaderName}', text, Language)
    
    def __LeadersTextDiplo(LeaderName: str, Language: str) -> None:
        with open('./_FCutils./patternsTextLeaderDiploAlmostDefault.xml', 'r', encoding = 'utf-8') as f:
            diplo = f.read()
        diplo = diplo.replace(PATTERN_LEADER_NAME, LeaderName)
        diplo = diplo.replace(PATTERN_LANGUAGE_US, Language)
        if not APPLY_DEFAULT_LEADER_DEPLO:
            diplo = re.sub('<Text>.+?</Text>', '<Text></Text>', diplo)
        writeNewXML_Text(f'Text_{LeaderName}_Diplo', diplo, Language)
        
    def __LeadersTextPedia(LeaderName: str, Language: str) -> None:
        with open('./_FCutils./patternsTextLeaderPedia.xml', 'r', encoding = 'utf-8') as f:
            pedia = f.read()
        pedia = pedia.replace(PATTERN_LEADER_NAME, LeaderName)
        pedia = pedia.replace(PATTERN_LANGUAGE_HANS_CN, Language)
        pedia = re.sub('<Text>.+?</Text>', '<Text></Text>', pedia)
        writeNewXML_Text(f'Text_{LeaderName}_Pedia', pedia, Language)
        
    def __LeadersTextAgenda(LeaderName: str, Language: str) -> None:
        with open('./_FCutils./patternsTextLeaderAgenda.xml', 'r', encoding = 'utf-8') as f:
            agenda = f.read()
        agenda = agenda.replace(PATTERN_LEADER_NAME, LeaderName)
        agenda = agenda.replace(PATTERN_LANGUAGE_HANS_CN, Language)
        agenda = re.sub('<Text>.+?</Text>', '<Text></Text>', agenda)
        writeNewXML_Text(f'Text_{LeaderName}_Agenda', agenda, Language)
            
    def __CivilizationCtiiesName(Civilization: str, CitiesName: list[str], language: str) -> None:
        rep = ''
        for cityName in CitiesName:
            rep += TEXT_XML_REPLACE.format(
                tag = cityName,
                lang = language,
                text = '',
            )
        xml = TEXT_XML_BASE.format(replace = rep)
        writeNewXML_Text(f'Text_{CivilizaitonName}_Cities', xml, language)

    for lang in ModLanguages:
        __CivilizaitonText(CivilizaitonName, lang)
        for leaderName, _ in LeadersList:
            __LeaderText(leaderName, lang)
            __LeadersTextDiplo(leaderName, lang)
            __LeadersTextPedia(leaderName, lang)
            __LeadersTextAgenda(leaderName, lang)
            __CivilizationCtiiesName(CivilizaitonName, citiesNameList, lang)

def main():
    CivilizationDB()
    LeadersDB()
    Text()

if __name__ == '__main__':
    main()
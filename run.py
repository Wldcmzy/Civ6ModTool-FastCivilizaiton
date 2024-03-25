from _FCutils.patterns import *
from _FCutils.format_sql_columns import format_sql_columns
import os
output_folder = 'output'


CivilizaitonName = 'CIVILIZATION_X'
LeadersList = [
    ('LEADER_A', 'LOC_CITY_NAME_A'),
    ('LEADER_AB', 'LOC_CITY_NAME_AB'),
    ('LEADER_ABC', 'LOC_CITY_NAME_ABC'),
    ('LEADER_ABCD', 'LOC_CITY_NAME_ABCD'),
]

def writeNewFile(filenameRow: str, text: str):
    filename = ''
    for each in filenameRow.split('_'):
        filename += f'_{each.title()}'
    filename = filename[1 : ] + '.sql'
    if not os.path.exists(f'./{output_folder}'): os.makedirs(f'./{output_folder}')

    with open(f'./{output_folder}/{filename}', 'w', encoding = 'utf-8') as f:
        f.write(format_sql_columns(text))



def main():
    sql_civ = SQL_CIVILIZAITON.replace(CUSTOM_CIVILIZATION_NAME, CivilizaitonName)
    writeNewFile(CivilizaitonName, sql_civ)

    sql_leaderConfigs = ''
    for leaderName, CapitalCityName in LeadersList:
        sql_leader = SQL_LEADERS
        sql_leader = sql_leader.replace(CUSTOM_CIVILIZATION_NAME,CivilizaitonName)
        sql_leader = sql_leader.replace(CUSTOM_LEADER_NAME,leaderName)
        sql_leader = sql_leader.replace(CUSTOM_LEADER_CAPITAL_CITY_NAME,CapitalCityName)
        writeNewFile(leaderName, sql_leader)

        sql_cfg = SQL_LEADERS_CONFIG_PLAYERS
        sql_cfg = sql_cfg.replace(CUSTOM_CIVILIZATION_NAME,CivilizaitonName)
        sql_cfg = sql_cfg.replace(CUSTOM_LEADER_NAME,leaderName)
        sql_leaderConfigs += f'{sql_cfg},\n'
    
    sql_leaderConfigs = SQL_LEADERS_CONFIG.format(
        Players = sql_leaderConfigs.strip()[ : -1] + ';'
    )
    writeNewFile(f'{CivilizaitonName}_Config', sql_leaderConfigs)
        

if __name__ == '__main__':
    main()
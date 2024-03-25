import re
from _FCutils.format_sql_columns import format_sql_columns

# 注意此脚本的逻辑只保证带有括号的语句的顺序，如果你的sql语句中间有单行注释或空行，会导致排版错位。
# 以及，此脚本会直接删除/**/注释，否则会有被/**/注释的内容被解开注释的BUG。
if __name__ == '__main__':
    with open('./auto_format_INSERT_sql_strings.sql', 'r', encoding='utf-8') as f:
        s = f.read()
    
    s = re.sub(r'/\*.*?\*/', '', s, flags=re.DOTALL)

    with open('./auto_format_INSERT_sql_output.sql', 'w', encoding='utf-8') as f:
        f.write(format_sql_columns(s))
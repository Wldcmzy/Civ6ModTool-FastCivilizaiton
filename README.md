# Civ6ModTool-FastCivilizaiton

## 功能1：

`FastCivilization.py`

快速生成文明领袖的主干SQL代码，并生成相关的XML文本文件。

需要在`FastCivilization.py`中设置参数，生成结果保存于output文件夹中。

## 功能2：

`auto_format_INSERT_sql.py`

对简单的SQL语句的列缩进进行排版，脚本有较大局限性。

需要把待修改的语句存入`auto_farmat_INSERT_sql_strings.sql`，修改结果保存于`auto_farmat_INSERT_sql_output.sql`
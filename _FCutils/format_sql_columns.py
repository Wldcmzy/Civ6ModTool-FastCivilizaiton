import re
import math


def format_sql_columns(text: str, TAB_length: int = 4) -> str:
    ret = ''
    sqls = [s.strip() for s in re.split(r'(?<=;)', text)[ : -1]]
    for sql in sqls:
        max_value_length = None
        buffer = []
        lines = sql.split('\n')
        for line in lines:
            line = line.strip()
            if line == '' or line[0] != '(':
                ret += f'{line}\n'
            else:
                line = re.sub(r'\s+', '', line)
                line = re.sub(r'\(|\)', '', line)
                values = line[ : -1].split(',')
                buffer.append(values)
                if not max_value_length: max_value_length = [0] * len(values)
                for i, value in enumerate(values):
                    max_value_length[i] = max(max_value_length[i], len(value))
                    

        for i in range(len(max_value_length)):
            mod  = max_value_length[i] % TAB_length
            # if mod == TAB_length - 1:
            #     max_value_length[i] += TAB_length
            if mod != 0:
                max_value_length[i] += (TAB_length) - (mod)

        # print(max_value_length)
        
        for values in buffer:
            vline = '(\t'
            valuesNum = len(values)
            for i, value in enumerate(values):
                if i + 1 == valuesNum:
                    value += '),\n'
                    vline += value
                else:
                    value += ','
                    length = len(value)
                    # if value == "'TRAIT_LEADER_ABC',":
                    #     print(length)
                    if length < max_value_length[i]:
                        value += '\t' * math.ceil((max_value_length[i] - length) / TAB_length)
                    value += '\t'
                    vline += value
            ret += vline
        ret = ret.strip()[ : -1] + ';\n'
        ret += '\n'
    ret = ret.replace('VALUE),', ') VALUES')
    return ret

                    
                    
                
                
        
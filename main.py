KEYWORDS = ['=', '++', '--', 'scanf', 'printf', 'if', 'else', 'for']
KEYWORDS_DICT = {'=': '=', '++': '++', '--': '--', 'scanf': 'ввод', 'printf': 'вывод', 'for': 'для'}
TYPES = ['int ', 'void ', 'float ', 'double ', 'char ']
TYPES_LEN = len(TYPES)
LAST_VARIABLE_OUT = range(3, 7)
FOR_ALIKE = (5,)
ARITH = (0, 1, 2)
KEYWORDS_C = len(KEYWORDS)


def last_variable_out(line, code, fig_brackets):
    print('    ' * fig_brackets, end='')
    if code == 3:
        print('ввод ', end='')
        line = line.replace('scanf(', '').replace(');', '')
        line = list(line.replace(' ', '').split(','))
        print(line[-1].replace('&', ''))
    elif code == 4:
        print('вывод ', end='')
        line = line.replace('printf(', '').replace(');', '')
        if ',' in line:
            line = list(line.replace(' ', '').split(','))
            print(line[-1])
        else:
            print(line)
    elif code == 5:
        print(line.replace('if', 'если').replace('(', '', 1).replace(')', '', 1).replace('{', ''))


def main():
    # Picking File
    c_file_name = 'main.c'
    file = open(c_file_name, 'r')
    print(file.read())
    file.seek(0)
    text = list(str(file.read()).replace('    ', '').split('\n'))
    print(text)
    lines = len(text)
    in_func = False
    fig_brackets = 0
    for i in range(lines):
        current_line = text[i]
        if in_func:
            if '}' in current_line:
                fig_brackets -= 1
            for j in LAST_VARIABLE_OUT:
                if KEYWORDS[j] in current_line:
                    last_variable_out(current_line, j, fig_brackets)
            if '{' in current_line:
                fig_brackets += 1

        if not in_func:
            for j in TYPES:
                if j in current_line:
                    print('подпрограмма', current_line.replace('{', '', 1))
                    in_func = True
                    fig_brackets += 1
                    break

        if in_func and not fig_brackets:
            in_func = 0


if __name__ == '__main__':
    main()

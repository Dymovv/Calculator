# словарь для преобразования чисел словами в числа
dict_num = {
    "ноль": 0, "один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5,
    "шесть": 6, "семь": 7, "восемь": 8, "девять": 9, "десять": 10,
    "одиннадцать": 11, "двенадцать": 12, "тринадцать": 13, "четырнадцать": 14,
    "пятнадцать": 15, "шестнадцать": 16, "семнадцать": 17, "восемнадцать": 18,
    "девятнадцать": 19, "двадцать": 20, "тридцать": 30, "сорок": 40,
    "пятьдесят": 50, "шестьдесят": 60, "семьдесят": 70, "восемьдесят": 80,
    "девяносто": 90
}

# преобразование чисел в строковом представлении
dict_str = {val: key for key, val in dict_num.items()}

# функция для перевода строкового числа в числовое
def words_to_number(words):
    parts = words.split()
    if len(parts) == 1:
        return dict_num[parts[0]]
    elif len(parts) == 2:
        return dict_num[parts[0]] + dict_num[parts[1]]

# функция для перевода числового значения обратно в строку
def number_to_words(number):
    if number in dict_str:
        return dict_str[number]
    tens = number // 10 * 10
    units = number % 10
    return f"{dict_str[tens]} {dict_str[units]}"

# преобразование выражения в обратную польскую нотацию (RPN)
def to_rpn(tokens):
    precedence = {"плюс": 1, "минус": 1, "умножить": 2}
    output = []
    operators = []
    for token in tokens:
        if token in dict_num:
            output.append(token)
        elif token in precedence:
            while (operators and operators[-1] != "(" and
                   precedence[operators[-1]] >= precedence[token]):
                output.append(operators.pop())
            operators.append(token)
        elif token == "(":
            operators.append(token)
        elif token == ")":
            while operators and operators[-1] != "(":
                output.append(operators.pop())
            operators.pop()
    while operators:
        output.append(operators.pop())
    return output

# вычисление выражения в формате RPN
def evaluate_rpn(rpn_tokens):
    stack = []
    for token in rpn_tokens:
        if token in dict_num:
            stack.append(dict_num[token])
        else:
            b = stack.pop()
            a = stack.pop()
            if token == "плюс":
                stack.append(a + b)
            elif token == "минус":
                stack.append(a - b)
            elif token == "умножить":
                stack.append(a * b)
    return stack[0]

# главная функция
def calc(expression):
    # Замена текстовых скобок на обычные
    expression = expression.replace("скобка открывается", "(").replace("скобка закрывается", ")")
    tokens = expression.split()
    
    # преобразование в обратную польскую нотацию
    rpn = to_rpn(tokens)
    
    # вычисление результата
    result = evaluate_rpn(rpn)
    
    # преобразование результата в текст
    return number_to_words(result)

# пример использования
print(calc("пять плюс два умножить на три минус один"))  # десять
print(calc("скобка открывается пять плюс двенадцать скобка закрывается умножить на два минус восемь"))  # двадцать шесть

from .errors import *

PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2}

def get_token_type(token) -> str:
    """ Возращает тип токена: операция, скобка или число """

    if token in PRIORITY:
        return "Operation"
    elif token == '(':
        return "Open bracket"
    elif token == ')':
        return "Close bracket"
    else:
        return "Number"

def tokenization(expr) -> list:
    """ Разбивает выражение на токены и выполняет проверки на корректную запись """

    tokens = []
    is_unary = True

    i = 0
    while i < len(expr):
        if expr[i] == ' ' or expr[i] == '\t':
            i += 1
        elif expr[i].isdigit() or expr[i] in "+-" and is_unary or expr[i] == '.':
            num = ''
            if expr[i] in "+-":
                if is_unary: 
                    if expr[i] == '-': 
                        num += expr[i]
                    i += 1
                else:
                    raise ExcessOpError()
            is_unary = False
            while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                num += expr[i]
                i += 1  
            if num == '-' or not num: 
                raise ExcessOpError() 
            if num.count('.') > 1:
                raise NumberError()
            if num[0] == '0' and len(num) > 1 and num[1] != '.' or num[0] == '.':
                raise NumberError()
            if tokens and (tokens[-1] == ')' or get_token_type(tokens[-1]) == "Number"):
                raise MissingOpError()
            tokens.append(num)
        elif expr[i] in "+-*/()":
            if expr[i] in "+-*/":
                is_unary = True
            if expr[i] in "*/" and not tokens or expr[i] in "*/" and tokens[-1] == '(':
                raise OperandError()
            if expr[i] in "*/" and tokens[-1] in "+-*/":
                raise ExcessOpError()
            if expr[i] == ')' and tokens[-1] in "+-*/":
                raise OperandError()
            if expr[i] == '(':
                is_unary = True 
                if tokens and get_token_type(tokens[-1]) == "Number":
                    raise MissingOpError()
            tokens.append(expr[i])        
            i += 1
        else:
            raise UnitError(expr[i])
    if not tokens:
        raise EmptyError()
    if tokens[-1] in "+-*/":
        raise OperandError()
    return tokens

def shunting_yard(input_queue) -> list:
    """ Превращает обычную запись числа в ОПЗ """

    output_queue = []
    stack = []

    i = 0
    while i < len(input_queue):
        token = input_queue[i]
        token_type = get_token_type(token)
        match token_type:
            case "Number":
                output_queue.append(token)
            case "Operation":
                while stack and get_token_type(stack[-1]) == "Operation" and PRIORITY[stack[-1]] >= PRIORITY[token]:
                    output_queue.append(stack.pop())
                stack.append(token)
            case "Open bracket":
                stack.append(token)
            case "Close bracket":
                while stack and stack[-1] != '(':
                    output_queue.append(stack.pop())
                if not stack:
                    raise BracketError()
                stack.pop()
        i += 1

    while stack:
        if stack[-1] == '(':
            raise BracketError()
        output_queue.append(stack.pop())
    return output_queue

def polish_calculation(input_queue) -> list:
    """ Выполняет вычисление ОПЗ """

    if not input_queue:
        raise EmptyError()
    stack = []
    i = 0
    while i < len(input_queue):
        token = input_queue[i]
        token_type = get_token_type(token)
        match token_type:
            case "Number":
                stack.append(token)
            case "Operation":
                op1 = float(stack.pop())
                op2 = float(stack.pop())
                match token:
                    case '+':
                        res = op1 + op2
                    case '-':
                        res = op2 - op1
                    case '*':
                        res = op1 * op2
                    case '/':
                        if not op1:
                            raise DivisionError()
                        res = op2 / op1
                stack.append(res)
        i += 1
    return stack

def calculation(expr) -> float:
    """ Вызывает все функции, необходимые для вычисления выражения """
    
    tokens = tokenization(expr)
    output = shunting_yard(tokens)
    res =  polish_calculation(output)
    return float(res[0])
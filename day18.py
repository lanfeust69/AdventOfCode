file = open('test.in')

def eval(line):
    stack = []
    i = 0
    while i < len(line):
        c = line[i]
        if c == ' ':
            i += 1
            continue
        if '0' <= c <= '9':
            cur_val = int(c)
            while i + 1 < len(line) and '0' <= line[i + 1] <= '9':
                cur_val = cur_val * 10 + int(line[i + 1])
                i += 1
            if len(stack) > 1 and (stack[-1] == '+' or stack[-1] == '*'):
                op = stack.pop()
                operand = stack.pop()
                cur_val = operand + cur_val if op == '+' else operand * cur_val
            stack.append(cur_val)
            i += 1
            continue
        if c == ')':
            cur_val = stack.pop()
            if stack[-1] != '(':
                raise ValueError
            stack.pop()
            if len(stack) > 1 and (stack[-1] == '+' or stack[-1] == '*'):
                op = stack.pop()
                operand = stack.pop()
                cur_val = operand + cur_val if op == '+' else operand * cur_val
            stack.append(cur_val)
            i += 1
            continue
        stack.append(c)
        i += 1
    return stack[0]

def eval_prec(line):
    stack = []
    i = 0
    while i < len(line):
        c = line[i]
        if c == ' ':
            i += 1
            continue
        if '0' <= c <= '9':
            cur_val = int(c)
            while i + 1 < len(line) and '0' <= line[i + 1] <= '9':
                cur_val = cur_val * 10 + int(line[i + 1])
                i += 1
            if len(stack) > 1 and stack[-1] == '+':
                stack.pop()
                operand = stack.pop()
                cur_val = operand + cur_val
            stack.append(cur_val)
            i += 1
            continue
        if c == ')':
            cur_val = stack.pop()
            while len(stack) > 1 and stack[-1] == '*':
                stack.pop()
                operand = stack.pop()
                cur_val = operand * cur_val
            assert stack[-1] == '('
            stack.pop()
            if len(stack) > 1 and stack[-1] == '+':
                stack.pop()
                operand = stack.pop()
                cur_val = operand + cur_val
            stack.append(cur_val)
            i += 1
            continue
        stack.append(c)
        i += 1
    while len(stack) > 1:
        assert len(stack) > 2
        operand2 = stack.pop()
        op = stack.pop()
        assert op == '*'
        operand1 = stack.pop()
        stack.append(operand1 * operand2)
    return stack[0]

# print(list(eval_prec(line[:-1]) for line in file))
print(sum(eval_prec(line[:-1]) for line in file))

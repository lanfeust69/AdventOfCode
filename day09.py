for line in open('test.in'):
    stream = line.rstrip()

pos = 0
stack = []
score = 0
garbage = 0
while pos < len(stream):
    if len(stack) > 0 and stack[-1] == '<':
        # in garbage
        if stream[pos] == '!':
            pos += 1
        elif stream[pos] == '>':
            stack.pop()
        else:
            garbage += 1
        pos += 1
        continue
    if stream[pos] == '{':
        stack.append('{')
    elif stream[pos] == '<':
        stack.append('<')
    elif stream[pos] == '}':
        score += len(stack)
        stack.pop()
    pos += 1

print(score)
print(garbage)

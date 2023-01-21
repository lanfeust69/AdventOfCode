bots = {}
bot_actions = {}
outputs = {}

def set_bot_obj(bot, value):
    if bot in bots:
        bots[bot][1] = value
        bots[bot].sort()
        return bot
    else:
        bots[bot] = [value, -1]
        return -1

def set_output_obj(output, value):
    if output in outputs:
        outputs[output].append(value)
    else:
        outputs[output] = [value]
    return -1

def make_actions(bot, dest_low, dest_high, is_low_output, is_high_output):
    if is_low_output:
        low = lambda: set_output_obj(dest_low, bots[bot][0])
    else:
        low = lambda: set_bot_obj(dest_low, bots[bot][0])
    if is_high_output:
        high = lambda: set_output_obj(dest_high, bots[bot][1])
    else:
        high = lambda: set_bot_obj(dest_high, bots[bot][1])
    return (low, high)

complete = []

for line in open('test.in'):
    tokens = line.rstrip().split()
    if tokens[0] == 'value':
        bot, value = int(tokens[-1]), int(tokens[1])
        if set_bot_obj(bot, value) != -1:
            complete.append(bot)
    else:
        bot = int(tokens[1])
        bot_actions[bot] = make_actions(bot, int(tokens[6]), int(tokens[-1]), tokens[5] == 'output', tokens[-2] == 'output')

while len(complete) > 0:
    new_complete = []
    for bot in complete:
        a, b = bots[bot]
        if (a, b) == (17, 61):
            print(bot)
        for i in range(2):
            completed = bot_actions[bot][i]()
            if completed != -1:
                new_complete.append(completed)
    complete = new_complete

print(outputs[0][0] * outputs[1][0] * outputs[2][0])

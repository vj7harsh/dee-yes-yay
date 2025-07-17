from collections import defaultdict
def checklocks(commands):
    stack = []
    in_use = defaultdict(bool)

    for index, c in enumerate(commands, start= 1):
        action, value = c.split()
        if action == "ACQUIRE":
            if in_use[value]:
                return index
            in_use[value] = True
            stack.append(value)
            
        elif action == "RELEASE":
            if stack[-1] != value:
                return index
            stack.pop()
            in_use[value] = False

    if len(stack) != 0:         
        return len(commands) + 1
    return 0
            

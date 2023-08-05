def clamp(number, min=1, max=10):
    result = number
    if number < min: result = min
    if number > max: result = max
    return result

def abs(number):
    result = str(number)
    if number < 0: result = result[1:]
    return int(result)

def neg(number):
    result = str(number)
    if number >= 0: result = f"-{result}"
    return int(result)

def opposite(number):
    if number >= 0: return neg(number)
    else: return abs(number)

def binary_logicgates(logictype, *args):
    if logictype.lower() == "and":
        if args[0] == 1 and args[1] == 1:
            return 1
        return 0
    elif logictype.lower() == "not":
        if args[0] == 1:
            return 0
        elif args[0] == 0:
            return 1
    elif logictype.lower() == "or":
        if args[0] == 1 or args[1] == 1:
            return 1
        return 0



# hey no looking at source code is no good >:(
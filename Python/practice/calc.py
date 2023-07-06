import dis

def calc(code):
    data = code.split()
    print(f"data : {data}")
    stack = []
    for x in data:
        print(stack, x, end=" => ")
        if x == '+':
            b = stack.pop()
            a = stack.pop()
            stack.append(a+b)
        elif x == '-':
            b = stack.pop()
            a = stack.pop()
            stack.append(a-b)
        elif x == '*':
            b = stack.pop()
            a = stack.pop()
            stack.append(a*b)
        elif x == '/':
            b = stack.pop()
            a = stack.pop()
            stack.append(a//b)
        else:
            stack.append(int(x))
        print(stack)
    print(stack.pop())


calc("1 2 + 3 * 4 /")
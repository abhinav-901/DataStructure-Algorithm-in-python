from stack import Stack


def convert_int_to_binary(number: int):
    stack = Stack()
    quotient: int = number
    binary = ''
    if number == 0:
        return 0
    while quotient >= 1:
        quotient, remainder = divmod(quotient, 2)
        stack.push(remainder)
    for i in range(len(stack.get_stack())):
        binary += str(stack.pop())
    return int(binary)


if __name__ == '__main__':
    value = convert_int_to_binary(142)
    print(value)

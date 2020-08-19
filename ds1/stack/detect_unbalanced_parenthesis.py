from stack import Stack


def is_parenthesis_balanced(parenthesis_string: str):
    paren_pair_dict = {'[': ']', '{': '}', '(': ')'}
    stack = Stack()
    is_balanced: bool = False
    index: int = 0

    while index < len(parenthesis_string):
        paren_str = parenthesis_string[index]
        if index == 0 and paren_str in paren_pair_dict.values():
            return is_balanced
        if paren_str in paren_pair_dict.keys():
            stack.push(paren_str)
        if paren_str in paren_pair_dict.values() and not stack.is_empty():
            if paren_pair_dict[stack.pop()] == paren_str:
                is_balanced = True
        else:
            is_balanced = False
        index += 1
    if not stack.is_empty():
        is_balanced = False
    return is_balanced


if __name__ == "__main__":
    result = is_parenthesis_balanced("([{}])")
    print(result)

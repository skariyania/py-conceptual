# Input: pushed = { 1, 2, 3, 4, 5 }, popped = { 4, 5, 3, 2, 1 }
# Output: True
# Following sequence can be performed:
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
# Input: pushed = { 1, 2, 3, 4, 5 }, popped = { 4, 3, 5, 1, 2 }
# Output: False
# 1 can't be popped before 2.

import logging

logging.basicConfig(level=logging.DEBUG)


def validate(pushed: list, popped: list):
    """ validates if stack elements can be popped with given pop sequence """
    stack = []
    pointer = 0
    for p in pushed:
        stack.append(p)

        while stack and pointer < len(popped) and stack[-1] == popped[pointer]:
            stack.pop()
            pointer += 1
    logging.debug("pointer={%s} popped={%s}", pointer, popped)
    return pointer == len(popped)

if __name__ == "__main__":
    pushed1 = [1, 2, 3, 4, 5]
    popped1 = [4, 5, 3, 2, 1]
    RES1 = validate(pushed1, popped1)
    print(f"result for Q1 is {RES1}")

    pushed1 = [1, 2, 3, 4, 5]
    popped1 = [4, 3, 5, 1, 2]
    RES2 = validate(pushed1, popped1)
    print(f"result for Q2 is {RES2}")

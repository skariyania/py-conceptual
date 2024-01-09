"""module - string rotation"""
def is_same(a: chr, b: chr):
    """utility function to compare `a` and `b`

    Args:
        a (chr): input char a
        b (chr): input char b

    Returns:
        bool: returns true if both characters are same
    """
    return True if a == b else False

def solution(a):
    """
    1. rotate sting - times of length of the string
    2. compare first and last character
    3. if same increase counter
    4. return counter
    """
    count = 0
    for index, elem in enumerate(a):
        if index + 1 == len(a):
            next_elem = a[0]
            is_same(elem, a[0])
        else:
            next_elem = a[index + 1]
        if is_same(elem, next_elem):
            count += 1
    return count

if __name__ == "__main__":
    problems = ["absolutely", "taunt", "bab", "cccc"]
    for problem in problems:
        RESULT = solution(problem)
        print(f"problem={problem}, result={RESULT}")

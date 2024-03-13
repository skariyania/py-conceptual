""" semantic string - two pointer """


def provider_runner(runnable):
    """ runner function implements executable """
    parsed = get_parsed_runnable(runnable=runnable)
    max_continuity = 0
    left_index = 0
    right_index = 1
    input_length = len(parsed)
    if input_length < 2:
        return max_continuity
    for index, _ in enumerate(parsed):
        right_value = parsed[right_index]
        left_value = parsed[left_index]
        interim_continuity = 0
        while (
            comparator(right_value, left_value)
        ):
            interim_continuity += 1
            max_continuity = max(interim_continuity, max_continuity)
            left_index -= 1
            right_index += 1
            if left_index < 0 or right_index >= input_length:
                break
            right_value = parsed[right_index]
            left_value = parsed[left_index]
        left_index = index
        right_index = index + 1
    return max_continuity


def comparator(curr, prev):
    """ checks previous and current value falls as required semantic """
    p_checklist = ["(", "?"]
    c_checklist = [")", "?"]
    return curr in c_checklist and prev in p_checklist


def get_parsed_runnable(runnable):
    """ converts string to required list format """
    return list(runnable)


if __name__ == "__main__":
    inputs = [
        "(())",
        "))((",
        "??????",
        "?",
        "(()((()?)",
        "((?)?)"
    ]
    for i in inputs:
        result = provider_runner(i)
        print(f"input='{i}' result={result}")

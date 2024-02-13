class Solution(object):
    def is_palindrome(self, x):
        """
        checks if given number is palindrome
        """
        string_val=str(x)
        # in Python, string_val[::-1] is a slicing notation used to
        # reverse the order of characters in the string string_val.
        # Here's a breakdown of what it does:
        # string_val is a string variable or string literal.
        # [::-1] is a slicing notation where:
        # The first : indicates the start of the slice
        #   (which defaults to the beginning of the sequence).
        # The second : indicates the end of the slice (which defaults to the end of the sequence).
        # The -1 indicates the step size, which in this case is -1,
        #   meaning it iterates over the sequence in reverse order.
        # So, string_val[::-1] returns a new string that is a reversed version of string_val.
        return string_val == string_val[::-1]


if __name__ == "__main__":
    RESULT = Solution().is_palindrome(12321)
    print(RESULT)
        
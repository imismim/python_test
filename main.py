class Func:

    @staticmethod
    def checkout_palindrome(str_input: str) -> bool:
        return str_input == str_input[::-1]


if __name__ == '__main__':
    print(Func.checkout_palindrome("111"))
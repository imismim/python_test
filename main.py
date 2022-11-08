class Func:

    @staticmethod
    def checkout_palindrome(str_input: str) -> bool:
        return str_input == str_input[::-1]

    @staticmethod
    def list_uniq_elements(list_input: list) -> list:
        return list(set(list_input))


if __name__ == '__main__':
    print(Func.checkout_palindrome("111"))
    print(Func.list_uniq_elements([1,1,1,23213,123]))

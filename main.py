class Func:

    @staticmethod
    def checkout_palindrome(str_input: str) -> bool:
        return str_input == str_input[::-1]

    @staticmethod
    def list_uniq_elements(list_input: list) -> list:
        return list(set(list_input))

    @staticmethod
    def count_words(text_input: str) -> dict:
        import string
        return {
            "count words": len(text_input.split()),
            "count different symbols": len([i for i in text_input if i in string.punctuation])
        }

    @staticmethod
    def count_digits_in_text(text_input: str) -> int:
        return len([i for i in text_input if i.isdigit()])


if __name__ == '__main__':
    print(Func.checkout_palindrome("111"))
    print(Func.list_uniq_elements([1, 1, 1, 23213, 123]))
    print(Func.count_words("I am learning git and github. Ohoo!"))

from typing import Union, List, Tuple


class UserInterface:
    def __init__(self, player):
        self._player = player

    def _input(self) -> str:
        return input(">>> ")

    def _input_int(self, input_range: Tuple[int, int] = None) -> int:
        """
        Asks for a user input until it gets one that is an integer.
        :return: User input converted to an integer.
        """
        in_input_range = lambda x: True if input_range is None else (int(x) in range(*input_range))

        while True:
            user_in = self._input()
            if not user_in.isdecimal():
                print("Input must be an integer.\n")
            elif not in_input_range(user_in):
                print(f"{user_in} is not a valid option.\n")
            else:
                return int(user_in)

    def _prefix_a_or_an(self, word: str, capital: bool = False) -> str:
        """
        Decide whether to put 'a' or 'an' in front of a word based on if the word has a vowel as the first character.
        :param word: Word to put 'a' or 'an' in front of.
        :param capital: If True use 'A' or 'An' instead.
        :return: String in the form 'a/an <word>'.
        """
        first_char_vowel = word[0].lower() in ("a", "e", "i", "o", "u")
        return f"{'An' if capital else 'an'} {word}" if first_char_vowel else f"{'A' if capital else 'a'} {word}"

    def _separator(self):
        print("-" * 50)

    def output_responses(self, responses: Union[List["Response"], Tuple["Response", ...]]) -> None:
        results_list = [response() for response in responses]
        for result in results_list:
            for line in result:
                print(line)
            if result:
                print()

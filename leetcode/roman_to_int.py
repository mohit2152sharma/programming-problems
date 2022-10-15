"""Convert a givne roman number to integer"""

from collections import Counter


class Solution:
    def romanToInt(self, s: str) -> int:
        return self.edge_cases(remain_chars=s)

    @staticmethod
    def char_enumerate(s: str) -> int:
        one = {'I': 1}
        five = {'V': 5}
        ten = {'X': 10}
        fifty = {'L': 50}
        hundred = {'C': 100}
        five_hundred = {'D': 500}
        thousand = {'M': 1000}
        number = 0
        occurences = Counter(s)
        for pair in [one, five, ten, fifty, hundred, five_hundred, thousand]:
            for key, value in pair.items():
                if key in occurences.keys():
                    number += occurences[key]*value
        return number

    @staticmethod
    def edge_cases(remain_chars):
        four = {'IV': 4}
        nine = {'IX': 9}
        forty = {'XL': 40}
        ninety = {'XC': 90}
        four_hundred = {'CD': 400}
        nine_hundred = {'CM': 900}
        first_number = 0

        new_str = remain_chars

        for edge in [four, nine, forty, ninety, four_hundred, nine_hundred]:
            for key, value in edge.items():
                if key in new_str:
                    first_number += value
                    new_str = new_str.replace(key, '')
        first_number += Solution.char_enumerate(new_str)

        return first_number


if __name__ == '__main__':
    roman = input('enter romain number: ')
    integer = Solution().romanToInt(s=roman)
    print(integer)

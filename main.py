# This is a sample Python script.
from typing import List


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def longest_substring_with_distinct_characters(self, arr: List[str]) -> int:
        array_size = len(arr)
        array_index = 0
        max_substring_count = 0
        if array_size <= 1:
            return array_size
        while array_index < array_size:
            substring = {}
            for i in range(array_index, array_size):
                if arr[i] in substring.keys():
                    break
                substring[arr[i]] = True
                print(substring)
            max_substring_count = max(max_substring_count, len(substring.keys()))
            if max_substring_count >= array_size - array_index:
                return max_substring_count
            array_index += 1
        return max_substring_count


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(Solution().longest_substring_with_distinct_characters(['a', 'b', 'b', 'c', 'b', 'a']))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

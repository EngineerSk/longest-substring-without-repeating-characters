# This is a sample Python script.
from typing import List


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def longest_substring_with_distinct_characters(self, arr: List[str]) -> int:
        array_size = len(arr)
        if array_size <= 1:
            return array_size
        substring_map = {}
        left = 0
        right = 0
        max_substring_count = 0
        while left < array_size and right < array_size:
            element = arr[right]
            if element in substring_map.keys():
                left = max(left, substring_map[element] + 1)
            substring_map[element] = right
            max_substring_count = max(max_substring_count, right - left + 1)
            if max_substring_count > array_size - left:
                return max_substring_count
            right += 1
        return max_substring_count


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(Solution().longest_substring_with_distinct_characters(['a', 'b', 'b', 'c', 'b', 'a']))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

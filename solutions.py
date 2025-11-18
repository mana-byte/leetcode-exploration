# this are the solutions of the leetcode problems I solved
# WARNING: Some soltutions are suboptimal and can be optimized further


# 1. Two Sum
def twoSum(nums, target):
    result = []
    for index, num in enumerate(nums):
        for index_, num_ in enumerate(nums):
            if not index_ == index and target == num + num_:
                if not index_ in result:
                    result.append(index_)
                if not index in result:
                    result.append(index)
    return result


# Notions utilized : enumerate => to get (index, value) pairs in list
# Time complexity : O(n^2) => because of the nested loops


# 2. Add Two Numbers WARNING: SUBOPTIMAL SOLUTION MORE OPTIMAL SOLUTION AT 883
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        num1 = self.create_number(self.extract_linked_list_to_list(l1)[::-1])
        num2 = self.create_number(self.extract_linked_list_to_list(l2)[::-1])
        num_t = [int(i) for i in str(num1 + num2)][::-1]
        return self.extract_list_to_linked_list(num_t)

    def create_number(self, l):
        total = ""
        for num in l:
            total += str(num)
        return int(total)

    def extract_linked_list_to_list(self, l1):
        l_ = l1
        num = []
        while not l_ is None:
            num.append(l_.val)
            l_ = l_.next
        return num

    def extract_list_to_linked_list(self, l):
        l_ = None
        if not l == []:
            l_ = ListNode(val=l[0], next=self.extract_list_to_linked_list(l[1::]))
        return l_


# Notion utilized : Linked List => singly linked list have two attributes (val, next) : val an int and next a Linked List
# [1::] => slicing to get all elements except the first one
# [::-1] => slicing to reverse a list
# Time complexity : O(n) => because of the while loop and the recursive calls


# 3. Longest Substring Without Repeating Characters NOTE: SLIDING WINDOW PROBLEM WITH CLASSIC WHILE LOOP
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        left = 0
        right = 0
        substring = s[right]
        max_len = 0
        while right < len(s) + 1:  # O(n)
            sub_set = set(substring)  # O(m)
            if len(substring) != len(sub_set):
                substring = s[left : right + 1]  # O(n)
                left += 1
            else:
                max_len = max(
                    len(substring), max_len
                )  # update the answer each time its valid not when there is a issue
                right += 1
                if right < len(s):
                    substring += s[right]

        return max_len


# Suboptimal methode: in O(n^2) time complexity => because of the while loop and the set creation and slicing
# Space complexity : O(m) => because of the set creation and slicing (m = length of the longest substring without repeating characters) => A good for space trade off for time complexity


# Optimal methode: NOTE: SLIDING WINDOW PROBLEM WITH FOR AND WHILE LOOPS
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        chars = (
            {}
        )  # dictionary to store the count of each character in the current window
        max_len = 0
        for char in s:  # initialize the dictionary with all characters in the string
            chars[char] = 0

        for right, char in enumerate(s):
            chars[char] += 1  # Count the current character
            while (
                chars[char] > 1
            ):  # If a character is ever detected as a duplicate we shrink the window from the left until there are no more duplicates
                chars[
                    s[left]
                ] -= 1  # This while loop ensures that there are no dupplicates except for the current character (because all duplicates would have been removed before)
                left += 1  # slide window
            max_len = max(max_len, right - left + 1)  # Updates the lenght
        return max_len


# in O(n) time complexity and O(m) space complexity (m = length of the longest substring without repeating characters) => Worse in space but a lot better in time


# Median of Two Sorted Arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_t = len(nums1) + len(nums2)
        nums_t = []
        if len(nums1) > len(nums2):
            nums_t = self.merge_list(nums1, nums2)
        else:
            nums_t = self.merge_list(nums2, nums1)
        if len_t % 2 == 1:
            return nums_t[(len_t // 2)]
        else:
            return (nums_t[(len_t // 2)] + nums_t[(len_t // 2) - 1]) / 2

    def merge_list(self, l1, l2):
        l_t = []
        while len(l1) > 0 and len(l2) > 0:
            if l1[0] >= l2[0]:
                l_t.append(l2.pop(0))
            else:
                l_t.append(l1.pop(0))
        if not len(l1) == 0:
            l_t = l_t + l1
        if not len(l2) == 0:
            l_t = l_t + l2
        return l_t


# Notions utilized : merging two sorted lists
# Time complexity : O(m + n) => because of the merging process
# Space complexity : O(m + n) => because of the merged lists


# Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        biggest_pal = s[0]
        for cursor, letter in enumerate(s):
            remaining_s = s[cursor + 1 : :][::-1]
            if len(remaining_s) < len(biggest_pal):
                break
            for cursor_, letter_ in enumerate(remaining_s):
                reverse_cursor = len(s) - cursor_
                if self.check_palindrome(s[cursor:reverse_cursor]):
                    biggest_pal = max([biggest_pal, s[cursor:reverse_cursor]], key=len)
        return biggest_pal

    def check_palindrome(self, s):
        return s == s[::-1]


# Notions utilized : palindrome => a string that reads the same forwards and backwards
# [::-1] => slicing to reverse a lists
# Time complexity : O(n^2) => because of the nested loops and the palindrome check

# Reverse 32 bit int


class Solution:
    def reverse(self, x: int) -> int:
        if x <= -(2**31) or x >= (2**31) - 1:
            return 0
        if x < 0:
            return -int(str(-x)[::-1])
        else:
            return int(str(x)[::-1])


# Notions utilized : string manipulation => converting int to string to reverse int
# [::-1] => slicing to reverse a lists
# Time complexity : O(n) => because of the string manipulation
# Space complexity : O(1) => because of the constant space used


# myAtoi
class Solution:
    def myAtoi(self, s: str) -> int:
        composed_number = ""
        for index, char in enumerate(s):
            if not char == " ":
                if not char in "abcdefghijklmnopqurstuvwxyz.,":
                    if char in "+-":
                        if composed_number == "":
                            composed_number += char
                        else:
                            break
                    else:
                        composed_number += char
                else:
                    break
            elif composed_number != "":
                break
        if composed_number in " +-":
            composed_number = 0
        if int(composed_number) <= -(2**31):
            composed_number = -(2**31)
        if int(composed_number) >= (2**31) - 1:
            composed_number = (2**31) - 1
        return int(composed_number)


# Notions utilized : string manipulation => converting int to string to reverse int
# Time complexity : O(n) => because of the string manipulation
# Space complexity : O(1) => because of the constant space used


# Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        cursor_right = 0
        cursor_left = len(height) - 1
        while cursor_left > cursor_right:
            area = min(height[cursor_right], height[cursor_left]) * (
                cursor_left - cursor_right
            )
            max_area = max(area, max_area)
            if height[cursor_right] < height[cursor_left]:
                cursor_right += 1
            else:
                cursor_left -= 1
        return max_area


# Notions utilized : two pointer technique => using two pointers to traverse the list from both ends
# Time complexity : O(n) => because of the while loops
# Space complexity : O(1) => because of the constant space used


# Integer to Roman
class Solution:
    def intToRoman(self, num: int) -> str:
        val = [  # Use of mapping values to symbols
            1000,
            900,
            500,
            400,  # 900 = CM, 400 = CD are subtractive notations
            100,
            90,
            50,
            40,
            10,
            9,
            5,
            4,
            1,
        ]
        syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman = ""
        for i in range(len(val)):
            count = num // val[i]  # Returns how many times the value can fit into num
            roman += syms[i] * count
            num -= val[i] * count
        return roman


# Notions utilized : greedy algorithm => always choosing the largest possible value to form the roman numeral
# Time complexity : O(n) => because of the for loop
# Space complexity : O(1) => because of the constant space used


# Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        ignore_next = False
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        for index, roman in enumerate(s):
            if not ignore_next:
                if index == len(s) - 1:
                    num += val[syms.index(roman)]
                    break
                if roman + s[index + 1] in syms:
                    num += val[syms.index(roman + s[index + 1])]
                    ignore_next = True
                else:
                    num += val[syms.index(roman)]
            else:
                ignore_next = False
        return num


# Notions utilized : greedy algorithm => always choosing the largest possible value to form the roman numeral
# Time complexity : O(n) => because of the for loop
# Space complexity : O(1) => because of the constant space used


# Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_com = ""
        commons = [
            (id, p) for id, (p, *r) in enumerate(zip(*strs)) if all(p == i for i in r)
        ]
        for index, (i, letter) in enumerate(commons):
            if index == i:
                prefix_com += letter
            else:
                break
        return prefix_com


# * : unpacking operator => ["a", "b", "c"] => a, b, c in function(*["a", "b", "c"])
# all() => to check if all for output are == i for i in r
# Notions utilized : zip(*) => to group letters by their index in each string
# all() => to check if all letters in a group are the same
# Time complexity : O(n*m) => because of the nested loops (n = number of strings, m = length of the shortest string)
# Space complexity : O(1) => because


# Remove Duplicates from Sorted Array II
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0
        fill = max(nums) + 1
        index = 0
        while index < len(nums):
            if nums[index] == fill:
                break
            if index != 0 and index != 1:
                if nums[index - 1] == nums[index] and nums[index - 2] == nums[index]:
                    p += 1
                    nums.append(fill)
                    nums.pop(index)
                    index -= 1
            index += 1
        return len(nums) - p


# Complexity analysis: O(n) time | O(1) space


# Best Time to Buy and Sell Stock II
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for index in range(1, len(prices)):
            if prices[index - 1] < prices[index]:
                profit += (
                    prices[index] - prices[index - 1]
                )  # If the prices of yesterday are lower than the prices of today then SELL
        return profit


# Notions utilized : greedy algorithm => always choosing to sell when the price is higher than the previous day


# Jump Game :NOTE: GREEDY ALGORITHM DYNAMIC PROGRAMMING PROBLEM
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i, jump in enumerate(nums):
            if farthest == len(nums) - 1:
                return True
            if jump == 0 and farthest == i:  # checks you are stuck in place
                return False
            farthest = max(
                farthest, i + jump
            )  # updates the farthest index you can reach
        return True


# The goal here is not to play the game but to see what is the maximum possible index you can reach

# H index:


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        pot_hindex = [0]
        for cit in range(max(citations) + 1):
            p = 0
            for index_, cit_ in enumerate(citations):
                if cit <= cit_:
                    p += 1
            if p >= cit:
                pot_hindex.append(cit)
        return max(pot_hindex)


# Complexity : O(n^2) time | O(1) space


import random


# Implement solution such that you can control the index of the array using a hashmap
class RandomizedSet:

    def __init__(self):
        self.random_set_dict = {}  # stores values and their index: [values]: index
        self.random_set = []  # stores values

    def insert(self, val: int) -> bool:
        if val in self.random_set:
            return False
        self.random_set.append(val)
        self.random_set_dict[val] = len(self.random_set) - 1
        return True

    def remove(self, val: int) -> bool:
        if not val in self.random_set:
            return False
        index = self.random_set_dict[val]
        last = self.random_set[len(self.random_set) - 1]
        self.random_set[index] = last
        self.random_set_dict[last] = index
        self.random_set.pop()
        del self.random_set_dict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.random_set)


# Insert Delete GetRandom O(1) => Sol : Make a hashmap that stores the indexes of the list elements
import random


# Implement solution such that you can control the index of the array using a hashmap
class RandomizedSet:

    def __init__(self):
        self.random_set_dict = {}  # stores values and their index: [values]: index
        self.random_set = []  # stores values

    def insert(self, val: int) -> bool:
        if val in self.random_set:
            return False
        self.random_set.append(val)
        self.random_set_dict[val] = len(self.random_set) - 1
        return True

    def remove(self, val: int) -> bool:
        if not val in self.random_set:
            return False
        index = self.random_set_dict[val]
        last = self.random_set[len(self.random_set) - 1]
        self.random_set[index] = last
        self.random_set_dict[last] = index
        self.random_set.pop()
        del self.random_set_dict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.random_set)


# Complexity : O(1) time | O(n) space


# Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for i in range(len(nums))]

        left = 1
        for i in range(
            len(nums)
        ):  # Multiplies all the numbers left from the current index i and stores it in output
            output[i] = output[i] * left
            left = left * nums[i]

        right = 1
        for i_ in range(
            len(nums)
        ):  # multiplies all the numbers right from the current index i (which traverses the list from right to left) and stores and multiplies it in output
            i = len(nums) - 1 - i_
            output[i] = output[i] * right
            right = right * nums[i]

        return output


# O(n) time | O(1) space (output array does not count as extra space)


# gas station
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if (
            sum(gas) - sum(cost) < 0
        ):  # Checks if there is enough fuel to even complete the circuit
            return -1
        start = 0
        tank = 0
        for i_ in range(
            len(gas) * 2
        ):  # Iterates twice to ensure a circular route is possible
            i = i_ % len(gas)
            tank += gas[i] - cost[i]  # Accumulate the fuel
            if (
                start + len(gas) == i_
            ):  # checks if we have gone full circle and if that is the case finish
                return start
            if (
                tank < 0
            ):  # If tank is negative it means we cannot start from 'start' index so we reset the tank and move start to the next index
                tank = 0
                start = (
                    i + 1
                )  # Move to the next possible start index. All start index before are not possible because even with a surplus from the first start index it was still not possible so with even less fuel it is impossible
        return start


# O(2n) time | O(1) space => O(n) time | O(1) space


# Candy => HARD
class Solution:
    def candy(self, ratings: List[int]) -> int:
        dist_candies = [0 for i in range(len(ratings))]  # O(n) time
        for i in range(len(ratings) - 1):  # O(n) time
            if ratings[i] < ratings[i + 1]:
                dist_candies[i + 1] = (
                    1 + dist_candies[i]
                )  # Don't need to cumulate because we only care about relative values and we want the absolute minimum possible

        for i_ in range(1, len(ratings)):  # O(n) time
            i = len(ratings) - i_
            if (
                ratings[i - 1] > ratings[i] and dist_candies[i - 1] <= dist_candies[i]
            ):  # avoid changing candies if it is already greater when going back in from right to left
                dist_candies[i - 1] = 1 + dist_candies[i]
        return len(ratings) + sum(dist_candies)


# O(3n) time | O(n) space => O(n) time | O(n) space


# Reverse Words in a String
class Solution:
    def reverseWords(self, s: str) -> str:
        space = " "
        words = s.split(space)  # O(n)
        final_s = ""
        for index, word in enumerate(words[::-1]):  # O(n)
            if word != "":
                final_s += word + space
        return final_s[0 : len(final_s) - 1]  # O(n)


# O(3n) time | O(n) space => O(n) time | O(n) space


# Two Sum II - Input Array Is Sorted NOTE: CLASSIC TWO POINTER PROBLEM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        sum_ = -1
        while sum_ != target:
            sum_ = numbers[left] + numbers[right]
            if sum_ < target:
                left += 1
            if sum_ > target:
                right -= 1
        return [left + 1, right + 1]


# O(n) time | O(1) space

# 3Sum NOTE: CLASSIC TWO POINTER PROBLEM


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # O(logn n)

        output_set = (
            set()
        )  # Using set to avoid duplicates in O(1) time because in for set lookup are in O(1) compared to O(n) in list
        output = []
        for i, num in enumerate(nums):  # O(n)
            left = i + 1
            right = len(nums) - 1
            sum_ = 0
            while left < right:  # O(n)
                sum_ = num + nums[left] + nums[right]
                if (
                    sum_ == 0
                    and i != left
                    and i != right
                    and not frozenset({nums[left], num, nums[right]}) in output_set
                ):  # O(1) # Frozenset makes the set hashable so that i can enter the bigger set
                    output_set.add(frozenset({nums[left], num, nums[right]}))
                    output.append([nums[left], num, nums[right]])
                if sum_ < 0:
                    left += 1
                else:
                    right -= 1

        return output


# O(n logn + n^2) time | O(n) space => O(n^2) time | O(n) space
# Can be optimized ? No because of the sorting step


# Minimum size subarray sum  NOTE: CLASSIC SLIDING WINDOW PROBLEM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        sum_ = nums[right]
        min_sub = len(nums) + 1

        while right < len(
            nums
        ):  # O(n) Explanation: right pointer traverses the list once and left pointer traverses the list at most once
            if sum_ >= target:  #
                min_sub = min(
                    min_sub, right - left + 1
                )  # Get the minimum subarray length # Update answer first
                sum_ -= nums[left]  # update sum second
                left += 1  # Move pointer to shrink the window when the condition is satisfied
            else:  # Else we need to expand the window to try and satisfy the condition
                right += 1  # slide the window to the right to expand
                if (
                    right <= len(nums) - 1
                ):  # Avoid being out of range while on the last element if we put this in the while condition it will skip the last element
                    sum_ += nums[right]

        if min_sub != len(nums) + 1:  # If min_sub was updated
            return min_sub
        else:
            return 0


# O(n) time | O(1) space : This algo is a must know for interviews


# Group Anagrams NOTE: HASHMAP PROBLEM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = set()
        output_dict = {}
        for s in strs:  # O(n)
            sorted_s = "".join(
                sorted(s)
            )  # O(klogk) # Separe the string into a sorted list and joins the string back together => it now sorted
            if sorted_s in seen:
                output_dict[sorted_s].append(
                    s
                )  # Stores the anagrams together thanks to the sorted string as key
            else:
                output_dict[sorted_s] = [s]
                seen.add(sorted_s)
        output = []
        for values in output_dict.values():  # creates the output list
            output.append(values)
        return output


# O(n klogk) time | O(nk) space (n = number of strings, k = length of the longest string)


# Longest Consecutive Sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums_set = set(nums)
        max_len = 1
        for num in nums_set:
            if not num - 1 in nums_set:  # look for a start of sequence / solo number
                seq_len = 1
                while (
                    num + 1 in nums_set
                ):  # see if this is a sequence and calculate its length
                    num += 1
                    seq_len += 1
                max_len = max(seq_len, max_len)  # see if it is the longest
        return max_len


# O(n) time | O(n) space
# The reason why this is O(n) if because the for loop goes through only the start positions. Once a start is detected the while loop goes through the sequence. But the for loop never goes through any number in the sequence because they are not start positions. So each number is visited at most twice (once in for loop once in while loop) => O(2n) => O(n)

# Merge Intervals NOTE: CLASSIC INTERVAL PROBLEM


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(
            key=lambda x: x[0]
        )  # O(nlogn) # Sort intervals based on their first edge
        output = []
        prev = intervals[
            0
        ]  # Initialize the previous interval => this is needed to merge repeatly if there are more than one merge
        for index, interval in enumerate(intervals[1:]):
            if prev[1] >= interval[0]:  # check if interval 0 and +1 overlap
                prev = [
                    prev[0],
                    max(prev[1], interval[1]),
                ]  # Merge interval and don't save it => Need to wait to check if the merged interval can be merged again with another
            else:
                output.append(
                    prev
                )  # Once we check that i can't be merged again save it
                prev = interval  # Update prev to the current interval to check for next interval merge
        output.append(
            prev
        )  # For last elt since it won't be saved because the for loop doesn't save it

        return output


# O(nlogn + n) time | O(n) space => O(nlogn) time | O(n) space


# Insert Interval NOTE: CLASSIC INTERVAL PROBLEM
class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:

        for i in range(len(intervals) + 1):  # Insert new interval in O(n)
            if i == len(intervals):  # checks if the new interval is the biggest
                intervals.append(newInterval)
                break
            if (
                newInterval[0] <= intervals[i][0]
            ):  # checks if the new interval is smaller than the current interval
                intervals.insert(
                    i, newInterval
                )  # inserts the new interval at the correct position
                break

        # Same as merge intervals problem from here
        prev = intervals[0]
        output = []

        for interval in intervals[1 : len(intervals)]:
            if prev[1] >= interval[0]:
                prev = [prev[0], max(prev[1], interval[1])]
            else:
                output.append(prev)
                prev = interval
        output.append(prev)
        return output


# O(n) time | O(n) space since the interval is already sorted


# Minimum Number of Arrows to Burst Balloons NOTE: CLASSIC INTERVAL PROBLEM BUT WITH INTERVAL INTERSECTION
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        prev = points[0]
        counter = 1
        for point in points:
            if prev[1] >= point[0]:
                prev = [point[0], min(prev[1], point[1])]
            else:
                counter += 1
                prev = point
        return counter


# O(nlogn + n) time | O(1) space => O(nlogn) time | O(1) space


# Simplify Path NOTE: STACK PROBLEM
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack_path = path.split("/")  # O(n)
        stack_path = [""] + [s for s in stack_path if s != ""]  # O(2n)
        simplified_stack = []
        remove_next = 0
        for i_ in range(1, len(stack_path)):  # O(n)
            i = len(stack_path) - i_
            if stack_path[i] in {".", ".."}:  # O(1)
                remove_next += len(stack_path[i]) // 2
            elif remove_next == 0:
                simplified_stack.append("/" + stack_path[i])
            else:
                remove_next -= 1

        if len(simplified_stack) == 0:
            return "/"
        return "".join(simplified_stack[::-1])  # O(n)


# O(5n) time | O(n) space => O(n) time | O(n) space
# This solution is optimal but a bit hard to explain in an interview so here is a more intuitive one:


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack_path = path.split("/")  # O(n)
        simplified = []

        for dir_ in stack_path:  # O(n)
            if dir_ in {".", "..", ""}:  # check if "", "..", "." because special cases
                if (
                    len(simplified) != 0 and dir_ == ".."
                ):  # Only ".." is useful so the rest is ignored
                    simplified.pop()  # remove the last directory if possible
            else:
                simplified.append(dir_)  # add the directory to the path

        return "/" + "/".join(
            simplified
        )  # Joins the path back together with / between each directory


# O(3n) time | O(n) space => O(n) time | O(n) space
# A much simpler solution


# Min Stack NOTE: STACK PROBLEM
class MinStack:  # O(1) time for each operation

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        minval = self.getMin()
        if minval is not None:
            minval = min(val, minval)  # O(1)
        else:
            minval = val
        self.stack.append(
            [val, minval]
        )  # Uses a double storage solution to store the minval of the previous stack state + the current value. So the minimum of the current stack is always stored at the top of the stack

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return (
            self.stack[-1][0] if self.stack else None
        )  # So that it doesn't crash when calling it

    def getMin(self) -> int:
        return (
            self.stack[-1][1] if self.stack else None
        )  # None checking to avoid crash when pushing the first element


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# WARNING: CAN SEEM EASY BUT THE GOAL IS TO GET O(1) TIME FOR EACH OPERATION !
# This solution is to avoid doing min(self.stack) which is O(n)


# Reverse Polish Notation NOTE: STACK PROBLEM
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Use a stack
        # Iterate over the list:
        # If number put it in stack
        # If operand pop the last two numbers and put the result operations in stack
        # return the last elt in the stack
        number_stack = []
        for token in tokens:
            if token.lstrip(
                "-"
            ).isnumeric():  # O(1) # isnumeric() only works for positive numbers so we need to strip the - sign if it exists
                number_stack.append(int(token))
            else:
                num1 = number_stack.pop()
                num2 = number_stack.pop()
                res = 0
                if token == "*":
                    res = num2 * num1
                if token == "+":
                    res = num2 + num1
                if token == "-":
                    res = num2 - num1
                if token == "/":
                    res = int(num2 / num1)  # Handle division towards 0
                number_stack.append(res)
        return number_stack[0]  # Last elt in stack is the result


# O(n) time | O(n) space


# Add two numbers represented by linked lists NOTE: LINKED LIST PROBLEM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Traverser les linked list
        # Recuperer les nombres et les ajouter dans un string
        # Addionner les deux strings
        # creer la linked list output
        num1 = self.getNumber(l1)
        num2 = self.getNumber(l2)
        sum_ = num1 + num2

        dummy = ListNode()  # Creates a empty Node val = 0, next = None
        curr = dummy  # Cursor points to dummy
        for i in str(sum_)[
            ::-1
        ]:  # NOTE: Classic way to create a linked list from a list
            curr.next = ListNode(
                int(i)
            )  # Creates a new node with the value of the current digit
            curr = curr.next  # Puts cursor to the next node
        return dummy.next

    def getNumber(self, l):  # NOTE: Classic function to get through a linked list
        curr = l
        output = ""
        while curr is not None:
            output += str(curr.val)
            curr = curr.next
        return int(output[::-1])


# O(n) time | O(n) space

#  Copy List with Random Pointer NOTE: LINKED LIST PROBLEM
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        # Creer une nouvelle liste avec uniquement les valeurs de l'ancienne (sans random)
        # Faire une traverser de la linked list ou l'on assigne les pointer random de la liste d'avant a la nouvelle liste

        output = Node(0)  # Initialize output node
        curr_output = output
        curr_head = head
        map_head = (
            {}
        )  # Map to store the index of each node in the original list [Node] = index
        map_output = (
            {}
        )  # Map to store the node of each index in the new list [index] = Node
        # Making this we will be able to correspond the relations : Node => index => Node (in new list)
        counter = 0
        while curr_head is not None:  # DEEPCOPY OF VALUES
            curr_output.next = Node(curr_head.val)  # Creates new Node (deepcopy)
            map_head[curr_head] = counter  # Maps current node to its index (head)
            map_output[counter] = (
                curr_output.next
            )  # Maps index to the new node (output)
            curr_head = curr_head.next
            curr_output = curr_output.next
            counter += 1

        curr_head = head
        curr_output = output
        while curr_head is not None:  # DEEPCOPY OF RANDOM POINTERS
            if curr_head.random is not None:  # if random pointer exists
                index_rand = map_head[curr_head.random]  # Node => Index
                curr_output.next.random = map_output[
                    index_rand
                ]  # Index => Node (in new list)
            else:
                curr_output.next.random = None
            curr_head = curr_head.next
            curr_output = curr_output.next

        return output.next


# O(n) time | O(n) space Can be optimized to O(1) space but the code is a bit more complex and less intuitive


# Reverse Linked List II NOTE: LINKED LIST PROBLEM


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        # Explication: This algo has 4 steps:
        # 1. Get the elements to be reversed and the leftovers (elements not to be reversed)
        # 2. Reverse the elements to be reversed and create a new linked list with them
        # 3. Add the leftover elements to the new linked list
        # 4. Create a new linked list with the beginning of head and the rest of the new linked list

        # Obtient la liste des éléments concernés et des leftovers
        curr = head
        counter = 1
        reverse_elt = []  # elements to be reversed
        left_over = (
            ListNode()
        )  # Leftover elements (elements not to be reversed) stored as Linked List because we are not modifing them
        while curr:  # O(n)
            if counter >= left and counter <= right:
                reverse_elt.append(curr.val)
            if counter == right:
                left_over.next = curr.next
            curr = curr.next
            counter += 1

        reverse_elt = reverse_elt[
            ::-1
        ]  # O(right - left) # Reverse the elements to be reversed

        # Creer la linked list baser sur les elt dans reverse_elt
        reverse_lk = ListNode(0)
        curr = reverse_lk
        for i in reverse_elt:  # O(right - left)
            curr.next = ListNode(i)
            curr = curr.next

        # Rajouter le reste de la linked list
        curr.next = left_over.next

        # Creer une nouvelle linked list avec le début de head et le reste de reverse_lk
        output = ListNode(0)
        curr = output
        curr_head = head
        counter = 1
        while curr_head:  # O(n)
            if counter == left:
                curr.next = reverse_lk.next
                break
            curr.next = ListNode(curr_head.val)
            curr_head = curr_head.next
            curr = curr.next
            counter += 1

        return output.next


# O(n) time | O(n) space => Intuitive solution but can be optimized to O(1) space with a bit more complex code

# Remove Nth Node From End of List NOTE: LINKED LIST PROBLEM


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Traverser la liste une fois pour savoir l'index a retirer (len(lk) - n + 1)
        # Traverser la liste une autre fois pour remplacer le node par son prochain

        # Traverse la liste pour avoid sa longueur
        curr = head
        len_lk = 0  # 0 because it will count the None node
        while curr:
            curr = curr.next
            len_lk += 1

        # Get the index to remove - 1 because we want the node before the one to remove
        remove_index = (
            len_lk - n
        )  # On veut changer le curr.next donc on s'arrete au node avant

        # Edge case where we need to remove the head
        if remove_index == 0:
            head = head.next
            return head

        # Traverse la liste pour retirer le node
        curr = head
        counter = 1
        while curr:
            if (
                counter == remove_index
            ):  # When we reach the node before the one to remove we change its next pointer to skip the next node
                curr.next = curr.next.next
                break
            curr = curr.next
            counter += 1

        return head


# O(2n) time | O(1) space => O(n) time | O(1) space

# Construct Binary Tree from Preorder and Inorder Traversal NOTE: BINARY TREE PROBLEM


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Regarder le premier elt de preorder : root = preorder.val
        # TreeNode.val = root
        # Séparer la inorder liste en deux left, right par rapport a root
        # Séparer la preorder list en fonction des elt dans left et right ATTENTION: GARDER L'ORDRE
        # utiliser buildTree(pre_left, in_left, TreeNode.left) et buildTree(pre_right, in_right, TreeNode.right)
        if preorder == [] or inorder == []:  # If no more nodes to add
            return None

        tree = TreeNode()  # Create a node

        root = preorder[
            0
        ]  # The root value is the first element of preorder because it is root -> left -> right
        tree.val = root  # Set node value
        root_index = inorder.index(
            root
        )  # Get the index of the root in inorder to separate left and right subtrees # O(n)

        left_in = inorder[
            :root_index
        ]  # In inorder if we get the root we can know all the elements left of the root and all the elements right of the root
        right_in = inorder[root_index + 1 :]  # +1 to avoid taking the root itself

        left_pre = preorder[
            1 : len(left_in) + 1
        ]  # Get new preorder list for right and left. In preorder after the root all the elements of the left subtree are present in order since we know the len we can get all the elt
        right_pre = preorder[len(left_in) + 1 :]  # +1 to avoid taking the root

        tree.left = self.buildTree(
            left_pre, left_in
        )  # Recursive calls to build the left and right subtrees
        tree.right = self.buildTree(
            right_pre, right_in
        )  # O(n) time for each call because of the index() function

        return tree


# O(n^2) time | O(n) space => Suboptimal solution

# OPTIMAL
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Creer une hashmap pour eviter devoir trouver l'index du root en O(n)
        # Utiliser une queu sur preorder car on sait que preorder possede les roots
        # des subtrees de tout l'arbre dans l'ordre
        # Utiliser une fonction récursive pour traverser l'arbre dans l'ordre de preorder
        # Cette traverser se fait a l'aide de inorder pour savoir le nombre d'éléments restant a droite et
        # a gauche du node actuelle et pour mettre une condition d'arret si la liste est vide (end - start)

        inorder_map = {}  # Use hashmap to avoid doing index()
        queue_pre = deque()
        for i in range(len(preorder)):
            inorder_map[inorder[i]] = i
            queue_pre.append(preorder[i])

        # can also do this: queue_pre = deque(preorder)
        # and this: inorder_map = {v: i for i, v in enumerate(inorder)}

        def building(start, end):  # Use two pointers to get sub list
            if end - start < 0:  # If no more elements to add
                return None
            root = TreeNode(queue_pre.popleft())
            index_root = inorder_map[root.val]

            root.left = building(
                start, index_root - 1
            )  # What we really need is the length of the left subtree which is index_root - start to know how many elements are in the left subtree and stop when we reach the end of the left subtree
            root.right = building(index_root + 1, end)

            return root

        return building(0, len(preorder) - 1)


# O(n) time | O(n) space

# Construct Binary Tree from Inorder and Postorder Traversal NOTE: BINARY TREE PROBLEM


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # [9,|,15,20,7] in => Need to get index
        # [9,15,7,20,X] post
        # [9] (1) [15, 20, 7] (3) In
        # [9] [15, 7, 20] Post => c'est nombre la ne sont pas utiles => on veut juste le nb d'elt restant
        # buildTree(In_right, post_right) # DROITE EN PREMIER CAR c'est l'ordre du stack postorder
        # buildTree(In_left, post_left)

        # METHODE
        # Utiliser une hashmap sur inorder pour avoir les index
        # Considerer postorder comme un stack ou le dernier elt est une root d'une subtree
        # Implémentation récursive:
        # Utilisation de deux pointeur pour obtenir le nombre restant d'elt a droite et a gauche d'un node donnée

        index_inorder = {v: k for k, v in enumerate(inorder)}  # O(n) time | O(n) space

        def build(start, end):  # O(n) time | O(n) space
            if end - start < 0:
                return None
            root = TreeNode(postorder.pop())
            index_root = index_inorder[root.val]

            root.right = build(
                index_root + 1, end
            )  # Right first because of the order of postorder stack
            root.left = build(start, index_root - 1)
            return root

        return build(0, len(postorder) - 1)


# O(n) time | O(n) space


# Subsets NOTE: BACKTRACKING PROBLEM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # We use backtracking to get all the possible combinations
        # We represent the algo in a tree where each node has two branches : pick or don't pick the current number
        # for example [1,2,3] would be represented as:
        #               []
        #          /         \
        #        []          [1]    # Don't pick 1 or pick 1
        #      /    \      /     \
        #    []     [2]  [1]     [1,2] # Don't pick 2 or pick 2
        #   / \     / \   / \     / \
        # [] [3]  [2] [2,3] [1,3] [1,2,3] # Don't pick 3 or pick 3
        # NOTE: Time complexity is the depth of the tree which is 2^n where n is the number of elements in nums

        output = []
        sol = []

        def backtracking(
            i,
        ):  # We represent the choice of picking or not picking using backtracking with the index i. i reprents the current num and i + 1 the next num depending on the choice
            # If we reached the end of the list we add the current solution to the output
            if i == len(nums):
                output.append(sol[:])  # We add a copy of the current solution
                return

            # Don't pick nums[i]
            backtracking(i + 1)

            # Pick nums[i]
            sol.append(nums[i])  # We pick
            backtracking(i + 1)
            sol.pop()  # we backtrack to the previous state

        backtracking(0)
        return output


# O(2^n) time | O(n) space => To see it represent the solution as a tree

# Letter Combinations of a Phone Number NOTE: BACKTRACKING PROBLEM


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # We use backtracking but this time we have multiple branches at each node
        # each node has at least 4 branches counting the choice of not picking any letter
        # for example for "23" we have:
        #               ""
        #          /    |    |    \
        #        ""    "a"  "b"   "c"    # Don't pick or pick a, b, c # digit 2 (its the same as pick or don't pick digit 2 but digit 2 has 3 letters)
        #      / | \   /|\   /|\   /|\
        #    "" "d" "e" "f" "ad" "ae" "af" "bd" "be" "bf" "cd" "ce" "cf" # digit 3 (same as pick or don't pick digit 3 but digit 3 has 3 letters)
        if digits == "":
            return []

        phone_map = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
        }
        output = []
        # Compared to the last problem sol here is the letters var which stores the current combination of letters

        def backtrack(idx, letters):
            if idx == len(digits):
                if len(letters) == len(
                    digits
                ):  # We only want to add the combination if we picked a letter for each digit # Again this can be removed because we are forced to pick a letter for each digit
                    output.append(letters)
                return

            # Don't pick any letter for the current digit
            backtrack(
                idx + 1, letters
            )  # We can remove this line because the choice of not picking is not needed for the result we are forced to pick a letter for each digit

            # Pick a letter for the current digit 3 branches
            for letter in phone_map[int(digits[idx])]:
                backtrack(idx + 1, letters + letter)

        backtrack(0, "")
        return output


# O(4^n) time | O(n) space => 4^n because the max number of letters for a digit is 4 (7 and 9)


# Combinations NOTE: BACKTRACKING PROBLEM
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # We use backtracking to get all the possible combinations of k numbers from 1 to n
        # We represent the algo in a tree where each node has two branches : pick or don't pick the current number
        # for example n = 4, k = 2 would be represented as:
        #              []
        #          /    \
        #        []     [1]    # Don't pick 1 or pick 1
        #      /  \     /  \
        #    []  [2]  [1]  [1,2] # Don't pick 2 or pick 2
        #   / \   / \  / \   / \
        # [] [3] [2] [2,3] [1,3] [1,2,3] # Don't pick 3 or pick 3
        #  / \   / \   / \    / \    /  \
        # [] [4] [3] [3,4] [1,4] [1,3,4] [2,4] [2,3,4] [1,2,4] [1,2,3,4] # Don't pick 4 or pick 4
        # We cut off the branches where the length of the current solution is greater than k

        output = []
        sol = []

        def backtrack(num):  # O(2^n)? other sol O(n^k)
            if num == n + 1:
                if len(sol) == k:
                    output.append(sol[:])
                return

            # Don't pick
            backtrack(num + 1)

            # Pick the next number
            if len(sol) < k:
                sol.append(num)
                backtrack(num + 1)
                sol.pop()

        backtrack(1)
        return output


# O(2^n) time | O(k) space


# Permutations NOTE: BACKTRACKING PROBLEM
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # We use backtracking to get all the possible permutations
        # In [1, 2, 3] we represent the algo in a tree where each node has n branches where n is the number of elements not yet picked
        #         []
        #      /  |  \
        #    [1] [2] [3]  # Pick 1, 2 or 3
        #   /|\   /|\   /|\
        # [1,2][1,3][2,1][2,3][3,1][3,2] # Pick 1, 2 or 3 from the remaining elements
        # /|\   /|\   /|\   /|\   /|\   /|\
        # [1,2,3][1,3,2][2,1,3][2,3,1][3,1,2][3,2,1] # Pick the last remaining element

        # One small remark:  In output.append(perm) we can see that the list is not copied but the reference is added directly to the output.
        # This is because in backtrack(perm + [i]) we create a new list each time so perm is always a new list and not a reference to the same list
        # So python creates a new list for each instance of recursion. These list will get garbage collected once the recursion is done so we don't need to copy the list when adding it to the output
        # This is specific to python because of its memory management
        if nums == []:
            return []
        output = []
        nums_set = set(nums)  # Use set because nums is full of distinct numbers

        def backtrack(perm):  # O(n!) (recursion depth) * O(n) (complexity in recursion)
            if len(perm) == len(nums):
                output.append(perm)
                return
            for i in nums_set - set(perm):
                backtrack(perm + [i])

        backtrack([])
        return output


# O(n * n!) time | O(n) space

# Combination Sum NOTE: BACKTRACKING PROBLEM


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []

        def backtrack(
            idx, nums_sum, sum_
        ):  # O(n^m) where n is the number of candidates and m is target / min(candidates) (worst case we use the smallest candidate to reach the target)
            if sum_ == target:
                output.append(nums_sum)
                return
            if sum_ > target:
                return
            for i in range(
                idx, len(candidates)
            ):  # O(n) # Here we look at the candidates starting from idx to avoid duplicates because candidates before idx have all their combinations already calculated
                cand = candidates[i]
                backtrack(i, nums_sum + [cand], sum_ + cand)

        backtrack(0, [], 0)
        return output


# O(n^(target/min(candidates))) time | O(target/min(candidates)) space


# Search a 2D Matrix NOTE: BINARY SEARCH PROBLEM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # m * n  matrix size
        # We represent the sorted matrix into a list and do a binary search on it
        # To convert the index of the list to the index of the matrix we use:
        # col_index = index % n (n = number of columns)
        # row_index = index // n (n = number of columns)
        # WHY ?: because if we have a list of k elt and we want to create a matrix from that list with n columns
        # we will have k // n rows and k % n columns in the last row

        n = len(matrix[0])
        m = len(matrix)
        left = 0
        right = n * m - 1

        while left <= right:  # O(log(m*n)) = O(logm + logn)
            avg = (right + left) // 2
            avg_n = avg % n  # Get the column index
            avg_m = avg // n  # Get the row index

            if matrix[avg_m][avg_n] > target:
                right = (
                    avg - 1
                )  # Move the right pointer to avg - 1 because avg is already checked
            elif matrix[avg_m][avg_n] < target:
                left = (
                    avg + 1
                )  # Move the left pointer to avg + 1 because avg is already checked
            else:
                return True
        return False


# O(log(m*n)) time | O(1) space


# Find Peak Element NOTE: BINARY SEARCH PROBLEM
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        # Set default peak
        peak = 0
        peak_val = max(nums[left], nums[right])

        if nums[left] == peak_val:
            peak = left
        else:
            peak = right

        while left <= right:
            mid = (left + right) // 2
            mid_l_val = nums[mid - 1] if mid - 1 >= 0 else float("-inf")  # Check bounds
            mid_r_val = nums[mid + 1] if mid + 1 < len(nums) else float("-inf")

            max_mid = max(
                mid_l_val, mid_r_val
            )  # Since nums[i+1] != nums[i] we are sure that max_mid != nums[mid] so we can always move in the direction of the max_mid

            if peak_val < nums[mid]:  # Update peak if we found a new one
                peak_val = nums[mid]
                peak = mid

            if max_mid == mid_r_val:
                left = mid + 1
            else:
                right = mid - 1
        return peak


# O(logn) time | O(1) space


# Number of Islands NOTE: GRAPH PROBLEM
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # What we do is check all the grid and when we find "1" we do a DFS to remove all the connected "1" and increase the counter of islands by 1

        if not grid or not grid[0]:
            return 0

        output = 0
        m = len(grid)
        n = len(grid[0])

        def remove_island(row, col):  # O(k)
            if grid[row][col] == "0":
                return
            grid[row][col] = "0"
            for vert, lat in [
                (1, 0),
                (0, 1),
                (-1, 0),
                (0, -1),
            ]:  # Check all 4 directions
                new_row = row + vert
                new_col = col + lat
                if not (
                    new_row >= m or new_col >= n or new_row < 0 or new_col < 0
                ):  # Check bounds
                    remove_island(new_row, new_col)

        for row in range(m):  # O(m*n) # Traverse the grid
            for col in range(n):
                if grid[row][col] == "1":
                    remove_island(row, col)
                    output += 1

        return output


# O(m*n) time | O(m*n) space in worst case where the grid is full of land


# Generate Parentheses NOTE: BACKTRACKING PROBLEM
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # We use backtracking to add open parentheses and close parenthenses only when there is enough open parentheses to close
        # Here is the tree representation for n = 1:
        #               ""
        #          /         \
        #        "("          ")"    # Add open parenthese or close parenthese (only if there is enough open parentheses to close) # Here we don't explore ) because we can't close a parenthese if there is no open parenthese
        #      /    \      /     \
        #    "(("   "()"   "()"    "))" # Add open parenthese or close parenthese (only if there is enough open parentheses to close)
        # So the only result is "()" because )) and (( are invalid and we don't want to explore these branches


        res = [] # We can also use a set to avoid duplicates but here there is no need because we are only adding valid parentheses

        def dfs(openP, closeP, s):
            if (
                openP == closeP and openP + closeP == n * 2
            ):  # Max len is n * 2 because we have n open and n close parentheses
                res.append(s)
                return

            if (
                openP < n
            ):  # Only add an open parenthese if we haven't reached the limit of n since we need to close them later
                dfs(openP + 1, closeP, s + "(")

            if (
                closeP < openP
            ):  # Only add a close parenthese if there is enough open parentheses to close
                dfs(openP, closeP + 1, s + ")")

        dfs(0, 0, "")

        return res


# O(2^2 * n) time | O(n) space => O(4^n / sqrt(n)) time | O(n) space (Catalan number)

# Surrounded Regions NOTE: GRAPH PROBLEM
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # The idea is to explore all the edges to get all the not surrounded regions
        # When we find a O on the edge we explore all its neighbors and add them to a set of not_replace => DFS
        # Finally we traverse the board and replace all the O that are not in not_replace by
        # Simple solution big implementation
        m = len(board)
        n = len(board[0])
        not_replace = set() # Use a set because we will do a lot of lookups and we want O(1) time for that
        
        def explore_region(row, col):
            if board[row][col] == "X" or (row, col) in not_replace: # If we hit an X or if we already explored this region
                return
            
            not_replace.add((row, col))
            for vert, lat in [(1,0), (0,1), (-1,0), (0,-1)]: # Explore all 4 directions
                new_row = row + vert
                new_col = col + lat
                if not(new_row >= m or new_col >= n or new_row < 0 or new_col < 0): # Check bounds
                    explore_region(new_row, new_col)

        # Watch top and bottom
        for row in [0, m-1]:
            for col in range(n): # O(2n)
                if board[row][col] == 'O':
                    explore_region(row, col) # Explore the region and add all the connected 'O' to not_replace set
        # Watch Right and left
        for row in range(m): # O(2m)
            for col in [0, n-1]:
                if board[row][col] == 'O':
                    explore_region(row, col)
        
        # Replace everything that is not in not_replace inside (not on the edge)
        for row in range(1, m-1): # O((m-2)*(n-2))
            for col in range(1, n-1):
                if board[row][col] == 'O' and (row, col) not in not_replace:
                    board[row][col] = 'X'

# O(m*n) time | O(m*n) space in worst case where the board is full of 'O' => Even though there are 3 for in for loops we actually only traverse the whole board only 1 time !
# Because we traverse the edges (top, bot, right, left) and then the inside

# Valid Sudoku NOTE: MATRIX PROBLEM
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # The idea is to traverse the board using the squares as the main point of reference
        # Use hashmaps with sets to store values that have the same row annd col index
        # Use a set for a square traversal
        # If we find a duplicate in any of the 3 sets we return false
        # else we add the current val to the 3 sets according to their row, col and square

        rows = {i: set() for i in range(len(board))} # Hashmap to store values for each row
        cols = {i: set() for i in range(len(board[0]))}

        # Traverse the sudoku in squares
        # O(m * n)
        for row,col in [(1, 1), (4, 1), (7, 1), (1, 4), (4, 4), (7, 4), (1, 7), (4, 7), (7, 7)]: # Center of each square # This is hard coded but we could also do a loop to get these values range(1,8,3) and range(1,8,3)
            square = set() # Set to store values for the current square
            for lat, vert in [(0, 0), (-1, -1), (0, -1), (-1, 1), (-1, 0), (0, 1), (1, -1), (1, 0), (1, 1)]: # All the relative positions of the square
                new_row = row + vert
                new_col = col + lat
                val = board[new_row][new_col]

                if val != ".":
                    if val in rows[new_row] or val in cols[new_col] or val in square: # If the value is already in the row, column or square we return false because it is a duplicate
                        return False
                    rows[new_row].add(val)
                    cols[new_col].add(val)
                    square.add(val)

        return True

# O(m * n) time | O(m * n) space => Constant time because the board is always 9 * 9
# This solution is not standard because of the hardcoded values but it is more intuitive to understand

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        
        # The board traversal is done row by row
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[(r // 3, c // 3)]: # if the value is already in the row, column or box we return false because it is a duplicate
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c]) # Each box is identified by its (row // 3, col // 3) index (division by 3 because each box is 3 * 3)
        
        return True
# More standard solution

# Spiral Matrix NOTE: MATRIX PROBLEM
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # The idea is to do a dfs that keeps track of the direction we are going
        # We start with the direction right and if we hit a border we change the direction based on the order right -> down -> left -> up
        # If a direction is taken we forget about all other directions until we hit a border again
        output = []
        m = len(matrix)
        n = len(matrix[0])
        
        def dfs_first(row, col, dir_):
            output.append(matrix[row][col])
            matrix[row][col] = '.' # Mark as visited

            new_row = row + dir_[1]
            new_col = col +dir_[0]
            if not (new_col < 0 or new_row < 0 or new_col >= n or new_row >= m or matrix[new_row][new_col] == '.'): # Check if we can keep going in the same direction
                dfs_first(new_row, new_col, dir_)
                return

            for lat, vert in [(1, 0), (0, 1), (-1, 0), (0, -1)]: # If not we try all other directions in order right -> down -> left -> up
                if (lat, vert) == dir_: # Avoid checking the same direction again
                    continue
                new_col = col + lat
                new_row = row + vert
                if not (new_col < 0 or new_row < 0 or new_col >= n or new_row >= m or matrix[new_row][new_col] == '.'):
                    dfs_first(new_row, new_col, (lat, vert)) # Change direction
                    return  # Forget about all other directions once we changed direction

        dfs_first(0, 0, (1, 0))
        return output

# O(m*n) time | O(1) space (we don't take into account the output list) => We modify the input matrix to keep track of visited cells so that we get O(1) space

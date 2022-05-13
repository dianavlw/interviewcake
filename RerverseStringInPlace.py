
"""
Write a function that takes a list of chracters and reverses the letters in place
https://www.interviewcake.com/question/python/reverse-string-in-place?course=fc1&section=array-and-string-manipulation

"""

We swap the first and last characters, then the second and second-to-last characters, and so on until we reach the middle.
O(n) time and O(1)O(1) space.

def reverse(list_of_chars):

    left_index  = 0
    right_index = len(list_of_chars) - 1

    while left_index < right_index:
        # Swap characters
        list_of_chars[left_index], list_of_chars[right_index] = \
            list_of_chars[right_index], list_of_chars[left_index]
        # Move towards middle
        left_index  += 1
        right_index -= 1
        
 """
https://leetcode.com/problems/reverse-string/
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
https://www.youtube.com/watch?v=_d0T_2Lk2qA
 """
Time: O(n) Space: O(1)

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        L, R = 0, len(s)-1
        
        while L < R:
            s[L], s[R] = s[R], s[L]
            L, R = L +1, R -1






Time: O(n) Space: O(n)

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if L < R:
          s[L], s[R] = s[R], s[L]
          reverse(L+1, R-1)
        reverse(0,len(s)-1)
        
        

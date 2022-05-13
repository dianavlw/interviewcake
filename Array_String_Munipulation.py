"""
05132022

Your company built an in-house calendar tool called HiCal. 
You want to add a feature to see the times in a day when everyone is available.

[(1, 10), (2, 6), (3, 5), (7, 9)]

https://www.interviewcake.com/question/python/merging-ranges?course=fc1&section=array-and-string-manipulation

"""

def merge_ranges(meetings):
    # Sort by start time
    sorted_meetings = sorted(meetings)

    # Initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # If the current meeting overlaps with the last merged meeting, use the
        # later end time of the two
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start,
                                   max(last_merged_meeting_end,
                                       current_meeting_end))
        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings
  
    # O(nlgn) time and O(n)O(n) space.
  
  """
  LeetCode:
  
  https://leetcode.com/problems/merge-intervals/
  
  """
  
  class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()
        
        if intervals == []:
            return []
        for interval in intervals:
            if result == [] or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result [-1][1] = max(result[-1][1] , interval[1])
        return result
# https://www.youtube.com/watch?v=5EY9rHCfa8g


"""

"""
56. Merge Intervals

input: [[1,3], [2,6], [8,10], [15,18]]
output: [[1,6],[8,10],[15,18]]

"""

class Solution:
  def merge(self, intervals:List[List[int]]) -> List[List[int]]:
    # what is the interval is empty? return [] empty list
    if intervals == []:
      return []
    # we will be returning a new [] where we have a merged intervals so our we are returning a new []
    result = []
    # sort the start time first index of all index of the list ,and then we can go thro and iterate
    intervals.sort()
    for intervals in intervals:
      if result == [] or result[-1][1] < interval[0]: # the entire to the output first or no overlap // endtime is less that the start time, its endtime is less than the start time
        result.append(interval) #interval to result
      else: # if there is an overlap covers the entire range the max of the end time, or end time of interval 
        result[-1][1] = max(result[-1][1], interval[1])
        
"""


*** explanation for code: ***

intervals = [[1,3],[2,6],[8,10],[15,18]]

result = []
is result empty? YES
result.append(interval)
append [1,3] to result
result = [[1,3]]

is result empty? NO
or does its last interval in the results end time: [[1,3]], result[-1][1] come before my start time [2,6]? # line20 
[[1,3],[2,6], my end time starts before my start time so yes overlap
there is an overlap...so max(result[-1][1], interval[1])
result = [1,6]

move on to the next interval
[8,10]
is result empty? NO
or does its end time come before my start time? YES
result.append(interval)
[[1,3],[2,6],[8,10]]

move on to the next interval
[15,18]
is result empty? NO
or does its end time come before my start time? YES
result.append(interval) 
[[1,3],[2,6],[8,10],[15,18]]


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

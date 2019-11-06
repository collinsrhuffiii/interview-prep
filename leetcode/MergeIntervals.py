'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
'''

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x:x.end)
        intervals = sorted(intervals, key=lambda x:x.start)
        i = 0
        while(i < len(intervals) - 1):
            int1 = intervals[i]
            int2 = intervals[i+1]
            if int1.end >= int2.start:
                new_int = Interval(int1.start, max(int1.end, int2.end))
                intervals[i] = new_int
                intervals.pop(i+1)
            else:
                i += 1
        return intervals

sol = Solution()

list_intervals = [Interval(1,4), Interval(2,3)]

print('Input:')
for interval in list_intervals:
    print(interval.start, interval.end)
print('Output:')
ret_ints = sol.merge(list_intervals)
for interval in ret_ints:
    print(interval.start, interval.end)
print()

list_intervals = [Interval(1,3), Interval(2,6), Interval(8,10),
        Interval(15,18)]
print('Input:')
for interval in list_intervals:
    print(interval.start, interval.end)
print('Output:')
ret_ints = sol.merge(list_intervals)
for interval in ret_ints:
    print(interval.start, interval.end)
print()

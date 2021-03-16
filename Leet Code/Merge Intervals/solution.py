# First Attempt - 88 - 92 ms
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        answers = []
        #edge case
        if len(intervals) == 1:
            return intervals
        # reverse stack
        intervals = intervals[::-1]
        l1 = intervals.pop()
        i = 0
        # merge
        while intervals:
            l2 = intervals.pop()
            if l1[1] >= l2[0]:
                l3 = [min(l1[0], l2[0]), max(l1[1], l2[1])]
                if answers:
                    answers.pop()
                answers.append(l3)
                l1 = l3
            else:
                if i == 0:
                    answers.append(l1)
                answers.append(l2)
                l1 = l2
            i += 1
        return answers

# Second Attempt - In Place Merge 80-84 ms faster than 91.78 %
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # edge case
        if len(intervals) == 1:
            return intervals
        # sort and reverse intervals
        intervals = sorted(intervals, key = lambda x : x[0])[::-1]
        p2 = len(intervals) - 1
        # merge
        for p1 in range(p2 - 1, -1, -1):
            # 비교
            if intervals[p2][1] >= intervals[p1][0]:
                merged = [min(intervals[p1][0], intervals[p2][0]), max(intervals[p1][1], intervals[p2][1])]
                intervals.pop(p2)
                intervals[p1] = merged
            p2 -= 1
        return intervals[::-1]

# Best Solution
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # edge case 
        if len(intervals) == 1:
            return intervals
        merged = []
        for i in sorted(intervals, key = lambda x : x[0]):
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(i[1], merged[-1][1])
            else:
                merged += i,
        return merged














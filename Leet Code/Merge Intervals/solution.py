# First Attempt
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

# Second Attempt
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals
        # edge case

# 카운터
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0
        while True:
            subCount = 0
            for task, _ in counter.most_common(n+1):
                subCount += 1
                result += 1
                counter.subtract(task)
                #0 이하인 아이템을 목록에서 완전히 제거
                counter += collections.Counter()
            if not counter:
                break
                
            result += n - subCount + 1
        
        return result

# Intuition
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        count = collections.Counter(tasks)
        L = sorted(count.values(), reverse = True)
        maxOccur = L[0]
        num_maxOccur = L.count(maxOccur)
        answer = (maxOccur- 1) * (n + 1) + num_maxOccur
        return max(len(tasks), answer)

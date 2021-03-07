# My first attempt
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums).most_common()
        return [i for i, v in counter][:k]



# Using Counter and MinHeap
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        freqs_heap = []
        for f in counter:
            heapq.heappush(freqs_heap, (-counter[f], f))
        topq = list()
        for _ in range(k):
            topq.append(heapq.heappop(freqs_heap)[1])
        return topq

# Pythonic Way


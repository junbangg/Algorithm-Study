def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums).most_common()
        return [i for i, v in counter][:k]


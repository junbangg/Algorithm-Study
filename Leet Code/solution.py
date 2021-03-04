def numJewelsInStones(self, jewels: str, stones: str) -> int:
        table = collections.defaultdict(int)
        for s in stones:
            table[s] += 1
        return sum([table[j] for j in jewels]) 

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        words, digs = [], []
        for l in logs:
            a = l.split()
            if a[1].isalpha(): words.append(l)
            else: digs.append(l)
        words = sorted(words, key = lambda log: (log.split()[1:], log.split()[0]))
        return words + digs

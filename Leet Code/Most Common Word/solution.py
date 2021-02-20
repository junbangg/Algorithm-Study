class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        par = ""
        for c in paragraph:
            if c == " " or c.isalpha():
                par += c.lower()
            else: par += " "
        par = [word for word in par.split() if word not in banned]
        dic = Counter(par)
        return max(dic, key=dic.get)

class Page:
    def __init__(self, url, score, numberOfLinks, linkedPages):
        self.url = url
        self.score = score
        self.numberOfLinks = numberOfLinks
        self.outputLinkScore = self.getOutputLinkScore(self)
        self.linkScore = self.getLinkScore(linkedPages)
        self.matchingScore = self.getMatchingScore(self)

    def getMatchingScore(self):
        return self.score // self.linkScore

    def getLinkScore(linkedPages):
        total = 0
        for page in linkedPages:
            total += page.outputLinkScore
        return total
        
    def getOutputLinkScore(self):
        return self.score // self.numberOfLinks

def getWordScore():
    pass

def solution(word, pages):
    answer = 0
    for data in pages.split("head>\n"):
        print(data)

    return answer
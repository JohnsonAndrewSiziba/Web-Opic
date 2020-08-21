import requests
from bs4 import BeautifulSoup


class Search:

    def __init__(self, query):
        self.results = []
        self.query = query
        self.searchLink = self.generateSearchLink()
        print(self.searchLink)
        self.linksCollection = []
        self.makeSearches()

    def generateSearchLink(self):
        # todo
        #     1. generate search link: joiners and replace special chars
        #     2. results page link
        #     3. return the link fully formed
        return self.query

    def getSoupData(self):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
                   "Accept-Encoding": "gzip, deflate",
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1",
                   "Connection": "close", "Upgrade-Insecure-Requests": "1"}
        r = requests.get(self.searchLink, headers=headers)  # , proxies=proxies)
        content = r.content
        soup = BeautifulSoup(content, features="html.parser")
        # print(type(soup))
        return soup

    def makeSearches(self):
        data = self.getSoupData()
        self.makeSearchResults(data)

    def resultsPageLink(self, currLink):
        return self.searchLink

    def makeSearchResults(self, data):
        pass

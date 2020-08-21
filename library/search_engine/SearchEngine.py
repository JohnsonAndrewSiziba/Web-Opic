from library.search_engine.Bing import Bing
from library.search_engine.Google import Google


class SearchEngine:

    def __init__(self, query):
        self.query = query
        self.googleResults = Google(query, 0).results
        self.bingResults = Bing(query, 0).results
        self.searchResults = self.compileResults()
        print(len(self.compileResults()))

    def compileResults(self):
        temp = []
        if len(self.googleResults) == 0:
            return self.bingResults

        if len(self.bingResults) == 0:
            return self.googleResults

        links = []
        for result in self.googleResults:
            link = result.link
            if result.link not in links:
                links.append(link)
                temp.append(result)

        for result in self.bingResults:
            link = result.link
            if result.link not in links:
                links.append(link)
                temp.append(result)

        return temp


# inc = SearchEngine("same girl")

from library.search_engine.Search import Search
from library.search_engine.src import makeLink


class Yahoo(Search):
    def __init__(self, query):
        super().__init__(query)

    def generateSearchLink(self):
        # todo
        #     1. generate search link: joiners and replace special chars
        #     2. results page link
        #     3. return the link fully formed
        link = "https://search.yahoo.com/search?p={}&ie=utf-8&oe=utf-8".format(makeLink(self.query))
        # link = self.resultsPageLink(link)
        return link

    def makeSearchResults(self, data):
        results = data.find_all('div', attrs={'class': 'dd algo algo-sr relsrch lst richAlgo'})
        for result in results:
            # try:
            # link = result.find('h2').find('a').get('href')
            # if link in self.linksCollection:
            #     continue
            # self.linksCollection.append(link)
            title = result.find('a').contents[0]
            # extract = result.select("p")[0].text.strip()
            print("Title: ", title)
            # print("Link: ", link)
            # print("Extract: ", extract)
            # new = SearchResult(title, link, extract)
            # self.results.append(new)
            # except Exception:
            #     pass
            print()
            print()


# y = Yahoo('guardians of the galaxy')
# y.makeSearches()

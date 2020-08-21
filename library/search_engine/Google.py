from library.search_engine.Search import Search
from library.search_engine.SearchResult import SearchResult
from library.search_engine.src import makeLink


class Google(Search):

    def __init__(self, query, startAt):
        self.startAt = startAt
        super().__init__(query)

    def generateSearchLink(self):
        link = "https://www.google.com/search?q={}&ie=utf-8&oe=utf-8".format(makeLink(self.query))
        link = self.resultsPageLink(link)
        return link

    def resultsPageLink(self, currLink):
        if self.startAt != 0:
            start_at = self.startAt * 10
            extension = "&start=" + str(start_at)
            o = currLink + extension
            return o
        else:
            return currLink

    def makeSearchResults(self, data):
        results = data.find_all('div', attrs={'class': 'rc'})
        print("Google Results:", len(results))
        for result in results:
            try:
                link = result.find('a').get('href')
                if link in self.linksCollection:
                    continue
                self.linksCollection.append(link)
                title = result.find('h3', attrs={'class': 'LC20lb DKV0Md'}).contents[0]
                extract = result.select("span.st")[0].text.strip()
                # print("Title: ", title)
                # print("Link: ", link)
                # print("Extract: ", extract)
                new = SearchResult(title, link, extract)
                self.results.append(new)
            except Exception:
                pass


# g = Google("sia", 0)
# g.makeSearches()

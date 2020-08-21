class SearchResult:
    title = ""
    link = ""
    extract = ""

    def __init__(self, title, link, extract):
        self.title = title
        self.link = link
        self.extract = extract

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, SearchResult):
            return self.link == other.link
        return False

    def __str__(self):
        return self.title


# rs = SearchResult("Hello", "Jesus", "I Love You")
# print(rs)

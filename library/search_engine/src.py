def joiners(data):
    queryLs = data.strip().split()
    d = ""
    counter = 0
    for e in queryLs:
        if counter == 0:
            d = e
        else:
            d += "+" + e
        counter += 1
    return d


def reservedChars(data):
    o = ""
    specialChars = ["!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "/", ":", ";", "=", "?", "@", "[",
                    "]"]  # 19
    replacements = ["%21", "%23", "%24", "%25", "%26", "%27", "%28", "%29", "%2A", "%2B", "%2C", "%2F", "%3A",
                    "%3B", "%3D", "%3F", "%40", "%5B", "%5D"]

    for e in data:
        if e in specialChars:
            e = replacements[specialChars.index(e)]
        o += e

    return o


def makeLink(data):
    data = reservedChars(data)
    data = joiners(data)
    return data


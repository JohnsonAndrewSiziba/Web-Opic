from django.shortcuts import render
from library.search_engine.SearchEngine import SearchEngine


def index(request):
    return render(request, 'optic/index.html')


def search(request):
    q = request.GET.get('query', None)
    searchEngine = SearchEngine(q)
    data = searchEngine.searchResults
    return render(request, 'optic/results.html', {'data': data, 'query': q})

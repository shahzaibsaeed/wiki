from django.shortcuts import render
from django.http import Http404
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entryPage(request, title):
    title = title
    entries = util.list_entries()
    if title in entries:
        return render(request, "encyclopedia/entryPage.html", {
            "title": title
    })
    else:
      raise Http404("The request page was not existed")
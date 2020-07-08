from django.shortcuts import render
from django.http import Http404
from . import util
from django.contrib import messages
import re


def index(request):
    # getting all encyclopedia entries
    entries = util.list_entries()

    # check if request is made by form
    if request.method == "POST":
        query = request.POST.get("query")

        if len(query) != 0:
            # print(f"\n\n\n{query}\n\n\n")

            if query in entries:
                print(f"\n\n\nEntry Exits\n\n\n")
                return render(request, "encyclopedia/entryPage.html", {
                    "title": query
                })
            else:
                print(f"\n\n\nMatching the entries from the list\n\n\n")
                for entry in entries:
                    sortedEntry = entry.lower()
                    result = re.findall(query, sortedEntry)
                    print(f"Result: {result}")
                    if result != []:
                        print(f"\n\n\n{entry}\n\n\n")
                        return render(request, "encyclopedia/index.html", {
                            "query": query,
                            "entry": entry
                        })

        else:
            print(f"\n\ntype something\n\n")
            messages.add_message(request, messages.WARNING, 'Type something ')
    return render(request, "encyclopedia/index.html", {
        "entries": entries,       
    })


def entryPage(request, title):
    title = title
    entries = util.list_entries()
    if title in entries:
        return render(request, "encyclopedia/entryPage.html", {
            "title": title
        })
    else:
        raise Http404("The request page does not existed")

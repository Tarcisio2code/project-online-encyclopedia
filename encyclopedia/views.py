from django.shortcuts import render
from markdown2 import Markdown
from . import util

def markdown_converter(title):
    source = util.get_entry(title)
    markdowner = Markdown()
    if source == None:
        return None
    else:
        return markdowner.convert(source)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entryContent = markdown_converter(title)
    if entryContent == None:
        return render(request, "encyclopedia/error.html",{
            "message": "This entry not exist"
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": entryContent
        })

def search(request):
    if request.method == "POST":
        searchText = request.POST['q']
        entryContent = markdown_converter(searchText)
        if entryContent is not None:
            return render(request, "encyclopedia/entry.html",{
                "title": searchText,
                "content": entryContent
            })
        else:
            entryList = util.list_entries()
            similarEntries = []
            for entry in entryList:
                if searchText.lower() in entry.lower():
                    similarEntries.append(entry)
            return render(request, "encyclopedia/search.html", {
                "similarEntries": similarEntries
            })

def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/newpage.html")
    else:
        title = request.POST["title"]
        entryContent = request.POST["content"]
        titleExist = util.get_entry(title)
        if titleExist is None:
            util.save_entry(title, entryContent)
            htmlContent = markdown_converter(title)
            return render(request, "encyclopedia/entry.html",{
                "title": title,
                "content": htmlContent
            })
        else:
            return render(request, "encyclopedia/error.html", {
                "message":"Entry page already existis"
            })
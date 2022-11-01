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
    entry_content = markdown_converter(title)
    if entry_content == None:
        return render(request, "encyclopedia/error.html",{
            "message": "This entry not exist"
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": entry_content
        })
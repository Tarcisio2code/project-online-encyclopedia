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


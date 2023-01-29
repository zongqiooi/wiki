
import random 
from . import util
from markdown2 import Markdown
from django.shortcuts import render

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry): 
    if util.get_entry(entry) is None: 
        return render(request, "encyclopedia/error404.html", {
            "entry": entry, 
            "title": "Error404", 
        })
    else: 
        markdowner = Markdown()
        
        return render(request, "encyclopedia/entry.html", {
            "content": markdowner.convert(util.get_entry(entry)), 
            "title": entry
        })

def search(request): 
    # if request.method == "GET": # when manually typed "wiki/search"
    #     return render(request, "encyclopedia/index.html", {
    #     "entries": util.list_entries()
    # })
    if request.method == "POST": 
        entry = request.POST["q"]
        
        if util.get_entry(entry) is None: 
            return render(request, "encyclopedia/search.html", {
                "entries": util.search_entries(entry)
            })
        else: 
            markdowner = Markdown()
            
            return render(request, "encyclopedia/entry.html", {
                "content": markdowner.convert(util.get_entry(entry)), 
                "title": entry
            })

def new(request): 
    if request.method == "GET": # when manually typed "wiki/new"
        return render(request, "encyclopedia/new.html", {
            "error": False
        })
    elif request.method == "POST": 
        title = request.POST["title"]
        content = request.POST["content"]
        
        if title.upper() in [i.upper() for i in util.list_entries()]: 
            return render(request, "encyclopedia/new.html", {
                "error": True, 
                "title": title
            })
        else: 
            util.save_entry(title, content)
            markdowner = Markdown()
            
            return render(request, "encyclopedia/entry.html", {
                "content": markdowner.convert(util.get_entry(title)), 
                "title": title
            })

def edit(request): 
    if request.method == "GET": # when manually typed "wiki/edit"
        return render(request, "encyclopedia/edit.html")
    elif request.method == "POST": 
        title = request.POST["entry_title"]
        content = util.get_entry(title)
        
        return render(request, "encyclopedia/edit.html", {
            "content": content, 
            "title": title
        })
        
def edit_save(request):
    if request.method == "GET": 
        return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    }) 
    elif request.method == "POST": 
        title = request.POST["title"]
        content = request.POST["content"]
        util.save_entry(title, content)
        markdowner = Markdown()
        
        return render(request, "encyclopedia/entry.html", {
            "content": markdowner.convert(util.get_entry(title)), 
            "title": title
        })
        
def rand(request): 
    entries = util.list_entries()
    entry = random.choice(entries)
    markdowner = Markdown()
        
    return render(request, "encyclopedia/entry.html", {
        "content": markdowner.convert(util.get_entry(entry)), 
        "title": entry
    })
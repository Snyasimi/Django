import random
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from . import util
from django.urls import reverse

class Page(forms.Form):
    title = forms.CharField(label="TITLE")
    new_page = forms.CharField(widget=forms.Textarea)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def create_page(request):
    #IF THE USER SUBMITED THE FORM IT VALIDATES AND STORES WHATEVE THE USER INPUT
    if request.method == "POST":
        new_page = Page(request.POST)
        if new_page.is_valid():
            #SAVE THE FILE IN THE DISK
            contents = new_page.cleaned_data["new_page"]
            title = new_page.cleaned_data["title"]
            util.save_entry(title,contents)

            return HttpResponseRedirect(reverse("encyclopedia:create_page"))
        else :
            return render(request,"encyclopedia/create_page.html",{
                "new_page" : Page()
            })

            


    return render(request,"encyclopedia/create_page.html",{
        "new_page": Page()

    })

def Random_page(request):
    pages = util.list_entries()
    page_to_display = random.choice(pages)
    #util.get_entry(page_to_display)
    return render(request,"encyclopedia/Random_page.html",{
        "page" : util.get_entry(page_to_display)
            })


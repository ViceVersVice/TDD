from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, List
# Create your views here.
def SomeView(request):
    return render(request, "home.html")
    #return render(request, "home.html")

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def new_list(request):
    list_ = List.objects.create()
    item_text = request.POST.get("item_text", "")
    Item.objects.create(text=item_text, list=list_)
    return redirect("/some-view/list1/")

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, List
# Create your views here.
def SomeView(request):
    return render(request, "home.html")
    #return render(request, "home.html")

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {"list": list_})

def new_list(request):
    list_ = List.objects.create()
    item_text = request.POST.get("item_text", "")
    Item.objects.create(text=item_text, list=list_)
    return redirect(f"/some-view/{list_.id}/")

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    item_text = request.POST.get("item_text", "")
    Item.objects.create(text=item_text, list=list_)
    return redirect(f"/some-view/{list_.id}/")

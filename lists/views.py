from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
# Create your views here.
def SomeView(request):
    if request.method == "POST":
        item_text = request.POST.get("item_text", "")
        Item.objects.create(text=item_text)
        return redirect("/some-view/list1/")
    else:
        item_text = ""
    items = Item.objects.all()
    return render(request, "home.html",
                  {"items": items})
    #return render(request, "home.html")

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

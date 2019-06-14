from django.conf.urls import url, include
from . import views
# Create your views here.

app_name = "ists-app"
urlpatterns = [
    url(r"^some-view/$", views.SomeView, name="some_view"),
    url(r"^some-view/new$", views.new_list, name="new_list"),
    url(r"^some-view/list1/$", views.view_list, name="view_list"),

]

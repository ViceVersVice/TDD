from django.conf.urls import url, include
from . import views
# Create your views here.


urlpatterns = [
    url(r"^new$", views.new_list, name="new_list"),
    url(r"^(\d+)/$", views.view_list, name="view_list"),
    url(r"^(\d+)/add-item$", views.add_item, name="add_item"),

]

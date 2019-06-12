from django.conf.urls import url, include
from . import views
# Create your views here.

app_name = "ists-app"
urlpatterns = [
    url(r"^some-view/", views.SomeView, name="some_view"),
]

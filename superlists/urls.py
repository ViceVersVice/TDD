from django.conf.urls import url, include
from lists import urls as list_urls
from lists import views as list_views
# Create your views here.

urlpatterns = [
    url(r"^some-view/$", list_views.SomeView, name="some_view"),
    url(r"^some-view/", include(list_urls))

]

print("PATTERNS", urlpatterns)

from django.conf.urls import url, include
from rest_framework import routers
from . import views


CRUD_Car_router = routers.SimpleRouter()
CRUD_Car_router.register("cars", views.CRUD_CarView)


app_name = "UsersApp"
urlpatterns = [
    url(r"^", include(CRUD_Car_router.urls)),

    # this is without drf
    url(r"^", views.CarsView, name="cars_view"),
    url(r"^<int:id>/", views.CarsView, name="cars_view"),

]

from django.urls import path, include
from rest_framework import routers
from . import views


CRUD_Car_router = routers.SimpleRouter()
CRUD_Car_router.register("cars", views.CRUD_CarView)


app_name = "UsersApp"
urlpatterns = [
    path("", include(CRUD_Car_router.urls)),

    # this is without drf
    path("", views.CarsView, name="cars_view"),
    path("<int:id>/", views.CarsView, name="cars_view"),

]

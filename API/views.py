from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Car
from .serializers import CarSerializer
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.http import QueryDict
# Create your views here.


class CRUD_CarView(ModelViewSet):
    """CRUD car view"""
    # viewset is the best choice for standart CRUD
    queryset = Car.objects.all()
    serializer_class = CarSerializer


# without django REST framework
@csrf_exempt
def CarsView(request, id=None):
    if request.method == "GET":
        if id:
            car = get_object_or_404(Car, id=id)
            data = car.values()
            print(data)
            return JsonResponse(data)
        else:
            data = [obj for obj in Car.objects.all().values()]
            return JsonResponse(data, safe=False)
    elif request.method == "POST":
        if id:
            return HttpResponse(status=403)
        post_data = request.POST
        data = post_data.dict()
        try:
            car = Car.objects.create(**data)
            return JsonResponse(model_to_dict(car))
        except Exception as e:
            return HttpResponse(f"Field validation error....{e}")

    elif request.method == "PATCH":
        """However Django do not have good request body parsers for other Http methods,
        like PUT, PATCH, so it will be difficult to do something with this"""
        if not id:
            return HttpResponse(status=403)
        #car = get_object_or_404(Car, id=id)
        #car.update()
        data = QueryDict(request.body)
        return HttpResponse("...............")

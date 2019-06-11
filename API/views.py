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
from django.core import serializers
import json
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
            #fields = tuple([field.name for field in car._meta.get_fields()])
            #obj = json.loads(json.dumps(model_to_dict(car)))
            obj = model_to_dict(car)
            #data = serializers.serialize("json", [car,], fields=fields)
            #print(data)
            return JsonResponse(obj)
        else:
            #data = [obj for obj in Car.objects.all().values()]
            data = list(Car.objects.all().values())
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
        data = json.loads(request.body)
        car = get_object_or_404(Car, id=id)
        for attr, val in data.items():
            setattr(car, attr, val)
        car.save()
        return JsonResponse(model_to_dict(car))

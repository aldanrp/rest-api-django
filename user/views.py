from todoproject.response import Response
from . import transformer
from .models import Users , Foods ,Pesanans
import json
from django.contrib.auth.hashers import make_password



def index(request):
    if request.method == 'GET':
        user = Users.objects.all()
        user = transformer.transform(user)
        return Response.ok(user)
    elif request.method == 'POST':
        json_data = json.loads(request.body)
        jumlah =[json_data["food"]]
        user = Users()
        user.foods = Foods.objects.get(id = json_data["food"])

        return Response.ok(
            values=transformer.singleTransform(user),
            message="Added!"
        )

def show(request, id):
    if request.method == 'GET':
        user = Users.objects.filter(id=id).first()

        if not user:
            return Response.badRequest(message='Pengguna tidak ditemukan!')

        user = transformer.singleTransform(user)
        return Response.badRequest(values=user)
    elif request.method == 'PUT':
        json_data = json.loads(request.body)

        user = Users.objects.filter(id=id).first()
        if not user:
            return Response.badRequest(message="Pengguna tidak ditemukan")
        user.jumlah= json_data['jumlah']
        user.foods = Foods.objects.get(id = json_data["food"])
        user.save()

        return Response.ok(
            values=transformer.singleTransform(user),
            message="Updated!"
        )
    elif request.method == 'DELETE':
        user = Users.objects.filter(id=id).first()
        if not user:
            return Response.badRequest(message="Pengguna tidak ditemukan")
        
        user.delete()
        return Response.ok(message="Deleted!")
    else:
        return Response.badRequest(message="Invalid method!")


def indexfood(request):
    if request.method == 'GET':
        user = Foods.objects.all()
        user = transformer.foodtransform(user)
        return Response.ok(values=user)
    elif request.method == 'POST':
        json_data = json.loads(request.body)

        user = Foods()
        user.name = json_data['name']
        user.price = json_data['harga']
        user.isready = json_data['isready']
        user.save() 

        return Response.ok(
            values=transformer.foodTransform(user),
            message="Added!"
        )

def showfood(request, id):
    if request.method == 'GET':
        user = Foods.objects.filter(id=id).first()

        if not user:
            return Response.badRequest(message='Pengguna tidak ditemukan!')

        user = transformer.foodTransform(user)
        return Response.badRequest(values=user)
    elif request.method == 'PUT':
        json_data = json.loads(request.body)

        user = Foods.objects.filter(id=id).first()
        if not user:
            return Response.badRequest(message="Pengguna tidak ditemukan")
        user.name = json_data['name']
        user.price = json_data['harga']
        user.isready = json_data['isready']
        user.save()

        return Response.ok(
            values=transformer.foodTransform(user),
            message="Updated!"
        )
    elif request.method == 'DELETE':
        user = Foods.objects.filter(id=id).first()
        if not user:
            return Response.badRequest(message="Pengguna tidak ditemukan")
        
        user.delete()
        return Response.ok(message="Deleted!")
    else:
        return Response.badRequest(message="Invalid method!")

def pesanansindex(request):
    if request.method == 'GET':
        user = Pesanans.objects.all()
        user = transformer.pesananstransform(user)
        return Response.ok(user)
    elif request.method == 'POST':
        json_data = json.loads(request.body)
        
        user = Pesanans()
        user.nama= json_data['nama']
        user.nomeja= json_data['nomor meja']
        user.keranjang = Users.objects.get(id=json_data['keranjang'])
        user.save()

        return Response.ok(
            values=transformer.pesanansTransform(user),
            message="Added!"
        )

def pesanansshow(request, id):
    if request.method == 'GET':
        user = Pesanans.objects.filter(id=id).first()

        if not user:
            return Response.badRequest(message='Pengguna tidak ditemukan!')

        user = transformer.pesanansTransform(user)
        return Response.badRequest(values=user)
    elif request.method == 'PUT':
        json_data = json.loads(request.body)

        user = Pesanans.objects.filter(id=id).first()
        if not user:
            return Response.badRequest(message="Pengguna tidak ditemukan")
        user.nama= json_data['nama']
        user.nomeja= json_data['nomor meja']
        user.keranjang = Users.objects.all()
        user.save()

        return Response.ok(
            values=transformer.pesanansTransform(user),
            message="Updated!"
        )
    elif request.method == 'DELETE':
        user = Pesanans.objects.filter(id=id).first()
        if not user:
            return Response.badRequest(message="Pengguna tidak ditemukan")
        
        user.delete()
        return Response.ok(message="Deleted!")
    else:
        return Response.badRequest(message="Invalid method!")

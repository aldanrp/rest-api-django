from .models import Users , Foods ,Pesanans



def transform(values):
    arr = []

    for item in values:
        arr.append(singleTransform(item))

    return arr

def foodtransform(values):
    arr = []
    for item in values:
        arr.append(foodTransform(item))

    return arr

def pesananstransform(values):
    arr = []
    for item in values:
        arr.append(pesanansTransform(item))

    return arr

def singleTransform(Users):
    return {
        "id": Users.id,
        "jumlah": Users.jumlah,
        "food": foodTransform(Users.foods),
    }

def foodTransform(values):
    return {
        "id": values.id,
        "nama": values.name,
        "price": values.price,
        "isready": values.isready,
    }

def pesanansTransform(values):
    data = Users.objects.all()
    return{
        "id": values.id,
        "nama": values.nama,
        "no_meja": values.nomeja,
        "pesanan" : singleTransform(values.keranjang)
    }
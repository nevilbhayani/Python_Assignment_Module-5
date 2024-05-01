from faker import Faker
from .models import*
import random

fack=Faker()

def data(n=50):
    for _ in range(n):
        model=['i3','15','i7','i9']
        ram=['4gb','6gb','8gb','16gb','18gb']
        product=ProductMst.objects.all()
        productrange=random.randint(0,len(product)-1)
        pro=product[productrange]
        price=random.randint(10000,100000)
        image= fack.image_url(width=100, height=100)
        modelrange=random.randint(0,len(model)-1)
        mod=model[modelrange]
        ramrange=random.randint(0,len(ram)-1)
        ram1=ram[ramrange]
        laptop=ProductSubCat.objects.create(product=pro,product_price=price,product_image=image,product_model=mod,product_ram=ram1)
        
def delete():
    product=ProductSubCat.objects.all()
    product.delete()

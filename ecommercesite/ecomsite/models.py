from django.db import models

# Create your models here.
from django.forms import forms


class C1(models.Model):
    c_id=models.AutoField(primary_key=True)
    car_name=models.CharField(max_length=50)
    curcive_text=models.CharField(max_length=50)
    bold_text=models.CharField(max_length=50)
    big_bold_text=models.CharField(max_length=50)
    since_date=models.CharField(max_length=50)
    carousal_link=models.CharField(max_length=50)
    carousal_image=models.ImageField(upload_to="ecomsite/images",default="")
    def __str__(self):
        return self.car_name



class our_story(models.Model):
    story_id=models.AutoField(primary_key=True)
    story_name=models.CharField(max_length=50)
    story_title=models.CharField(max_length=50)
    bold_title=models.CharField(max_length=50)
    para1=models.TextField(default="")
    para2=models.TextField(default="")
    btn_link= models.CharField(max_length=50)

    def __str__(self):
        return self.story_name


class choose_us(models.Model):
    choose_id=models.AutoField(primary_key=True)
    card_name=models.CharField(max_length=50)
    card_image=models.ImageField(upload_to="ecomsite/images",default="")
    card_tite_1=models.CharField(max_length=50,default="")
    card_tite_2=models.CharField(max_length=50,default="")
    card_content=models.TextField(default="")

    def __str__(self):
        return self.card_name

class supp(models.Model):
    supp_id=models.AutoField(primary_key=True)
    supp_name=models.CharField(max_length=50)
    supp_image=models.ImageField(upload_to="ecomsite/images",default="")

    def __str__(self):
        return self.supp_name




class sold_prod(models.Model):
    sell_id=models.AutoField(primary_key=True)
    curcive_text = models.CharField(max_length=50)
    text_1=models.CharField(max_length=50)
    text_2=models.CharField(max_length=50)
    sub_text=models.CharField(max_length=50)
    sp_image = models.ImageField(upload_to="ecomsite/images", default="")

    def __str__(self):
        return self.curcive_text

class ww(models.Model):
    ww_id=models.AutoField(primary_key=True)
    ww_name=models.CharField(max_length=50)
    ww_image=models.ImageField(upload_to="ecomsite/images",default="")

    def __str__(self):
        return self.ww_name

class mng(models.Model):
    mng_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    icon_1=models.ImageField(upload_to="ecomsite/images",default="")
    icon_2=models.ImageField(upload_to="ecomsite/images",default="")
    icon_3=models.ImageField(upload_to="ecomsite/images",default="")
    image=models.ImageField(upload_to="ecomsite/images",default="")

    def __str__(self):
        return self.title


class fleet(models.Model):
    fleet_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    para_1=models.TextField(default="")
    para_2=models.TextField(default="")
    link=models.CharField(max_length=50)

    def __str__(self):
        return self.title


class region(models.Model):
    region_id=models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="ecomsite/images", default="")
    title = models.CharField(max_length=50)
    para_1 = models.TextField(default="")
    para_2 = models.TextField(default="")
    link = models.CharField(max_length=50)
    def __str__(self):
        return self.title


class reg(models.Model):
    reg_id=models.AutoField(primary_key=True)
    firstname =models.CharField(max_length=50)
    lastname =models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    passwd = models.CharField(max_length=255)
    confpasswd = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    streetadd = models.TextField(default="")
    city = models.CharField(max_length=50)
    postalcode = models.CharField(max_length=50)
    provunce = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    shipsa = models.TextField(default="")
    shipcity = models.CharField(max_length=50)
    shippostalode = models.CharField(max_length=50)
    shipprovince = models.CharField(max_length=50)
    shipcountry = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name

class prodlist(models.Model):
    prod_id=models.AutoField(primary_key=True)
    prod_image=models.ImageField(upload_to="ecomsite/images", default="")
    prod_name= models.CharField(max_length=50)
    prod_desc=models.TextField(default="")


    prod_Bran = models.ForeignKey('list_of_brands', on_delete=models.PROTECT , null=True)
    prod_supp = models.ForeignKey('list_of_Supplier', on_delete=models.PROTECT , null=True)
    prod_cat = models.ForeignKey('list_of_Category', on_delete=models.PROTECT , null=True)
    prod_details = models.TextField(default="Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam non ummy nibh euismod tincidunt ut laoreet dolore magna aliquam eratv olu tpat. Ut wisi enim ad minim veniam lorem ipsum dolor sit amet, con sect etuer adipiscing elit, sed diam nonummy.")
    prod_price_per_unit = models.CharField(max_length=10,default="7.99" )
    Flash_Sale = models.BooleanField(default=False)
    Seasonal_Promotion = models.BooleanField(default=False)
    Show_on_Dekstop = models.BooleanField(default=False)



    def __str__(self):
        return self.prod_name

class list_of_brands(models.Model):
    b_name = models.CharField(max_length=50)
    def __str__(self):
        return self.b_name


class list_of_Category(models.Model):
    c_name = models.CharField(max_length=50)
    def __str__(self):
        return self.c_name


class list_of_Supplier(models.Model):
    c_name = models.CharField(max_length=50)
    def __str__(self):
        return self.c_name


class Cart(models.Model):
    id=models.AutoField(primary_key=True)
    user_id= models.CharField(max_length=50)
    product_id=models.CharField(max_length=50)
    quantity=models.CharField(max_length=50)

    def __str__(self):
        return self.user_id


class Wish(models.Model):
    id=models.AutoField(primary_key=True)
    user_id= models.CharField(max_length=50)
    product_id=models.CharField(max_length=50)
    quantity=models.CharField(max_length=50)

    def __str__(self):
        return self.user_id
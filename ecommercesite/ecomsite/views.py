import json
import pdb
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import C1,our_story,choose_us,supp,sold_prod,ww,mng,fleet,region,reg,Contact,prodlist,list_of_brands,list_of_Category,list_of_Supplier,Cart,Wish
from django.views.decorators.csrf import csrf_exempt



def index(request):
    car=C1.objects.all()
    nSlides = len(car)
    stry=our_story.objects.all()
    cu=choose_us.objects.all()
    sup=supp.objects.all()

    sell=sold_prod.objects.all()
    wrk=ww.objects.all()
    manag=mng.objects.all()
    flet=fleet.objects.all()
    reg=region.objects.all()
    plist = prodlist.objects.all()
    p={'car':car,'range':range(0,nSlides),'stry':stry,'cu':cu,'sup':sup,'sell':sell,'wrk':wrk,'m':manag,'flet':flet,'reg':reg,'plist':plist}
    return render(request, 'ecomsite/home.html', p)

def register(request):
    error={}
    if request.method == "POST":
        firstname=request.POST.get('firstname', '')
        lastname=request.POST.get('lastname', '')
        phone=request.POST.get('phone', '')
        passwd=request.POST.get('passwd', '')
        confpasswd=request.POST.get('confpasswd', '')
        if passwd != confpasswd :
            error['error'] = 'please check password';
            return render(request, 'ecomsite/registe.html', {'error': error})
        email=request.POST.get('email', '')
        streetadd=request.POST.get('streetadd', '')
        city=request.POST.get('city', '')
        postalcode=request.POST.get('postalcode', '')
        provunce=request.POST.get('provunce', '')
        country=request.POST.get('country', '')
        shipsa=request.POST.get('shipsa', '')
        shipcity=request.POST.get('shipcity', '')
        shippostalode=request.POST.get('shippostalode', '')
        shipprovince=request.POST.get('shipprovince', '')
        shipcountry=request.POST.get('shipcountry', '')
        Reg=reg(firstname=firstname,lastname=lastname,phone=phone,passwd=make_password(passwd),confpasswd=confpasswd,email=email,streetadd=streetadd,city=city,postalcode=postalcode,provunce=provunce,country=country,shipsa=shipsa,shipcity=shipcity,shippostalode=shippostalode,shipprovince=shipprovince,shipcountry=shipcountry)
        Reg.save()
        return redirect('login')
    return render(request,'ecomsite/registe.html')



def login(request):
        print(request.session)
        if 'user_id' in request.session:
            return redirect('index')

        error = {}
        if request.method == 'POST':
            uname = request.POST.get('username')
            pwd = request.POST.get('password')
            try:

                check_user = reg.objects.get(email=uname)

                if check_user:
                    print(check_user)
                    if check_password(pwd, check_user.passwd):
                        request.session['user_id'] = check_user.reg_id
                        request.session['user_name'] = check_user.firstname
                        return redirect('index')
                    else:
                        error['error'] = 'Credentilas does not match';
                        return render(request, 'ecomsite/login.html',{'error': error})

                else:
                    error['error'] = 'User not found';
                    return render(request, 'ecomsite/login.html',{'error': error})
            except:
                error['error'] = 'User not found';
                return render(request, 'ecomsite/login.html', {'error': error})
        return render(request, 'ecomsite/login.html',{'error': error})


def logout(request):
    try:
        del request.session['user_id']
        del request.session['user_name']
    except Exception as e:
        print(e)
    return redirect('index')


def contactus(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request,'ecomsite/contactus.html')


def aboutus(request):
    stry = our_story.objects.all()
    cu = choose_us.objects.all()
    flet = fleet.objects.all()
    reg = region.objects.all()
    p = {'stry':stry,'cu':cu,'flet':flet,'reg':reg}
    return render(request, 'ecomsite/aboutus.html',p)


def cart(request):
    cart_items=[]
    id_list=[]
    sub_total = 0
    sess = request.session['user_id']
    result = Cart.objects.filter(user_id=sess).values('product_id','quantity','id','user_id')
    for row in result:
        product_info_object = prodlist.objects.filter(prod_id=row['product_id']).values('prod_name','prod_price_per_unit','prod_image')
        product_info = product_info_object[0]
        cart_item = {'id': row['id'], 'product_name': product_info['prod_name'], 'quantity': row['quantity'], 'product_price': product_info['prod_price_per_unit'], 'total_price': "{:.2f}".format(float(row['quantity']) * float(product_info['prod_price_per_unit'])), 'product_image': product_info['prod_image']}
        cart_items.append(cart_item)
        id_list.append(row['id'])
        sub_total = sub_total + float(row['quantity']) * float(product_info['prod_price_per_unit'])
    rounded_sub_total="{:.2f}".format(sub_total)
    if request.method == "POST":
        for up_item in cart_items:
            updated_quantity = request.POST.get('item_'+str(up_item['id']))
            Update_cart = Cart.objects.get(id=up_item['id'])
            Update_cart.quantity = updated_quantity
            Update_cart.save()
        return redirect('cart')
    p={'cart_items':cart_items,'rounded_sub_total':rounded_sub_total}
    
    return render(request,'ecomsite/cart.html',p)

def productcategory(request):
    list = json.loads(request.POST['products'])
    produc = prodlist.objects.filter(prod_category__in=list)
    p={'plist':produc}
    return render(request,'ecomsite/Shop_by_category.html',p)

def product(request):
    plist=prodlist.objects.all()
    blist=list_of_brands.objects.all()
    clist=list_of_Category.objects.all()
    slist=list_of_Supplier.objects.all()

    sell = sold_prod.objects.all()
    wrk = ww.objects.all()
    manag = mng.objects.all()
    flet = fleet.objects.all()
    reg = region.objects.all()

    p = {'sell': sell, 'wrk': wrk,'m': manag, 'flet': flet, 'reg': reg,'plist':plist,'blist':blist,'clist':clist,'slist':slist}
    return render(request,'ecomsite/product.html',p)

def flashsale(request):
    plist=prodlist.objects.all()
    sell = sold_prod.objects.all()
    wrk = ww.objects.all()
    manag = mng.objects.all()
    flet = fleet.objects.all()
    reg = region.objects.all()
    p = {'sell': sell, 'wrk': wrk,'m': manag, 'flet': flet, 'reg': reg,'plist':plist}
    return render(request,'ecomsite/flashsale.html',p)

def seasonalpromotion(request):
    plist=prodlist.objects.all()
    sell = sold_prod.objects.all()
    wrk = ww.objects.all()
    manag = mng.objects.all()
    flet = fleet.objects.all()
    reg = region.objects.all()
    p = {'sell': sell, 'wrk': wrk,'m': manag, 'flet': flet, 'reg': reg,'plist':plist}
    return render(request,'ecomsite/seasonalpromotion.html',p)


def productdetail(request,id):

    plist = prodlist.objects.all()
    a = prodlist.objects.filter(prod_id=id)
    p = {'plist': plist,'id':id,'a':a}
    return render(request,'ecomsite/productdetail.html',p)

def search(request):
    query=request.GET['query']
    print(query)
    prid = list_of_Category.objects.filter(c_name=query)
    print(prid)
    allPosts= prodlist.objects.filter(prod_cat__in=prid)
    blist=list_of_brands.objects.all()
    clist=list_of_Category.objects.all()
    slist=list_of_Supplier.objects.all()
    plist = prodlist.objects.all()
    sell = sold_prod.objects.all()
    wrk = ww.objects.all()
    manag = mng.objects.all()
    flet = fleet.objects.all()
    reg = region.objects.all()
    params={'sell': sell, 'wrk': wrk,'m': manag, 'flet': flet, 'reg': reg,'plist':plist,'a': allPosts,'blist':blist,'clist':clist,'slist':slist}
    return render(request, 'ecomsite/product.html', params )


def compare(request):
    list = json.loads(request.POST['products'])

    list2 = []
    for i in range(len(list)-1):
        t = int(list[i])
        if len(list2)<3:
            list2.append(t)
        else:
            list2.pop(0)
            list2.append(t)


    produc= prodlist.objects.filter(prod_id__in=list2)



    p={'plist':produc}

    return render(request,'ecomsite/recent_products.html',p)



def add_to_cart(request):
    product_id = json.loads(request.POST['product_id'])
    user = json.loads(request.POST['user'])
    result = Cart.objects.filter(user_id=user,product_id=product_id).values('id','user_id','product_id')
    if result.exists():
        cart_value =list(result)[0]
        Update_cart = Cart.objects.get(id=cart_value['id'])
        Update_cart.quantity = int(Update_cart.quantity) + 1
        Update_cart.save()
    else:
        cart=Cart(user_id=user,product_id=product_id,quantity=1)
        cart.save()
    return JsonResponse({'error': True, 'msg': 'Success'});

def add_to_wish(request):
    product_id = json.loads(request.POST['product_id'])
    user = json.loads(request.POST['user'])
    result = Wish.objects.filter(user_id=user,product_id=product_id).values('id','user_id','product_id')
    if result.exists():
        cart_value =list(result)[0]
        Update_cart = Cart.objects.get(id=cart_value['id'])
        Update_cart.quantity = int(Update_cart.quantity) + 1
        Update_cart.save()
    else:
        wish=Wish(user_id=user,product_id=product_id,quantity=1)
        wish.save()
    return JsonResponse({'error': True, 'msg': 'Success'});


def wishlist(request):
    wish_items = []
    id_list = []
    sub_total = 0
    sess = request.session['user_id']
    result = Wish.objects.filter(user_id=sess).values('product_id', 'quantity', 'id', 'user_id')
    for row in result:
        product_info_object = prodlist.objects.filter(prod_id=row['product_id']).values('prod_name',
                                                                                        'prod_price_per_unit',
                                                                                        'prod_image')
        product_info = product_info_object[0]
        wish_item = {'id': row['id'], 'product_name': product_info['prod_name'], 'quantity': row['quantity'],
                     'product_price': product_info['prod_price_per_unit'], 'total_price': "{:.2f}".format(
                float(row['quantity']) * float(product_info['prod_price_per_unit'])),
                     'product_image': product_info['prod_image']}
        wish_items.append(wish_item)
        id_list.append(row['id'])
        sub_total = sub_total + float(row['quantity']) * float(product_info['prod_price_per_unit'])
    rounded_sub_total = "{:.2f}".format(sub_total)
    if request.method == "POST":
        for up_item in wish_items:
            updated_quantity = request.POST.get('item_' + str(up_item['id']))
            Update_cart = Cart.objects.get(id=up_item['id'])
            Update_cart.quantity = updated_quantity
            Update_cart.save()
        return redirect('cart')
    p = {'cart_items': wish_items, 'rounded_sub_total': rounded_sub_total}
    return render(request,'ecomsite/wishlist.html',p)


def delete_crt_item(request,id):

    result = Cart.objects.filter(id=id)
    result.delete()
    return redirect('cart')
def clerarcart(request):
    sess = request.session['user_id']
    result = Cart.objects.filter(user_id=sess)
    result.delete()
    return redirect('cart')

def clerarlist(request):
    sess = request.session['user_id']
    result = Wish.objects.filter(user_id=sess)
    result.delete()
    return redirect('wishlist')

def delete_list_item(request,id):

    result = Wish.objects.filter(id=id)
    result.delete()
    return redirect('wishlist')



def cart_info(request):
    sub_total = 0
    total_quantity=0
    sess = request.session['user_id']
    result = Cart.objects.filter(user_id=sess).values('product_id', 'quantity', 'id', 'user_id')
    for row in result:
        product_info_object = prodlist.objects.filter(prod_id=row['product_id']).values('prod_name','prod_price_per_unit','prod_image')
        product_info = product_info_object[0]

        sub_total=sub_total + float(row['quantity']) * float(product_info['prod_price_per_unit'])
        total_quantity=total_quantity+int(row['quantity'])

    rounded_sub_total="{:.2f}".format(sub_total)
    plist={'sub_total':rounded_sub_total,'total_qty':total_quantity}

    return JsonResponse({'error': True, 'msg': 'Success','data':plist});




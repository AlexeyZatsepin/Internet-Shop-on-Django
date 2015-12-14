from django.http import HttpResponse
from catalog.models import *
from loginsys.models import User
from django.shortcuts import render_to_response, redirect, render
from django.core.paginator import Paginator
from .forms import CommentForm, CartForm, OrderForm
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf
from django.core.mail import send_mail


def index(request, page_number=1):
    all_products = Product.objects.all()
    current_page = Paginator(all_products, 9)
    args = {'products': current_page.page(page_number),
            'categories': Category.objects.all(),
            'newest_products': Product.objects.all().order_by('-release_date')[:4],
            'cheap_products': Product.objects.all().order_by('product_cost')[:6]}
    username = request.user.id
    if username is not None:
        args['username'] = auth.get_user(request).username
    return render_to_response('catalog.html', args)


def one_category(request, id):
    args = {'category': Category.objects.filter(id=id), 'products': Product.objects.filter(product_category=id),
            'categories': Category.objects.all()}
    print(Category.objects.filter(id=id))
    username = request.user.id
    if username is not None:
        args['username'] = auth.get_user(request).username
    return render_to_response('catalog.html', args)


def product(request, id):
    comment_form = CommentForm
    cart_form = CartForm
    args = {'comments': Comment.objects.filter(comment_product_id=id),
            'form': comment_form,
            'cart_add_form': cart_form,
            'product': Product.objects.get(id=id),
            'categories': Category.objects.all(),
            'other_products': Product.objects.exclude(id=id).order_by('product_category')[:5]}
    if SmartPhone.objects.filter(id=id):
        args['smart_phone'] = SmartPhone.objects.get(id=id)
    if TV.objects.filter(id=id):
        args['tv'] = TV.objects.get(id=id)
    if Notebook.objects.filter(id=id):
        args['notebook'] = Notebook.objects.get(id=id)
    if FlashMemory.objects.filter(id=id):
        args['flash'] = FlashMemory.objects.get(id=id)
    args.update(csrf(request))
    username = request.user.id
    if username is not None:
        args['username'] = auth.get_user(request).username
    return render_to_response('product.html', args)


def add_comment(request, id):
    product_id = id
    if request.POST and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_product = Product.objects.get(id=product_id)
            comment.comment_author = User.objects.get(id=request.user.id)
            form.save()
            request.session.set_expiry(30)
            request.session['pause'] = True
    return redirect('/product/%s/' % product_id)


def add_to_cart(request, id):
    product_id = id
    if request.POST:
        form = CartForm(request.POST)
        if form.is_valid():
            cart = form.save(commit=False)
            cart.owner = User.objects.get(id=request.user.id)
            cart.product = Product.objects.get(id=id)
            form.save()
    return redirect('/product/%s/' % product_id)


def cart(request):
    username = request.user.id
    args = {'categories': Category.objects.all()}
    if username is not None:
        args['username'] = auth.get_user(request).username
        args['email']=OrderForm
        args.update(csrf(request))
        args['cart'] = Cart.objects.filter(owner=request.user.id).raw(
            'SELECT cart.id,product_title,catalog_product.product_cost AS cost,quantity*catalog_product.product_cost AS price,quantity,product_id FROM cart,catalog_product WHERE cart.product_id=catalog_product.id ')
        return render_to_response('cart.html', args)
    else:
        return redirect('/auth/login/')


def order(request):
    if request.POST:
        form=OrderForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            send_mail('Subject', 'you have order', 'alexzatsepin7@gmail.com',[email])
            return redirect('/')
        else:
            return redirect('/cart/')


def del_from_cart(request, id):
    Cart.objects.get(id=id).delete()
    return redirect('/cart/')


def search(request):
    args = {'username': auth.get_user(request).username}
    if 'search' in request.GET and request.GET['search']:
        s = request.GET['search']
        result = Product.objects.filter(product_title=s)
        if result is None:
            result = Product.objects.filter(product_distributor=s)
            print(result)
        args['products'] = result
        args['categories'] = Category.objects.all()
        return render_to_response('catalog.html', args)
    else:
        args['search'] = 'nothing finded'
        args['categories'] = Category.objects.all()
        return render_to_response('catalog.html', args)

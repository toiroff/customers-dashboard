from django.shortcuts import render,redirect,get_object_or_404
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import Group

from .models import *
from .form import OrderForm,CreationUserForm,CustomerForm
from .filters import OrderFilter
from .decoraters import unauthenticaterd_user,allowed_users,admin_only


# Create your views here.
@unauthenticaterd_user
def register(request):

   form = CreationUserForm()

   if request.method == 'POST':
      form = CreationUserForm(request.POST)
      if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            # ADDING TO GROUP
            # group = Group.objects.get(name='customer')
            # user.groups.add(group)

      
            
            # MESSAGE
            messages.success(request,'Account was created for ' + username)
            return redirect('login')  


   content = {'form':form}
   return render(request, 'accounts/register.html',content)


@unauthenticaterd_user
def loginPage(request):
   if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')

      if username and password:
         user = authenticate(request, username=username, password=password)
         if user is not None:
               login(request, user)
               return redirect('home')
         else:
               messages.error(request, 'Username or password is incorrect')
      else:
         messages.error(request, 'Both username and password are required')

   content = {}
   return render(request,'accounts/login.html',content)

def logoutPage(request):
   logout(request)
   return redirect('login')



@login_required(login_url='login')
@admin_only
def home(request):
  orders = Order.objects.all()
  customers = Customer.objects.all()

  total_orders = orders.count()
  delivered = orders.filter(status='Delivered').count()
  pending = orders.filter(status='Pending').count()
  
  content = {
     'orders':orders,
     'customers':customers,
     'delivered':delivered,
     'total_orders':total_orders,
     'pending':pending,

  }
  return render(request, 'accounts/dashboard.html',content)

@login_required(login_url='login')
def customer(request,pk):
    customer = Customer.objects.get(id=pk)

    orders = customer.order_set.all()
    total_orders = orders.count()

   # FILTERS
    myFilter = OrderFilter(request.GET,queryset=orders)
    orders = myFilter.qs

    content = {
       'customer':customer,
       'orders':orders,
       'total_orders':total_orders,
       'myFilter':myFilter
    }
    return render(request, 'accounts/customer.html',content)

@login_required(login_url='login')
@allowed_users(allowed_roles='customer')
def user(request):
   orders = request.user.customer.order_set.all()

   total_orders = orders.count()
   delivered = orders.filter(status='Delivered').count()
   pending = orders.filter(status='Pending').count()

   content = {
      'orders':orders,
      'delivered':delivered,
     'total_orders':total_orders,
     'pending':pending,}
   
   return render(request,'accounts/user.html',content)


@login_required(login_url='login')
def user_settings(request):
   customer = request.user.customer
   form = CustomerForm(instance=customer)
   if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
         


   content = {
      'form':form
   }
   return render(request,'accounts/account_settings.html',content )


@login_required(login_url='login')
def products(request):
    products = Product.objects.all()
    content = {
       'products':products
    }
    return render(request, 'accounts/products.html',content)












@login_required(login_url='login')
def create_order(request,pk):
   customer = get_object_or_404(Customer, id=pk)

   #Inline Formset
   OrderFormSet = inlineformset_factory(Customer,Order,fields=('product','status'))
   formset = OrderFormSet(queryset=Order.objects.none() #this to not to show orders that have already
   ,instance=customer)

   # Basic Create
   form = OrderForm(initial={'customer': customer})
   
   # Algorithm to add database with from
   if request.method == 'POST':
      formset = OrderFormSet(request.POST,instance=customer)
      if formset.is_valid():
         formset.save()
         return redirect('/')
      
   content = {'formset':formset}
   return render(request,'accounts/order_form.html',content)

@login_required(login_url='login')
def update_order(request,pk):
   order = Order.objects.get(id=pk)
   form = OrderForm(instance=order)

   if request.method == 'POST':
      form = OrderForm(request.POST, instance=order)
      if form.is_valid():
         form.save()
         return redirect('/')

   content = {
      'form':form
   }
   return render(request,'accounts/order_form.html',content)


@login_required(login_url='login')
def delete_order(request,pk):
   order = Order.objects.get(id=pk)

   if request.method == 'POST':
      order.delete()
      return redirect('/')
   
   content = {
      'item':order
   }
   return render(request,'accounts/delete.html',content)

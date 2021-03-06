# from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import *
from .models import *
# from django.http import HttpResponse
#
#
# def home(request):
#     return render(request, 'MainApp/index.html')
#
#
# def home_index(request, pk_customer):
#     customer = Customer.objects.get(id=pk_customer)
#     context = {'c': customer}
#     return render(request, 'MainApp/customer_index.html', context)
#
#
# def menu(request):
#     return render(request, 'MainApp/menu.html')
#
#
# def register(request):
#     form = RegistrationForm
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#     context = {'F': form}
#     return render(request, 'MainApp/register.html', context)
#
#
# def customer(request, pk_customer):
#     customer = Customer.objects.get(id=pk_customer)
#     order = Order.objects.get(customer_id=pk_customer)
#     context = {'C': customer, 'O': order}
#     return render(request, "MainApp/customer.html", context)
#
#
# def edit_customer(request, pk_customer):
#     button_text = 'Create account'
#     customer = Customer.objects.get(id=pk_customer)
#     form = RegistrationForm(instance=customer)
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST, instance=customer)
#         if form.is_valid():
#             form.save()
#
#     context = {'F': form, 'button_text': button_text}
#     return render(request, 'MainApp/register.html', context)


class UserView(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = CustomerSerializer


class MenuView(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

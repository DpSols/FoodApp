from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('customer', views.UserView)
router.register('menu', views.MenuView)
router.register('order', views.OrderView)

urlpatterns = [
    path('', include(router.urls)),
    path('menu', include(router.urls), name='menu'),
    path('order', include(router.urls), name='order')
]

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('<str:pk_customer>', views.home_index, name='home_index'),
#     path('menu', views.menu, name='menu'),
#     path('register', views.register, name='register'),
#     path('customer/<str:pk_customer>/', views.customer, name='customer'),
#     path('register/<str:pk_customer>', views.edit_customer, name='edit'),
#
#
#
# ]

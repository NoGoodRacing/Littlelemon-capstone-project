from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('api-token-auth/', obtain_auth_token),
    path('menu-items/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
]

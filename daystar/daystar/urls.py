"""
URL configuration for daystar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
# from . import views
# from .views import login_view, register_view, password_reset_view, forgot_password_view
from index import views
urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication URLs
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('password_reset/', views.password_reset_view, name='password_reset'),
    path('forgot_password/', views.forgot_password_view, name='forgot_password'),

    # Baby URLs
    path('baby/', views.baby_list, name='baby_list'),
    path('baby/add/', views.add_baby, name='add_baby'),
    path('baby/<int:baby_id>/', views.baby_detail, name='baby_detail'),
    path('baby/<int:baby_id>/edit/', views.edit_baby, name='edit_baby'),
    path('baby/<int:baby_id>/delete/', views.delete_baby, name='delete_baby'),

    # Sitter URLs
    path('sitter/', views.sitter_list, name='sitter_list'),
    path('sitter/add/', views.add_sitter, name='add_sitter'),
    path('sitter/<int:sitter_id>/', views.sitter_detail, name='sitter_detail'),
    path('sitter/<int:sitter_id>/edit/', views.edit_sitter, name='edit_sitter'),
    path('sitter/<int:sitter_id>/delete/', views.delete_sitter, name='delete_sitter'),

    # Payment URLs
    path('payment/', views.payment_list, name='payment_list'),
    path('payment/add/', views.add_payment, name='add_payment'),
    path('payment/<int:payment_id>/', views.payment_detail, name='payment_detail'),
    path('payment/<int:payment_id>/edit/', views.edit_payment, name='edit_payment'),
    path('payment/<int:payment_id>/delete/', views.delete_payment, name='delete_payment'),

    # Procurement Item URLs
    path('procurement/', views.procurement_list, name='procurement_list'),
    path('procurement/add/', views.add_procurement_item, name='add_procurement_item'),
    path('procurement/<int:item_id>/', views.procurement_item_detail, name='procurement_item_detail'),
    path('procurement/<int:item_id>/edit/', views.edit_procurement_item, name='edit_procurement_item'),
    path('procurement/<int:item_id>/delete/', views.delete_procurement_item, name='delete_procurement_item'),
]

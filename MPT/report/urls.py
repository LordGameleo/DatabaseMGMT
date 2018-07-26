"""MPT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.main, name = 'main' ),
    path('modify', views.modify, name = 'modify'),
    path('modify/options/', views.modify_options, name = 'modify_options'),
    path('modify/slot/<int:slot_id>/', views.modify_slot, name = 'modify_slot'),
    path('delete/', views.delete_view, name = 'delete'),
    path('add_options/', views.add_options, name = 'add_options'),
    path('add/slot/', views.add_slot_views, name = 'add_slot_views'),
    path('add_slot/<int:shift_id>/', views.add_slot, name = 'add_slot'),
    path('add/', views.add, name = 'add'),
    path('add_shift_end/', views.add_shift_end, name = 'add_shift_end'),
    path('search/', views.search, name = 'search'),
    path('delete/date/<int:date_id>/', views.delete_date_entry),
    path('report_options/', views.report_options, name = 'report_options'),
    path('rgen/', views.generate_report, name = 'rgen'),
    path('vesselwise_tonnage/', views.vesselwise_tonnage, name = 'vesselwise_tonnage'),
    path('delete/shift/<int:shift_id>/', views.delete_shift_entry),
    path('delete/slot/<int:slot_id>/', views.delete_slot_entry),
]

"""
URL configuration for store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path
from inventory import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('list-items/', views.list_items, name='list_items'),
    path('add-items/', views.add_items, name='add_items'),
    path('update-items/<str:pk>/', views.update_items, name='update_items'),
    path('delete-items/<str:pk>/', views.delete_items, name='delete_items'),
    path('stock-detail/<str:pk>/', views.stock_detail, name='stock_detail'),
    path('issue-items/<str:pk>/', views.issue_items, name='issue_items'),
    path('receive-items/<str:pk>/', views.receive_items, name='receive_items'),
    path('reorder-level/<str:pk>/', views.reorder_level, name='reorder_level'),
    path('list-history/', views.list_history, name='list_history'),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]

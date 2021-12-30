from typing import Text
from django.contrib.messages import views
from django.urls import path
from . import views
from .views import (Home, 
                    DebtList, DebtCreate, DebtDetail, 
                    DebtUpdate, DebtDelete,
                    BookCreate, BookList, AdminList,
                    BookDetail, BookUpdate, BookDelete)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('debts/', DebtList.as_view(), name='debt_list'),
    path('create/', DebtCreate.as_view(), name='debt_create'),
    path('debt/<int:pk>/', DebtDetail.as_view(), name='debt_detail'),
    path('debt/<int:pk>/update', DebtUpdate.as_view(), name='debt_update'),
    path('debt/<int:pk>/delete', DebtDelete.as_view(), name='debt_delete'),
    path('book/', BookCreate.as_view(), name='book_create'),
    path('books/', BookList.as_view(), name='book_list'),
    path('admino/', AdminList.as_view(), name='admin_list'),
    path('contact/', views.contact, name="contact"),
    path('books/<int:pk>/', BookDetail.as_view(), name='book_detail'),
    path('books/<int:pk>/update/', BookUpdate.as_view(), name='update'),
    path('books/<int:pk>/delete', BookDelete.as_view(), name='delete')
    
]
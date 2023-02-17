
from django.contrib import admin
from django.urls import path
from crudoperations import views


#from .views import api_response,json_response,add_data

# urlpatterns = [
#     path('getdata', api_response),
#     path('getjson', json_response),
#     path('add', add_data),

# ]

urlpatterns = [
    path('studs', views.studs),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.delete),  
]
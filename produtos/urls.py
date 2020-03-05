from django.urls import path
from .views import produtos_list, produtos_new, produtos_update, produtos_delete


urlpatterns = [
    path('list/', produtos_list, name="produtos_list"),
    path('new/', produtos_new, name="produtos_new"),
    path('update/<int:id>/', produtos_update, name="produtos_update"),
    path('delete/<int:id>/', produtos_delete, name="produtos_delete"),
]
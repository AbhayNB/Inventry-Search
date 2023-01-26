from django.urls import path
from . import views
urlpatterns = [
    path('', views.ShowInvetory, name="find_item"),
    path('update',views.UpdateI,name="update"),
]
from django.contrib import admin
from django.urls import path
from search import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.search, name='search'),
    path('shoppingcart', views.shoppingcart, name='shoppingcart'),
    path('searchresult', views.searchresult, name='search-result'),
]
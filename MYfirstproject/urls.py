from django.urls import path
from . import views

urlpatterns = [
    path('',views.Hi,name='home'),
    path('Show/',views.Show,name='Show'),
    path('Enter/',views.Enter,name='Enter'),
    path('count/',views.count, name='count')

]

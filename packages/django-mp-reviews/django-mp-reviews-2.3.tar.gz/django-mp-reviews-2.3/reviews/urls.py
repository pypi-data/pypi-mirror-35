
from django.urls import path

from reviews import views


app_name = 'reviews'


urlpatterns = [

    path('', views.index, name='index'),

    path('modal/', views.get_new_review_modal, name='modal'),

    path('add/', views.add_review, name='add'),

]

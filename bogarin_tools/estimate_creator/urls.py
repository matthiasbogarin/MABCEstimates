from django.urls import path
from . import views


app_name = 'estimate_creator'


urlpatterns = [
    # Estimate Creator Home
    path('/', views.index, name='index'),
]
from django.urls import path
from . import views

app_name = "iris"

urlpatterns = [
    path('', views.index, name='index'),
    path('prediction/', views.predict_chances, name='submit_prediction'),
    path('results/', views.view_results, name='results')
]
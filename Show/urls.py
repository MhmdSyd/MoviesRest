from django.urls import path
from . import views

urlpatterns = [
    path('norestnomodel/', views.no_rest_no_model),
    path('norestfrommodel/', views.no_rest_from_model),
    path('fbv/', views.FBV_list),
    path('fbv/<int:pk>', views.FBV_pk)

]
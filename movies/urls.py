from django.urls import path, include
from .views import no_rest_no_model, no_rest_from_model, no_rest_from_model_filter, FBV_list, FBV_pk
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('movies', views.viewsets_movie)

urlpatterns=[
    path('jsonnomodel/', no_rest_no_model),
    
    path('jsonfrommodel/', no_rest_from_model),
    path('jsonfrommodelfilter/', no_rest_from_model_filter),
    
    path('FBV/', FBV_list),
    path('FBV/<int:pk>',FBV_pk),

    path('CBV/', views.CBV_List.as_view()),
    path('CBV/<int:pk>', views.CBV_pk.as_view()),

    path('mixins/', views.mixins_list.as_view()),
    path('mixins/<int:pk>', views.mixins_pk.as_view()),

    path('generics/', views.generics_list.as_view()),
    path('generics/<int:pk>', views.generics_pk.as_view()),

    path('viewsets/', include(router.urls)),
]
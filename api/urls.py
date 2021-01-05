from django.urls import path
from rest_framework import routers

from .views import category_views, actor_views, picture_views, movie_views, access_views

router = routers.DefaultRouter()
router.register('actors', actor_views.ActorViewSet)
router.register('accesses', access_views.AccessViewSet)

app_name = 'api'

urlpatterns = [
    path('categories/', category_views.CategoryList.as_view()),
    path('categories/<int:pk>/', category_views.CategoryDetail.as_view()),

    path('pictures/', picture_views.PictureList.as_view()),
    path('pictures/<int:pk>/', picture_views.PictureDetail.as_view()),

    path('movies/', movie_views.MovieList.as_view()),
    path('movies/<int:pk>/', movie_views.MovieDetail.as_view()),
]

urlpatterns += router.urls

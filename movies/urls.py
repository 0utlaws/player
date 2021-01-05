from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'movies'

urlpatterns = [
    path('categories/', views.MovieCategoriesView.as_view(), name='categories'),
    path('category/<int:pk>/videos', views.CategoryVideosView.as_view(), name='category-videos'),
    path('validate/access/', views.ValidateUserAccess.as_view(), name='validate-access'),
    path('video/<int:pk>/', views.VideoView.as_view(), name='video'),
    path('tickets/', views.TicketListView.as_view(), name='tickets'),
    path('tickets/add/', views.TicketCreateView.as_view(), name='add-ticket'),
    path('tickets/<int:pk>/messages/', views.TicketMessageListView.as_view(), name='ticket-messages'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

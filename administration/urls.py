from django.urls import path

from .views import actor_views, category_views, movie_views, access_views, user_views, support_views, email_views

app_name = 'administration'

urlpatterns = [
    path('', actor_views.ActorListView.as_view(), name='actor-list'),
    path('actors/data/', actor_views.ActorData.as_view(), name='actors-data'),
    path('actors/add/', actor_views.ActorCreateView.as_view(), name='add-actor'),
    path('actors/<int:pk>/update/', actor_views.ActorUpdateView.as_view(), name='update-actor'),
    path('actors/<int:pk>/delete/', actor_views.ActorDeleteView.as_view(), name='delete-actor'),

    path('categories/', category_views.CategoryListView.as_view(), name='category-list'),
    path('categories/add/', category_views.CategoryCreateView.as_view(), name='add-category'),
    path('categories/<int:pk>/update/', category_views.CategoryUpdateView.as_view(), name='update-category'),
    path('categories/<int:pk>/delete/', category_views.CategoryDeleteView.as_view(), name='delete-category'),

    path('videos/', movie_views.MovieListView.as_view(), name='movie-list'),
    path('videos/add/', movie_views.MovieCreateView.as_view(), name='add-movie'),
    path('videos/<int:pk>/update/', movie_views.MovieUpdateView.as_view(), name='update-movie'),
    path('videos/<int:pk>/delete/', movie_views.MovieDeleteView.as_view(), name='delete-movie'),

    path('accesses/', access_views.AccessListView.as_view(), name='access-list'),
    path('accesses/add/', access_views.AccessCreateView.as_view(), name='add-access'),
    path('accesses/<int:pk>/update/', access_views.AccessUpdateView.as_view(), name='update-access'),
    path('accesses/<int:pk>/delete/', access_views.AccessDeleteView.as_view(), name='delete-access'),

    path('users/', user_views.UserListView.as_view(), name='user-list'),
    path('users/add/', user_views.UserCreateView.as_view(), name='add-user'),
    path('users/<int:pk>/update/', user_views.UserUpdateView.as_view(), name='update-user'),
    path('users/<int:pk>/delete/', user_views.UserDeleteView.as_view(), name='delete-user'),
    path('users/<int:pk>/change_password/', user_views.UserChangePasswordView.as_view(), name='change-password'),

    path('tickets/', support_views.TicketListView.as_view(), name='ticket-list'),
    path('tickets/<int:pk>/update/', support_views.TicketUpdateView.as_view(), name='update-ticket'),
    path('ticket/<int:pk>/messages/', support_views.TicketMessageListAndCreateView.as_view(), name='ticket-messages'),

    path('send/single/email/', email_views.SingleSendEmailView.as_view(), name='single-email'),
    path('send/multiple/email/', email_views.MultipleSendEmailView.as_view(), name='multiple-email')
]

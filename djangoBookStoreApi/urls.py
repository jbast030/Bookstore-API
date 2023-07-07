from django.urls import path
from .views.test_views import test_view
from .views.shopping_carts_view import shopping_carts_view
from .views.user_profile_view import UserProfileView
from .views.user_profile_view import CreateUserView
from .views.user_profile_view import UserDetailView
from .views.wish_list_books_view import wish_list_books_view

# add route paths here
urlpatterns = [
    path('test/', test_view),
    path('user/<int:id>/shopping_carts', shopping_carts_view),
    path('user/<int:user_id>/profile', UserProfileView.as_view(), name='user_profile'),
    path('user/create', CreateUserView.as_view(), name='user-create'),
    path('user/', UserDetailView.as_view(), name='user-detail'),
    path('user/<int:id>/wishlist', wish_list_books_view),
]
#h
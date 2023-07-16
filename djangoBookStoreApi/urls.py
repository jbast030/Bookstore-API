from django.urls import path
from .views.test_views import test_view
from .views.shopping_carts_view import ShoppingCartsView
from .views.user_profile_view import UserProfileView
from .views.user_profile_view import CreateUserView
from .views.user_profile_view import UserDetailView
from .views.wish_list_books_view import wish_list_books_view
from .views.wish_list_books_view import add_book_to_wishlist
from .views.wish_list_books_view import create_new_wishlist
from .views.books_view import books_view
from .views.book_details_view import book_details_view, genre_view, best_selling_books

urlpatterns = [
    path('test/', test_view),
    path('user/<int:id>/shopping_carts', ShoppingCartsView.as_view()),
    path('user/<int:user_id>/profile', UserProfileView.as_view(), name='user_profile'),
    path('user/create', CreateUserView.as_view(), name='user-create'),
    path('user/', UserDetailView.as_view(), name='user-detail'),
    path('user/<int:id>/wishlist', wish_list_books_view),
    path('user/wishlist/add_book', add_book_to_wishlist),
    path('user/wishlist/create_wishlist', create_new_wishlist),
    path('books/', books_view, name='books'),
    path('books/genre/', genre_view, name='genre'),
    path('books/top_sellers/', best_selling_books, name='top_sellers'),
    path('books/<int:id>/details', book_details_view),
]

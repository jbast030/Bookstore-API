from django.http import JsonResponse
from django.core import serializers
import json

from ..models.WishLists import WishLists
from ..models.WishListBooks import WishListBooks
from ..models.Books import Books

#Get Request via WishList Id
def wish_list_books_view(request, id):
    #Generates a queryset of a inner join between wish_list_books and books tables
    queryset = WishListBooks.objects.filter(wish_list=id).select_related('book')
    book_list = []
    #Store book names inside an empty array by going through each object
    for qs in queryset:
        book_list.append({
            'Book Name:' : qs.book.name
        })
    return JsonResponse(book_list, safe=False)

def add_book_to_wishlist(request):
    #Generate queryset of all book and wishlists.
    bookset = Books.objects.all()
    wishlistSet = WishLists.objects.all()

    #List to be filled with IDs for checks
    bookID_list = []
    for bID in bookset:
        bookID_list.append(bID.id)
    
    wishlist_list = []
    for wID in wishlistSet:
        wishlist_list.append(wID.id)
    
    #Obtain book ID and wishlist ID from POST request
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        data = {}

    #Obtain both IDs and set them to their associated variables for checks.
    bookID = data.get('bookID')
    wishlistID = data.get('wishlistID')

    #Check if either ID is missing in request. If so, send error. Else, continue with bookID check.
    if bookID == None or wishlistID == None:
        response = {
            'Error' : 'BookID or WishlistID missing. Please enter it again.'
        }
        return JsonResponse(response, safe=False)
    
    #Check for existing book ID. If not, send error. Else, continue to wishlistID check.
    if bookID not in bookID_list:
        response = {
            'Error' : 'BookID submitted does not exist within the database.'
        }
        return JsonResponse(response, safe=False)
    
    #Check for existing wishlist ID. If not, send error. Else, create new wishlist_book into associated table.
    if wishlistID not in wishlist_list:
        response = {
            'Error' : 'WishlistID submitted does not exist within the database.'
        }
        return JsonResponse(response, safe=False)
    else:
        #Create new book entry in to the Wish_List_Books table on mysql. Then state its success.
        addbook = WishListBooks.objects.create(
            book_id = bookID,
            wish_list_id = wishlistID
        )

        response = {
            'Message' : 'Book ID has been successfully added to associated Wishlist.'
            
        }
        return JsonResponse(response, safe=False)
    
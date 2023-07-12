from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.core import serializers
from ..models.BookComments import BookComments


def book_comments_view(request, id):
    model_values = BookComments.objects.get(id = id)
    data = serializers.serialize('json', model_values)
    return JsonResponse(data, safe=False)

# def post(self, request, id):
#     try:
#         book_commments = get_object_or_404()
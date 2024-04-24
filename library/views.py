from django.shortcuts import render
from django.http import JsonResponse

from .models import Circulation

# Create your views here.
def checkout_book(request):
    try:
        book_id = request.POST.get('book_id')
        member_id = request.POST.get('member_id')
        resp = Circulation.checkout_book(book_id, member_id)
        return JsonResponse(resp)
    except Exception as e:
        return JsonResponse({'status': False, 'message': str(e)})
        

def return_book(request):
    try:
        book_id = request.POST.get('book_id')
        member_id = request.POST.get('member_id')
        resp = Circulation.return_book(book_id, member_id)
        return JsonResponse(resp)
    except Exception as e:
        return JsonResponse({'status': False, 'message': str(e)})

def fulfill_book(request):
    try:
        book_id = request.POST.get('book_id')
        member_id = request.POST.get('member_id')
        resp = Circulation.fulfill(book_id, member_id)
        return JsonResponse(resp)    
    except Exception as e:
        return JsonResponse({'status': False, 'message': str(e)})
    
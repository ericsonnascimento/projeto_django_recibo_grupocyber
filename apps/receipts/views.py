from django.shortcuts import render

# Create your views here.

def receipts(request):
    return render(request, 'receipts/receipts.html')
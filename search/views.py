from django.shortcuts import render


def search(request):
    if request.method == "GET":



     return render(request, 'searchcart.html')

    else:

     return render(request, 'searchcart.html')

def shoppingcart(request):
    if request.method == "POST":

     return render(request, 'shoppingcart.html')

    else:

     return render(request, 'shoppingcart.html')
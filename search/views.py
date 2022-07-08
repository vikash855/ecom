from django.shortcuts import render
import requests
import json

def search(request):
    data = {}
    url = 'https://geektrust.s3.ap-southeast-1.amazonaws.com/coding-problems/shopping-cart/catalogue.json'
    response = requests.get(url)
    data = response.json()
    return render(request, 'searchcart.html', {'data': data})


def searchresult(request):

    if request.method == "POST":
        item = request.POST['item']
        url = 'https://geektrust.s3.ap-southeast-1.amazonaws.com/coding-problems/shopping-cart/catalogue.json'
        response = requests.get(url)
        search_item = response.json()
        return render(request, 'searchresult.html', {'item': item, 'search_item': search_item})
    else:
        return render(request, 'searchresult.html')

def shoppingcart(request):

    if request.method == "POST":
     return render(request, 'shoppingcart.html')
    else:
     return render(request, 'shoppingcart.html')
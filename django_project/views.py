import requests
from django.shortcuts import render

def index(request):
    response = requests.get("https://zenquotes.io/api/random")
    quote = response.json()[0] if response.ok else {"q": "Error fetching quote", "a": ""}
    return render(request, 'index.html', {'quote': quote})

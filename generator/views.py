from django.shortcuts import render
from random import choice

# Create your views here.

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def generate_password(request):
    lowercase_characters = list('qwertyuiopasdfghjklñzxcvbnm')
    numbers = list('1234567890')
    special_characters = list(',.-_/*+')

    characters = lowercase_characters

    if request.GET.get('uppercase'):
        characters.extend(list(map(str.upper, lowercase_characters)))
    if request.GET.get('special'):
        characters.extend(special_characters)
    if request.GET.get('numbers'):
        characters.extend(numbers)

    length = int(request.GET.get('length'))
    generated_password = ""

    for i in range(length):
        generated_password += choice(characters)

    return render(request, 'password.html', {'password': generated_password})

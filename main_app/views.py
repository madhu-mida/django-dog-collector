from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


class Dog:  # Note that parens are optional if not inheriting from another class
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age


dogs = [
    Dog('Ziva', 'Maltipoo', 'Honey Bunch Sugar Sweet', 1),
    Dog('Zara', 'Yorkiepoo', 'Charming Face', 2),
    Dog('Lulu', 'Husky', 'Ferocious Look', 4)
]


def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')


def about(request):
    return render(request, 'about.html')


def dogs_index(request):
    return render(request, 'dogs/index.html', {'dogs': dogs})

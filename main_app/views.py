from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Dog
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm


# Create your views here.


# class Dog:  # Note that parens are optional if not inheriting from another class
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age


# dogs = [
#     Dog('Ziva', 'Maltipoo', 'Honey Bunch Sugar Sweet', 1),
#     Dog('Zara', 'Yorkiepoo', 'Charming Face', 2),
#     Dog('Lulu', 'Husky', 'Ferocious Look', 4)
# ]


def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')


def about(request):
    return render(request, 'about.html')


def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {'dogs': dogs})


def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    # instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    return render(request, 'dogs/detail.html', {'dog': dog, 'feeding_form': feeding_form})

# add this new function below dogs_detail


def add_feeding(request, dog_id):
    pass


def add_feeding(request, dog_id):
    # create the ModelForm using the data in request.POST
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the dog_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.dog_id = dog_id
        new_feeding.save()
    return redirect('detail', dog_id=dog_id)


class DogCreate(CreateView):
    model = Dog
    fields = '__all__'
    success_url = '/dogs/'


class DogUpdate(UpdateView):
    model = Dog
    # Let's disallow the renaming of a dog by excluding the name field!
    fields = ['breed', 'description', 'age']


class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs/'

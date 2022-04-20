from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm


def index(request):

    entries = Entry.objects.order_by('-date_posted')
    entries2 = Entry.objects.order_by('-date_posted')[:1]

    context = {'entries': entries, 'entries2': entries2}

    return render(request, 'entries/index.html', context)


def add(request):

    if request.method == "POST":
        form = EntryForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('home')

    else:

        form = EntryForm()

    context = {"form": form}

    return render(request, 'entries/add.html', context)


def about(request):
    return render(request, 'entries/about.html')

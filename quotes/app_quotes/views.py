from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, Page
from mongoengine import connect


from .utils import Author, Quote
from .forms import AuthorForm, QuoteForm

connect(db='database', host="mongodb+srv://olesyashevchuk0402:JeJ6Bb00zAnOUTRL@cluster0.ki8cwf1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

def hello(request):
    return render(request, 'app_quotes/index.html', context={"msg": "Hello in quotes website!"})

def index(request, page=1):
    quotes = Quote.objects.all()
    paginator = Paginator(quotes, 20)
    quotes_on_page = paginator.page(page)
    return render(request, 'app_quotes/quotes.html', context={'quotes_on_page': quotes_on_page})


def author(request, author_name):
    author = Author.objects.get(fullname=author_name)
    return render(request, 'app_quotes/author.html', context={"author": author})


@login_required
def add_author_to_db(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = Author(
                fullname=form.fullname,
                born_date=form.born_date,
                born_location=form.born_location,
                description=form.description
            )
            form.save()
            author.save()
            return redirect(to='app_quotes:quotes')
    else:
        form = AuthorForm()
    return render(request, 'app_quotes/add_author.html', {'form': form})

@login_required
def add_quote_to_db(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = Quote(
                quote=form.quote,
                author=form.author,
                tags=form.tags
            )
            form.save()
            quote.save()
            return redirect(to='app_quotes:quotes')
    else:
        form = QuoteForm()
    return render(request, 'app_quotes/add_quote.html', {'form': form})
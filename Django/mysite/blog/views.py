from django.shortcuts import render
# from .Fetch import query_database

posts = [
    {
        "title": "jaws",
        "vtypes": "movie",
        "year": "1980",
        "runtime": "1h30m"
    },
    {
        "title": "scary movie",
        "vtypes": "movie",
        "year": "2001",
        "runtime": "1h15m"
    }
]


def home(request):
    context = {
        'title': 'Home',
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

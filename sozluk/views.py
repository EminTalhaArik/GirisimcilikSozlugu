from multiprocessing import context
from django.http.response import HttpResponse
from django.shortcuts import render
from sozluk.models import Term, Category
from django.db.models import Q
from django.shortcuts import redirect

# Create your views here.


def index(request, slug=""):

    search_term = request.GET.get('search')

    if search_term:
        terms = Term.objects.filter(Q(title__icontains=search_term) | Q(
            description__icontains=search_term))

    elif slug != "":
        terms = Term.objects.filter(category__slug=slug)

    else:
        terms = Term.objects.all().order_by('title')

    context = {
        "terms": terms,
        "categories": Category.objects.all().order_by('name'),
        "slug": slug
    }

    return render(request, "sozluk/index.html", context)

def about(request):
    return render(request, "sozluk/about.html")


def view_404(request, exception=None):
    return redirect('/') # or redirect('name-of-index-url')

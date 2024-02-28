from django.shortcuts import render, redirect, get_object_or_404
from . import models
from .forms import StockListingForm
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()

def index(request: HttpRequest) -> HttpResponse:
    context = {
        'listing_count': models.StockListing.objects.count(),
        'users_count': models.User.objects.count(),
    }
    return render(request, 'multi_stock/index.html', context)

@login_required
def listing_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = StockListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.user = request.user
            listing.save()
            return redirect('listing_detail', listing.pk)
    else:
        form = StockListingForm()
    return render(request, 'multi_stock/listing_create.html', {'form': form})

def listing_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'multi_stock/listing_list.html', {
        'listing_list': models.StockListing.objects.all(),
    })

def listing_detail(request: HttpRequest, pk) -> HttpResponse:
    return render(request, 'multi_stock/listing_detail.html', {
        'listing': get_object_or_404(models.StockListing, pk=pk),
    })

def listing_search(request: HttpRequest) -> HttpResponse:
    search_term = request.GET.get('search', '')
    listing_list = models.StockListing.objects.all()
    print(f"Search term: {search_term}")
    if search_term:
        listing_list = listing_list.filter(
            Q(title__icontains=search_term) | 
            Q(category__icontains=search_term)
        )

    context = {'listing_search': listing_list}
    return render(request, 'listing_search.html', context)
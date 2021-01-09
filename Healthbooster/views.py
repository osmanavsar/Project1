from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from Healthbooster.models import Investor, Relative, Patient
from Healthbooster.forms import InvestorForm, PatientForm, RelativeForm

def add_investor(request):
    if request.method == 'POST':
        form = InvestorForm(request.POST)
        if form.is_valid():
            a = Investor(first_name=form.cleaned_data["first_name"],
                       last_name=form.cleaned_data["last_name"],
                       email=form.cleaned_data["email"])
            a.save()
            return HttpResponseRedirect('/investors/')
    else:
        form = InvestorForm()
    return render(request, 'add_investor.html', {'form': form})

def all_investors(request):
    investors_list = Investor.objects.all()
    return render(request, "investors.html", {'investors_list': investors_list})

def investor_search(request):
    result_set = Investor.objects.filter(email__contains='gmail.com', last_name__contains= 'G')
    return HttpResponse(result_set)

def search_form(request):
    return render(request, "search_form.html")

def search(request):
    errors = []
    if request.GET['q']:
        q = request.GET['q']
        print('query', q)
        if len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html', {'books': books, 'query': q})
    else:
        errors.append('Enter a search term.')

    return render(request, 'search_form.html', {'errors': errors})

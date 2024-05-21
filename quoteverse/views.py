from django.shortcuts import render
from .models import Quote
from .forms import QuoteForm

def home(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            author = form.cleaned_data['author']
            language = form.cleaned_data['language']
            new_quote = Quote(text=text, author=author, language=language)
            new_quote.save()
    else:
        form = QuoteForm()

    quotes = Quote.objects.all()
    return render(request, 'quoteverse/home.html', {'form': form, 'quotes': quotes})

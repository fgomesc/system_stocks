from django.shortcuts import render, redirect
import requests
import json
from apps.quotes.forms import StockForm
from apps.quotes.models import Stock
from django.contrib import messages



def home(request):

    # pk_2555a18193de468a81a8c37f9bade585

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_2555a18193de468a81a8c37f9bade585")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = 'Error...'
        return render(request, 'home.html', {'api': api})

    else:
        return render(request, 'home.html', {'ticker': 'Enter a ticker Symbol Above...'})


def about(request):
    return render(request, 'about.html', {})


def add_stocks(request):
    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ('Stock has been Added'))
            return redirect(add_stocks)
    else:
        ticker = Stock.objects.all()
        output = []

        for ticker_item in ticker:

            api_request = requests.get(
                "https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_2555a18193de468a81a8c37f9bade585")

            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = 'Error...'

        return render(request, 'add_stcoks.html', {'ticker': ticker, 'output': output})

def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ('Stock Had Benn Deleted!'))
    return redirect(delete_stocks)


def delete_stocks(request):
    ticker = Stock.objects.all()
    return render(request, 'delete_stocks.html', {'ticker': ticker})
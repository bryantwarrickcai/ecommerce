from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        "appname": "BryShop",
        "name": "Bryant Warrick Cai",
        "npm": "2306256255",
        "class": "KKI"
    }

    return render(request, "main.html", context)

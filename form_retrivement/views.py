from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse

# Create your views here.


def index(request):
    if request.method == "POST":
        return HttpResponseRedirect("/done")

    return render(request, "form_retrivement/index.html")


def done(request):
    return HttpResponse("done")

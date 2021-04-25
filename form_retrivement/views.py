from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse
from bissness.dict_to_json import dict_to_json
import requests


def index(request):
    if request.method == "POST":
        post_data = request.POST.copy()

        # there is a bunch of info to add to the post_data before transmitting it to json format
        del post_data['csrfmiddlewaretoken']

        # todo this data must be retrieved from the database
        post_data['vagrantEnvPath'] = "/home/pfe21/Documents/cyber_range/vagrant_environments/prof_1/exo1/instance-1"
        post_data['dockerImagesPaths'] = {"vulnerables/web-dvwa": "/home/pfe21/Desktop/TP01/dockerimage"}
        post_data['vagrantBoxesPaths'] = {}

        json_data = dict_to_json(post_data)
        print(json_data)
        print("------------------------------------------ requests -------------------------------------------")
        response = requests.post("http://localhost:8080/cyber_range_api/virtual_machine/create", json=json_data)
        print(response.status_code)
        return HttpResponseRedirect("/done")

    return render(request, "form_retrivement/index.html")


def done(request):
    return HttpResponse("done")

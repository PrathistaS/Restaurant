from django.shortcuts import render
from .models import Destination
import requests
from accounts.views import geo_current_location
# Create your views here.


def index(request):

    dests = Destination.objects.all()
    #current_location = geo_current_location()

    return render(request, "index.html", {'dests': dests})

def search(request):
    dests = Destination.objects.get()
    # current_location = geo_current_location()

    return render(request, "index.html", {'dests': dests})


def get_search_details(request,query):
    api_key = 'AIzaSyASP9vWd3OTWFUDn6FoliMof9g8k3PVYds'

    # url variable store url
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

    # The text string on which to search
    # query = input('Search query: ')

    # get method of requests module
    # return response object
    r = requests.get(url + 'query=' + query +
                     '&key=' + api_key)

    # json method of response object convert
    # json format data into python format data
    x = r.json()

    # now x contains list of nested dictionaries
    # we know dictionary contain key value pair
    # store the value of result key in variable y
    dests = x['results']

    return render(request, "index.html", {'dests': dests})

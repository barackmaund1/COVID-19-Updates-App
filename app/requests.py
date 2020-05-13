import requests
from .model import Country


# Getting the movie base url
Countries_url = None

def configure_request(app):
    global Countries_url
    Countries_url = app.config['COUNTRIES_BASE_URL']

def get_countries() :   


    url = "https://api.covid19api.com/countries"

    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

    return response.text.encode('utf8')
def process_result(country_list):
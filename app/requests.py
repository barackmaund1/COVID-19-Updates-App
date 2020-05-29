from .model import Country,Kenyan
import urllib.request,json
import requests
from config import Config


# Getting the movie base url
Countries_url = None
Kenyan_url=None
def configure_request(app):
    global Countries_url,Kenyan_url
    Countries_url = app.config['COUNTRIES_BASE_URL']
    Kenyan_url=app.config['KENYAN_BASE_URL']


def get_countries(): 
    url = Countries_url

    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)
    
    data = response.json()
    
    country_results = []
    for country_item in data:
        
        country =country_item.get('country')
        cases =country_item.get('cases') 
        todayCases = country_item.get('todayCases')
        todayDeath =country_item.get('todayDeath') 
        recovered =country_item.get('recovered') 
        active =country_item.get('active') 
        critical =country_item.get('Critical') 
        totalTests =country_item.get('totalTests') 
        country_object = Country(country,cases,todayCases,todayDeath,recovered,active,critical,
        totalTests)
        country_results.append(country_object)
            
    
    return country_results


def search_country(country_name):
    search_country_url = 'https://coronavirus-19-api.herokuapp.com/countries/{}'.format(country_name)
    with urllib.request.urlopen(search_country_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_country_data)

        search_movie_results = None

        if search_country_response['results']:
            search_country_list = search_country_response['results']
            search_country_results = process_results(search_country_list)


    return search_country_results     


def get_kenya():   

    '''
    Function that gets the json response to our url request
    '''
    get_countries_url = Kenyan_url.format()

    with urllib.request.urlopen(get_countries_url) as url:
        get_countries_data = url.read()
        get_countries_response = json.loads(get_countries_data)

        country_object = None
        

        if get_countries_response:
            
            country =get_countries_response.get('country')
            cases =get_countries_response.get('cases') 
            todayCases =get_countries_response.get('todayCases')
            deaths=get_countries_response.get('deaths')
            todayDeath =get_countries_response.get('todayDeath') 
            recovered =get_countries_response.get('recovered') 
            active =get_countries_response.get('active') 
            critical =get_countries_response.get('critical') 
            casesPerOneMillion =get_countries_response.get('casesPerOneMillion') 
            deathsPerOneMillion=get_countries_response.get('deathsPerOneMillion')
            totalTests =get_countries_response.get('totalTests') 
            
        
            country_object = Kenyan(country,cases,todayCases,deaths,todayDeath,recovered,active,critical,
                casesPerOneMillion,deathsPerOneMillion,totalTests)
            
    return country_object
      
      


import requests
from .model import Country



# Getting the movie base url
Countries_url = None

def configure_request(app):
    global Countries_url
    Countries_url = app.config['COUNTRIES_BASE_URL']

def get_countries(): 
    url = Countries_url

    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

    process_results(response.text.encode('utf8'))

    return response
def process_results(country_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    country_results = []
    for country_item in country_list:
        country =country.get('country')
        slug =country.get('slug') 
        IS02 = country.get('IS02')
    
        if poster:
            country_object = Country(country,slug,IS02)
            country_results.append(country_object)

    return country_results    

# def get_countries():   
#      '''
#     Function that gets the json response to our url request
#     '''
#     get_countries_url = countries_url.format()

#     with urllib.request.urlopen(get_countries_url) as url:
#         get_countries_data = url.read()
#         get_countries_response = json.loads(get_countries_data)

#         country_results = None

#         if get_countries_response['countries']:
#             country_results_list = get_countries_response['countries']
#             country_results = process_results(country_results_list)
#     return country_results    

# def process_results(country_list):
#     '''
#     Function  that processes the movie result and transform them to a list of Objects

#     Args:
#         movie_list: A list of dictionaries that contain movie details

#     Returns :
#         movie_results: A list of movie objects
#     '''
#     country_results = []
#     for country_item in country_list:
#         country =country.get('country')
#         slug =country.get('slug') 
#         IS02 = country.get('IS02')
    
#         if poster:
#             country_object = Country(country,slug,IS02)
#             country_results.append(country_object)

#     return country_results

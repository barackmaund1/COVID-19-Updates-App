from .model import Country
import urllib.request,json
import requests
from config import Config


# Getting the movie base url
Countries_url = None
Kenyan_url=None
def configure_request(app):
    global Countries_url
    Countries_url = app.config['COUNTRIES_BASE_URL']
    # Kenyan_url=app.config['KENYAN_BASE_URL']

def get_countries(): 
    url = Countries_url

    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)
    import pdb; pdb.set_trace()

    return response.text.encode('utf8')


# def get_countries(countryName):   

#     '''
#     Function that gets the json response to our url request
#     '''
#     get_countries_url = Kenyan_url.format(countryName)

#     with urllib.request.urlopen(get_countries_url) as url:
#         get_countries_data = url.read()
#         get_countries_response = json.loads(get_countries_data)

#         country_results = None

#         if get_countries_response:
#             print(country_item)
#             country =country_item.getdata('country')
#             cases =country_item.getdata('cases') 
#             todayCases = country_item.getdata('todayCases')
#             todayDeath =country_item.getdata('todayDeath') 
#             recovered =country_item.getdata('recovered') 
#             active =country_item.getdata('active') 
#             critical =country_item.getdata('Critical') 
#             casesPerOneMillion =country_item.getdata('casesPerOneMillion') 
#             deathPerOneMillion=country_item.getdata('deathPerOneMillion')
#             totalTests =country_item.getdata('totalTests') 
#             testPerOneMillion =country_item.getdata('testPeronemillion')
        
#             country_object = Country(country,cases,todayCases,todayDeath,recovered,active,critical,
#                 casesPerOneMillion,deathPerOneMillion,totalTestst,testPerOneMillion)
#             country_results.append(country_object)

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
#         print(country_item)
#         country =country_item.getdata('country')
#         cases =country_item.getdata('cases') 
#         todayCases = country_item.getdata('todayCases')
#         todayDeath =country_item.getdata('todayDeath') 
#         recovered =country_item.getdata('recovered') 
#         active =country_item.getdata('active') 
#         critical =country_item.getdata('Critical') 
#         casesPerOneMillion =country_item.getdata('casesPerOneMillion') 
#         deathPerOneMillion=country_item.getdata('deathPerOneMillion')
#         totalTests =country_item.getdata('totalTests') 
#         testPerOneMillion =country_item.getdata('testPeronemillion')
#         if poster:
#             country_object = Country(country,cases,todayCases,todayDeath,recovered,active,critical,
#             casesPerOneMillion,deathPerOneMillion,totalTestst,testPerOneMillion)
#             country_results.append(country_object)

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

# def get_countries():   
#     '''
#     Function that gets the json response to our url request
#     '''
#     get_countries_url = Countries_url.format()

#     with urllib.request.urlopen(get_countries_url) as url:
#         get_countries_data = url.read()
#         get_countries_response = json.loads(get_countries_data)
#         print(get_countries_response)
#         country_results = None

#         if get_countries_response[0]:
#             country_results_list = get_countries_response[0]
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
#         print(country_item)
#         country =country_item.getdata('country')
#         slug =country_item.getdata('slug') 
#         IS02 = country_item.getdata('IS02')
    
#         if poster:
#             country_object = Country(country,slug,IS02)
#             country_results.append(country_object)

#     return country_results

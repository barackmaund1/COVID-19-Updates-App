from flask import render_template,request,redirect,url_for,abort
from . import main
from ..requests import get_countries
from ..model import Country


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title='Covid19-updates'
    countries=get_countries('kenya')

    return render_template('index.html', title = title, countries=countries )
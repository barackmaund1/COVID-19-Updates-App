from flask import render_template,request,redirect,url_for,abort
from . import main
from ..requests import get_countries
from ..model import Country
from flask_login import login_required
from ..corona import Coronavirus

@main.route('/',methods = ['POST','GET'])
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title='Covid19-updates'
    countries=get_countries()

    return render_template('index.html', title = title, countries=countries )
@main.route('/subscribe/',methods = ['POST','GET'])
@login_required
def subscribe():
    email = request.form.get('subscriber')
    new_subscriber = Subscriber(email = email)
    new_subscriber.save_subscriber()
    corona=Coronavirus()
    mail_message("Coronavirus stats in your country today!'","email/welcome_subscriber",new_subscriber.email,new_subscriber=new_subscriber,corona=corona)
    flash('Sucessfuly subscribed')
    return redirect(url_for('main.index'))    
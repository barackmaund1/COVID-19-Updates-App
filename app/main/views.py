from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from ..requests import get_kenya,get_countries
from ..model import Country,Kenyan,Subscriber
from flask_login import login_required
from ..email import mail_message
from flask_login import  current_user
from datetime import datetime, timedelta
from threading import Timer


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title='Covid19-updates'
    # covid_results=get_countries()

    return render_template('base.html', title = title,)

@main.route('/allcountries/')
def allcountries():

    '''
    View root page function that returns the index page and its data
    '''
    title='Updates :: allcountries'
    covid_results=get_countries()

    return render_template('allstats.html', title = title, countries=covid_results )     
@main.route('/subscribe/',methods = ['POST','GET'])
@login_required
def subscribe():
    if request.method == "POST":
        
        email = request.form.get('subscriber')
        new_subscriber = Subscriber(email = email)
        new_subscriber.save_subscriber()
        corona=get_kenya()
        
        mail_message("Current Corona stats in Kenya!","email/welcome_subscriber",new_subscriber.email,new_subscriber=new_subscriber,corona=corona)
        flash('Sucessfully subscribed  and confirm your email for updates')
    
        return redirect(url_for('main.index')) 
    return redirect(url_for('auth.login'))       
 
x=datetime.today()
y=x.replace(day=x.day+1, hour=1, minute=0, second=0, microsecond=0) + timedelta(days=1)
delta_t=y-x


delta_t=y-x

secs=delta_t.total_seconds()

def hello_world():
    subscribers = Subscriber.query.all()
    corona=get_kenya()
    for subscriber in subscribers:
        mail_message("Current Corona stats in Kenya!","email/welcome_subscriber",subscriber.email,corona=corona)
    
t = Timer(secs, hello_world)
t.start()    
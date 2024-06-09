from datetime import datetime
from tkinter import W
from flask import Flask, make_response, render_template, sessions, url_for, flash, redirect,session,Markup
import numpy as np 
from analyse import Analyse_Retro
from calcul import prix

from forms import RegistrationForm, LoginForm
from datetime import datetime
from mail import  send_email_with_attachment
import os

from pdf import pdf
from pricing import  total
from voice import vocal

#from pdf import pdf

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'



@app.route("/")
@app.route("/Accueil")
def Accueil():
    return render_template('Accueil.html')


@app.route("/index1")
def index1():
    return render_template('index1.html', title='contact')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.is_submitted():
        d1=datetime.strptime((form.date1.raw_data)[0], '%Y-%m-%d').date()
        print(d1)
        a=d1.strftime("%d/%m/%Y")
        if form.submit2.data:
            v=vocal()
            flash(f'la ville choisie est {v}!', 'success')    
        x= total(form.ca.data,form.pivot.data,form.couts.data,a,form.ville.choices[int(form.ville.data)- 1][1])
        flash(f'la prime proposée est {x}', 'success')
        pdf(form.username.data,form.ville.choices[int(form.ville.data)- 1][1],d1,form.ca.data,form.pivot.data,form.couts.data,x)
        if form.submit.data:
            send_email_with_attachment(form.username.data, form.email.data, form.username.data)
            #flash(f'Account created for {form.couts.data}!', 'success')
        elif form.submit1.data:
           path = form.username.data+'.pdf'
           os.system(path)
           # return render_template('about.html', title='About') 
        elif form.submit2.data:
            v=vocal()
            flash(f'la ville choisie est {v}!', 'success')    
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
   
    if form.is_submitted():
        v=form.ville.choices[int(form.ville.data)-1][1]
        Analyse_Retro(v,form.ca.data,form.pivot.data,form.couts.data)
        
    return render_template('login.html', title='retro', form=form)



if __name__ == '__main__':
    app.run(debug=True)
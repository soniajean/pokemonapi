
from app import app

from flask import render_template, request, url_for, redirect
from flask_login import current_user, login_user, logout_user

from .auth.forms import SignUpForm, LoginForm
from .models import User
from .auth.forms import PokemonForm
from .services import getPokemon
import requests, json

@app.route('/')
def homePage():
    Pokey = [
        {
        'name': 'pikachu',
        'ability': 456,
        'spec' : 'Vim'
        },
        {
        'name': 'charizard',
        'ability' : 342,
        'spec' : 'student relations'
        },
        {
        'name' : 'Bulbasaur',
        'ability' : 567,
        'spec': 'none'
        }
    ]
    fav_animal = 'Poke'
    return render_template('index.html', pokey=Pokey, f = fav_animal)

@app.route('/login')
def loginPage():
    return render_template('login.html')


@app.route('/signUp', methods=["GET", "POST"])
def signUpPage():
    form = SignUpForm()
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            print(username, email, password)


            user = User(username, email, password)            
            user.saveUser()
            return redirect(url_for('loginPage'))

    return render_template('register.html', form=form)


@app.route('/pokemon_search', methods=["GET", "POST"])
def findpokemon():
    form = PokemonForm()
    if request.method == 'POST':
        if form.validate():  
            pokemon = form.pokemon.data

            pokedict= getPokemon(pokemon)
            print(pokedict)
            return render_template('pokemon_search.html', form=form, pokedict=pokedict)

    return render_template('pokemon_search.html', form=form)